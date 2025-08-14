
#!/usr/bin/env python3
"""
Comprehensive example using the Pingera generated OpenAPI client.

This example demonstrates:
- Full API client setup and configuration
- Using all available API endpoints
- Type-safe model handling
- Proper error handling and cleanup
"""

import os
from datetime import datetime

from pingera import ApiClient, Configuration
from pingera.api import (
    StatusPagesComponentsApi,
    StatusPagesIncidentsApi,
    ChecksApi,
    AlertsApi,
    HeartbeatsApi,
    OnDemandChecksApi,
    ChecksUnifiedResultsApi
)
from pingera.models import (
    ComponentUptimeBulkRequest,
    IncidentCreate,
    IncidentUpdateCreate,
    ExecuteCustomCheckRequest
)
from pingera.exceptions import ApiException


class PingeraClient:
    """Wrapper class for the Pingera generated client."""
    
    def __init__(self):
        """Initialize the client with authentication."""
        self.configuration = Configuration()
        self.configuration.host = "https://api.pingera.ru"
        
        # Set up authentication
        bearer_token = os.getenv("PINGERA_BEARER_TOKEN")
        api_key = os.getenv("PINGERA_API_KEY")
        
        if bearer_token:
            self.configuration.access_token = bearer_token
        elif api_key:
            self.configuration.api_key['Authorization'] = f"Bearer {api_key}"
        else:
            raise ValueError("No authentication credentials found. Set PINGERA_BEARER_TOKEN or PINGERA_API_KEY environment variable.")
        
        self.api_client = ApiClient(self.configuration)
        
        # Initialize all API instances
        self.components = StatusPagesComponentsApi(self.api_client)
        self.incidents = StatusPagesIncidentsApi(self.api_client)
        self.checks = ChecksApi(self.api_client)
        self.alerts = AlertsApi(self.api_client)
        self.heartbeats = HeartbeatsApi(self.api_client)
        self.on_demand_checks = OnDemandChecksApi(self.api_client)
        self.unified_results = ChecksUnifiedResultsApi(self.api_client)
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.api_client.__exit__(exc_type, exc_val, exc_tb)


def demonstrate_checks_api(client: PingeraClient):
    """Demonstrate the Checks API functionality."""
    print("\n=== Checks API ===")
    
    try:
        # List checks
        checks_response = client.checks.v1_checks_get(page=1, page_size=10)
        if hasattr(checks_response, 'checks') and checks_response.checks:
            print(f"✓ Found {len(checks_response.checks)} checks")
            
            for check in checks_response.checks[:3]:
                name = getattr(check, 'name', 'unnamed')
                check_type = getattr(check, 'type', 'unknown')
                status = getattr(check, 'status', 'unknown')
                print(f"  - {name} ({check_type}): {status}")
                
                # Get check details
                check_id = getattr(check, 'id', None)
                if check_id:
                    try:
                        detail = client.checks.v1_checks_check_id_get(check_id)
                        print(f"    URL: {getattr(detail, 'url', 'N/A')}")
                    except ApiException as e:
                        print(f"    Could not get details: {e.reason}")
        else:
            print("✓ No checks found")
            
    except ApiException as e:
        print(f"✗ Failed to list checks: [{e.status}] {e.reason}")


def demonstrate_heartbeats_api(client: PingeraClient):
    """Demonstrate the Heartbeats API functionality."""
    print("\n=== Heartbeats API ===")
    
    try:
        # List heartbeat checks
        heartbeats_response = client.heartbeats.v1_heartbeats_get(page=1, page_size=5)
        if hasattr(heartbeats_response, 'heartbeat_checks') and heartbeats_response.heartbeat_checks:
            print(f"✓ Found {len(heartbeats_response.heartbeat_checks)} heartbeat checks")
            
            for heartbeat in heartbeats_response.heartbeat_checks[:3]:
                name = getattr(heartbeat, 'name', 'unnamed')
                status = getattr(heartbeat, 'status', 'unknown')
                print(f"  - {name}: {status}")
        else:
            print("✓ No heartbeat checks found")
            
    except ApiException as e:
        print(f"✗ Failed to list heartbeats: [{e.status}] {e.reason}")


def demonstrate_alerts_api(client: PingeraClient):
    """Demonstrate the Alerts API functionality."""
    print("\n=== Alerts API ===")
    
    try:
        # List alerts
        alerts_response = client.alerts.v1_alerts_get(page=1, page_size=5)
        if hasattr(alerts_response, 'alerts') and alerts_response.alerts:
            print(f"✓ Found {len(alerts_response.alerts)} alerts")
            
            for alert in alerts_response.alerts[:3]:
                alert_type = getattr(alert, 'type', 'unknown')
                status = getattr(alert, 'status', 'unknown')
                print(f"  - {alert_type}: {status}")
        else:
            print("✓ No alerts found")
            
    except ApiException as e:
        print(f"✗ Failed to list alerts: [{e.status}] {e.reason}")


def demonstrate_on_demand_checks(client: PingeraClient):
    """Demonstrate on-demand check execution."""
    print("\n=== On-Demand Checks ===")
    
    try:
        # Example of executing a custom check
        custom_check = ExecuteCustomCheckRequest(
            url="https://httpbin.org/status/200",
            type="http",
            regions=["us-east-1"]
        )
        
        print("✓ Executing custom check...")
        result = client.on_demand_checks.v1_on_demand_checks_custom_post(custom_check)
        print(f"✓ Check executed with job ID: {getattr(result, 'job_id', 'unknown')}")
        
    except ApiException as e:
        print(f"✗ Failed to execute custom check: [{e.status}] {e.reason}")
    except Exception as e:
        print(f"✗ Error executing custom check: {e}")


def main():
    """Main demonstration function."""
    
    print("=== Pingera Generated Client Comprehensive Example ===")
    
    try:
        with PingeraClient() as client:
            print("✓ Client initialized successfully")
            
            # Demonstrate all API functionalities
            demonstrate_checks_api(client)
            demonstrate_heartbeats_api(client)
            demonstrate_alerts_api(client)
            demonstrate_on_demand_checks(client)
            
            print("\n=== Type Safety Demonstration ===")
            print("✓ All API methods are fully type-hinted")
            print("✓ Request and response models provide validation")
            print("✓ IDE autocompletion and error detection available")
            
            print("\n=== Available APIs ===")
            print("  - StatusPagesComponentsApi: Manage status page components")
            print("  - StatusPagesIncidentsApi: Manage incidents and updates")  
            print("  - ChecksApi: Manage monitoring checks")
            print("  - AlertsApi: Manage alerts and notifications")
            print("  - HeartbeatsApi: Manage heartbeat monitoring")
            print("  - OnDemandChecksApi: Execute checks on-demand")
            print("  - ChecksUnifiedResultsApi: Get unified check results")
            
            print("\n=== Example completed successfully! ===")
            
    except ValueError as e:
        print(f"\n✗ Configuration error: {e}")
        print("Please set PINGERA_BEARER_TOKEN or PINGERA_API_KEY environment variable.")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")


if __name__ == "__main__":
    main()
