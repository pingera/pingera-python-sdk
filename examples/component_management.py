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
from pingera.models import Component, ComponentUptimeBulkRequest, Component1
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
                # Get the actual raw response using the with_raw_response method
                import pingera

                # Let's make a direct API call to see the raw HTTP response
                print("🔧 Debug: Making direct API call...")

                # Access the underlying HTTP client to see raw response
                with api_client as client:
                    # Get the configuration to see what URL will be called
                    config = client.configuration
                    url = f"{config.host}/v1/pages/{PAGE_ID}/components"
                    headers = {
                        'User-Agent': 'OpenAPI-Generator/1.0.0/python',
                        'Accept': 'application/json'
                    }

                    # Add authentication header
                    if config.api_key and 'apiKeyAuth' in config.api_key:
                        headers['Authorization'] = config.api_key['apiKeyAuth']
                    elif config.access_token:
                        headers['Authorization'] = f"Bearer {config.access_token}"

                    print(f"🔧 Debug: URL: {url}")
                    print(f"🔧 Debug: Headers: {headers}")

                    # Make raw HTTP request to see what we get
                    import httpx
                    raw_response = httpx.get(url, headers=headers, timeout=30)
                    print(f"🔧 Debug: Raw HTTP Status: {raw_response.status_code}")
                    print(f"🔧 Debug: Raw HTTP Headers: {dict(raw_response.headers)}")
                    print(f"🔧 Debug: Raw HTTP Content: {raw_response.text[:500]}...")

                # Now try the SDK call
                components_response = components_api.v1_pages_page_id_components_get(PAGE_ID)

                # Debug the response structure
                print(f"🔧 Debug: SDK Response type: {type(components_response)}")
                if components_response is not None:
                    print(f"🔧 Debug: SDK Response attributes: {dir(components_response)}")

                # Try different ways to access the data
                components = None
                if components_response is None:
                    print("🔧 Debug: SDK returned None - this indicates a deserialization issue")
                    components = []
                elif hasattr(components_response, 'data'):
                    components = components_response.data
                    print(f"🔧 Debug: Found 'data' attribute with {len(components) if components else 0} items")
                elif hasattr(components_response, 'components'):
                    components = components_response.components
                    print(f"🔧 Debug: Found 'components' attribute with {len(components) if components else 0} items")
                elif isinstance(components_response, list):
                    components = components_response
                    print(f"🔧 Debug: Response is a list with {len(components)} items")
                else:
                    # Check if the response itself is the components list
                    try:
                        # Try to iterate to see if it's iterable
                        components = list(components_response) if components_response else []
                        print(f"🔧 Debug: Converted response to list with {len(components)} items")
                    except:
                        print(f"🔧 Debug: Could not convert response to list")
                        components = []

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
                new_component = Component(
                    name=f"Test Component {datetime.now().strftime('%H:%M:%S')}",
                    description="Created by Python SDK example",
                    status="operational",
                    start_date=datetime.now().strftime('%Y-%m-%d')
                )

                print(f"   Creating component: {new_component}")
                print(f"   Component type: {type(new_component)}")

                # Debug the API call
                created = components_api.v1_pages_page_id_components_post(PAGE_ID, new_component)
                print(f"   Raw response: {created}")
                print(f"   Response type: {type(created)}")
                comp_id = getattr(created, 'id', None)
                comp_name = getattr(created, 'name', 'unknown')

                if comp_id:
                    print(f"✓ Created component: {comp_name} (ID: {comp_id})")

                    # Update the component status
                    print("   Updating component status...")
                    comp_update = Component1(
                        name=comp_name,
                        description="Updated by Python SDK example",
                        status="degraded_performance"
                    )

                    updated = components_api.v1_pages_page_id_components_component_id_put(
                        PAGE_ID, comp_id, comp_update
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