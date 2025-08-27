
# Pingera Python SDK - API Methods Documentation

This document provides a complete reference of all available methods in the Pingera Python SDK. The SDK is built on top of OpenAPI-generated client and provides access to all Pingera monitoring platform APIs.

## Table of Contents

1. [Client Initialization](#client-initialization)
2. [Authentication](#authentication)
3. [Available API Modules](#available-api-modules)
4. [Alerts API Methods](#alerts-api-methods)
5. [Checks API Methods](#checks-api-methods)
6. [Checks Unified Results API Methods](#checks-unified-results-api-methods)
7. [Heartbeats API Methods](#heartbeats-api-methods)
8. [On-Demand Checks API Methods](#on-demand-checks-api-methods)
9. [Status Pages Components API Methods](#status-pages-components-api-methods)
10. [Status Pages Incidents API Methods](#status-pages-incidents-api-methods)
11. [Data Models](#data-models)
12. [Error Handling](#error-handling)

## Client Initialization

### PingeraClient Class

The main entry point for the SDK is the `PingeraClient` class.

```python
from pingera import PingeraClient

# Initialize with environment variables
client = PingeraClient.from_env()

# Initialize with Bearer token
client = PingeraClient.from_bearer_token("your_bearer_token")

# Initialize with API key
client = PingeraClient.from_api_key("your_api_key")

# Manual initialization
from pingera import BearerTokenAuth
client = PingeraClient(auth=BearerTokenAuth("token"), base_url="https://api.pingera.ru")
```

### Client Properties

- `client.alerts` - AlertsApi instance
- `client.checks` - ChecksApi instance  
- `client.checks_unified_results` - ChecksUnifiedResultsApi instance
- `client.heartbeats` - HeartbeatsApi instance
- `client.on_demand_checks` - OnDemandChecksApi instance
- `client.status_pages` - StatusPagesApi instance
- `client.components` - StatusPagesComponentsApi instance
- `client.incidents` - StatusPagesIncidentsApi instance

## Authentication

### Authentication Classes

```python
from pingera import BearerTokenAuth, APIKeyAuth

# Bearer token authentication
auth = BearerTokenAuth("your_bearer_token")

# API key authentication  
auth = APIKeyAuth("your_api_key")
```

### Environment Variables

- `PINGERA_BEARER_TOKEN` - Bearer token for authentication
- `PINGERA_API_KEY` - API key for authentication
- `PINGERA_PAGE_ID` - Default page ID for status page operations

## Status Pages API Methods

### StatusPagesApi (`client.status_pages`)

Methods for managing status pages themselves:

```python
# List all status pages
pages = client.status_pages.v1_pages_get(
    page=1,           # Optional: page number
    page_size=20      # Optional: items per page
)

# Get specific status page
page = client.status_pages.v1_pages_page_id_get(page_id="page_123")

# Create new status page
from pingera.models import StatusPageCreate
new_page = StatusPageCreate(
    name="My Status Page",
    description="Status page for our services",
    subdomain="status",
    theme="light"
)

created_page = client.status_pages.v1_pages_post(new_page)

# Update status page
updated_page = client.status_pages.v1_pages_page_id_put(
    page_id="page_123",
    page_data=updated_data
)

# Delete status page
client.status_pages.v1_pages_page_id_delete(page_id="page_123")
```

## Available API Modules

The SDK provides access to 8 main API modules, each corresponding to a specific area of the Pingera platform:

1. **AlertsApi** (`client.alerts`) - Manage alerts and notifications
2. **ChecksApi** (`client.checks`) - Manage monitoring checks
3. **ChecksUnifiedResultsApi** (`client.checks_unified_results`) - Query unified check results
4. **HeartbeatsApi** (`client.heartbeats`) - Manage heartbeat monitoring
5. **OnDemandChecksApi** (`client.on_demand_checks`) - Execute checks on demand
6. **StatusPagesApi** (`client.status_pages`) - Manage status pages
7. **StatusPagesComponentsApi** (`client.components`) - Manage status page components
8. **StatusPagesIncidentsApi** (`client.incidents`) - Manage incidents and maintenance

## Alerts API Methods

### AlertsApi (`client.alerts`)

Methods for managing alerts and notifications:

```python
# Get all alerts
alerts = client.alerts.v1_alerts_get(
    page=1,           # Optional: page number
    page_size=20,     # Optional: number of items per page
    status="active"   # Optional: filter by alert status
)

# Get specific alert
alert = client.alerts.v1_alerts_alert_id_get(alert_id="alert_123")

# Create new alert
from pingera.models import Alert
new_alert = client.alerts.v1_alerts_post(alert_data)

# Update alert
updated_alert = client.alerts.v1_alerts_alert_id_put(
    alert_id="alert_123",
    alert_data=updated_data
)

# Delete alert
client.alerts.v1_alerts_alert_id_delete(alert_id="alert_123")

# Get alert statistics
stats = client.alerts.v1_alerts_stats_get()

# Get alert channels
channels = client.alerts.v1_alert_channels_get()

# Get alert rules
rules = client.alerts.v1_alert_rules_get()
```

## Checks API Methods

### ChecksApi (`client.checks`)

Methods for managing monitoring checks:

```python
# List all checks
checks = client.checks.v1_checks_get(
    page=1,           # Optional: page number
    page_size=20,     # Optional: items per page
    type="web",       # Optional: filter by check type
    status="active"   # Optional: filter by status
)

# Get specific check
check = client.checks.v1_checks_check_id_get(check_id="check_123")

# Create new check
new_check = client.checks.v1_checks_post(check_data)

# Update check
updated_check = client.checks.v1_checks_check_id_put(
    check_id="check_123",
    check_data=updated_data
)

# Delete check
client.checks.v1_checks_check_id_delete(check_id="check_123")

# Get check results
results = client.checks.v1_checks_check_id_results_get(
    check_id="check_123",
    from_date="2023-01-01T00:00:00Z",  # Optional: start date
    to_date="2023-12-31T23:59:59Z",    # Optional: end date
    page=1,                            # Optional: page number
    page_size=50                       # Optional: items per page
)

# Get specific check result by ID
specific_result = client.checks.v1_checks_check_id_results_check_result_id_get(
    check_id="check_123",
    check_result_id="result_456"
)

# Get check statistics
stats = client.checks.v1_checks_check_id_stats_get(check_id="check_123")

# Pause/Resume check
client.checks.v1_checks_check_id_pause_post(check_id="check_123")
client.checks.v1_checks_check_id_resume_post(check_id="check_123")

# Get check jobs
jobs = client.checks.v1_checks_jobs_get()

# Get specific job
job = client.checks.v1_checks_jobs_job_id_get(job_id="job_123")
```

## Checks Unified Results API Methods

### ChecksUnifiedResultsApi (`client.checks_unified_results`)

Methods for querying unified check results across multiple sources:

```python
# Get unified results
results = client.checks_unified_results.v1_checks_unified_results_get(
    check_ids=["check_1", "check_2"],     # Optional: specific check IDs
    from_date="2023-01-01T00:00:00Z",     # Optional: start date
    to_date="2023-12-31T23:59:59Z",       # Optional: end date
    status="success",                      # Optional: filter by status
    page=1,                               # Optional: page number
    page_size=100                         # Optional: items per page
)

# Get aggregated statistics
aggregated_stats = client.checks_unified_results.v1_checks_unified_results_stats_get(
    check_ids=["check_1", "check_2"],
    from_date="2023-01-01T00:00:00Z",
    to_date="2023-12-31T23:59:59Z"
)
```

## Heartbeats API Methods

### HeartbeatsApi (`client.heartbeats`)

Methods for managing heartbeat monitoring:

```python
# List all heartbeats
heartbeats = client.heartbeats.v1_heartbeats_get(
    page=1,           # Optional: page number
    page_size=20,     # Optional: items per page
    status="active"   # Optional: filter by status
)

# Get specific heartbeat
heartbeat = client.heartbeats.v1_heartbeats_heartbeat_id_get(heartbeat_id="hb_123")

# Create new heartbeat
new_heartbeat = client.heartbeats.v1_heartbeats_post(heartbeat_data)

# Update heartbeat
updated_heartbeat = client.heartbeats.v1_heartbeats_heartbeat_id_put(
    heartbeat_id="hb_123",
    heartbeat_data=updated_data
)

# Delete heartbeat
client.heartbeats.v1_heartbeats_heartbeat_id_delete(heartbeat_id="hb_123")

# Send heartbeat ping
client.heartbeats.v1_heartbeats_heartbeat_id_ping_post(heartbeat_id="hb_123")

# Get heartbeat logs
logs = client.heartbeats.v1_heartbeats_heartbeat_id_logs_get(
    heartbeat_id="hb_123",
    from_date="2023-01-01T00:00:00Z",  # Optional: start date
    to_date="2023-12-31T23:59:59Z",    # Optional: end date
    page=1,                            # Optional: page number
    page_size=50                       # Optional: items per page
)
```

## On-Demand Checks API Methods

### OnDemandChecksApi (`client.on_demand_checks`)

Methods for executing checks on demand:

```python
# Execute custom check
from pingera.models import ExecuteCustomCheckRequest

check_request = ExecuteCustomCheckRequest(
    url="https://example.com",
    type="web",               # Options: "web", "synthetic", "api"
    timeout=30,
    name="On-demand check",
    parameters={
        "pw_script": "console.log('test');"  # For synthetic checks
    }
)

response = client.on_demand_checks.v1_checks_execute_post(check_request)
job_id = response.job_id

# Execute existing check
existing_check_response = client.on_demand_checks.v1_checks_check_id_execute_post(
    check_id="check_123"
)

# Get job status
job_status = client.on_demand_checks.v1_checks_jobs_job_id_get(job_id=job_id)

# List on-demand checks
on_demand_checks = client.on_demand_checks.v1_on_demand_checks_get(
    page=1,
    page_size=20
)
```

## Status Pages Components API Methods

### StatusPagesComponentsApi (`client.components`)

Methods for managing status page components:

```python
# List components for a status page
components = client.components.v1_pages_page_id_components_get(
    page_id="page_123",
    page=1,           # Optional: page number
    page_size=20      # Optional: items per page
)

# Get specific component
component = client.components.v1_pages_page_id_components_component_id_get(
    page_id="page_123",
    component_id="comp_123"
)

# Create new component
from pingera.models import Component
new_component = Component(
    name="API Server",
    description="Main API endpoint", 
    status="operational"
)

created_component = client.components.v1_pages_page_id_components_post(
    page_id="page_123",
    component=new_component
)

# Update component
updated_component = client.components.v1_pages_page_id_components_component_id_put(
    page_id="page_123",
    component_id="comp_123",
    component=updated_data
)

# Delete component
client.components.v1_pages_page_id_components_component_id_delete(
    page_id="page_123",
    component_id="comp_123"
)

# Update component status
client.components.v1_pages_page_id_components_component_id_status_put(
    page_id="page_123",
    component_id="comp_123", 
    status="degraded_performance"
)

# Get component uptime
uptime = client.components.v1_pages_page_id_components_component_id_uptime_get(
    page_id="page_123",
    component_id="comp_123",
    from_date="2023-01-01T00:00:00Z",  # Optional: start date
    to_date="2023-12-31T23:59:59Z"     # Optional: end date
)

# Bulk update component uptime
from pingera.models import ComponentUptimeBulkRequest
bulk_request = ComponentUptimeBulkRequest(...)
client.components.v1_pages_page_id_components_uptime_bulk_post(
    page_id="page_123",
    bulk_request=bulk_request
)
```

## Status Pages Incidents API Methods

### StatusPagesIncidentsApi (`client.incidents`)

Methods for managing incidents and maintenance:

```python
# List incidents for a status page
incidents = client.incidents.v1_pages_page_id_incidents_get(
    page_id="page_123",
    page=1,           # Optional: page number
    page_size=20,     # Optional: items per page
    status="open"     # Optional: filter by status
)

# Get specific incident
incident = client.incidents.v1_pages_page_id_incidents_incident_id_get(
    page_id="page_123",
    incident_id="inc_123"
)

# Create new incident
from pingera.models import IncidentCreate
new_incident = IncidentCreate(
    name="Database Issues",
    body="We are investigating database connectivity issues",
    status="investigating",
    impact="major"
)

created_incident = client.incidents.v1_pages_page_id_incidents_post(
    page_id="page_123",
    incident=new_incident
)

# Update incident
updated_incident = client.incidents.v1_pages_page_id_incidents_incident_id_put(
    page_id="page_123",
    incident_id="inc_123",
    incident=updated_data
)

# Delete incident
client.incidents.v1_pages_page_id_incidents_incident_id_delete(
    page_id="page_123",
    incident_id="inc_123"
)

# Add incident update
from pingera.models import IncidentUpdateCreate
incident_update = IncidentUpdateCreate(
    body="We have identified the issue and are working on a fix",
    status="identified"
)

client.incidents.v1_pages_page_id_incidents_incident_id_updates_post(
    page_id="page_123",
    incident_id="inc_123",
    update=incident_update
)

# Get incident updates
updates = client.incidents.v1_pages_page_id_incidents_incident_id_updates_get(
    page_id="page_123",
    incident_id="inc_123"
)

# Get specific incident update
update = client.incidents.v1_pages_page_id_incidents_incident_id_updates_update_id_get(
    page_id="page_123",
    incident_id="inc_123",
    update_id="upd_123"
)

# Update incident update
updated_update = client.incidents.v1_pages_page_id_incidents_incident_id_updates_update_id_put(
    page_id="page_123",
    incident_id="inc_123",
    update_id="upd_123",
    update=updated_update_data
)

# Delete incident update
client.incidents.v1_pages_page_id_incidents_incident_id_updates_update_id_delete(
    page_id="page_123",
    incident_id="inc_123",
    update_id="upd_123"
)
```

## Data Models

### Key Data Models Available

The SDK uses Pydantic models for all API requests and responses. Key models include:

```python
from pingera.models import (
    Alert,                           # Alert configuration
    AlertChannel,                    # Alert notification channels
    AlertRule,                       # Alert rules and conditions
    Component,                       # Status page component
    CheckJob,                        # Check execution job
    ExecuteCustomCheckRequest,       # On-demand check request
    HeartbeatCheck,                  # Heartbeat configuration
    IncidentCreate,                  # Incident creation data
    IncidentUpdateCreate,            # Incident update data
    ComponentUptimeBulkRequest,      # Bulk uptime update
    Error                            # API error response
)
```

### Common Model Properties

- **Component**: `name`, `description`, `status`, `created_at`, `updated_at`
- **Incident**: `name`, `body`, `status`, `impact`, `created_at`, `resolved_at`
- **Check**: `name`, `type`, `url`, `interval`, `timeout`, `status`
- **Alert**: `name`, `type`, `conditions`, `channels`, `enabled`
- **Heartbeat**: `name`, `interval`, `grace_period`, `last_ping_at`

### Status Values

- **Component Status**: `operational`, `degraded_performance`, `partial_outage`, `major_outage`
- **Incident Status**: `investigating`, `identified`, `monitoring`, `resolved`
- **Incident Impact**: `none`, `minor`, `major`, `critical`
- **Check Status**: `active`, `paused`, `error`

## Error Handling

### Exception Classes

```python
from pingera.exceptions import (
    PingeraError,                    # Base exception
    PingeraAuthenticationError,      # Authentication failures
    PingeraNotFoundError,           # Resource not found (404)
    PingeraValidationError,         # Request validation errors (400)
    PingeraRateLimitError,          # Rate limit exceeded (429)
    PingeraNetworkError             # Network-related errors
)

from pingera.exceptions import ApiException  # Generated client exceptions
```

### Error Handling Example

```python
try:
    checks = client.checks.v1_checks_get()
except ApiException as e:
    print(f"API Error [{e.status}]: {e.reason}")
    if e.body:
        print(f"Details: {e.body}")
except PingeraAuthenticationError as e:
    print(f"Authentication failed: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Common Parameters

### Pagination Parameters

Most list endpoints support pagination:
- `page`: Page number (default: 1)
- `page_size`: Items per page (default: 20, max: 100)

### Date Range Parameters

Many endpoints support date filtering:
- `from_date`: Start date in ISO 8601 format (`2023-01-01T00:00:00Z`)
- `to_date`: End date in ISO 8601 format (`2023-12-31T23:59:59Z`)

### Filter Parameters

Common filters across endpoints:
- `status`: Filter by status value
- `type`: Filter by type/category
- `check_ids`: Array of check IDs (for unified results)

## Usage Examples

### Complete Workflow Example

```python
from pingera import PingeraClient
from pingera.models import Component, IncidentCreate

# Initialize client
client = PingeraClient.from_env()

# Get status page ID (you'll need this from your organization)
page_id = "your_page_id"

# Create a component
component = Component(
    name="API Gateway",
    description="Main API gateway service",
    status="operational"
)
new_component = client.components.v1_pages_page_id_components_post(
    page_id=page_id,
    component=component
)

# Create an incident
incident = IncidentCreate(
    name="API Gateway Maintenance",
    body="Scheduled maintenance for API gateway",
    status="scheduled",
    impact="minor"
)
new_incident = client.incidents.v1_pages_page_id_incidents_post(
    page_id=page_id,
    incident=incident
)

# List all checks
checks = client.checks.v1_checks_get(page_size=50)
print(f"Found {len(checks.checks)} checks")

# Execute an on-demand check
from pingera.models import ExecuteCustomCheckRequest
check_request = ExecuteCustomCheckRequest(
    url="https://api.example.com/health",
    type="web",
    timeout=30,
    name="Health Check"
)
job_response = client.on_demand_checks.v1_checks_execute_post(check_request)
```

This documentation covers all available methods in the Pingera Python SDK. Each method corresponds to specific API endpoints and provides full type safety through Pydantic models.
