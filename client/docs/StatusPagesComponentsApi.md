# pingera.StatusPagesComponentsApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_component_statuses_get**](StatusPagesComponentsApi.md#v1_component_statuses_get) | **GET** /v1/component-statuses | Get available components&#39; statuses
[**v1_pages_page_id_component_groups_component_id_delete**](StatusPagesComponentsApi.md#v1_pages_page_id_component_groups_component_id_delete) | **DELETE** /v1/pages/{page_id}/component-groups/{component_id} | Delete component group
[**v1_pages_page_id_component_groups_component_id_get**](StatusPagesComponentsApi.md#v1_pages_page_id_component_groups_component_id_get) | **GET** /v1/pages/{page_id}/component-groups/{component_id} | Get component group
[**v1_pages_page_id_component_groups_component_id_patch**](StatusPagesComponentsApi.md#v1_pages_page_id_component_groups_component_id_patch) | **PATCH** /v1/pages/{page_id}/component-groups/{component_id} | Update component group
[**v1_pages_page_id_component_groups_component_id_put**](StatusPagesComponentsApi.md#v1_pages_page_id_component_groups_component_id_put) | **PUT** /v1/pages/{page_id}/component-groups/{component_id} | Update component group
[**v1_pages_page_id_component_groups_get**](StatusPagesComponentsApi.md#v1_pages_page_id_component_groups_get) | **GET** /v1/pages/{page_id}/component-groups | Get component groups
[**v1_pages_page_id_component_groups_post**](StatusPagesComponentsApi.md#v1_pages_page_id_component_groups_post) | **POST** /v1/pages/{page_id}/component-groups | Create component group
[**v1_pages_page_id_components_component_id_delete**](StatusPagesComponentsApi.md#v1_pages_page_id_components_component_id_delete) | **DELETE** /v1/pages/{page_id}/components/{component_id} | Delete component
[**v1_pages_page_id_components_component_id_get**](StatusPagesComponentsApi.md#v1_pages_page_id_components_component_id_get) | **GET** /v1/pages/{page_id}/components/{component_id} | Get component
[**v1_pages_page_id_components_component_id_patch**](StatusPagesComponentsApi.md#v1_pages_page_id_components_component_id_patch) | **PATCH** /v1/pages/{page_id}/components/{component_id} | Update component
[**v1_pages_page_id_components_component_id_put**](StatusPagesComponentsApi.md#v1_pages_page_id_components_component_id_put) | **PUT** /v1/pages/{page_id}/components/{component_id} | Update component
[**v1_pages_page_id_components_component_id_uptime_get**](StatusPagesComponentsApi.md#v1_pages_page_id_components_component_id_uptime_get) | **GET** /v1/pages/{page_id}/components/{component_id}/uptime | Get component uptime
[**v1_pages_page_id_components_get**](StatusPagesComponentsApi.md#v1_pages_page_id_components_get) | **GET** /v1/pages/{page_id}/components | Get page components
[**v1_pages_page_id_components_post**](StatusPagesComponentsApi.md#v1_pages_page_id_components_post) | **POST** /v1/pages/{page_id}/components | Create component
[**v1_pages_page_id_components_uptime_post**](StatusPagesComponentsApi.md#v1_pages_page_id_components_uptime_post) | **POST** /v1/pages/{page_id}/components/uptime | Get bulk component uptime


# **v1_component_statuses_get**
> v1_component_statuses_get()

Get available components' statuses

Get statuses that components can have

### Example


```python
import pingera
from pingera.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pingera.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = pingera.Configuration(
    host = "https://api.pingera.ru"
)


# Enter a context with an instance of the API client
with pingera.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pingera.StatusPagesComponentsApi(api_client)

    try:
        # Get available components' statuses
        api_instance.v1_component_statuses_get()
    except Exception as e:
        print("Exception when calling StatusPagesComponentsApi->v1_component_statuses_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of components successfully retrieved |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_component_groups_component_id_delete**
> v1_pages_page_id_component_groups_component_id_delete(page_id, component_id)

Delete component group

Delete a component group permanently and reset group membership for all components in the group

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
    api_instance = pingera.StatusPagesComponentsApi(api_client)
    page_id = 'page_id_example' # str | 
    component_id = 'component_id_example' # str | 

    try:
        # Delete component group
        api_instance.v1_pages_page_id_component_groups_component_id_delete(page_id, component_id)
    except Exception as e:
        print("Exception when calling StatusPagesComponentsApi->v1_pages_page_id_component_groups_component_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **component_id** | **str**|  | 

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
**500** | Internal Server Error |  -  |
**404** | Component group not found |  -  |
**403** | Forbidden - Access denied |  -  |
**401** | Unauthorized - Authentication required |  -  |
**204** | Component group deleted successfully |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_component_groups_component_id_get**
> Component v1_pages_page_id_component_groups_component_id_get(page_id, component_id)

Get component group

Get a specific component group by ID with detailed information

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.component import Component
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
    api_instance = pingera.StatusPagesComponentsApi(api_client)
    page_id = 'page_id_example' # str | 
    component_id = 'component_id_example' # str | 

    try:
        # Get component group
        api_response = api_instance.v1_pages_page_id_component_groups_component_id_get(page_id, component_id)
        print("The response of StatusPagesComponentsApi->v1_pages_page_id_component_groups_component_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesComponentsApi->v1_pages_page_id_component_groups_component_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **component_id** | **str**|  | 

### Return type

[**Component**](Component.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Component group successfully retrieved |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied |  -  |
**404** | Component group not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_component_groups_component_id_patch**
> Component1 v1_pages_page_id_component_groups_component_id_patch(page_id, component_id, component1)

Update component group

Update a component group with new configuration (PATCH for partial updates, PUT for full replacement)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.component1 import Component1
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
    api_instance = pingera.StatusPagesComponentsApi(api_client)
    page_id = 'page_id_example' # str | 
    component_id = 'component_id_example' # str | 
    component1 = pingera.Component1() # Component1 | 

    try:
        # Update component group
        api_response = api_instance.v1_pages_page_id_component_groups_component_id_patch(page_id, component_id, component1)
        print("The response of StatusPagesComponentsApi->v1_pages_page_id_component_groups_component_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesComponentsApi->v1_pages_page_id_component_groups_component_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **component_id** | **str**|  | 
 **component1** | [**Component1**](Component1.md)|  | 

### Return type

[**Component1**](Component1.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | Component group updated successfully |  -  |
**400** | Bad Request - Validation error |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied |  -  |
**404** | Component group not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_component_groups_component_id_put**
> Component1 v1_pages_page_id_component_groups_component_id_put(page_id, component_id, component1)

Update component group

Update a component group with new configuration (PATCH for partial updates, PUT for full replacement)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.component1 import Component1
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
    api_instance = pingera.StatusPagesComponentsApi(api_client)
    page_id = 'page_id_example' # str | 
    component_id = 'component_id_example' # str | 
    component1 = pingera.Component1() # Component1 | 

    try:
        # Update component group
        api_response = api_instance.v1_pages_page_id_component_groups_component_id_put(page_id, component_id, component1)
        print("The response of StatusPagesComponentsApi->v1_pages_page_id_component_groups_component_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesComponentsApi->v1_pages_page_id_component_groups_component_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **component_id** | **str**|  | 
 **component1** | [**Component1**](Component1.md)|  | 

### Return type

[**Component1**](Component1.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | Component group updated successfully |  -  |
**400** | Bad Request - Validation error |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied |  -  |
**404** | Component group not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_component_groups_get**
> List[Component] v1_pages_page_id_component_groups_get(page_id)

Get component groups

Get all component groups for a specific status page with optional filtering

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.component import Component
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
    api_instance = pingera.StatusPagesComponentsApi(api_client)
    page_id = 'page_id_example' # str | 

    try:
        # Get component groups
        api_response = api_instance.v1_pages_page_id_component_groups_get(page_id)
        print("The response of StatusPagesComponentsApi->v1_pages_page_id_component_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesComponentsApi->v1_pages_page_id_component_groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 

### Return type

[**List[Component]**](Component.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of component groups successfully retrieved |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied |  -  |
**404** | Page not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_component_groups_post**
> Component v1_pages_page_id_component_groups_post(page_id, component)

Create component group

Create a new component group for organizing related components on a status page

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.component import Component
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
    api_instance = pingera.StatusPagesComponentsApi(api_client)
    page_id = 'page_id_example' # str | 
    component = pingera.Component() # Component | 

    try:
        # Create component group
        api_response = api_instance.v1_pages_page_id_component_groups_post(page_id, component)
        print("The response of StatusPagesComponentsApi->v1_pages_page_id_component_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesComponentsApi->v1_pages_page_id_component_groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **component** | [**Component**](Component.md)|  | 

### Return type

[**Component**](Component.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**201** | Component group created successfully |  -  |
**400** | Bad Request - Validation error |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied |  -  |
**404** | Page not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_components_component_id_delete**
> v1_pages_page_id_components_component_id_delete(page_id, component_id)

Delete component

Delete a component permanently or mark it as deleted (soft delete for regular components, hard delete for groups)

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
    api_instance = pingera.StatusPagesComponentsApi(api_client)
    page_id = 'page_id_example' # str | 
    component_id = 'component_id_example' # str | 

    try:
        # Delete component
        api_instance.v1_pages_page_id_components_component_id_delete(page_id, component_id)
    except Exception as e:
        print("Exception when calling StatusPagesComponentsApi->v1_pages_page_id_components_component_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **component_id** | **str**|  | 

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
**500** | Internal Server Error |  -  |
**404** | Component not found |  -  |
**403** | Forbidden - Access denied |  -  |
**401** | Unauthorized - Authentication required |  -  |
**204** | Component deleted successfully |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_components_component_id_get**
> Component v1_pages_page_id_components_component_id_get(page_id, component_id)

Get component

Get a specific component by ID with detailed information

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.component import Component
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
    api_instance = pingera.StatusPagesComponentsApi(api_client)
    page_id = 'page_id_example' # str | 
    component_id = 'component_id_example' # str | 

    try:
        # Get component
        api_response = api_instance.v1_pages_page_id_components_component_id_get(page_id, component_id)
        print("The response of StatusPagesComponentsApi->v1_pages_page_id_components_component_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesComponentsApi->v1_pages_page_id_components_component_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **component_id** | **str**|  | 

### Return type

[**Component**](Component.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Component successfully retrieved |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied |  -  |
**404** | Component not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_components_component_id_patch**
> Component v1_pages_page_id_components_component_id_patch(page_id, component_id, component1)

Update component

Update a component with new configuration (PATCH for partial updates, PUT for full replacement)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.component import Component
from pingera.models.component1 import Component1
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
    api_instance = pingera.StatusPagesComponentsApi(api_client)
    page_id = 'page_id_example' # str | 
    component_id = 'component_id_example' # str | 
    component1 = pingera.Component1() # Component1 | 

    try:
        # Update component
        api_response = api_instance.v1_pages_page_id_components_component_id_patch(page_id, component_id, component1)
        print("The response of StatusPagesComponentsApi->v1_pages_page_id_components_component_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesComponentsApi->v1_pages_page_id_components_component_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **component_id** | **str**|  | 
 **component1** | [**Component1**](Component1.md)|  | 

### Return type

[**Component**](Component.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | Component updated successfully |  -  |
**400** | Bad Request - Validation error |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied |  -  |
**404** | Component not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_components_component_id_put**
> Component v1_pages_page_id_components_component_id_put(page_id, component_id, component1)

Update component

Update a component with new configuration (PATCH for partial updates, PUT for full replacement)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.component import Component
from pingera.models.component1 import Component1
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
    api_instance = pingera.StatusPagesComponentsApi(api_client)
    page_id = 'page_id_example' # str | 
    component_id = 'component_id_example' # str | 
    component1 = pingera.Component1() # Component1 | 

    try:
        # Update component
        api_response = api_instance.v1_pages_page_id_components_component_id_put(page_id, component_id, component1)
        print("The response of StatusPagesComponentsApi->v1_pages_page_id_components_component_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesComponentsApi->v1_pages_page_id_components_component_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **component_id** | **str**|  | 
 **component1** | [**Component1**](Component1.md)|  | 

### Return type

[**Component**](Component.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | Component updated successfully |  -  |
**400** | Bad Request - Validation error |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied |  -  |
**404** | Component not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_components_component_id_uptime_get**
> v1_pages_page_id_components_component_id_uptime_get(page_id, component_id)

Get component uptime

Get uptime data for a specific component with optional date range filtering

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
    api_instance = pingera.StatusPagesComponentsApi(api_client)
    page_id = 'page_id_example' # str | 
    component_id = 'component_id_example' # str | 

    try:
        # Get component uptime
        api_instance.v1_pages_page_id_components_component_id_uptime_get(page_id, component_id)
    except Exception as e:
        print("Exception when calling StatusPagesComponentsApi->v1_pages_page_id_components_component_id_uptime_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **component_id** | **str**|  | 

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
**200** | Component uptime data successfully calculated |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied |  -  |
**404** | Component not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_components_get**
> List[Component] v1_pages_page_id_components_get(page_id)

Get page components

Get all components for a specific status page with optional filtering

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.component import Component
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
    api_instance = pingera.StatusPagesComponentsApi(api_client)
    page_id = 'page_id_example' # str | 

    try:
        # Get page components
        api_response = api_instance.v1_pages_page_id_components_get(page_id)
        print("The response of StatusPagesComponentsApi->v1_pages_page_id_components_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesComponentsApi->v1_pages_page_id_components_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 

### Return type

[**List[Component]**](Component.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of components successfully retrieved |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied |  -  |
**404** | Page not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_components_post**
> Component v1_pages_page_id_components_post(page_id, component)

Create component

Create a new component for a specific status page

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.component import Component
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
    api_instance = pingera.StatusPagesComponentsApi(api_client)
    page_id = 'page_id_example' # str | 
    component = pingera.Component() # Component | 

    try:
        # Create component
        api_response = api_instance.v1_pages_page_id_components_post(page_id, component)
        print("The response of StatusPagesComponentsApi->v1_pages_page_id_components_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesComponentsApi->v1_pages_page_id_components_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **component** | [**Component**](Component.md)|  | 

### Return type

[**Component**](Component.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**201** | Component successfully created |  -  |
**400** | Bad Request - Validation error |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied |  -  |
**404** | Page not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_components_uptime_post**
> v1_pages_page_id_components_uptime_post(page_id, component_uptime_bulk_request)

Get bulk component uptime

Get uptime data for multiple components in bulk with optional date range filtering

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.component_uptime_bulk_request import ComponentUptimeBulkRequest
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
    api_instance = pingera.StatusPagesComponentsApi(api_client)
    page_id = 'page_id_example' # str | 
    component_uptime_bulk_request = pingera.ComponentUptimeBulkRequest() # ComponentUptimeBulkRequest | 

    try:
        # Get bulk component uptime
        api_instance.v1_pages_page_id_components_uptime_post(page_id, component_uptime_bulk_request)
    except Exception as e:
        print("Exception when calling StatusPagesComponentsApi->v1_pages_page_id_components_uptime_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **component_uptime_bulk_request** | [**ComponentUptimeBulkRequest**](ComponentUptimeBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | Uptime data successfully calculated |  -  |
**400** | Bad Request - Validation error |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied |  -  |
**404** | Components not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

