"""Checks that the generated client covers the API spec stored in openapi/openapi.json."""
import inspect
import json
import re
from pathlib import Path

import pytest

import pingera.api
import pingera.models

SPEC = json.loads((Path(__file__).resolve().parent.parent / "openapi" / "openapi.json").read_text(encoding="utf-8"))
HTTP_METHODS = ("get", "post", "put", "patch", "delete")


def _model_class_name(schema_name):
    words = re.sub(r"[^0-9A-Za-z]+", " ", schema_name).split()
    return "".join(word[:1].upper() + word[1:] for word in words)


def _sdk_operations():
    operations = set()
    for _, api_class in inspect.getmembers(pingera.api, inspect.isclass):
        source = inspect.getsource(api_class)
        for method, path in re.findall(r"method='(\w+)',\s*resource_path='([^']+)'", source):
            operations.add((method.lower(), path))
    return operations


def _enum_properties():
    for schema_name, schema in SPEC["components"]["schemas"].items():
        for prop, prop_schema in (schema.get("properties") or {}).items():
            is_array = prop_schema.get("type") == "array"
            values = (prop_schema.get("items") or {}).get("enum") if is_array else prop_schema.get("enum")
            if values:
                yield pytest.param(schema_name, prop, is_array, [v for v in values if v is not None],
                                   id=f"{schema_name}.{prop}")


def test_every_operation_has_an_sdk_method():
    expected = {(m, p) for p, ops in SPEC["paths"].items() for m in ops if m in HTTP_METHODS}
    actual = _sdk_operations()
    assert sorted(expected - actual) == [], "Operations missing from the SDK; run generate_client.py"
    assert sorted(actual - expected) == [], "SDK has operations that are no longer in the API"


def test_every_schema_has_a_model():
    # Free-form objects without properties are generated as plain dicts, not models
    missing = [name for name, schema in SPEC["components"]["schemas"].items()
               if schema.get("properties") and not hasattr(pingera.models, _model_class_name(name))]
    assert missing == []


@pytest.mark.parametrize("schema_name,prop,is_array,values", list(_enum_properties()))
def test_models_accept_every_enum_value_in_the_spec(schema_name, prop, is_array, values):
    model = getattr(pingera.models, _model_class_name(schema_name))
    validator = getattr(model, f"{prop}_validate_enum", None)
    if validator is None:
        pytest.skip("no enum validator generated")
    for value in values:
        validator([value] if is_array else value)
