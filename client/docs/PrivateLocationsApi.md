# pingera.PrivateLocationsApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_private_locations_get**](PrivateLocationsApi.md#v1_private_locations_get) | **GET** /v1/private-locations | List private locations
[**v1_private_locations_location_id_delete**](PrivateLocationsApi.md#v1_private_locations_location_id_delete) | **DELETE** /v1/private-locations/{location_id} | Delete a private location
[**v1_private_locations_location_id_get**](PrivateLocationsApi.md#v1_private_locations_location_id_get) | **GET** /v1/private-locations/{location_id} | Get a private location with its runners and tokens
[**v1_private_locations_location_id_patch**](PrivateLocationsApi.md#v1_private_locations_location_id_patch) | **PATCH** /v1/private-locations/{location_id} | Update a private location
[**v1_private_locations_location_id_tokens_post**](PrivateLocationsApi.md#v1_private_locations_location_id_tokens_post) | **POST** /v1/private-locations/{location_id}/tokens | Create a runner token (returned once)
[**v1_private_locations_location_id_tokens_token_id_delete**](PrivateLocationsApi.md#v1_private_locations_location_id_tokens_token_id_delete) | **DELETE** /v1/private-locations/{location_id}/tokens/{token_id} | Revoke a runner token
[**v1_private_locations_post**](PrivateLocationsApi.md#v1_private_locations_post) | **POST** /v1/private-locations | Create a private location


# **v1_private_locations_get**
> PrivateLocationList v1_private_locations_get()

List private locations

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.private_location_list import PrivateLocationList
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
    api_instance = pingera.PrivateLocationsApi(api_client)

    try:
        # List private locations
        api_response = api_instance.v1_private_locations_get()
        print("The response of PrivateLocationsApi->v1_private_locations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLocationsApi->v1_private_locations_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PrivateLocationList**](PrivateLocationList.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Private locations and plan usage |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_locations_location_id_delete**
> v1_private_locations_location_id_delete(location_id)

Delete a private location

Fails with 409 while checks still use the location as a region.

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
    api_instance = pingera.PrivateLocationsApi(api_client)
    location_id = 'location_id_example' # str | 

    try:
        # Delete a private location
        api_instance.v1_private_locations_location_id_delete(location_id)
    except Exception as e:
        print("Exception when calling PrivateLocationsApi->v1_private_locations_location_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Private location deleted |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_locations_location_id_get**
> PrivateLocationDetail v1_private_locations_location_id_get(location_id)

Get a private location with its runners and tokens

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.private_location_detail import PrivateLocationDetail
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
    api_instance = pingera.PrivateLocationsApi(api_client)
    location_id = 'location_id_example' # str | 

    try:
        # Get a private location with its runners and tokens
        api_response = api_instance.v1_private_locations_location_id_get(location_id)
        print("The response of PrivateLocationsApi->v1_private_locations_location_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLocationsApi->v1_private_locations_location_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | 

### Return type

[**PrivateLocationDetail**](PrivateLocationDetail.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The private location |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_locations_location_id_patch**
> PrivateLocationDetail v1_private_locations_location_id_patch(location_id, private_location_update)

Update a private location

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.private_location_detail import PrivateLocationDetail
from pingera.models.private_location_update import PrivateLocationUpdate
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
    api_instance = pingera.PrivateLocationsApi(api_client)
    location_id = 'location_id_example' # str | 
    private_location_update = pingera.PrivateLocationUpdate() # PrivateLocationUpdate | 

    try:
        # Update a private location
        api_response = api_instance.v1_private_locations_location_id_patch(location_id, private_location_update)
        print("The response of PrivateLocationsApi->v1_private_locations_location_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLocationsApi->v1_private_locations_location_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | 
 **private_location_update** | [**PrivateLocationUpdate**](PrivateLocationUpdate.md)|  | 

### Return type

[**PrivateLocationDetail**](PrivateLocationDetail.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated private location |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_locations_location_id_tokens_post**
> RunnerTokenCreated v1_private_locations_location_id_tokens_post(location_id, runner_token_create)

Create a runner token (returned once)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.runner_token_create import RunnerTokenCreate
from pingera.models.runner_token_created import RunnerTokenCreated
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
    api_instance = pingera.PrivateLocationsApi(api_client)
    location_id = 'location_id_example' # str | 
    runner_token_create = pingera.RunnerTokenCreate() # RunnerTokenCreate | 

    try:
        # Create a runner token (returned once)
        api_response = api_instance.v1_private_locations_location_id_tokens_post(location_id, runner_token_create)
        print("The response of PrivateLocationsApi->v1_private_locations_location_id_tokens_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLocationsApi->v1_private_locations_location_id_tokens_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | 
 **runner_token_create** | [**RunnerTokenCreate**](RunnerTokenCreate.md)|  | 

### Return type

[**RunnerTokenCreated**](RunnerTokenCreated.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created runner token |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_locations_location_id_tokens_token_id_delete**
> v1_private_locations_location_id_tokens_token_id_delete(location_id, token_id)

Revoke a runner token

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
    api_instance = pingera.PrivateLocationsApi(api_client)
    location_id = 'location_id_example' # str | 
    token_id = 'token_id_example' # str | 

    try:
        # Revoke a runner token
        api_instance.v1_private_locations_location_id_tokens_token_id_delete(location_id, token_id)
    except Exception as e:
        print("Exception when calling PrivateLocationsApi->v1_private_locations_location_id_tokens_token_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | 
 **token_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Runner token revoked |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_locations_post**
> PrivateLocationCreated v1_private_locations_post(private_location_create)

Create a private location

Creates the location and its first runner token. The token value is only returned once.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.private_location_create import PrivateLocationCreate
from pingera.models.private_location_created import PrivateLocationCreated
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
    api_instance = pingera.PrivateLocationsApi(api_client)
    private_location_create = pingera.PrivateLocationCreate() # PrivateLocationCreate | 

    try:
        # Create a private location
        api_response = api_instance.v1_private_locations_post(private_location_create)
        print("The response of PrivateLocationsApi->v1_private_locations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLocationsApi->v1_private_locations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_location_create** | [**PrivateLocationCreate**](PrivateLocationCreate.md)|  | 

### Return type

[**PrivateLocationCreated**](PrivateLocationCreated.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created private location |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

