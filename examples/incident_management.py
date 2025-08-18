#!/usr/bin/env python3
"""
Incident management example using the Pingera generated OpenAPI client.

This example demonstrates:
- Listing incidents
- Creating and updating incidents
- Managing incident updates
- Scheduling maintenance windows
"""

import os
from datetime import datetime, timedelta

from pingera import ApiClient, Configuration
from pingera.api import StatusPagesIncidentsApi
from pingera.models import IncidentCreate
from pingera.exceptions import ApiException


def setup_client():
    """Set up the API client with authentication."""
    configuration = Configuration()
    configuration.host = "https://api.pingera.ru"

    bearer_token = os.getenv("PINGERA_BEARER_TOKEN")
    api_key = os.getenv("PINGERA_API_KEY")

    print(f"🔧 Debug: API Host: {configuration.host}")
    print(f"🔧 Debug: Bearer token present: {bool(bearer_token)}")
    print(f"🔧 Debug: API key present: {bool(api_key)}")

    if bearer_token:
        configuration.access_token = bearer_token
        print("🔧 Debug: Using Bearer token authentication")
    elif api_key:
        configuration.api_key['apiKeyAuth'] = api_key
        print("🔧 Debug: Using API key authentication")
        print(f"🔧 Debug: API key starts with: {api_key[:10]}..." if len(api_key) > 10 else f"🔧 Debug: API key: {api_key}")
    else:
        raise ValueError("Authentication required: Set PINGERA_BEARER_TOKEN or PINGERA_API_KEY")

    return ApiClient(configuration)


def main():
    """Incident management example."""

    print("=== Pingera Incident Management Example ===\n")

    # Note: You'll need to replace 'your_page_id' with an actual page ID
    PAGE_ID = os.getenv("PINGERA_PAGE_ID", "your_page_id")

    if PAGE_ID == "your_page_id":
        print("⚠️  Please set PINGERA_PAGE_ID environment variable with your actual page ID")
        print("   You can get this from your Pingera dashboard")
        return

    try:
        with setup_client() as api_client:
            incidents_api = StatusPagesIncidentsApi(api_client)

            print(f"Working with page ID: {PAGE_ID}\n")

            # List existing incidents
            print("1. Listing existing incidents...")
            try:
                incidents_response = incidents_api.v1_pages_page_id_incidents_get(PAGE_ID)
                incidents = getattr(incidents_response, 'data', [])

                if incidents:
                    print(f"✓ Found {len(incidents)} incidents:")
                    for incident in incidents[:5]:  # Show first 5
                        name = getattr(incident, 'name', 'unnamed')
                        status = getattr(incident, 'status', 'unknown')
                        impact = getattr(incident, 'impact', 'unknown')
                        incident_id = getattr(incident, 'id', 'unknown')
                        created_at = getattr(incident, 'created_at', 'unknown')
                        print(f"  - {name} ({incident_id})")
                        print(f"    Status: {status}, Impact: {impact}")
                        print(f"    Created: {created_at}")
                else:
                    print("✓ No incidents found")

            except ApiException as e:
                print(f"✗ Failed to list incidents: [{e.status}] {e.reason}")
                if e.status == 404:
                    print("   Make sure the page ID is correct and you have access to it")
                return

            # Create a new incident (example)
            print("\n2. Creating a new incident...")
            try:
                now = datetime.now()
                new_incident = IncidentCreate(
                    name=f"Test Incident {now.strftime('%H:%M:%S')}",
                    body="This is a test incident created by the Python SDK",
                    status="investigating",
                    impact="minor",
                    components={}  # Add component statuses if needed
                )

                created = incidents_api.v1_pages_page_id_incidents_post(PAGE_ID, new_incident)
                incident_id = getattr(created, 'id', None)
                incident_name = getattr(created, 'name', 'unknown')

                if incident_id:
                    print(f"✓ Created incident: {incident_name} (ID: {incident_id})")

                    # Try to update incident status (if update method is available)
                    print("   Attempting to update incident...")
                    try:
                        # Get the current incident data
                        current_incident = incidents_api.v1_pages_page_id_incidents_incident_id_get(PAGE_ID, incident_id)
                        print(f"   Current status: {getattr(current_incident, 'status', 'unknown')}")
                        
                        # Note: Direct incident updates may require different model structure
                        # The OpenAPI spec may not include incident update models
                        print("   ℹ️  Incident updates may require manual API calls or different models")
                        
                    except Exception as e:
                        print(f"   ! Could not retrieve incident details: {e}")

                    # Clean up - delete the test incident
                    print("   Cleaning up test incident...")
                    incidents_api.v1_pages_page_id_incidents_incident_id_delete(PAGE_ID, incident_id)
                    print("✓ Test incident deleted")
                else:
                    print("✗ Failed to get incident ID from response")

            except ApiException as e:
                print(f"✗ Failed to create/manage incident: [{e.status}] {e.reason}")

            # Example: Show incident details and available operations
            print("\n3. Incident management capabilities...")
            print("   Available incident operations:")
            print("   ✓ Create incidents (v1_pages_page_id_incidents_post)")
            print("   ✓ List incidents (v1_pages_page_id_incidents_get)")
            print("   ✓ Get incident details (v1_pages_page_id_incidents_incident_id_get)")
            print("   ✓ Delete incidents (v1_pages_page_id_incidents_incident_id_delete)")
            print("   ⚠️  Incident updates may require manual API calls")
            print("   ⚠️  Scheduled maintenance may require specific model fields")
            
            # Show valid incident status values
            print("\n   Valid incident status values:")
            print("   - 'investigating' - Issue is being investigated")
            print("   - 'identified' - Root cause has been identified") 
            print("   - 'monitoring' - Fix has been applied, monitoring results")
            print("   - 'resolved' - Issue has been fully resolved")
            print("\n   Note: 'scheduled' is not a valid status for regular incidents")
            print("   Scheduled maintenance may require different endpoints or models")
            
            # Try incident status progression example
            try:
                print("\n   Demonstrating incident status progression...")
                
                # Create an incident in investigating status
                progression_incident = IncidentCreate(
                    name="API Response Time Issue",
                    body="Users are experiencing slow API response times.",
                    status="investigating",
                    impact="minor",
                    components={}
                )

                created = incidents_api.v1_pages_page_id_incidents_post(PAGE_ID, progression_incident)
                incident_id = getattr(created, 'id', None)

                if incident_id:
                    print(f"   ✓ Created incident for status progression (ID: {incident_id})")
                    
                    # Note about status updates
                    print("   ℹ️  To update incident status, you would typically:")
                    print("   1. Get current incident data")
                    print("   2. Modify the status field")
                    print("   3. Use PUT endpoint to update (if available)")
                    print("   4. Or create incident updates with new status information")
                    
                    # Clean up
                    print("   Cleaning up progression test incident...")
                    incidents_api.v1_pages_page_id_incidents_incident_id_delete(PAGE_ID, incident_id)
                    print("   ✓ Test incident deleted")
                else:
                    print("   ✗ Failed to create progression test incident")

            except ApiException as e:
                print(f"   ✗ Failed incident progression example: [{e.status}] {e.reason}")
            except Exception as e:
                print(f"   ✗ Unexpected error in progression example: {e}")

            print("\n=== Incident management example completed! ===")

    except ValueError as e:
        print(f"\n✗ Configuration error: {e}")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")


if __name__ == "__main__":
    main()