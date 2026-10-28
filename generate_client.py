#!/usr/bin/env python3
"""Regenerate the Pingera SDK from the Pingera API OpenAPI specification.

Usage:
    python generate_client.py                    # fetch the live spec and regenerate client/
    python generate_client.py --spec path.json   # regenerate from a local spec file
    python generate_client.py --check            # fail if client/ is out of date with the spec

The spec is saved to openapi/openapi.json so API changes are visible in git diffs.
Only the generated package (client/pingera), its docs (client/docs) and
client/README.md are kept; packaging is handled by the root pyproject.toml.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CLIENT_DIR = ROOT / "client"
SPEC_PATH = ROOT / "openapi" / "openapi.json"
PYPROJECT = ROOT / "pyproject.toml"

DEFAULT_SPEC_URL = "https://api.pingera.ru/openapi.json"
GENERATOR_VERSION = "7.26.0"
GENERATOR_IMAGE = f"openapitools/openapi-generator-cli:v{GENERATOR_VERSION}"
REPO_URL = "https://github.com/pingera/pingera-python-sdk"

# Generated outputs that are copied into client/; everything else the generator
# produces (setup.py, tox.ini, CI configs, test stubs, ...) is discarded.
MANAGED_DIRS = ("pingera", "docs")
MANAGED_FILES = ("README.md",)


def read_version() -> str:
    text = PYPROJECT.read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, re.MULTILINE)
    if not match:
        sys.exit(f"Could not find the project version in {PYPROJECT}")
    return match.group(1)


def load_spec(source: str) -> dict:
    if re.match(r"^https?://", source):
        print(f"Fetching OpenAPI spec from {source}")
        request = urllib.request.Request(source, headers={"Accept": "application/json"})
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.load(response)
    print(f"Reading OpenAPI spec from {source}")
    with open(source, encoding="utf-8") as fh:
        return json.load(fh)


def dump_spec(spec: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def patch_undocumented_responses(spec: dict) -> dict:
    """Make undocumented success responses return the raw JSON instead of breaking.

    Without a documented 2xx response the generated client falls back to the
    ``default`` (Error) schema or discards the body. Declaring an untyped JSON
    body makes the SDK return the decoded JSON (dict/list) for these operations.
    """
    spec = json.loads(json.dumps(spec))
    untyped = {"application/json": {"schema": {}}}
    for operations in spec.get("paths", {}).values():
        for method, operation in operations.items():
            if method not in ("get", "post", "put", "patch", "delete"):
                continue
            responses = operation.setdefault("responses", {})
            success = [code for code in responses if code.startswith("2")]
            if not success:
                responses["200"] = {"description": "Successful response", "content": untyped}
            for code in success:
                if code != "204" and not responses[code].get("content"):
                    responses[code]["content"] = untyped
    return spec


def run_generator(spec_file: Path, out_dir: Path, version: str, runner: str) -> None:
    args = [
        "generate",
        "-g", "python",
        "--package-name", "pingera",
        "--git-host", "github.com",
        "--git-user-id", "pingera",
        "--git-repo-id", "pingera-python-sdk",
        "--additional-properties",
        ",".join([
            f"packageVersion={version}",
            "projectName=pingera-sdk",
            f"packageUrl={REPO_URL}",
            f"httpUserAgent=pingera-sdk/{version}/python",
        ]),
    ]

    if runner == "docker":
        work = spec_file.parent
        cmd = ["docker", "run", "--rm", "-v", f"{work}:/local"]
        if hasattr(os, "getuid"):
            cmd += ["--user", f"{os.getuid()}:{os.getgid()}"]
        cmd += [GENERATOR_IMAGE, *args,
                "-i", f"/local/{spec_file.name}",
                "-o", f"/local/{out_dir.relative_to(work)}"]
    else:
        generator = os.environ.get("OPENAPI_GENERATOR_CMD", "openapi-generator-cli").split()
        cmd = [*generator, *args, "-i", str(spec_file), "-o", str(out_dir)]

    print(f"Running OpenAPI Generator {GENERATOR_VERSION} ({runner})")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError:
        sys.exit(f"Could not run '{cmd[0]}'. Install Docker, or use --runner local "
                 f"with openapi-generator-cli {GENERATOR_VERSION} on PATH.")
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        sys.exit("OpenAPI Generator failed")


def postprocess(generated: Path) -> None:
    """Replace the generator's packaging instructions, which don't apply to this repo."""
    readme = generated / "README.md"
    text = readme.read_text(encoding="utf-8")
    python = re.search(r'^requires-python\s*=\s*">=([^"]+)"',
                       PYPROJECT.read_text(encoding="utf-8"), re.MULTILINE)
    install = (
        "## Requirements\n\n"
        f"Python {python.group(1) if python else '3'}+\n\n"
        "## Installation\n\n"
        "```sh\npip install pingera-sdk\n```\n\n"
        "Then import the package:\n\n"
        "```python\nimport pingera\n```\n\n"
    )
    text, count = re.subn(r"^## Requirements\.?\n.*?(?=^## Getting Started)", install, text,
                          flags=re.MULTILINE | re.DOTALL)
    if count != 1:
        sys.exit("Unexpected README layout from the generator; update postprocess()")
    text = text.replace("[installation procedure](#installation--usage)",
                        "[installation procedure](#installation)")
    readme.write_text(text, encoding="utf-8")


def managed_files(base: Path) -> dict:
    files = {}
    for name in MANAGED_DIRS:
        for path in sorted((base / name).rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                files[path.relative_to(base).as_posix()] = path.read_bytes()
    for name in MANAGED_FILES:
        if (base / name).is_file():
            files[name] = (base / name).read_bytes()
    return files


def sync_client(generated: Path) -> None:
    CLIENT_DIR.mkdir(exist_ok=True)
    for name in MANAGED_DIRS:
        shutil.rmtree(CLIENT_DIR / name, ignore_errors=True)
        shutil.copytree(generated / name, CLIENT_DIR / name)
    for name in MANAGED_FILES:
        shutil.copy2(generated / name, CLIENT_DIR / name)


def check_drift(spec: dict, generated: Path) -> int:
    problems = []
    if not SPEC_PATH.exists() or json.loads(SPEC_PATH.read_text(encoding="utf-8")) != spec:
        problems.append(f"{SPEC_PATH.relative_to(ROOT)} differs from the API spec")

    expected, actual = managed_files(generated), managed_files(CLIENT_DIR)
    for name in sorted(expected.keys() | actual.keys()):
        if name not in actual:
            problems.append(f"missing: client/{name}")
        elif name not in expected:
            problems.append(f"stale: client/{name}")
        elif expected[name] != actual[name]:
            problems.append(f"outdated: client/{name}")

    if problems:
        print("The SDK is out of date with the API spec:")
        for problem in problems:
            print(f"  - {problem}")
        print("Run 'python generate_client.py' to regenerate it.")
        return 1
    print("The SDK is up to date with the API spec.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--spec", default=DEFAULT_SPEC_URL,
                        help=f"OpenAPI spec URL or file path (default: {DEFAULT_SPEC_URL})")
    parser.add_argument("--check", action="store_true",
                        help="Only check whether client/ matches the spec; don't modify files")
    parser.add_argument("--runner", choices=("docker", "local"), default="docker",
                        help="Run the generator via Docker (default) or a local "
                             "openapi-generator-cli (override with OPENAPI_GENERATOR_CMD)")
    options = parser.parse_args()

    spec = load_spec(options.spec)
    version = read_version()

    build_dir = ROOT / "build"
    build_dir.mkdir(exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="openapi-", dir=build_dir))
    try:
        spec_file = work / "openapi.json"
        dump_spec(patch_undocumented_responses(spec), spec_file)
        out_dir = work / "out"
        run_generator(spec_file, out_dir, version, options.runner)
        postprocess(out_dir)

        if options.check:
            return check_drift(spec, out_dir)

        dump_spec(spec, SPEC_PATH)
        sync_client(out_dir)
    finally:
        shutil.rmtree(work, ignore_errors=True)

    print(f"Regenerated pingera-sdk {version} in {CLIENT_DIR.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
