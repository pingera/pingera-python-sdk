# pingera.ChecksApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_checks_check_id_delete**](ChecksApi.md#v1_checks_check_id_delete) | **DELETE** /v1/checks/{check_id} | Delete a monitor check
[**v1_checks_check_id_get**](ChecksApi.md#v1_checks_check_id_get) | **GET** /v1/checks/{check_id} | Get a specific monitor check
[**v1_checks_check_id_patch**](ChecksApi.md#v1_checks_check_id_patch) | **PATCH** /v1/checks/{check_id} | Update a monitor check
[**v1_checks_check_id_results_check_result_id_get**](ChecksApi.md#v1_checks_check_id_results_check_result_id_get) | **GET** /v1/checks/{check_id}/results/{check_result_id} | Get a specific check result
[**v1_checks_check_id_results_get**](ChecksApi.md#v1_checks_check_id_results_get) | **GET** /v1/checks/{check_id}/results | Get results for a specific check
[**v1_checks_check_id_status_history_get**](ChecksApi.md#v1_checks_check_id_status_history_get) | **GET** /v1/checks/{check_id}/status-history | Get status history for a check
[**v1_checks_check_id_uptime_get**](ChecksApi.md#v1_checks_check_id_uptime_get) | **GET** /v1/checks/{check_id}/uptime | Get check uptime
[**v1_checks_get**](ChecksApi.md#v1_checks_get) | **GET** /v1/checks | Get all monitor checks
[**v1_checks_get_regions_get**](ChecksApi.md#v1_checks_get_regions_get) | **GET** /v1/checks/get-regions | Get available regions
[**v1_checks_post**](ChecksApi.md#v1_checks_post) | **POST** /v1/checks | Create a new regular check


# **v1_checks_check_id_delete**
> v1_checks_check_id_delete(check_id)

Delete a monitor check

Delete a monitor check. This will also delete all associated alert rules and results.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
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
    api_instance = pingera.ChecksApi(api_client)
    check_id = 'check_id_example' # str | The unique identifier of the monitor check to delete.

    try:
        # Delete a monitor check
        api_instance.v1_checks_check_id_delete(check_id)
    except Exception as e:
        print("Exception when calling ChecksApi->v1_checks_check_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The unique identifier of the monitor check to delete. | 

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_checks_check_id_get**
> MonitorCheck v1_checks_check_id_get(check_id)

Get a specific monitor check

Get a specific monitor check by ID

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.monitor_check import MonitorCheck
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
    api_instance = pingera.ChecksApi(api_client)
    check_id = 'check_id_example' # str | The unique identifier of the monitor check.

    try:
        # Get a specific monitor check
        api_response = api_instance.v1_checks_check_id_get(check_id)
        print("The response of ChecksApi->v1_checks_check_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->v1_checks_check_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The unique identifier of the monitor check. | 

### Return type

[**MonitorCheck**](MonitorCheck.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_checks_check_id_patch**
> MonitorCheck v1_checks_check_id_patch(check_id, monitor_check1)

Update a monitor check

Update a monitor check. Note: The "type" of a check cannot be changed after creation.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.monitor_check import MonitorCheck
from pingera.models.monitor_check1 import MonitorCheck1
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
    api_instance = pingera.ChecksApi(api_client)
    check_id = 'check_id_example' # str | The unique identifier of the monitor check to update.
    monitor_check1 = pingera.MonitorCheck1() # MonitorCheck1 | 

    try:
        # Update a monitor check
        api_response = api_instance.v1_checks_check_id_patch(check_id, monitor_check1)
        print("The response of ChecksApi->v1_checks_check_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->v1_checks_check_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The unique identifier of the monitor check to update. | 
 **monitor_check1** | [**MonitorCheck1**](MonitorCheck1.md)|  | 

### Return type

[**MonitorCheck**](MonitorCheck.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_checks_check_id_results_check_result_id_get**
> MonitorCheckResult v1_checks_check_id_results_check_result_id_get(check_id, check_result_id)

Get a specific check result

Get a specific check result by ID

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.monitor_check_result import MonitorCheckResult
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
    api_instance = pingera.ChecksApi(api_client)
    check_id = 'check_id_example' # str | The unique identifier of the monitor check.
    check_result_id = 'check_result_id_example' # str | The unique identifier of the check result.

    try:
        # Get a specific check result
        api_response = api_instance.v1_checks_check_id_results_check_result_id_get(check_id, check_result_id)
        print("The response of ChecksApi->v1_checks_check_id_results_check_result_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->v1_checks_check_id_results_check_result_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The unique identifier of the monitor check. | 
 **check_result_id** | **str**| The unique identifier of the check result. | 

### Return type

[**MonitorCheckResult**](MonitorCheckResult.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_checks_check_id_results_get**
> MonitorCheckResultList v1_checks_check_id_results_get(check_id, page=page, page_size=page_size, start_date=start_date, end_date=end_date, failed_only=failed_only)

Get results for a specific check

Get results for a specific check with pagination

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.monitor_check_result_list import MonitorCheckResultList
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
    api_instance = pingera.ChecksApi(api_client)
    check_id = 'check_id_example' # str | The unique identifier of the monitor check.
    page = 1 # int | Page number for pagination (default: 1). (optional) (default to 1)
    page_size = 20 # int | Number of items per page (default: 20, max: 100). (optional) (default to 20)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter results from this date (ISO format). (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter results until this date (ISO format). (optional)
    failed_only = False # bool | Show only failed checks (default: false). (optional) (default to False)

    try:
        # Get results for a specific check
        api_response = api_instance.v1_checks_check_id_results_get(check_id, page=page, page_size=page_size, start_date=start_date, end_date=end_date, failed_only=failed_only)
        print("The response of ChecksApi->v1_checks_check_id_results_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->v1_checks_check_id_results_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The unique identifier of the monitor check. | 
 **page** | **int**| Page number for pagination (default: 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default: 20, max: 100). | [optional] [default to 20]
 **start_date** | **datetime**| Filter results from this date (ISO format). | [optional] 
 **end_date** | **datetime**| Filter results until this date (ISO format). | [optional] 
 **failed_only** | **bool**| Show only failed checks (default: false). | [optional] [default to False]

### Return type

[**MonitorCheckResultList**](MonitorCheckResultList.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_checks_check_id_status_history_get**
> MonitorCheckStatusHistoryList v1_checks_check_id_status_history_get(check_id, page=page, page_size=page_size)

Get status history for a check

Get status history for a check with pagination

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.monitor_check_status_history_list import MonitorCheckStatusHistoryList
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
    api_instance = pingera.ChecksApi(api_client)
    check_id = 'check_id_example' # str | The unique identifier of the monitor check.
    page = 1 # int | Page number for pagination (default: 1). (optional) (default to 1)
    page_size = 20 # int | Number of items per page (default: 20, max: 100). (optional) (default to 20)

    try:
        # Get status history for a check
        api_response = api_instance.v1_checks_check_id_status_history_get(check_id, page=page, page_size=page_size)
        print("The response of ChecksApi->v1_checks_check_id_status_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->v1_checks_check_id_status_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The unique identifier of the monitor check. | 
 **page** | **int**| Page number for pagination (default: 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default: 20, max: 100). | [optional] [default to 20]

### Return type

[**MonitorCheckStatusHistoryList**](MonitorCheckStatusHistoryList.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_checks_check_id_uptime_get**
> Error v1_checks_check_id_uptime_get(check_id, start_time=start_time, end_time=end_time)

Get check uptime

Get check uptime by ID. Shows uptime for the last 24 hours by default. Set end_time and start_time to define the period.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.error import Error
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
    api_instance = pingera.ChecksApi(api_client)
    check_id = 'check_id_example' # str | The unique identifier of the monitor check.
    start_time = '2013-10-20T19:20:30+01:00' # datetime | Start time for uptime calculation (ISO format). Defaults to 24 hours ago. (optional)
    end_time = '2013-10-20T19:20:30+01:00' # datetime | End time for uptime calculation (ISO format). Defaults to current time. (optional)

    try:
        # Get check uptime
        api_response = api_instance.v1_checks_check_id_uptime_get(check_id, start_time=start_time, end_time=end_time)
        print("The response of ChecksApi->v1_checks_check_id_uptime_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->v1_checks_check_id_uptime_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The unique identifier of the monitor check. | 
 **start_time** | **datetime**| Start time for uptime calculation (ISO format). Defaults to 24 hours ago. | [optional] 
 **end_time** | **datetime**| End time for uptime calculation (ISO format). Defaults to current time. | [optional] 

### Return type

[**Error**](Error.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_checks_get**
> MonitorCheckList v1_checks_get(page=page, page_size=page_size, group_id=group_id, status=status, name=name, type=type)

Get all monitor checks

Get all monitor checks for current organization with pagination and filtering

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.monitor_check_list import MonitorCheckList
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
    api_instance = pingera.ChecksApi(api_client)
    page = 1 # int | Page number for pagination (default: 1). (optional) (default to 1)
    page_size = 20 # int | Number of items per page (default: 20, max: 100). (optional) (default to 20)
    group_id = 'group_id_example' # str | Filter checks by group ID. Use \"ungrouped\" to get checks not assigned to any group. (optional)
    status = 'status_example' # str | Filter checks by status. Can specify multiple statuses separated by commas (e.g., \"ok,failed\"). (optional)
    name = 'name_example' # str | Filter checks by name using case-insensitive partial matching. (optional)
    type = 'type_example' # str | Filter checks by type. (optional)

    try:
        # Get all monitor checks
        api_response = api_instance.v1_checks_get(page=page, page_size=page_size, group_id=group_id, status=status, name=name, type=type)
        print("The response of ChecksApi->v1_checks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->v1_checks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number for pagination (default: 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default: 20, max: 100). | [optional] [default to 20]
 **group_id** | **str**| Filter checks by group ID. Use \&quot;ungrouped\&quot; to get checks not assigned to any group. | [optional] 
 **status** | **str**| Filter checks by status. Can specify multiple statuses separated by commas (e.g., \&quot;ok,failed\&quot;). | [optional] 
 **name** | **str**| Filter checks by name using case-insensitive partial matching. | [optional] 
 **type** | **str**| Filter checks by type. | [optional] 

### Return type

[**MonitorCheckList**](MonitorCheckList.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_checks_get_regions_get**
> RegionsList v1_checks_get_regions_get(check_type=check_type)

Get available regions

Get available regions for serverless check execution, optionally filtered by check type

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.regions_list import RegionsList
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
    api_instance = pingera.ChecksApi(api_client)
    check_type = 'check_type_example' # str | Filter regions by check type support. (optional)

    try:
        # Get available regions
        api_response = api_instance.v1_checks_get_regions_get(check_type=check_type)
        print("The response of ChecksApi->v1_checks_get_regions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->v1_checks_get_regions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_type** | **str**| Filter regions by check type support. | [optional] 

### Return type

[**RegionsList**](RegionsList.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_checks_post**
> MonitorCheck v1_checks_post(monitor_check)

Create a new regular check

Create a new regular check

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.monitor_check import MonitorCheck
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
    api_instance = pingera.ChecksApi(api_client)
    monitor_check = pingera.MonitorCheck() # MonitorCheck | 

    try:
        # Create a new regular check
        api_response = api_instance.v1_checks_post(monitor_check)
        print("The response of ChecksApi->v1_checks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->v1_checks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_check** | [**MonitorCheck**](MonitorCheck.md)|  | 

### Return type

[**MonitorCheck**](MonitorCheck.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**201** | Created |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

