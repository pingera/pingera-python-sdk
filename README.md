
# Pingera SDK

A comprehensive Python SDK for the [Pingera monitoring platform API](https://api.pingera.ru), built using OpenAPI Generator for full type safety and complete API coverage.

## Features

- **Complete API Coverage**: Auto-generated from the official OpenAPI specification
- **Type Safety**: Full type hints and Pydantic model validation
- **Easy Authentication**: Support for Bearer tokens and API keys
- **Comprehensive**: All Pingera API endpoints supported:
  - Status Pages (Components & Incidents)
  - Monitoring Checks
  - Heartbeats
  - Alerts
  - On-demand Checks
  - Unified Results

## Installation

```bash
pip install pingera-sdk
```

Or install from source:

```bash
git clone https://github.com/pingera/pingera-sdk.git
cd pingera-sdk
pip install -e .
```

## Quick Start

### Authentication

Set your API token via environment variable:

```bash
export PINGERA_API_KEY="your_api_token"
```

### Basic Usage

```python
from pingera_generated import ApiClient, Configuration
from pingera_generated.api import ChecksApi, StatusPagesComponentsApi

# Configure the client
configuration = Configuration()
configuration.host = "https://api.pingera.ru"
configuration.api_key['apiKeyAuth'] = "your_api_token"

# Create API client
with ApiClient(configuration) as api_client:
    # Initialize API instances
    checks_api = ChecksApi(api_client)
    components_api = StatusPagesComponentsApi(api_client)
    
    # List monitoring checks
    checks = checks_api.v1_checks_get(page=1, page_size=10)
    print(f"Found {len(checks.checks)} checks")
    
    # List components for a status page
    components = components_api.v1_pages_page_id_components_get("your_page_id")
    print(f"Found {len(components.data)} components")
```

### Available APIs

The SDK provides access to all Pingera API endpoints through these API classes:

```python
from pingera_generated.api import (
    StatusPagesComponentsApi,    # Manage status page components
    StatusPagesIncidentsApi,     # Manage incidents and maintenance
    ChecksApi,                   # Manage monitoring checks
    AlertsApi,                   # Manage alerts and notifications
    HeartbeatsApi,               # Manage heartbeat monitoring
    OnDemandChecksApi,           # Execute checks on-demand
    ChecksUnifiedResultsApi      # Get unified check results
)
```

### Working with Models

All API requests and responses use typed Pydantic models:

```python
from pingera_generated.models import (
    Component,
    IncidentCreate,
    IncidentUpdateCreate,
    ExecuteCustomCheckRequest
)

# Create a new component
new_component = Component(
    name="API Server",
    description="Main API endpoint",
    status="operational"
)

# Create an incident
new_incident = IncidentCreate(
    name="Database Connectivity Issues", 
    body="We are investigating connectivity issues",
    status="investigating",
    impact="major"
)
```

## Examples

Check the `examples/` directory for comprehensive usage examples:

- [`basic_usage.py`](examples/basic_usage.py) - Basic client setup and operations
- [`component_management.py`](examples/component_management.py) - Component CRUD operations
- [`incident_management.py`](examples/incident_management.py) - Incident and maintenance management
- [`generated_client_usage.py`](examples/generated_client_usage.py) - Comprehensive API demonstration
- [`on_demand_synthetic_check.py`](examples/on_demand_synthetic_check.py) - Execute synthetic check with playwright script and get the result

## Configuration

### Environment Variables

| Variable | Description |
|----------|-------------|
| `PINGERA_API_KEY` | Your Pingera API token |
| `PINGERA_PAGE_ID` | Default page ID for status page operations |

### Manual Configuration

```python
from pingera_generated import Configuration

configuration = Configuration()
configuration.host = "https://api.pingera.ru"

# API token authentication
configuration.api_key['apiKeyAuth'] = "your_api_token"

# Optional: configure timeouts, retries, etc.
configuration.timeout = 30
```

## Error Handling

The SDK uses proper exception handling:

```python
from pingera_generated.exceptions import ApiException

try:
    checks = checks_api.v1_checks_get()
except ApiException as e:
    print(f"API Error [{e.status}]: {e.reason}")
    if e.body:
        print(f"Details: {e.body}")
```

## Development

### Regenerating the Client

If the Pingera API specification changes, you can regenerate the client:

```bash
# Install the OpenAPI generator
pip install openapi-generator-cli[jdk4py]

# Regenerate the client
python generate_client.py
```

### Running Tests

```bash
pip install -e ".[dev]"
pytest
```

### Running Examples

```bash
# Set your credentials
export PINGERA_API_KEY="your_api_token"
export PINGERA_PAGE_ID="your_page_id"

# Run examples
python examples/basic_usage.py
python examples/component_management.py
python examples/incident_management.py
```

## API Documentation

For detailed API documentation, visit:
- [Official Pingera API Docs](https://docs.pingera.ru/api/overview)
- [Generated Client Docs](client/README.md)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Run the test suite
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 📧 Email: [privet@pingera.ru](mailto:privet@pingera.ru)  
- 📖 Documentation: [docs.pingera.ru](https://docs.pingera.ru)
- 🌐 Website: [pingera.ru](https://pingera.ru)
- 📊 Status: [status.pingera.ru](https://status.pingera.ru)

## Links

- [Pingera Platform](https://app.pingera.ru)
- [API Documentation](https://docs.pingera.ru/api/overview)
- [Status Page](https://status.pingera.ru)
- [Website](https://pingera.ru)
