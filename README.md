# Pingera Python SDK

[![PyPI](https://img.shields.io/pypi/v/pingera-sdk)](https://pypi.org/project/pingera-sdk/)
[![Python versions](https://img.shields.io/pypi/pyversions/pingera-sdk)](https://pypi.org/project/pingera-sdk/)
[![CI](https://github.com/pingera/pingera-python-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/pingera/pingera-python-sdk/actions/workflows/ci.yml)

The official Python SDK for the [Pingera](https://pingera.ru) monitoring and status page platform API.
It is generated from the [Pingera OpenAPI specification](https://api.pingera.ru/openapi.json), so it
covers every endpoint and ships typed [Pydantic](https://docs.pydantic.dev) models for all requests
and responses.

## Installation

```bash
pip install pingera-sdk
```

Requires Python 3.10 or newer.

## Quick start

Create an API token in the Pingera app under [Settings → API tokens](https://app.pingera.ru/settings/tokens)
and export it:

```bash
export PINGERA_API_KEY="your_api_token"
```

```python
import os

from pingera import ApiClient, ChecksApi, Configuration, StatusPagesApi, StatusPagesComponentsApi

configuration = Configuration()  # defaults to https://api.pingera.ru
configuration.api_key["apiKeyAuth"] = os.environ["PINGERA_API_KEY"]

with ApiClient(configuration) as api_client:
    pages = StatusPagesApi(api_client).v1_pages_get()
    print(f"Found {len(pages.pages)} status pages")

    checks = ChecksApi(api_client).v1_checks_get(page=1, page_size=10)
    for check in checks.checks:
        print(check.name, check.type, check.status)

    components = StatusPagesComponentsApi(api_client).v1_pages_page_id_components_get("your_page_id")
    print(f"Found {len(components)} components")
```

### Authentication

Use an API token (recommended for scripts and integrations):

```python
configuration.api_key["apiKeyAuth"] = "your_api_token"
```

Or a JWT access token obtained by logging in:

```python
configuration = Configuration(access_token="your_jwt")
```

## Available APIs

All API classes can be imported from `pingera` or `pingera.api`. Method names follow the endpoint
path and HTTP method, e.g. `GET /v1/checks/{check_id}` is `ChecksApi.v1_checks_check_id_get`.

| API class | Purpose |
| --- | --- |
| `ChecksApi` | Monitoring checks, results, regions, uptime and status history |
| `CheckGroupsApi` | Group checks together |
| `CheckSecretsApi` / `SecretsApi` | Secrets and their assignment to checks |
| `ChecksUnifiedResultsApi` | Unified results across checks |
| `ExecutionGroupsApi` | Multi-region execution results |
| `OnDemandChecksApi` | Run checks on demand and poll for results |
| `HeartbeatsApi` | Heartbeat (cron job) monitoring |
| `PrivateLocationsApi` | Private locations and runner tokens for self-hosted runners |
| `AlertsApi` | Alerts, alert rules and notification channels |
| `StatusPagesApi` | Status pages, custom sender email domains |
| `StatusPagesComponentsApi` | Status page components and their uptime |
| `StatusPagesIncidentsApi` | Incidents, maintenance and postmortems |
| `PagePasswordsApi` | Password protection for status pages |
| `ReportsApi` | PDF report generation |
| `AuditApi` | Organization audit trail |
| `OrganizationsApi` / `UsageApi` | Organization settings, plans, subscriptions and usage |
| `UsersApi` / `AuthEnhancedApi` / `OAuthApi` / `WebauthnApi` | Users, API tokens and authentication |

The full reference for every method and model is in [client/README.md](client/README.md) and
[client/docs/](client/docs/).

## Working with models

```python
from pingera import StatusPagesIncidentsApi
from pingera.models import IncidentCreate, IncidentUpdateCreate

incidents_api = StatusPagesIncidentsApi(api_client)

incident = incidents_api.v1_pages_page_id_incidents_post(
    "your_page_id",
    IncidentCreate(
        name="Database connectivity issues",
        body="We are investigating connectivity issues",
        status="investigating",
        impact="major",
    ),
)

incidents_api.v1_pages_page_id_incidents_incident_id_incident_updates_post(
    "your_page_id",
    incident.id,
    IncidentUpdateCreate(status="identified", body="The cause has been found"),
)
```

Models can be converted with `to_dict()` / `to_json()` and created with `from_dict()` / `from_json()`.

## Error handling

Failed requests raise `pingera.ApiException`, or a subclass for common statuses
(`BadRequestException`, `UnauthorizedException`, `ForbiddenException`, `NotFoundException`,
`ServiceException`):

```python
from pingera.exceptions import ApiException, NotFoundException

try:
    check = ChecksApi(api_client).v1_checks_check_id_get("missing")
except NotFoundException:
    print("Check not found")
except ApiException as e:
    print(f"API error {e.status}: {e.body}")
```

## Examples

See the [examples/](examples/) directory:

- [`basic_usage.py`](examples/basic_usage.py) - client setup and basic calls
- [`status_pages_management.py`](examples/status_pages_management.py) - status page CRUD
- [`component_management.py`](examples/component_management.py) - component CRUD
- [`incident_management.py`](examples/incident_management.py) - incidents and maintenance
- [`list_regions.py`](examples/list_regions.py) - available check regions
- [`on_demand_synthetic_check.py`](examples/on_demand_synthetic_check.py) - run a Playwright check on demand and wait for the result
- [`comprehensive_sdk_usage.py`](examples/comprehensive_sdk_usage.py) and [`generated_client_usage.py`](examples/generated_client_usage.py) - tours of most APIs

The examples read `PINGERA_API_KEY` (or `PINGERA_BEARER_TOKEN`) and, where needed, `PINGERA_PAGE_ID`.

## Development

```bash
pip install -e ".[dev]"
pytest
```

### Regenerating the client

The SDK is generated with [OpenAPI Generator](https://openapi-generator.tech), run through Docker:

```bash
python generate_client.py                  # fetch https://api.pingera.ru/openapi.json and regenerate
python generate_client.py --spec spec.json # regenerate from a local spec file
python generate_client.py --check          # only check whether the SDK matches the live API
```

The script stores the spec in [openapi/openapi.json](openapi/openapi.json) and rewrites
`client/pingera/`, `client/docs/` and `client/README.md`. Don't edit those generated files by hand.
Use `--runner local` to call a locally installed `openapi-generator-cli` instead of Docker.

A [scheduled workflow](.github/workflows/api-drift.yml) runs `--check` against the live API every
day, so new endpoints, fields and enum values are noticed quickly.

### Releasing

1. Regenerate the client and run the tests.
2. Bump `version` in [pyproject.toml](pyproject.toml) (the only place it is defined), then run
   `python generate_client.py` again so the generated code picks up the new version.
3. Add an entry to [CHANGELOG.md](CHANGELOG.md).
4. Build and upload: `python -m build && twine upload dist/*`.

## License

MIT, see [LICENSE](LICENSE).

## Links

- [SDK documentation](https://docs.pingera.ru/devs/sdk)
- [API documentation](https://docs.pingera.ru/api/overview)
- [Pingera app](https://app.pingera.ru)
- [Status page](https://status.pingera.ru)
- Support: [privet@pingera.ru](mailto:privet@pingera.ru)
