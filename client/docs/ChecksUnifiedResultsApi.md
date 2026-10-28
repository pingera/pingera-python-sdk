# pingera.ChecksUnifiedResultsApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_checks_all_results_get**](ChecksUnifiedResultsApi.md#v1_checks_all_results_get) | **GET** /v1/checks/all-results | Get all check results (regular and on-demand)
[**v1_checks_check_id_response_times_get**](ChecksUnifiedResultsApi.md#v1_checks_check_id_response_times_get) | **GET** /v1/checks/{check_id}/response-times | Get aggregated response time metrics for a specific check
[**v1_checks_status_history_get**](ChecksUnifiedResultsApi.md#v1_checks_status_history_get) | **GET** /v1/checks/status-history | Get time-bucketed status history metrics


# **v1_checks_all_results_get**
> UnifiedResultList v1_checks_all_results_get(page=page, page_size=page_size, check_id=check_id, status=status, check_type=check_type, result_type=result_type, region=region, execution_group_id=execution_group_id, result_id=result_id, is_multi_region=is_multi_region, start_date=start_date, end_date=end_date, has_alerts=has_alerts)

Get all check results (regular and on-demand)

Get all check results (regular and on-demand) for the organization, sorted by creation date. Supports filtering by check ID, result ID, job ID, status, type, region, execution group, date range, and alert presence. Date range is limited to 6 months in the past.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.unified_result_list import UnifiedResultList
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

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with pingera.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pingera.ChecksUnifiedResultsApi(api_client)
    page = 1 # int | Page number for pagination (starting from 1). (optional) (default to 1)
    page_size = 20 # int | Number of results per page (maximum 100). (optional) (default to 20)
    check_id = 'chk123abc456' # str | Filter by specific check ID. (optional)
    status = 'ok' # str | Filter by check result status. (optional)
    check_type = 'web' # str | Filter by check type. (optional)
    result_type = 'regular' # str | Filter by result type. (optional)
    region = 'us-west-1' # str | Filter by region where check was executed. (optional)
    execution_group_id = 'grp123abc456' # str | Filter by specific execution group ID. Shows all regional results from a multi-region execution. (optional)
    result_id = 'o8gzgweldbw2' # str | Filter by specific result ID to get a single result. (optional)
    is_multi_region = true # bool | Filter to show only multi-region executions (true) or only single-region executions (false). Omit to show all results. (optional)
    start_date = '2024-01-15T00:00Z' # datetime | Start date for filtering results (ISO format). Limited to 6 months in the past. (optional)
    end_date = '2024-01-15T23:59:59Z' # datetime | End date for filtering results (ISO format). (optional)
    has_alerts = true # bool | Filter to show only results that have triggered alerts (true) or only results without alerts (false). Omit to show all results. (optional)

    try:
        # Get all check results (regular and on-demand)
        api_response = api_instance.v1_checks_all_results_get(page=page, page_size=page_size, check_id=check_id, status=status, check_type=check_type, result_type=result_type, region=region, execution_group_id=execution_group_id, result_id=result_id, is_multi_region=is_multi_region, start_date=start_date, end_date=end_date, has_alerts=has_alerts)
        print("The response of ChecksUnifiedResultsApi->v1_checks_all_results_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksUnifiedResultsApi->v1_checks_all_results_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number for pagination (starting from 1). | [optional] [default to 1]
 **page_size** | **int**| Number of results per page (maximum 100). | [optional] [default to 20]
 **check_id** | **str**| Filter by specific check ID. | [optional] 
 **status** | **str**| Filter by check result status. | [optional] 
 **check_type** | **str**| Filter by check type. | [optional] 
 **result_type** | **str**| Filter by result type. | [optional] 
 **region** | **str**| Filter by region where check was executed. | [optional] 
 **execution_group_id** | **str**| Filter by specific execution group ID. Shows all regional results from a multi-region execution. | [optional] 
 **result_id** | **str**| Filter by specific result ID to get a single result. | [optional] 
 **is_multi_region** | **bool**| Filter to show only multi-region executions (true) or only single-region executions (false). Omit to show all results. | [optional] 
 **start_date** | **datetime**| Start date for filtering results (ISO format). Limited to 6 months in the past. | [optional] 
 **end_date** | **datetime**| End date for filtering results (ISO format). | [optional] 
 **has_alerts** | **bool**| Filter to show only results that have triggered alerts (true) or only results without alerts (false). Omit to show all results. | [optional] 

### Return type

[**UnifiedResultList**](UnifiedResultList.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | OK |  -  |
**400** | Bad Request - Invalid parameters or date range |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error - Failed to fetch results |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_checks_check_id_response_times_get**
> Dict[str, object] v1_checks_check_id_response_times_get(check_id, region=region, status=status, execution_group_id=execution_group_id, is_multi_region=is_multi_region, start_date=start_date, end_date=end_date)

Get aggregated response time metrics for a specific check

Get aggregated response time metrics for a specific check, grouped by region. Returns average, 95th percentile, and 99th percentile response times for each time bucket and region. Supports filtering by execution group for multi-region executions. Time intervals are automatically determined based on the date range.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

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

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with pingera.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pingera.ChecksUnifiedResultsApi(api_client)
    check_id = 'check_id_example' # str | 
    region = 'us-west-1' # str | Filter by specific region. (optional)
    status = 'ok' # str | Filter by check status. (optional)
    execution_group_id = 'grp123abc456' # str | Filter by specific execution group ID for multi-region analysis. (optional)
    is_multi_region = true # bool | Filter to show only multi-region executions (true) or only single-region executions (false). (optional)
    start_date = '2024-01-15T00:00Z' # datetime | Start date for metrics (ISO format). Limited to 6 months in the past. (optional)
    end_date = '2024-01-15T23:59:59Z' # datetime | End date for metrics (ISO format). (optional)

    try:
        # Get aggregated response time metrics for a specific check
        api_response = api_instance.v1_checks_check_id_response_times_get(check_id, region=region, status=status, execution_group_id=execution_group_id, is_multi_region=is_multi_region, start_date=start_date, end_date=end_date)
        print("The response of ChecksUnifiedResultsApi->v1_checks_check_id_response_times_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksUnifiedResultsApi->v1_checks_check_id_response_times_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**|  | 
 **region** | **str**| Filter by specific region. | [optional] 
 **status** | **str**| Filter by check status. | [optional] 
 **execution_group_id** | **str**| Filter by specific execution group ID for multi-region analysis. | [optional] 
 **is_multi_region** | **bool**| Filter to show only multi-region executions (true) or only single-region executions (false). | [optional] 
 **start_date** | **datetime**| Start date for metrics (ISO format). Limited to 6 months in the past. | [optional] 
 **end_date** | **datetime**| End date for metrics (ISO format). | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | OK |  -  |
**400** | Bad Request - Invalid parameters or date range |  -  |
**401** | Unauthorized - Authentication required |  -  |
**404** | Check not found or you do not have permission to access it |  -  |
**500** | Internal Server Error - Failed to fetch response time metrics |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_checks_status_history_get**
> Dict[str, object] v1_checks_status_history_get(check_id=check_id, region=region, status=status, result_type=result_type, execution_group_id=execution_group_id, is_multi_region=is_multi_region, start_date=start_date, end_date=end_date, has_alerts=has_alerts, check_type=check_type)

Get time-bucketed status history metrics

Get a time-bucketed history of check counts by status for a check or all checks. Returns counts for each status (ok, failed, degraded, timeout) grouped by region and time bucket. If no check_id is provided, returns metrics for all checks in the organization. Can be filtered by result type (regular or on_demand), execution group, and by alert presence.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

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

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with pingera.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pingera.ChecksUnifiedResultsApi(api_client)
    check_id = 'chk123abc456' # str | Filter by specific check ID. If not provided, returns metrics for all checks. (optional)
    region = 'us-west-1' # str | Filter by specific region. (optional)
    status = 'ok' # str | Filter by check status. (optional)
    result_type = 'regular' # str | Filter by result type. (optional)
    execution_group_id = 'grp123abc456' # str | Filter by specific execution group ID for multi-region analysis. (optional)
    is_multi_region = true # bool | Filter to show only multi-region executions (true) or only single-region executions (false). (optional)
    start_date = '2024-01-15T00:00Z' # datetime | Start date for status history (ISO format). Limited to 6 months in the past. (optional)
    end_date = '2024-01-15T23:59:59Z' # datetime | End date for status history (ISO format). (optional)
    has_alerts = true # bool | Filter to show only results that have triggered alerts (true) or only results without alerts (false). Omit to show all results. (optional)
    check_type = 'synthetic' # str | Filter by check type (e.g., web, synthetic, multistep, api, ssl, icmp, dns, tcp, port_scan). (optional)

    try:
        # Get time-bucketed status history metrics
        api_response = api_instance.v1_checks_status_history_get(check_id=check_id, region=region, status=status, result_type=result_type, execution_group_id=execution_group_id, is_multi_region=is_multi_region, start_date=start_date, end_date=end_date, has_alerts=has_alerts, check_type=check_type)
        print("The response of ChecksUnifiedResultsApi->v1_checks_status_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksUnifiedResultsApi->v1_checks_status_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| Filter by specific check ID. If not provided, returns metrics for all checks. | [optional] 
 **region** | **str**| Filter by specific region. | [optional] 
 **status** | **str**| Filter by check status. | [optional] 
 **result_type** | **str**| Filter by result type. | [optional] 
 **execution_group_id** | **str**| Filter by specific execution group ID for multi-region analysis. | [optional] 
 **is_multi_region** | **bool**| Filter to show only multi-region executions (true) or only single-region executions (false). | [optional] 
 **start_date** | **datetime**| Start date for status history (ISO format). Limited to 6 months in the past. | [optional] 
 **end_date** | **datetime**| End date for status history (ISO format). | [optional] 
 **has_alerts** | **bool**| Filter to show only results that have triggered alerts (true) or only results without alerts (false). Omit to show all results. | [optional] 
 **check_type** | **str**| Filter by check type (e.g., web, synthetic, multistep, api, ssl, icmp, dns, tcp, port_scan). | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | OK |  -  |
**400** | Bad Request - Invalid parameters or date range |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error - Failed to fetch status history |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

