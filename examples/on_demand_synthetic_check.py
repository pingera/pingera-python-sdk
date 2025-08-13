
#!/usr/bin/env python3
"""
On-demand synthetic check example using Playwright script for pingera.ru

This example demonstrates:
- Creating a synthetic check with Playwright script
- Executing the check on-demand
- Waiting for results and displaying full JSON output
"""

import os
import time
import json
from datetime import datetime

from pingera import ApiClient, Configuration
from pingera.api import OnDemandChecksApi
from pingera.models import ExecuteCustomCheckRequest
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


def create_playwright_script():
    """Create a comprehensive Playwright script for testing pingera.ru"""
    return """
// Comprehensive Playwright test for pingera.ru
const { test, expect } = require('@playwright/test');

test('Basic Screenshot', async ({ page }) => {
  // Navigate to the page
  await page.goto('https://playwright.dev/');

  // Wait for the page to be in a stable state (e.g., network idle)
  await page.waitForLoadState('networkidle');

  // Take page screenshot
  await page.screenshot({ path: 'screenshot.png', fullPage: false });

  console.log('Successfully took a page screenshot.');
});

"""


def wait_for_job_completion(api_client, job_id, max_wait_time=300, poll_interval=5):
    """
    Wait for job completion and return the results.
    
    Args:
        api_client: The API client instance
        job_id: The job ID to monitor
        max_wait_time: Maximum time to wait in seconds (default: 5 minutes)
        poll_interval: How often to check job status in seconds (default: 5 seconds)
    
    Returns:
        dict: The job results
    """
    on_demand_api = OnDemandChecksApi(api_client)
    start_time = time.time()
    
    print(f"⏳ Waiting for job {job_id} to complete...")
    print(f"   Max wait time: {max_wait_time} seconds")
    print(f"   Polling every: {poll_interval} seconds")
    
    while time.time() - start_time < max_wait_time:
        try:
            # Get job status
            job_status = on_demand_api.v1_checks_jobs_job_id_get(job_id)
            
            if hasattr(job_status, 'status'):
                status = getattr(job_status, 'status', 'unknown')
                print(f"   Job status: {status}")
                
                if status in ['completed', 'finished', 'success']:
                    print("✅ Job completed successfully!")
                    return job_status
                elif status in ['failed', 'error']:
                    print("❌ Job failed!")
                    return job_status
                elif status in ['running', 'in_progress', 'executing']:
                    print(f"   Job still running... (elapsed: {int(time.time() - start_time)}s)")
                
        except ApiException as e:
            if e.status == 404:
                print(f"   Job not found yet... (elapsed: {int(time.time() - start_time)}s)")
            else:
                print(f"   Error checking job status: [{e.status}] {e.reason}")
        
        time.sleep(poll_interval)
    
    print(f"⏰ Timeout reached after {max_wait_time} seconds")
    return None


