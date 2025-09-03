# pingera.CheckGroupsApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_check_groups_get**](CheckGroupsApi.md#v1_check_groups_get) | **GET** /v1/check-groups | Get all check groups
[**v1_check_groups_group_id_checks_get**](CheckGroupsApi.md#v1_check_groups_group_id_checks_get) | **GET** /v1/check-groups/{group_id}/checks | Get checks in a group
[**v1_check_groups_group_id_delete**](CheckGroupsApi.md#v1_check_groups_group_id_delete) | **DELETE** /v1/check-groups/{group_id} | Delete a check group
[**v1_check_groups_group_id_get**](CheckGroupsApi.md#v1_check_groups_group_id_get) | **GET** /v1/check-groups/{group_id} | Get a specific check group
[**v1_check_groups_group_id_patch**](CheckGroupsApi.md#v1_check_groups_group_id_patch) | **PATCH** /v1/check-groups/{group_id} | Update a check group
[**v1_check_groups_post**](CheckGroupsApi.md#v1_check_groups_post) | **POST** /v1/check-groups | Create a new check group
[**v1_checks_check_id_group_patch**](CheckGroupsApi.md#v1_checks_check_id_group_patch) | **PATCH** /v1/checks/{check_id}/group | Assign check to group


# **v1_check_groups_get**
> CheckGroupList v1_check_groups_get(page=page, page_size=page_size)

Get all check groups

Get all check groups for current organization with pagination

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.check_group_list import CheckGroupList
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
    api_instance = pingera.CheckGroupsApi(api_client)
    page = 1 # int | Page number for pagination (default: 1). (optional) (default to 1)
    page_size = 20 # int | Number of items per page (default: 20, max: 100). (optional) (default to 20)

    try:
        # Get all check groups
        api_response = api_instance.v1_check_groups_get(page=page, page_size=page_size)
        print("The response of CheckGroupsApi->v1_check_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckGroupsApi->v1_check_groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number for pagination (default: 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default: 20, max: 100). | [optional] [default to 20]

### Return type

[**CheckGroupList**](CheckGroupList.md)

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

# **v1_check_groups_group_id_checks_get**
> MonitorCheckList v1_check_groups_group_id_checks_get(group_id, page=page, page_size=page_size)

Get checks in a group

Get all checks that belong to a specific group

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
    api_instance = pingera.CheckGroupsApi(api_client)
    group_id = 'group_id_example' # str | The unique identifier of the check group.
    page = 1 # int | Page number for pagination (default: 1). (optional) (default to 1)
    page_size = 20 # int | Number of items per page (default: 20, max: 100). (optional) (default to 20)

    try:
        # Get checks in a group
        api_response = api_instance.v1_check_groups_group_id_checks_get(group_id, page=page, page_size=page_size)
        print("The response of CheckGroupsApi->v1_check_groups_group_id_checks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckGroupsApi->v1_check_groups_group_id_checks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The unique identifier of the check group. | 
 **page** | **int**| Page number for pagination (default: 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default: 20, max: 100). | [optional] [default to 20]

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

# **v1_check_groups_group_id_delete**
> v1_check_groups_group_id_delete(group_id)

Delete a check group

Delete a check group. All checks in the group will be moved to ungrouped.

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
    api_instance = pingera.CheckGroupsApi(api_client)
    group_id = 'group_id_example' # str | The unique identifier of the check group to delete.

    try:
        # Delete a check group
        api_instance.v1_check_groups_group_id_delete(group_id)
    except Exception as e:
        print("Exception when calling CheckGroupsApi->v1_check_groups_group_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The unique identifier of the check group to delete. | 

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

# **v1_check_groups_group_id_get**
> CheckGroup1 v1_check_groups_group_id_get(group_id)

Get a specific check group

Get a specific check group by ID

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.check_group1 import CheckGroup1
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
    api_instance = pingera.CheckGroupsApi(api_client)
    group_id = 'group_id_example' # str | The unique identifier of the check group.

    try:
        # Get a specific check group
        api_response = api_instance.v1_check_groups_group_id_get(group_id)
        print("The response of CheckGroupsApi->v1_check_groups_group_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckGroupsApi->v1_check_groups_group_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The unique identifier of the check group. | 

### Return type

[**CheckGroup1**](CheckGroup1.md)

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

# **v1_check_groups_group_id_patch**
> CheckGroup1 v1_check_groups_group_id_patch(group_id, check_group2)

Update a check group

Update a check group

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.check_group1 import CheckGroup1
from pingera.models.check_group2 import CheckGroup2
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
    api_instance = pingera.CheckGroupsApi(api_client)
    group_id = 'group_id_example' # str | The unique identifier of the check group to update.
    check_group2 = pingera.CheckGroup2() # CheckGroup2 | 

    try:
        # Update a check group
        api_response = api_instance.v1_check_groups_group_id_patch(group_id, check_group2)
        print("The response of CheckGroupsApi->v1_check_groups_group_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckGroupsApi->v1_check_groups_group_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The unique identifier of the check group to update. | 
 **check_group2** | [**CheckGroup2**](CheckGroup2.md)|  | 

### Return type

[**CheckGroup1**](CheckGroup1.md)

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

# **v1_check_groups_post**
> CheckGroup1 v1_check_groups_post(check_group1)

Create a new check group

Create a new check group

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.check_group1 import CheckGroup1
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
    api_instance = pingera.CheckGroupsApi(api_client)
    check_group1 = pingera.CheckGroup1() # CheckGroup1 | 

    try:
        # Create a new check group
        api_response = api_instance.v1_check_groups_post(check_group1)
        print("The response of CheckGroupsApi->v1_check_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckGroupsApi->v1_check_groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_group1** | [**CheckGroup1**](CheckGroup1.md)|  | 

### Return type

[**CheckGroup1**](CheckGroup1.md)

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

# **v1_checks_check_id_group_patch**
> Generated1 v1_checks_check_id_group_patch(check_id, generated)

Assign check to group

Assign a check to a group or remove it from a group (set group_id to null)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.generated import Generated
from pingera.models.generated1 import Generated1
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
    api_instance = pingera.CheckGroupsApi(api_client)
    check_id = 'check_id_example' # str | The unique identifier of the monitor check.
    generated = pingera.Generated() # Generated | 

    try:
        # Assign check to group
        api_response = api_instance.v1_checks_check_id_group_patch(check_id, generated)
        print("The response of CheckGroupsApi->v1_checks_check_id_group_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckGroupsApi->v1_checks_check_id_group_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The unique identifier of the monitor check. | 
 **generated** | [**Generated**](Generated.md)|  | 

### Return type

[**Generated1**](Generated1.md)

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

