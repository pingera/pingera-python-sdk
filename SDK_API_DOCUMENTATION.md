
# Pingera Python SDK - API Methods Documentation

> **Note**: This file is maintained for backward compatibility only. 
> 
> **For the most up-to-date and comprehensive API documentation, please refer to [client/README.md](client/README.md).**
>
> The client/README.md contains the official OpenAPI-generated documentation with complete method signatures, parameters, and examples.

## Quick Links

- **Main Documentation**: [client/README.md](client/README.md)
- **Generated API Docs**: [client/docs/](client/docs/) (Individual API class documentation)
- **Official Pingera API Docs**: [https://docs.pingera.ru/api/overview](https://docs.pingera.ru/api/overview)

## Basic Usage

For current usage examples and complete API reference, see:

```python
# See client/README.md for complete setup instructions
import pingera
from pingera.api import ChecksApi, StatusPagesComponentsApi
from pingera.models import Component, IncidentCreate

# Basic client setup
configuration = pingera.Configuration(host="https://api.pingera.ru")
configuration.api_key['apiKeyAuth'] = "your_api_key"

with pingera.ApiClient(configuration) as api_client:
    checks_api = ChecksApi(api_client)
    checks = checks_api.v1_checks_get()
```

## Available APIs

All API classes and methods are documented in [client/README.md](client/README.md):

- `AlertsApi` - Manage alerts and notifications
- `ChecksApi` - Manage monitoring checks  
- `CheckGroupsApi` - Manage check groups
- `ChecksUnifiedResultsApi` - Query unified check results
- `HeartbeatsApi` - Manage heartbeat monitoring
- `OnDemandChecksApi` - Execute checks on demand
- `StatusPagesApi` - Manage status pages
- `StatusPagesComponentsApi` - Manage status page components
- `StatusPagesIncidentsApi` - Manage incidents and maintenance

## Examples

Check the `examples/` directory for comprehensive usage examples:

- [`basic_usage.py`](examples/basic_usage.py) - Basic client setup and operations
- [`comprehensive_sdk_usage.py`](examples/comprehensive_sdk_usage.py) - Complete API demonstration
- [`component_management.py`](examples/component_management.py) - Component CRUD operations
- [`incident_management.py`](examples/incident_management.py) - Incident management
- [`list_regions.py`](examples/list_regions.py) - Fetching available regions
- [`on_demand_synthetic_check.py`](examples/on_demand_synthetic_check.py) - Synthetic monitoring

---

**Please refer to [client/README.md](client/README.md) for the complete, up-to-date documentation.**
