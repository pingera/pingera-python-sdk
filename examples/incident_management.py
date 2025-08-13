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

from pingera_generated import ApiClient, Configuration
from pingera_generated.api import StatusPagesIncidentsApi
from pingera_generated.models import IncidentCreate, IncidentUpdateCreate, IncidentUpdateEdit
from pingera_generated.exceptions import ApiException


def setup_client():
    """Set up the API client with authentication."""
    configuration = Configuration()
    configuration.host = "https://api.pingera.ru"

    bearer_token = os.getenv("PINGERA_BEARER_TOKEN")
    api_key = os.getenv("PINGERA_API_KEY")

    if bearer_token:
        configuration.access_token = bearer_token
    elif api_key:
        configuration.api_key['Authorization'] = f"Bearer {api_key}"
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

                    # Add an incident update
                    print("   Adding incident update...")
                    update = IncidentUpdateCreate(
                        body="We are investigating the issue and will provide updates shortly.",
                        status="investigating"
                    )

                    update_response = incidents_api.v1_pages_page_id_incidents_incident_id_updates_post(
                        PAGE_ID, incident_id, update
                    )
                    print("✓ Added incident update")

                    # Update incident status
                    print("   Updating incident status...")
                    status_update = IncidentUpdateEdit(
                        name=incident_name,
                        status="monitoring"
                    )

                    updated = incidents_api.v1_pages_page_id_incidents_incident_id_put(
                        PAGE_ID, incident_id, status_update
                    )
                    print(f"✓ Updated status to: {getattr(updated, 'status', 'unknown')}")

                    # Resolve the incident
                    print("   Resolving incident...")
                    resolve_update = IncidentUpdateCreate(
                        body="The issue has been resolved. All services are operating normally.",
                        status="resolved"
                    )

                    incidents_api.v1_pages_page_id_incidents_incident_id_updates_post(
                        PAGE_ID, incident_id, resolve_update
                    )
                    print("✓ Incident resolved")

                    # Clean up - delete the test incident
                    print("   Cleaning up test incident...")
                    incidents_api.v1_pages_page_id_incidents_incident_id_delete(PAGE_ID, incident_id)
                    print("✓ Test incident deleted")
                else:
                    print("✗ Failed to get incident ID from response")

            except ApiException as e:
                print(f"✗ Failed to create/manage incident: [{e.status}] {e.reason}")

            # Example: Create a scheduled maintenance (future)
            print("\n3. Scheduled maintenance example...")
            try:
                future_time = datetime.now() + timedelta(hours=1)
                end_time = future_time + timedelta(hours=2)

                maintenance = IncidentCreate(
                    name="Scheduled Database Maintenance",
                    body="We will be performing scheduled maintenance on our database servers.",
                    status="scheduled",
                    impact="minor",
                    scheduled_for=future_time.isoformat(),
                    scheduled_until=end_time.isoformat(),
                    auto_transition_to_maintenance_state=True,
                    auto_transition_to_operational_state=True,
                    components={}
                )

                scheduled = incidents_api.v1_pages_page_id_incidents_post(PAGE_ID, maintenance)
                maintenance_id = getattr(scheduled, 'id', None)

                if maintenance_id:
                    print(f"✓ Scheduled maintenance created (ID: {maintenance_id})")
                    print(f"   Starts: {future_time}")
                    print(f"   Ends: {end_time}")

                    # Clean up the scheduled maintenance
                    print("   Cleaning up scheduled maintenance...")
                    incidents_api.v1_pages_page_id_incidents_incident_id_delete(PAGE_ID, maintenance_id)
                    print("✓ Scheduled maintenance deleted")
                else:
                    print("✗ Failed to create scheduled maintenance")

            except ApiException as e:
                print(f"✗ Failed to create scheduled maintenance: [{e.status}] {e.reason}")

            print("\n=== Incident management example completed! ===")

    except ValueError as e:
        print(f"\n✗ Configuration error: {e}")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")


if __name__ == "__main__":
    main()