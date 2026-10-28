# pingera.ExecutionGroupsApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_checks_check_id_execution_groups_get**](ExecutionGroupsApi.md#v1_checks_check_id_execution_groups_get) | **GET** /v1/checks/{check_id}/execution-groups | Get execution groups for a check
[**v1_execution_groups_group_id_get**](ExecutionGroupsApi.md#v1_execution_groups_group_id_get) | **GET** /v1/execution-groups/{group_id} | Get execution group details
[**v1_execution_groups_group_id_regional_results_get**](ExecutionGroupsApi.md#v1_execution_groups_group_id_regional_results_get) | **GET** /v1/execution-groups/{group_id}/regional-results | Get regional results for execution group


# **v1_checks_check_id_execution_groups_get**
> ExecutionGroupList v1_checks_check_id_execution_groups_get(check_id, page=page, page_size=page_size, status=status)

Get execution groups for a check

Get list of multi-region execution groups for a specific check with pagination

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.execution_group_list import ExecutionGroupList
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
    api_instance = pingera.ExecutionGroupsApi(api_client)
    check_id = 'check_id_example' # str | The unique identifier of the monitor check
    page = 1 # int | Page number for pagination (default: 1) (optional) (default to 1)
    page_size = 20 # int | Number of items per page (default: 20, max: 100) (optional) (default to 20)
    status = 'status_example' # str | Filter by execution group status (optional)

    try:
        # Get execution groups for a check
        api_response = api_instance.v1_checks_check_id_execution_groups_get(check_id, page=page, page_size=page_size, status=status)
        print("The response of ExecutionGroupsApi->v1_checks_check_id_execution_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionGroupsApi->v1_checks_check_id_execution_groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The unique identifier of the monitor check | 
 **page** | **int**| Page number for pagination (default: 1) | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default: 20, max: 100) | [optional] [default to 20]
 **status** | **str**| Filter by execution group status | [optional] 

### Return type

[**ExecutionGroupList**](ExecutionGroupList.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_execution_groups_group_id_get**
> ExecutionGroup v1_execution_groups_group_id_get(group_id)

Get execution group details

Get details of a specific multi-region execution group including aggregated statistics

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.execution_group import ExecutionGroup
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
    api_instance = pingera.ExecutionGroupsApi(api_client)
    group_id = 'group_id_example' # str | The unique identifier of the execution group

    try:
        # Get execution group details
        api_response = api_instance.v1_execution_groups_group_id_get(group_id)
        print("The response of ExecutionGroupsApi->v1_execution_groups_group_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionGroupsApi->v1_execution_groups_group_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The unique identifier of the execution group | 

### Return type

[**ExecutionGroup**](ExecutionGroup.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_execution_groups_group_id_regional_results_get**
> RegionalResultsList v1_execution_groups_group_id_regional_results_get(group_id)

Get regional results for execution group

Get detailed results from each region within a multi-region execution group

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.regional_results_list import RegionalResultsList
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
    api_instance = pingera.ExecutionGroupsApi(api_client)
    group_id = 'group_id_example' # str | The unique identifier of the execution group

    try:
        # Get regional results for execution group
        api_response = api_instance.v1_execution_groups_group_id_regional_results_get(group_id)
        print("The response of ExecutionGroupsApi->v1_execution_groups_group_id_regional_results_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionGroupsApi->v1_execution_groups_group_id_regional_results_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The unique identifier of the execution group | 

### Return type

[**RegionalResultsList**](RegionalResultsList.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

