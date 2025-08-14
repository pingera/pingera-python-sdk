
#!/usr/bin/env python3
"""
Status pages management example using the Pingera generated OpenAPI client.

This example demonstrates:
- Listing status pages
- Creating and updating status pages
- Managing status page settings
- Getting page details
"""

import os
from datetime import datetime

from pingera import ApiClient, Configuration
from pingera.api import StatusPagesApi
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
    """Status pages management example."""

    print("=== Pingera Status Pages Management Example ===\n")

    try:
        with setup_client() as api_client:
            status_pages_api = StatusPagesApi(api_client)

            # List existing status pages
            print("1. Listing existing status pages...")
            try:
                pages_response = status_pages_api.v1_pages_get()
                
                # Handle different response formats
                if hasattr(pages_response, 'data') and pages_response.data:
                    pages = pages_response.data
                elif hasattr(pages_response, 'pages') and pages_response.pages:
                    pages = pages_response.pages
                elif isinstance(pages_response, list):
                    pages = pages_response
                else:
                    pages = []

                if pages:
                    print(f"✓ Found {len(pages)} status pages:")
                    for page in pages:
                        name = getattr(page, 'name', 'unnamed')
                        page_id = getattr(page, 'id', 'unknown')
                        status = getattr(page, 'status', 'unknown')
                        domain = getattr(page, 'domain', getattr(page, 'subdomain', 'N/A'))
                        created_at = getattr(page, 'created_at', 'unknown')
                        
                        print(f"  - {name} (ID: {page_id})")
                        print(f"    Status: {status}")
                        print(f"    Domain: {domain}")
                        print(f"    Created: {created_at}")
                        print()
                else:
                    print("✓ No status pages found")

            except ApiException as e:
                print(f"✗ Failed to list status pages: [{e.status}] {e.reason}")
                if e.status == 401:
                    print("   Make sure you have set PINGERA_BEARER_TOKEN or PINGERA_API_KEY")
                elif e.status == 403:
                    print("   Your account may not have access to status pages management")
                return

            # Get specific page details (if pages exist)
            if pages and len(pages) > 0:
                first_page = pages[0]
                page_id = getattr(first_page, 'id', None)
                
                if page_id:
                    print(f"2. Getting details for page: {getattr(first_page, 'name', 'unnamed')} ({page_id})...")
                    try:
                        page_details = status_pages_api.v1_pages_page_id_get(page_id)
                        
                        print(f"✓ Retrieved page details:")
                        print(f"   Name: {getattr(page_details, 'name', 'N/A')}")
                        print(f"   Description: {getattr(page_details, 'description', 'N/A')}")
                        print(f"   Domain: {getattr(page_details, 'domain', getattr(page_details, 'subdomain', 'N/A'))}")
                        print(f"   Status: {getattr(page_details, 'status', 'N/A')}")
                        print(f"   Theme: {getattr(page_details, 'theme', 'N/A')}")
                        print(f"   Custom CSS: {bool(getattr(page_details, 'custom_css', False))}")
                        print(f"   Notifications: {getattr(page_details, 'notifications_enabled', 'N/A')}")
                        
                    except ApiException as e:
                        print(f"✗ Failed to get page details: [{e.status}] {e.reason}")

            # Example: Create a test status page (commented out to avoid creating actual pages)
            print("\n3. Status page creation example (not executed)...")
            print("   To create a new status page, you would use:")
            print("   ```python")
            print("   from pingera.models import StatusPageCreate")
            print("   ")
            print("   new_page = StatusPageCreate(")
            print("       name='Test Status Page',")
            print("       description='Test page created by Python SDK',")
            print("       subdomain='test-sdk',")
            print("       theme='light'")
            print("   )")
            print("   ")
            print("   created_page = status_pages_api.v1_pages_post(new_page)")
            print("   ```")

            # Show available operations
            print("\n4. Available status page operations:")
            print("   - List pages: status_pages_api.v1_pages_get()")
            print("   - Get page: status_pages_api.v1_pages_page_id_get(page_id)")
            print("   - Create page: status_pages_api.v1_pages_post(page_data)")
            print("   - Update page: status_pages_api.v1_pages_page_id_put(page_id, page_data)")
            print("   - Delete page: status_pages_api.v1_pages_page_id_delete(page_id)")

            print("\n=== Status pages management example completed! ===")

    except ValueError as e:
        print(f"\n✗ Configuration error: {e}")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
