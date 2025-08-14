#!/usr/bin/env python3
"""
Component management example using the Pingera generated OpenAPI client.

This example demonstrates:
- Listing status page components
- Creating and updating components
- Managing component status
- Bulk operations
"""

import os
from datetime import datetime

from pingera import ApiClient, Configuration
from pingera.api import StatusPagesComponentsApi
from pingera.models import Component1, ComponentUptimeBulkRequest
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
        configuration.api_key['Authorization'] = f"Bearer {api_key}"
    else:
        raise ValueError("Authentication required: Set PINGERA_BEARER_TOKEN or PINGERA_API_KEY")

    return ApiClient(configuration)


def main():
    """Component management example."""

    print("=== Pingera Component Management Example ===\n")

    # Note: You'll need to replace 'your_page_id' with an actual page ID
    PAGE_ID = os.getenv("PINGERA_PAGE_ID", "your_page_id")

    if PAGE_ID == "your_page_id":
        print("⚠️  Please set PINGERA_PAGE_ID environment variable with your actual page ID")
        print("   You can get this from your Pingera dashboard or by listing your pages first")
        return

    try:
        with setup_client() as api_client:
            components_api = StatusPagesComponentsApi(api_client)

            print(f"Working with page ID: {PAGE_ID}\n")

            # List existing components
            print("1. Listing existing components...")
            try:
                components_response = components_api.v1_pages_page_id_components_get(PAGE_ID)
                components = getattr(components_response, 'data', [])

                if components:
                    print(f"✓ Found {len(components)} components:")
                    for component in components:
                        name = getattr(component, 'name', 'unnamed')
                        status = getattr(component, 'status', 'unknown')
                        comp_id = getattr(component, 'id', 'unknown')
                        print(f"  - {name} ({comp_id}): {status}")
                else:
                    print("✓ No components found")

            except ApiException as e:
                print(f"✗ Failed to list components: [{e.status}] {e.reason}")
                if e.status == 404:
                    print("   Make sure the page ID is correct and you have access to it")
                return

            # Create a new component (example)
            print("\n2. Creating a new component...")
            try:
                new_component = Component1(
                    name=f"Test Component {datetime.now().strftime('%H:%M:%S')}",
                    description="Created by Python SDK example",
                    status="operational"
                )

                created = components_api.v1_pages_page_id_components_post(PAGE_ID, new_component)
                comp_id = getattr(created, 'id', None)
                comp_name = getattr(created, 'name', 'unknown')

                if comp_id:
                    print(f"✓ Created component: {comp_name} (ID: {comp_id})")

                    # Update the component status
                    print("   Updating component status...")
                    updated_component = Component1(
                        name=comp_name,
                        description="Updated by Python SDK",
                        status="under_maintenance"
                    )

                    updated = components_api.v1_pages_page_id_components_component_id_put(
                        PAGE_ID, comp_id, updated_component
                    )
                    print(f"✓ Updated status to: {getattr(updated, 'status', 'unknown')}")

                    # Delete the test component
                    print("   Cleaning up test component...")
                    components_api.v1_pages_page_id_components_component_id_delete(PAGE_ID, comp_id)
                    print("✓ Test component deleted")
                else:
                    print("✗ Failed to get component ID from response")

            except ApiException as e:
                print(f"✗ Failed to create/manage component: [{e.status}] {e.reason}")

            # Demonstrate bulk uptime calculation (if components exist)
            print("\n3. Bulk uptime calculation...")
            try:
                if components:
                    # Get IDs of first few components
                    component_ids = [
                        getattr(comp, 'id') for comp in components[:3]
                        if hasattr(comp, 'id')
                    ]

                    if component_ids:
                        bulk_request = ComponentUptimeBulkRequest(component_ids=component_ids)
                        uptime_response = components_api.v1_pages_page_id_components_uptime_bulk_post(
                            PAGE_ID, bulk_request
                        )
                        print(f"✓ Bulk uptime calculation completed")
                        print(f"   Response: {type(uptime_response)}")
                    else:
                        print("! No component IDs available for bulk calculation")
                else:
                    print("! No components available for bulk uptime calculation")

            except ApiException as e:
                print(f"✗ Failed bulk uptime calculation: [{e.status}] {e.reason}")

            print("\n=== Component management example completed! ===")

    except ValueError as e:
        print(f"\n✗ Configuration error: {e}")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")


if __name__ == "__main__":
    main()