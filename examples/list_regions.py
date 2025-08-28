
#!/usr/bin/env python3
"""
Example demonstrating how to fetch available regions for check execution.

This example shows:
- Getting all available regions
- Filtering regions by check type
- Understanding region data structure
"""

import os
from pingera import ApiClient, Configuration
from pingera.api import ChecksApi
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
        raise ValueError("Authentication required: Set PINGERA_BEARER_TOKEN or PINGERA_API_KEY")

    return ApiClient(configuration)


def main():
    """Demonstrate regions API functionality."""
    
    print("=== Pingera Regions API Example ===\n")
    
    try:
        with setup_client() as api_client:
            checks_api = ChecksApi(api_client)
            
            # Get all available regions
            print("1. Getting all available regions...")
            try:
                all_regions = checks_api.v1_checks_get_regions_get()
                total_regions = getattr(all_regions, 'total_regions', 0)
                regions_list = getattr(all_regions, 'regions', [])
                
                print(f"✓ Found {total_regions} total regions")
                print("\nAll available regions:")
                for region in regions_list:
                    region_id = getattr(region, 'id', 'unknown')
                    region_name = getattr(region, 'name', 'unknown')
                    region_location = getattr(region, 'location', 'unknown')
                    print(f"  - {region_id}: {region_name} ({region_location})")
                    
            except ApiException as e:
                print(f"✗ Failed to get regions: [{e.status}] {e.reason}")
                return
            
            # Get regions filtered by check type
            check_types = ["web", "api", "ssl", "tcp", "synthetic", "multistep"]
            
            print(f"\n2. Getting regions by check type...")
            for check_type in check_types:
                try:
                    filtered_regions = checks_api.v1_checks_get_regions_get(check_type=check_type)
                    regions_list = getattr(filtered_regions, 'regions', [])
                    total = getattr(filtered_regions, 'total_regions', 0)
                    
                    print(f"\n{check_type.upper()} checks - {total} regions:")
                    for region in regions_list:
                        region_id = getattr(region, 'id', 'unknown')
                        region_name = getattr(region, 'name', 'unknown')
                        print(f"  - {region_id}: {region_name}")
                        
                except ApiException as e:
                    print(f"✗ Failed to get {check_type} regions: [{e.status}] {e.reason}")
            
            # Example usage for on-demand checks
            print(f"\n3. Example: Using regions for on-demand checks...")
            if regions_list:
                example_region = regions_list[0]
                region_id = getattr(example_region, 'id', 'us-east-1')
                print(f"Example region for checks: {region_id}")
                print(f"You can use this in ExecuteCustomCheckRequest:")
                print(f"""
from pingera.models import ExecuteCustomCheckRequest

check_request = ExecuteCustomCheckRequest(
    url="https://example.com",
    type="web",
    regions=["{region_id}"]  # Use regions from the API
)
""")
            
            print("\n=== Regions example completed! ===")
            
    except ValueError as e:
        print(f"\n✗ Configuration error: {e}")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")


if __name__ == "__main__":
    main()
