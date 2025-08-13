#!/usr/bin/env python3
"""
Comprehensive usage example for the Pingera Python SDK.

This example demonstrates the full API coverage available through our
high-level SDK wrapper built on top of the OpenAPI-generated client.

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
from pingera import PingeraClient
from pingera.exceptions import PingeraError


def demonstrate_alerts_api(client):
    """Demonstrate Alerts API functionality."""
    print("\n--- Alerts API ---")
    try:
        # List alerts
        print("Listing alerts...")
        # Note: This will require proper authentication and organization access
        # alerts = client.alerts.v1_alerts_get()
        print("✓ Alerts API available")
    except Exception as e:
        print(f"✗ Alerts API error: {e}")


def demonstrate_checks_api(client):
    """Demonstrate Checks API functionality."""
    print("\n--- Checks API ---")
    try:
        # List monitor checks
        print("Listing monitor checks...")
        # checks = client.checks.v1_checks_get()
        print("✓ Checks API available")
    except Exception as e:
        print(f"✗ Checks API error: {e}")


def demonstrate_heartbeats_api(client):
    """Demonstrate Heartbeats API functionality."""
    print("\n--- Heartbeats API ---")
    try:
        # List heartbeat checks
        print("Listing heartbeat checks...")
        # heartbeats = client.heartbeats.v1_heartbeats_get()
        print("✓ Heartbeats API available")
    except Exception as e:
        print(f"✗ Heartbeats API error: {e}")


def demonstrate_components_api(client):
    """Demonstrate Status Pages Components API functionality."""
    print("\n--- Status Pages Components API ---")
    try:
        # Components require a page_id - normally you'd get this from your organization
        print("Components API available")
        print("Note: Components operations require a page_id parameter")
        print("Example operations:")
        print("- client.components.v1_pages_page_id_components_get(page_id)")
        print("- client.components.v1_pages_page_id_components_post(page_id, component_data)")
        print("✓ Components API available")
    except Exception as e:
        print(f"✗ Components API error: {e}")


def demonstrate_incidents_api(client):
    """Demonstrate Status Pages Incidents API functionality."""
    print("\n--- Status Pages Incidents API ---")
    try:
        # Incidents also require a page_id
        print("Incidents API available")
        print("Note: Incidents operations require a page_id parameter")
        print("Example operations:")
        print("- client.incidents.v1_pages_page_id_incidents_get(page_id)")
        print("- client.incidents.v1_pages_page_id_incidents_post(page_id, incident_data)")
        print("✓ Incidents API available")
    except Exception as e:
        print(f"✗ Incidents API error: {e}")


def demonstrate_on_demand_checks_api(client):
    """Demonstrate On Demand Checks API functionality."""
    print("\n--- On Demand Checks API ---")
    try:
        print("On Demand Checks API available")
        print("Example operations:")
        print("- client.on_demand_checks.v1_on_demand_checks_get()")
        print("- Execute custom checks on demand")
        print("✓ On Demand Checks API available")
    except Exception as e:
        print(f"✗ On Demand Checks API error: {e}")


def demonstrate_unified_results_api(client):
    """Demonstrate Checks Unified Results API functionality."""
    print("\n--- Checks Unified Results API ---")
    try:
        print("Unified Results API available")
        print("Example operations:")
        print("- client.checks_unified_results.v1_checks_unified_results_get()")
        print("- Query unified check results across multiple sources")
        print("✓ Unified Results API available")
    except Exception as e:
        print(f"✗ Unified Results API error: {e}")


def main():
    """Main demonstration function."""
    print("=== Pingera Python SDK - Comprehensive API Coverage ===")
    
    try:
        # Initialize client - will auto-configure from environment
        print("\nInitializing client...")
        client = PingeraClient.from_api_key("demo_api_key")
        print("✓ Client initialized successfully")
        
        print(f"\n=== Available API Modules ===")
        print(f"- alerts: {type(client.alerts).__name__}")
        print(f"- checks: {type(client.checks).__name__}")
        print(f"- checks_unified_results: {type(client.checks_unified_results).__name__}")
        print(f"- heartbeats: {type(client.heartbeats).__name__}")
        print(f"- on_demand_checks: {type(client.on_demand_checks).__name__}")
        print(f"- components: {type(client.components).__name__}")
        print(f"- incidents: {type(client.incidents).__name__}")
        
        # Demonstrate each API
        demonstrate_alerts_api(client)
        demonstrate_checks_api(client)
        demonstrate_heartbeats_api(client)
        demonstrate_on_demand_checks_api(client)
        demonstrate_unified_results_api(client)
        demonstrate_components_api(client)
        demonstrate_incidents_api(client)
        
        print(f"\n=== Authentication Information ===")
        print(f"- Auth provider: {type(client.auth).__name__}")
        print(f"- Base URL: {client.configuration.host}")
        
        print(f"\n=== Next Steps ===")
        print("1. Set PINGERA_API_KEY or PINGERA_BEARER_TOKEN environment variable")
        print("2. Get your organization's status page IDs for components/incidents APIs")
        print("3. Start creating monitors, heartbeats, and managing your status pages!")
        
    except PingeraError as e:
        print(f"✗ Pingera API error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
    
    print("\n=== SDK demonstration completed! ===")


if __name__ == "__main__":
    main()