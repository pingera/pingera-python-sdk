
#!/usr/bin/env python3
"""
Comprehensive usage example for the Pingera Python SDK.

This example demonstrates the full API coverage available through the
OpenAPI-generated client.

APIs covered:
- Alerts API - Alert management and notifications
- Checks API - Monitor checks and results  
- Checks Unified Results API - Unified check result queries
- Heartbeats API - Heartbeat monitoring
- On Demand Checks API - Execute checks on demand
- Status Pages Components API - Status page component management
- Status Pages Incidents API - Incident management
"""

import os
from pingera import ApiClient, Configuration
from pingera.api import (
    AlertsApi,
    ChecksApi, 
    ChecksUnifiedResultsApi,
    HeartbeatsApi,
    OnDemandChecksApi,
    StatusPagesComponentsApi,
    StatusPagesIncidentsApi
)
from pingera.exceptions import ApiException


def setup_client():
    """Set up the API client with authentication."""
    configuration = Configuration()
    configuration.host = "https://api.pingera.ru"

    bearer_token = os.getenv("PINGERA_BEARER_TOKEN")
    api_key = os.getenv("PINGERA_API_KEY")

    if bearer_token:
        configuration.access_token = bearer_token
    elif api_key:
        configuration.api_key['apiKeyAuth'] = api_key
    else:
        # Use demo key for demonstration
        configuration.api_key['apiKeyAuth'] = "demo_api_key"

    return ApiClient(configuration)


def demonstrate_alerts_api(api_client):
    """Demonstrate Alerts API functionality."""
    print("\n--- Alerts API ---")
    try:
        alerts_api = AlertsApi(api_client)
        print("✓ Alerts API initialized")
        print("Available methods:")
        print("- v1_alerts_get() - List alerts")
        print("- v1_alerts_post() - Create alert")
        print("- v1_alerts_alert_id_get() - Get specific alert")
        print("- v1_alerts_alert_id_put() - Update alert")
        print("- v1_alerts_alert_id_delete() - Delete alert")
    except Exception as e:
        print(f"✗ Alerts API error: {e}")


def demonstrate_checks_api(api_client):
    """Demonstrate Checks API functionality."""
    print("\n--- Checks API ---")
    try:
        checks_api = ChecksApi(api_client)
        print("✓ Checks API initialized")
        print("Available methods:")
        print("- v1_checks_get() - List monitor checks")
        print("- v1_checks_post() - Create check")
        print("- v1_checks_check_id_get() - Get specific check")
        print("- v1_checks_check_id_put() - Update check")
        print("- v1_checks_check_id_delete() - Delete check")
        
        # Try to list checks if authentication is available
        if os.getenv("PINGERA_API_KEY") or os.getenv("PINGERA_BEARER_TOKEN"):
            try:
                checks = checks_api.v1_checks_get(page=1, page_size=5)
                print(f"✓ Successfully retrieved checks data")
            except ApiException as e:
                print(f"  Note: Authentication required for live data: [{e.status}]")
        
    except Exception as e:
        print(f"✗ Checks API error: {e}")


def demonstrate_heartbeats_api(api_client):
    """Demonstrate Heartbeats API functionality."""
    print("\n--- Heartbeats API ---")
    try:
        heartbeats_api = HeartbeatsApi(api_client)
        print("✓ Heartbeats API initialized")
        print("Available methods:")
        print("- v1_heartbeats_get() - List heartbeat checks")
        print("- v1_heartbeats_post() - Create heartbeat")
        print("- v1_heartbeats_heartbeat_id_get() - Get specific heartbeat")
        print("- v1_heartbeats_heartbeat_id_put() - Update heartbeat")
        print("- v1_heartbeats_heartbeat_id_delete() - Delete heartbeat")
        print("- v1_heartbeats_heartbeat_id_ping_post() - Ping heartbeat")
    except Exception as e:
        print(f"✗ Heartbeats API error: {e}")


def demonstrate_components_api(api_client):
    """Demonstrate Status Pages Components API functionality."""
    print("\n--- Status Pages Components API ---")
    try:
        components_api = StatusPagesComponentsApi(api_client)
        print("✓ Components API initialized")
        print("Available methods (require page_id):")
        print("- v1_pages_page_id_components_get(page_id) - List components")
        print("- v1_pages_page_id_components_post(page_id, component) - Create component")
        print("- v1_pages_page_id_components_component_id_get(page_id, component_id) - Get component")
        print("- v1_pages_page_id_components_component_id_put(page_id, component_id, data) - Update component")
        print("- v1_pages_page_id_components_component_id_delete(page_id, component_id) - Delete component")
        print("Note: These operations require a valid page_id parameter")
    except Exception as e:
        print(f"✗ Components API error: {e}")