def main():
    """Main function to execute the synthetic check."""
    
    print("=== Pingera On-Demand Synthetic Check Example ===")
    print(f"Target: https://pingera.ru")
    print(f"Check type: Synthetic (Playwright)")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print()

    try:
        with setup_client() as api_client:
            on_demand_api = OnDemandChecksApi(api_client)
            
            # Create the Playwright script
            playwright_script = create_playwright_script()
            
            print("📝 Prepared Playwright script:")
            print(f"   Script length: {len(playwright_script)} characters")
            print(f"   Script includes: navigation, title check, performance monitoring, error detection")
            print()
            
            # Create the check request with pw_script in parameters
            check_request = ExecuteCustomCheckRequest(
                url="https://pingera.ru",
                type="synthetic",
                timeout=30,  # 60 second timeout
                name="Pingera.ru Playwright Check",
                parameters={
                    "pw_script": playwright_script
                }
            )
            
            print("🚀 Executing synthetic check...")
            print(f"   URL: {check_request.url}")
            print(f"   Type: {check_request.type}")
            print(f"   Timeout: {check_request.timeout}s")
            print(f"   Name: {check_request.name}")
            print()
            
            # Execute the check
            response = on_demand_api.v1_checks_execute_post(check_request)
            
            if hasattr(response, 'job_id'):
                job_id = getattr(response, 'job_id')
                print(f"✅ Check submitted successfully!")
                print(f"   Job ID: {job_id}")
                print()
                
                # Wait for completion
                job_result = wait_for_job_completion(api_client, job_id, max_wait_time=300)
                
                if job_result:
                    print("📊 === FULL JOB RESULT (JSON) ===")
                    print()
                    
                    # Convert the response to dictionary and display as formatted JSON
                    result_dict = {}
                    
                    # Extract all attributes from the job_result object, excluding Pydantic internal attributes
                    pydantic_internal_attrs = {
                        'model_fields', 'model_computed_fields', 'model_config', 
                        'model_extra', 'model_fields_set', '__pydantic_core_schema__',
                        '__pydantic_custom_init_subfields__', '__pydantic_decorators__',
                        '__pydantic_generic_metadata__', '__pydantic_init_subclass__',
                        '__pydantic_post_init__', '__pydantic_private__', '__pydantic_serializer__',
                        '__pydantic_validator__', '__pydantic_fields_set__'
                    }
                    
                    for attr_name in dir(job_result):
                        if (not attr_name.startswith('_') and 
                            attr_name not in pydantic_internal_attrs and
                            not callable(getattr(job_result, attr_name, None))):
                            try:
                                attr_value = getattr(job_result, attr_name)
                                if attr_value is not None:
                                    # Handle nested objects that might have to_dict methods
                                    if hasattr(attr_value, 'to_dict') and callable(getattr(attr_value, 'to_dict')):
                                        result_dict[attr_name] = attr_value.to_dict()
                                    elif hasattr(attr_value, '__dict__'):
                                        # Convert objects with __dict__ to dictionaries
                                        result_dict[attr_name] = vars(attr_value)
                                    else:
                                        result_dict[attr_name] = attr_value
                            except Exception as e:
                                print(f"   Warning: Could not extract {attr_name}: {e}")
                    
                    # If the above didn't work, try the built-in to_dict method
                    if not result_dict and hasattr(job_result, 'to_dict'):
                        try:
                            result_dict = job_result.to_dict()
                        except Exception as e:
                            print(f"   Warning: to_dict() failed: {e}")
                    
                    # Last resort: try to access known fields directly
                    if not result_dict:
                        known_fields = ['id', 'status', 'result', 'check_id', 'check_parameters', 
                                      'created_at', 'completed_at', 'started_at', 'error_message', 
                                      'job_type']
                        for field in known_fields:
                            try:
                                value = getattr(job_result, field, None)
                                if value is not None:
                                    result_dict[field] = value
                            except:
                                pass
                    
                    # Pretty print the JSON
                    formatted_json = json.dumps(result_dict, indent=2, default=str, ensure_ascii=False)
                    print(formatted_json)
                    print()
                    
                    # Extract key information
                    status = result_dict.get('status', 'unknown')
                    print(f"📈 === SUMMARY ===")
                    print(f"   Final Status: {status}")
                    
                    if 'results' in result_dict and result_dict['results']:
                        results = result_dict['results']
                        if isinstance(results, list) and len(results) > 0:
                            first_result = results[0]
                            if isinstance(first_result, dict):
                                print(f"   Response Time: {first_result.get('response_time', 'N/A')}ms")
                                print(f"   Success: {first_result.get('success', 'N/A')}")
                                print(f"   Region: {first_result.get('region', 'N/A')}")
                    
                    print(f"   Job ID: {job_id}")
                    print(f"   Execution Time: {datetime.now().isoformat()}")
                    
                else:
                    print("❌ Job did not complete within the timeout period")
                    
            else:
                print("❌ Failed to get job ID from response")
                print("Raw response:")
                print(response)

    except ApiException as e:
        print(f"\n❌ API Error: [{e.status}] {e.reason}")
        if e.status == 401:
            print("   Make sure you have set PINGERA_BEARER_TOKEN or PINGERA_API_KEY")
        elif e.status == 403:
            print("   Your account may not have access to on-demand checks")
        elif e.status == 400:
            print("   Check request parameters may be invalid")
        
        if hasattr(e, 'body') and e.body:
            try:
                error_details = json.loads(e.body)
                print("   Error details:")
                print(f"   {json.dumps(error_details, indent=2)}")
            except:
                print(f"   Raw error body: {e.body}")
                
    except ValueError as e:
        print(f"\n❌ Configuration error: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()

    print("\n=== Example completed ===")


if __name__ == "__main__":
    main()
