# pingera.HeartbeatsApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_heartbeats_check_id_channels_channel_id_delete**](HeartbeatsApi.md#v1_heartbeats_check_id_channels_channel_id_delete) | **DELETE** /v1/heartbeats/{check_id}/channels/{channel_id} | Remove alert channel from heartbeat check
[**v1_heartbeats_check_id_channels_get**](HeartbeatsApi.md#v1_heartbeats_check_id_channels_get) | **GET** /v1/heartbeats/{check_id}/channels | Get alert channels assigned to heartbeat check
[**v1_heartbeats_check_id_channels_post**](HeartbeatsApi.md#v1_heartbeats_check_id_channels_post) | **POST** /v1/heartbeats/{check_id}/channels | Assign alert channels to heartbeat check
[**v1_heartbeats_check_id_delete**](HeartbeatsApi.md#v1_heartbeats_check_id_delete) | **DELETE** /v1/heartbeats/{check_id} | Delete a heartbeat check
[**v1_heartbeats_check_id_get**](HeartbeatsApi.md#v1_heartbeats_check_id_get) | **GET** /v1/heartbeats/{check_id} | Get specific heartbeat check
[**v1_heartbeats_check_id_patch**](HeartbeatsApi.md#v1_heartbeats_check_id_patch) | **PATCH** /v1/heartbeats/{check_id} | Update an existing heartbeat check
[**v1_heartbeats_check_id_ping_get**](HeartbeatsApi.md#v1_heartbeats_check_id_ping_get) | **GET** /v1/heartbeats/{check_id}/ping | Receive heartbeat ping (GET)
[**v1_heartbeats_check_id_ping_post**](HeartbeatsApi.md#v1_heartbeats_check_id_ping_post) | **POST** /v1/heartbeats/{check_id}/ping | Receive heartbeat ping (POST)
[**v1_heartbeats_check_id_pings_count_get**](HeartbeatsApi.md#v1_heartbeats_check_id_pings_count_get) | **GET** /v1/heartbeats/{check_id}/pings-count | Get ping count history
[**v1_heartbeats_check_id_pings_get**](HeartbeatsApi.md#v1_heartbeats_check_id_pings_get) | **GET** /v1/heartbeats/{check_id}/pings | Get ping history
[**v1_heartbeats_check_id_put**](HeartbeatsApi.md#v1_heartbeats_check_id_put) | **PUT** /v1/heartbeats/{check_id} | Update an existing heartbeat check
[**v1_heartbeats_get**](HeartbeatsApi.md#v1_heartbeats_get) | **GET** /v1/heartbeats | Get all heartbeat checks
[**v1_heartbeats_post**](HeartbeatsApi.md#v1_heartbeats_post) | **POST** /v1/heartbeats | Create a new heartbeat check


# **v1_heartbeats_check_id_channels_channel_id_delete**
> v1_heartbeats_check_id_channels_channel_id_delete(check_id, channel_id)

Remove alert channel from heartbeat check

Remove alert channel from heartbeat check

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
    api_instance = pingera.HeartbeatsApi(api_client)
    check_id = 'check_id_example' # str | The ID of the heartbeat check.
    channel_id = 'channel_id_example' # str | The ID of the alert channel to remove.

    try:
        # Remove alert channel from heartbeat check
        api_instance.v1_heartbeats_check_id_channels_channel_id_delete(check_id, channel_id)
    except Exception as e:
        print("Exception when calling HeartbeatsApi->v1_heartbeats_check_id_channels_channel_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The ID of the heartbeat check. | 
 **channel_id** | **str**| The ID of the alert channel to remove. | 

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

# **v1_heartbeats_check_id_channels_get**
> v1_heartbeats_check_id_channels_get(check_id)

Get alert channels assigned to heartbeat check

Get alert channels assigned to heartbeat check

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
    api_instance = pingera.HeartbeatsApi(api_client)
    check_id = 'check_id_example' # str | The ID of the heartbeat check.

    try:
        # Get alert channels assigned to heartbeat check
        api_instance.v1_heartbeats_check_id_channels_get(check_id)
    except Exception as e:
        print("Exception when calling HeartbeatsApi->v1_heartbeats_check_id_channels_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The ID of the heartbeat check. | 

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
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_heartbeats_check_id_channels_post**
> v1_heartbeats_check_id_channels_post(check_id, heartbeat_check_channel_assignment)

Assign alert channels to heartbeat check

Assign alert channels to heartbeat check

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.heartbeat_check_channel_assignment import HeartbeatCheckChannelAssignment
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
    api_instance = pingera.HeartbeatsApi(api_client)
    check_id = 'check_id_example' # str | The ID of the heartbeat check.
    heartbeat_check_channel_assignment = pingera.HeartbeatCheckChannelAssignment() # HeartbeatCheckChannelAssignment | 

    try:
        # Assign alert channels to heartbeat check
        api_instance.v1_heartbeats_check_id_channels_post(check_id, heartbeat_check_channel_assignment)
    except Exception as e:
        print("Exception when calling HeartbeatsApi->v1_heartbeats_check_id_channels_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The ID of the heartbeat check. | 
 **heartbeat_check_channel_assignment** | [**HeartbeatCheckChannelAssignment**](HeartbeatCheckChannelAssignment.md)|  | 

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
**201** | Created |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_heartbeats_check_id_delete**
> v1_heartbeats_check_id_delete(check_id)

Delete a heartbeat check

Delete a heartbeat check

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
    api_instance = pingera.HeartbeatsApi(api_client)
    check_id = 'check_id_example' # str | The ID of the heartbeat check.

    try:
        # Delete a heartbeat check
        api_instance.v1_heartbeats_check_id_delete(check_id)
    except Exception as e:
        print("Exception when calling HeartbeatsApi->v1_heartbeats_check_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The ID of the heartbeat check. | 

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

# **v1_heartbeats_check_id_get**
> HeartbeatCheckDetail v1_heartbeats_check_id_get(check_id)

Get specific heartbeat check

Get specific heartbeat check with recent pings

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.heartbeat_check_detail import HeartbeatCheckDetail
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
    api_instance = pingera.HeartbeatsApi(api_client)
    check_id = 'check_id_example' # str | The ID of the heartbeat check.

    try:
        # Get specific heartbeat check
        api_response = api_instance.v1_heartbeats_check_id_get(check_id)
        print("The response of HeartbeatsApi->v1_heartbeats_check_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeartbeatsApi->v1_heartbeats_check_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The ID of the heartbeat check. | 

### Return type

[**HeartbeatCheckDetail**](HeartbeatCheckDetail.md)

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

# **v1_heartbeats_check_id_patch**
> HeartbeatCheck v1_heartbeats_check_id_patch(check_id, heartbeat_check1)

Update an existing heartbeat check

Update an existing heartbeat check

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.heartbeat_check import HeartbeatCheck
from pingera.models.heartbeat_check1 import HeartbeatCheck1
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
    api_instance = pingera.HeartbeatsApi(api_client)
    check_id = 'check_id_example' # str | The ID of the heartbeat check.
    heartbeat_check1 = pingera.HeartbeatCheck1() # HeartbeatCheck1 | 

    try:
        # Update an existing heartbeat check
        api_response = api_instance.v1_heartbeats_check_id_patch(check_id, heartbeat_check1)
        print("The response of HeartbeatsApi->v1_heartbeats_check_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeartbeatsApi->v1_heartbeats_check_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The ID of the heartbeat check. | 
 **heartbeat_check1** | [**HeartbeatCheck1**](HeartbeatCheck1.md)|  | 

### Return type

[**HeartbeatCheck**](HeartbeatCheck.md)

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

# **v1_heartbeats_check_id_ping_get**
> HeartbeatPingResponse v1_heartbeats_check_id_ping_get(check_id)

Receive heartbeat ping (GET)

Public endpoint for receiving heartbeat pings via GET request (no authentication required)

### Example


```python
import pingera
from pingera.models.heartbeat_ping_response import HeartbeatPingResponse
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
    api_instance = pingera.HeartbeatsApi(api_client)
    check_id = 'check_id_example' # str | The ID of the heartbeat check.

    try:
        # Receive heartbeat ping (GET)
        api_response = api_instance.v1_heartbeats_check_id_ping_get(check_id)
        print("The response of HeartbeatsApi->v1_heartbeats_check_id_ping_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeartbeatsApi->v1_heartbeats_check_id_ping_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The ID of the heartbeat check. | 

### Return type

[**HeartbeatPingResponse**](HeartbeatPingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_heartbeats_check_id_ping_post**
> HeartbeatPingResponse v1_heartbeats_check_id_ping_post(check_id, request_body=request_body)

Receive heartbeat ping (POST)

Public endpoint for receiving heartbeat pings via POST request with optional JSON data (no authentication required)

### Example


```python
import pingera
from pingera.models.heartbeat_ping_response import HeartbeatPingResponse
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
    api_instance = pingera.HeartbeatsApi(api_client)
    check_id = 'check_id_example' # str | The ID of the heartbeat check.
    request_body = None # Dict[str, object] | Optional ping data (JSON) (optional)

    try:
        # Receive heartbeat ping (POST)
        api_response = api_instance.v1_heartbeats_check_id_ping_post(check_id, request_body=request_body)
        print("The response of HeartbeatsApi->v1_heartbeats_check_id_ping_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeartbeatsApi->v1_heartbeats_check_id_ping_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The ID of the heartbeat check. | 
 **request_body** | [**Dict[str, object]**](object.md)| Optional ping data (JSON) | [optional] 

### Return type

[**HeartbeatPingResponse**](HeartbeatPingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_heartbeats_check_id_pings_count_get**
> HeartbeatPingCountResponse v1_heartbeats_check_id_pings_count_get(check_id, start_date=start_date, end_date=end_date)

Get ping count history

Get ping count history for heartbeat check with hourly buckets. Returns ping counts grouped by hour for the specified time period.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.heartbeat_ping_count_response import HeartbeatPingCountResponse
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
    api_instance = pingera.HeartbeatsApi(api_client)
    check_id = 'check_id_example' # str | The ID of the heartbeat check.
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter pings from this date (ISO format). Defaults to 24 hours ago. (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter pings until this date (ISO format). Defaults to current time. (optional)

    try:
        # Get ping count history
        api_response = api_instance.v1_heartbeats_check_id_pings_count_get(check_id, start_date=start_date, end_date=end_date)
        print("The response of HeartbeatsApi->v1_heartbeats_check_id_pings_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeartbeatsApi->v1_heartbeats_check_id_pings_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The ID of the heartbeat check. | 
 **start_date** | **datetime**| Filter pings from this date (ISO format). Defaults to 24 hours ago. | [optional] 
 **end_date** | **datetime**| Filter pings until this date (ISO format). Defaults to current time. | [optional] 

### Return type

[**HeartbeatPingCountResponse**](HeartbeatPingCountResponse.md)

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

# **v1_heartbeats_check_id_pings_get**
> HeartbeatPingHistory v1_heartbeats_check_id_pings_get(check_id, page=page, per_page=per_page, start_date=start_date, end_date=end_date)

Get ping history

Get ping history for heartbeat check with pagination and filtering

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.heartbeat_ping_history import HeartbeatPingHistory
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
    api_instance = pingera.HeartbeatsApi(api_client)
    check_id = 'check_id_example' # str | The ID of the heartbeat check.
    page = 56 # int | Page number for pagination (default: 1) (optional)
    per_page = 56 # int | Number of items per page (default: 50, max: 100) (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter pings from this date (ISO format) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter pings until this date (ISO format) (optional)

    try:
        # Get ping history
        api_response = api_instance.v1_heartbeats_check_id_pings_get(check_id, page=page, per_page=per_page, start_date=start_date, end_date=end_date)
        print("The response of HeartbeatsApi->v1_heartbeats_check_id_pings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeartbeatsApi->v1_heartbeats_check_id_pings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The ID of the heartbeat check. | 
 **page** | **int**| Page number for pagination (default: 1) | [optional] 
 **per_page** | **int**| Number of items per page (default: 50, max: 100) | [optional] 
 **start_date** | **datetime**| Filter pings from this date (ISO format) | [optional] 
 **end_date** | **datetime**| Filter pings until this date (ISO format) | [optional] 

### Return type

[**HeartbeatPingHistory**](HeartbeatPingHistory.md)

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

# **v1_heartbeats_check_id_put**
> HeartbeatCheck v1_heartbeats_check_id_put(check_id, heartbeat_check1)

Update an existing heartbeat check

Update an existing heartbeat check

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.heartbeat_check import HeartbeatCheck
from pingera.models.heartbeat_check1 import HeartbeatCheck1
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
    api_instance = pingera.HeartbeatsApi(api_client)
    check_id = 'check_id_example' # str | The ID of the heartbeat check.
    heartbeat_check1 = pingera.HeartbeatCheck1() # HeartbeatCheck1 | 

    try:
        # Update an existing heartbeat check
        api_response = api_instance.v1_heartbeats_check_id_put(check_id, heartbeat_check1)
        print("The response of HeartbeatsApi->v1_heartbeats_check_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeartbeatsApi->v1_heartbeats_check_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The ID of the heartbeat check. | 
 **heartbeat_check1** | [**HeartbeatCheck1**](HeartbeatCheck1.md)|  | 

### Return type

[**HeartbeatCheck**](HeartbeatCheck.md)

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

# **v1_heartbeats_get**
> HeartbeatCheckList v1_heartbeats_get(page=page, per_page=per_page)

Get all heartbeat checks

Get all heartbeat checks for current organization with pagination

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.heartbeat_check_list import HeartbeatCheckList
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
    api_instance = pingera.HeartbeatsApi(api_client)
    page = 56 # int | Page number for pagination (default: 1) (optional)
    per_page = 56 # int | Number of items per page (default: 50, max: 100) (optional)

    try:
        # Get all heartbeat checks
        api_response = api_instance.v1_heartbeats_get(page=page, per_page=per_page)
        print("The response of HeartbeatsApi->v1_heartbeats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeartbeatsApi->v1_heartbeats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number for pagination (default: 1) | [optional] 
 **per_page** | **int**| Number of items per page (default: 50, max: 100) | [optional] 

### Return type

[**HeartbeatCheckList**](HeartbeatCheckList.md)

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

# **v1_heartbeats_post**
> HeartbeatCheck v1_heartbeats_post(heartbeat_check)

Create a new heartbeat check

Create a new heartbeat check

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.heartbeat_check import HeartbeatCheck
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
    api_instance = pingera.HeartbeatsApi(api_client)
    heartbeat_check = pingera.HeartbeatCheck() # HeartbeatCheck | 

    try:
        # Create a new heartbeat check
        api_response = api_instance.v1_heartbeats_post(heartbeat_check)
        print("The response of HeartbeatsApi->v1_heartbeats_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeartbeatsApi->v1_heartbeats_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heartbeat_check** | [**HeartbeatCheck**](HeartbeatCheck.md)|  | 

### Return type

[**HeartbeatCheck**](HeartbeatCheck.md)

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

