# pingera.OnDemandChecksApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_checks_check_id_execute_post**](OnDemandChecksApi.md#v1_checks_check_id_execute_post) | **POST** /v1/checks/{check_id}/execute | Execute an existing monitor check immediately
[**v1_checks_execute_post**](OnDemandChecksApi.md#v1_checks_execute_post) | **POST** /v1/checks/execute | Execute a custom check with user-provided parameters
[**v1_checks_jobs_get**](OnDemandChecksApi.md#v1_checks_jobs_get) | **GET** /v1/checks/jobs | List on-demand check jobs
[**v1_checks_jobs_job_id_get**](OnDemandChecksApi.md#v1_checks_jobs_job_id_get) | **GET** /v1/checks/jobs/{job_id} | Get job status and results


# **v1_checks_check_id_execute_post**
> ExecuteExistingCheckResponse v1_checks_check_id_execute_post(check_id)

Execute an existing monitor check immediately

Execute an existing monitor check immediately on-demand. This endpoint queues the check for immediate execution and returns a job ID for tracking progress and results.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.execute_existing_check_response import ExecuteExistingCheckResponse
from pingera.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pingera.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = pingera.Configuration(
    host = "https://api.pingera.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = pingera.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pingera.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pingera.OnDemandChecksApi(api_client)
    check_id = 'check_id_example' # str | 

    try:
        # Execute an existing monitor check immediately
        api_response = api_instance.v1_checks_check_id_execute_post(check_id)
        print("The response of OnDemandChecksApi->v1_checks_check_id_execute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnDemandChecksApi->v1_checks_check_id_execute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**|  | 

### Return type

[**ExecuteExistingCheckResponse**](ExecuteExistingCheckResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request - Invalid regions or validation error |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Credit limit exceeded or insufficient permissions |  -  |
**404** | Check not found or you do not have permission to access it |  -  |
**500** | Internal Server Error - Failed to queue check for execution |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_checks_execute_post**
> ExecuteExistingCheckResponse v1_checks_execute_post(execute_custom_check_request)

Execute a custom check with user-provided parameters

Execute a custom check with user-provided parameters on-demand. This endpoint allows you to run a one-time check without saving the configuration. The check parameters are validated and the check is queued for immediate execution.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.execute_custom_check_request import ExecuteCustomCheckRequest
from pingera.models.execute_existing_check_response import ExecuteExistingCheckResponse
from pingera.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pingera.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = pingera.Configuration(
    host = "https://api.pingera.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = pingera.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pingera.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pingera.OnDemandChecksApi(api_client)
    execute_custom_check_request = pingera.ExecuteCustomCheckRequest() # ExecuteCustomCheckRequest | Custom check configuration data

    try:
        # Execute a custom check with user-provided parameters
        api_response = api_instance.v1_checks_execute_post(execute_custom_check_request)
        print("The response of OnDemandChecksApi->v1_checks_execute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnDemandChecksApi->v1_checks_execute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execute_custom_check_request** | [**ExecuteCustomCheckRequest**](ExecuteCustomCheckRequest.md)| Custom check configuration data | 

### Return type

[**ExecuteExistingCheckResponse**](ExecuteExistingCheckResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Validation error - Invalid request data |  -  |
**202** | Accepted |  -  |
**400** | Bad Request - Invalid parameters, missing pw_script for multistep checks, or invalid regions |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Credit limit exceeded |  -  |
**500** | Internal Server Error - Failed to queue custom check for execution |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_checks_jobs_get**
> JobListResponse v1_checks_jobs_get(page=page, per_page=per_page, status=status)

List on-demand check jobs

List on-demand check jobs for the current organization with pagination support. Supports filtering by job status and ordering by creation date (newest first).

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.job_list_response import JobListResponse
from pingera.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pingera.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = pingera.Configuration(
    host = "https://api.pingera.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = pingera.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pingera.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pingera.OnDemandChecksApi(api_client)
    page = 1 # int | Page number for pagination (starting from 1). (optional) (default to 1)
    per_page = 20 # int | Number of jobs per page (maximum 100). (optional) (default to 20)
    status = 'status_example' # str | Filter jobs by status. (optional)

    try:
        # List on-demand check jobs
        api_response = api_instance.v1_checks_jobs_get(page=page, per_page=per_page, status=status)
        print("The response of OnDemandChecksApi->v1_checks_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnDemandChecksApi->v1_checks_jobs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number for pagination (starting from 1). | [optional] [default to 1]
 **per_page** | **int**| Number of jobs per page (maximum 100). | [optional] [default to 20]
 **status** | **str**| Filter jobs by status. | [optional] 

### Return type

[**JobListResponse**](JobListResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request - Invalid pagination parameters or status filter |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error - Database error occurred |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_checks_jobs_job_id_get**
> CheckJob v1_checks_jobs_job_id_get(job_id)

Get job status and results

Retrieve the status and results of a specific on-demand check job. Returns detailed information about the job execution including results, timing information, and any error messages.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.check_job import CheckJob
from pingera.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pingera.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = pingera.Configuration(
    host = "https://api.pingera.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = pingera.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pingera.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pingera.OnDemandChecksApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Get job status and results
        api_response = api_instance.v1_checks_jobs_job_id_get(job_id)
        print("The response of OnDemandChecksApi->v1_checks_jobs_job_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnDemandChecksApi->v1_checks_jobs_job_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**CheckJob**](CheckJob.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - Authentication required |  -  |
**404** | Job not found or you do not have permission to access it |  -  |
**500** | Internal Server Error - Database error occurred |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

