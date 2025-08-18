
#!/usr/bin/env python3
"""
Debug script to investigate component creation returning None
"""

import os
from datetime import datetime

from pingera import ApiClient, Configuration
from pingera.api import StatusPagesComponentsApi
from pingera.exceptions import ApiException

# Try different model imports to see which one works
try:
    from pingera.models import Component
    print("✓ Successfully imported Component")
    COMPONENT_MODEL = Component
except ImportError as e:
    print(f"✗ Failed to import Component: {e}")
    COMPONENT_MODEL = None

try:
    from pingera.models import Component1
    print("✓ Successfully imported Component1")
    if COMPONENT_MODEL is None:
        COMPONENT_MODEL = Component1
except ImportError as e:
    print(f"✗ Failed to import Component1: {e}")

try:
    from pingera.models import ComponentCreate
    print("✓ Successfully imported ComponentCreate")
    if COMPONENT_MODEL is None:
        COMPONENT_MODEL = ComponentCreate
except ImportError as e:
    print(f"✗ Failed to import ComponentCreate: {e}")

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

def debug_component_creation():
    """Debug component creation issue."""
    
    PAGE_ID = "tih6xo7z8v7n"  # Your page ID
    
    if COMPONENT_MODEL is None:
        print("❌ No component model available to test")
        return
    
    try:
        with setup_client() as api_client:
            components_api = StatusPagesComponentsApi(api_client)
            
            print(f"\n=== Debugging Component Creation ===")
            print(f"Using model: {COMPONENT_MODEL.__name__}")
            print(f"Page ID: {PAGE_ID}")
            
            # Create component
            new_component = COMPONENT_MODEL(
                name="API Server Debug Test",
                description="Debug test component",
                status="operational"
            )
            
            print(f"\nComponent data:")
            print(f"  Type: {type(new_component)}")
            print(f"  Name: {getattr(new_component, 'name', 'N/A')}")
            print(f"  Description: {getattr(new_component, 'description', 'N/A')}")
            print(f"  Status: {getattr(new_component, 'status', 'N/A')}")
            
            # Check if component has to_dict method
            if hasattr(new_component, 'to_dict'):
                print(f"  to_dict(): {new_component.to_dict()}")
            
            print(f"\n=== Making API Call ===")
            
            # Make the API call
            response = components_api.v1_pages_page_id_components_post(
                page_id=PAGE_ID,
                component=new_component
            )
            
            print(f"Response received:")
            print(f"  Raw response: {response}")
            print(f"  Response type: {type(response)}")
            print(f"  Response is None: {response is None}")
            
            # Try to extract attributes if response exists
            if response is not None:
                print(f"\nResponse attributes:")
                if hasattr(response, '__dict__'):
                    for attr, value in vars(response).items():
                        print(f"  {attr}: {value}")
                else:
                    print("  Response has no __dict__")
                
                # Try common attributes
                for attr in ['id', 'name', 'description', 'status', 'created_at']:
                    if hasattr(response, attr):
                        print(f"  {attr}: {getattr(response, attr)}")
            
            # Also try to list components to see if it was created
            print(f"\n=== Verifying Creation ===")
            components_list = components_api.v1_pages_page_id_components_get(PAGE_ID)
            
            if hasattr(components_list, 'data') and components_list.data:
                components = components_list.data
                print(f"Found {len(components)} components:")
                for comp in components[-3:]:  # Show last 3
                    comp_name = getattr(comp, 'name', 'N/A')
                    comp_id = getattr(comp, 'id', 'N/A')
                    print(f"  - {comp_name} (ID: {comp_id})")
            
    except ApiException as e:
        print(f"\n❌ API Error: [{e.status}] {e.reason}")
        if hasattr(e, 'body'):
            print(f"Error body: {e.body}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_component_creation()
