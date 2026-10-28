"""Request/response behaviour of the generated client, using a fake transport (no network)."""
import pytest

import pingera
from pingera.exceptions import ApiException, UnauthorizedException
from pingera.models import OrganizationUpdate, PrivateLocationCreate


def test_api_key_and_user_agent_headers(client, transport, pyproject_version):
    transport.respond(body=[])
    pingera.AlertsApi(client).v1_alerts_channels_get()

    assert transport.last.method == "GET"
    assert transport.last.url == "https://api.test/v1/alerts/channels"
    assert transport.last.headers["Authorization"] == "test-token"
    assert transport.last.headers["User-Agent"] == f"pingera-sdk/{pyproject_version}/python"


def test_bearer_token_auth(transport):
    configuration = pingera.Configuration(host="https://api.test", access_token="jwt")
    with pingera.ApiClient(configuration) as api_client:
        api_client.rest_client = transport
        transport.respond(body=[])
        pingera.AlertsApi(api_client).v1_alerts_channels_get()
    assert transport.last.headers["Authorization"] == "Bearer jwt"


def test_alert_channels_of_every_type_are_deserialized(client, transport):
    types = ["email", "webhook", "statuspage", "telegram", "sms", "max"]
    transport.respond(body=[{"id": t, "name": t, "type": t, "configuration": {}} for t in types])

    channels = pingera.AlertsApi(client).v1_alerts_channels_get()

    assert [c.type for c in channels] == types


def test_cron_scheduled_check_fields(client, transport):
    transport.respond(body={
        "id": "chk1", "name": "Nightly", "type": "web", "url": "https://example.com",
        "scheduling_type": "cron", "cron_schedule": "0 3 * * *", "effective_interval": 86400,
        "credit_throttled": False,
    })

    check = pingera.ChecksApi(client).v1_checks_check_id_get("chk1")

    assert transport.last.url == "https://api.test/v1/checks/chk1"
    assert (check.scheduling_type, check.cron_schedule, check.effective_interval) == ("cron", "0 3 * * *", 86400)


def test_create_private_location_sends_body_and_returns_token(client, transport):
    transport.respond(status=201, body={
        "id": "pl1", "region_id": "private-pl1", "name": "Office", "country": "DE",
        "check_types": ["web"], "enabled": True, "status": "never_connected", "runners_online": 0,
        "runners": [], "tokens": [{"id": "t1", "name": "default", "token_prefix": "prt_ab"}],
        "token": "prt_secret",
    })

    created = pingera.PrivateLocationsApi(client).v1_private_locations_post(
        PrivateLocationCreate(name="Office", country="DE", check_types=["web"]))

    assert (transport.last.method, transport.last.url) == ("POST", "https://api.test/v1/private-locations")
    assert transport.last.body == {"name": "Office", "country": "DE", "check_types": ["web"]}
    assert created.token == "prt_secret"
    assert created.tokens[0].token_prefix == "prt_ab"


def test_partial_update_only_sends_set_fields(client, transport):
    transport.respond(body={"id": "org1", "name": "Acme", "timezone": "Europe/Berlin"})

    org = pingera.OrganizationsApi(client).v1_organizations_org_id_patch(
        "org1", OrganizationUpdate(timezone="Europe/Berlin"))

    assert transport.last.method == "PATCH"
    assert transport.last.body == {"timezone": "Europe/Berlin"}
    assert org.timezone == "Europe/Berlin"


def test_list_query_parameters(client, transport):
    transport.respond(body={"audit_logs": [], "pagination": {"page": 2}})

    pingera.AuditApi(client).v1_audit_get(action="login", page=2, per_page=10)

    assert transport.last.url == "https://api.test/v1/audit?action=login&page=2&per_page=10"


def test_unauthorized_raises_specific_exception(client, transport):
    transport.respond(status=401, body={"code": "unauthorized", "message": "Invalid token"})

    with pytest.raises(UnauthorizedException) as error:
        pingera.ChecksApi(client).v1_checks_get()

    assert error.value.status == 401
    assert "Invalid token" in error.value.body


def test_other_errors_raise_api_exception_with_status(client, transport):
    transport.respond(status=402, body={"code": "plan_limit_reached", "message": "Upgrade"})

    with pytest.raises(ApiException) as error:
        pingera.PrivateLocationsApi(client).v1_private_locations_post(PrivateLocationCreate(name="x"))

    assert error.value.status == 402
