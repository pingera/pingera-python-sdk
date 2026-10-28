import importlib.resources

import pingera
import pingera.api


def test_version_matches_pyproject(pyproject_version):
    assert pingera.__version__ == pyproject_version


def test_user_agent_identifies_sdk(pyproject_version):
    assert pingera.ApiClient().user_agent == f"pingera-sdk/{pyproject_version}/python"


def test_package_is_typed():
    assert importlib.resources.files("pingera").joinpath("py.typed").is_file()


def test_api_classes_are_exported_from_package_root():
    api_classes = [name for name in dir(pingera.api) if name.endswith("Api")]
    assert len(api_classes) >= 20
    for name in api_classes:
        assert getattr(pingera, name) is getattr(pingera.api, name)


def test_default_host_is_production():
    assert pingera.Configuration().host == "https://api.pingera.ru"
