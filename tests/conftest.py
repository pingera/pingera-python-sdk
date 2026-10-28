import json
import re
from pathlib import Path
from types import SimpleNamespace

import pytest

import pingera
from pingera.rest import RESTResponse

ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = ROOT / "openapi" / "openapi.json"


@pytest.fixture(scope="session")
def spec():
    return json.loads(SPEC_PATH.read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def pyproject_version():
    text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    return re.search(r'^version\s*=\s*"([^"]+)"', text, re.MULTILINE).group(1)


class FakeTransport:
    """Replaces the urllib3-based REST client: records requests and returns queued responses."""

    def __init__(self):
        self.requests = []
        self.responses = []

    def respond(self, status=200, body=None, headers=None):
        data = b"" if body is None else json.dumps(body).encode()
        headers = {"Content-Type": "application/json", **(headers or {})}
        self.responses.append(SimpleNamespace(status=status, reason="", data=data, headers=headers))

    def request(self, method, url, headers=None, body=None, post_params=None, _request_timeout=None):
        self.requests.append(SimpleNamespace(method=method, url=url, headers=headers or {}, body=body))
        return RESTResponse(self.responses.pop(0))

    @property
    def last(self):
        return self.requests[-1]


@pytest.fixture
def transport():
    return FakeTransport()


@pytest.fixture
def client(transport):
    configuration = pingera.Configuration(host="https://api.test")
    configuration.api_key["apiKeyAuth"] = "test-token"
    with pingera.ApiClient(configuration) as api_client:
        api_client.rest_client = transport
        yield api_client
