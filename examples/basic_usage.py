#!/usr/bin/env python3
"""
Basic usage example for the Pingera Python SDK using the generated OpenAPI client.

This example demonstrates:
- Client initialization with authentication
- Basic API operations using the generated client
- Error handling
"""

import os
from datetime import datetime

from pingera import ApiClient, Configuration
from pingera.api import StatusPagesComponentsApi, StatusPagesIncidentsApi, ChecksApi
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
    """Main example function."""

    print("=== Pingera Generated Client Example ===\n")

    try:
        # Initialize the API client
        api_client = setup_client()

        with api_client:
            print("\n=== Testing API Operations ===")

            # Initialize API instances
            components_api = StatusPagesComponentsApi(api_client)
            incidents_api = StatusPagesIncidentsApi(api_client)
            checks_api = ChecksApi(api_client)

            # List checks
            print("\n1. Listing checks...")
            try:
                checks_response = checks_api.v1_checks_get(page=1, page_size=5)
                if hasattr(checks_response, 'checks') and checks_response.checks:
                    print(f"✓ Found {len(checks_response.checks)} checks")
                    for check in checks_response.checks[:3]:
                        status = getattr(check, 'status', 'unknown')
                        check_type = getattr(check, 'type', 'unknown')
                        name = getattr(check, 'name', 'unnamed')
                        print(f"  - {name} ({check_type}): {status}")
                else:
                    print("✓ No checks found or empty response")
            except ApiException as e:
                print(f"✗ Failed to list checks: [{e.status}] {e.reason}")
            except Exception as e:
                print(f"✗ Failed to list checks: {e}")

            # Note: For components and incidents, you'll need a page_id
            print("\n2. Components and incidents require a page_id...")
            print("   To use these endpoints, you need to:")
            print("   - Get your organization's status pages first")
            print("   - Use the page_id from those results")
            print("   - Example: components_api.v1_pages_page_id_components_get('your_page_id')")

            # Example of error handling
            print("\n3. Testing error handling...")
            try:
                # This will likely fail without proper page_id
                components_api.v1_pages_page_id_components_get("invalid_page_id")
            except ApiException as e:
                print(f"✓ Error handling working: [{e.status}] {e.reason}")
            except Exception as e:
                print(f"! Unexpected error: {e}")

            print("\n=== Generated client example completed! ===")

    except Exception as e:
        print(f"\n✗ Setup error: {e}")
        print("Make sure you have set PINGERA_BEARER_TOKEN or PINGERA_API_KEY environment variable.")


if __name__ == "__main__":
    main()