def demonstrate_incidents_api(api_client):
    """Demonstrate Status Pages Incidents API functionality."""
    print("\n--- Status Pages Incidents API ---")
    try:
        incidents_api = StatusPagesIncidentsApi(api_client)
        print("✓ Incidents API initialized")
        print("Available methods (require page_id):")
        print("- v1_pages_page_id_incidents_get(page_id) - List incidents")
        print("- v1_pages_page_id_incidents_post(page_id, incident) - Create incident")
        print("- v1_pages_page_id_incidents_incident_id_get(page_id, incident_id) - Get incident")
        print("- v1_pages_page_id_incidents_incident_id_put(page_id, incident_id, data) - Update incident")
        print("- v1_pages_page_id_incidents_incident_id_delete(page_id, incident_id) - Delete incident")
        print("- Incident updates and maintenance scheduling methods also available")
        print("Note: These operations require a valid page_id parameter")
    except Exception as e:
        print(f"✗ Incidents API error: {e}")


def demonstrate_on_demand_checks_api(api_client):
    """Demonstrate On Demand Checks API functionality."""
    print("\n--- On Demand Checks API ---")
    try:
        on_demand_api = OnDemandChecksApi(api_client)
        print("✓ On Demand Checks API initialized")
        print("Available methods:")
        print("- v1_checks_execute_post() - Execute custom check on demand")
        print("- v1_checks_jobs_job_id_get() - Get job status and results")
        print("Example: Execute synthetic checks, HTTP checks, etc.")
    except Exception as e:
        print(f"✗ On Demand Checks API error: {e}")


def demonstrate_unified_results_api(api_client):
    """Demonstrate Checks Unified Results API functionality."""
    print("\n--- Checks Unified Results API ---")
    try:
        unified_results_api = ChecksUnifiedResultsApi(api_client)
        print("✓ Unified Results API initialized")
        print("Available methods:")
        print("- v1_checks_unified_results_get() - Query unified check results")
        print("- Filter by time range, check types, regions, etc.")
        print("- Aggregate results across multiple monitoring sources")
    except Exception as e:
        print(f"✗ Unified Results API error: {e}")


def main():
    """Main demonstration function."""
    print("=== Pingera Python SDK - Comprehensive API Coverage ===")
    
    try:
        # Initialize client
        print("\nInitializing generated OpenAPI client...")
        api_client = setup_client()
        print("✓ Client initialized successfully")
        
        with api_client:
            print(f"\n=== API Configuration ===")
            print(f"- Host: {api_client.configuration.host}")
            print(f"- Authentication: {'Bearer Token' if api_client.configuration.access_token else 'API Key'}")
            user_agent = getattr(api_client.configuration, 'user_agent', 'N/A')
            print(f"- User Agent: {user_agent}")
            
            # Demonstrate each API
            demonstrate_alerts_api(api_client)
            demonstrate_checks_api(api_client)
            demonstrate_heartbeats_api(api_client)
            demonstrate_on_demand_checks_api(api_client)
            demonstrate_unified_results_api(api_client)
            demonstrate_components_api(api_client)
            demonstrate_incidents_api(api_client)
            
            print(f"\n=== Authentication Setup ===")
            print("To use live data, set one of these environment variables:")
            print("- PINGERA_API_KEY=your_api_key")
            print("- PINGERA_BEARER_TOKEN=your_bearer_token")
            
            print(f"\n=== Next Steps ===")
            print("1. Set authentication environment variables")
            print("2. Get your organization's status page IDs for components/incidents APIs")
            print("3. Check out specific examples:")
            print("   - examples/basic_usage.py - Basic operations")
            print("   - examples/component_management.py - Component CRUD")
            print("   - examples/incident_management.py - Incident management")
            print("   - examples/on_demand_synthetic_check.py - Synthetic monitoring")
            print("4. Start building your monitoring automation!")
        
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n=== SDK demonstration completed! ===")


if __name__ == "__main__":
    main()
