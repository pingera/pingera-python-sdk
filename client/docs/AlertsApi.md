# pingera.AlertsApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_alerts_alert_id_acknowledge_post**](AlertsApi.md#v1_alerts_alert_id_acknowledge_post) | **POST** /v1/alerts/{alert_id}/acknowledge | Acknowledge an alert
[**v1_alerts_alert_id_get**](AlertsApi.md#v1_alerts_alert_id_get) | **GET** /v1/alerts/{alert_id} | Get an alert by ID
[**v1_alerts_alert_id_notifications_get**](AlertsApi.md#v1_alerts_alert_id_notifications_get) | **GET** /v1/alerts/{alert_id}/notifications | Get all notifications for a specific alert
[**v1_alerts_alert_id_resolve_post**](AlertsApi.md#v1_alerts_alert_id_resolve_post) | **POST** /v1/alerts/{alert_id}/resolve | Manually resolve an alert
[**v1_alerts_channels_channel_id_delete**](AlertsApi.md#v1_alerts_channels_channel_id_delete) | **DELETE** /v1/alerts/channels/{channel_id} | Delete an alert channel by ID
[**v1_alerts_channels_channel_id_get**](AlertsApi.md#v1_alerts_channels_channel_id_get) | **GET** /v1/alerts/channels/{channel_id} | Get an alert channel by id
[**v1_alerts_channels_channel_id_put**](AlertsApi.md#v1_alerts_channels_channel_id_put) | **PUT** /v1/alerts/channels/{channel_id} | Update an alert channel by ID
[**v1_alerts_channels_get**](AlertsApi.md#v1_alerts_channels_get) | **GET** /v1/alerts/channels | Get all alert channels
[**v1_alerts_channels_post**](AlertsApi.md#v1_alerts_channels_post) | **POST** /v1/alerts/channels | Create a new alert channel
[**v1_alerts_get**](AlertsApi.md#v1_alerts_get) | **GET** /v1/alerts | Get all alerts
[**v1_alerts_rules_get**](AlertsApi.md#v1_alerts_rules_get) | **GET** /v1/alerts/rules | Get all alert rules
[**v1_alerts_rules_post**](AlertsApi.md#v1_alerts_rules_post) | **POST** /v1/alerts/rules | Create a new alert rule
[**v1_alerts_rules_rule_id_delete**](AlertsApi.md#v1_alerts_rules_rule_id_delete) | **DELETE** /v1/alerts/rules/{rule_id} | Delete an alert rule by ID
[**v1_alerts_rules_rule_id_get**](AlertsApi.md#v1_alerts_rules_rule_id_get) | **GET** /v1/alerts/rules/{rule_id} | Get an alert rule by ID
[**v1_alerts_rules_rule_id_put**](AlertsApi.md#v1_alerts_rules_rule_id_put) | **PUT** /v1/alerts/rules/{rule_id} | Update an alert rule by ID
[**v1_alerts_stats_get**](AlertsApi.md#v1_alerts_stats_get) | **GET** /v1/alerts/stats | Get alert statistics


# **v1_alerts_alert_id_acknowledge_post**
> Alert v1_alerts_alert_id_acknowledge_post(alert_id)

Acknowledge an alert

Acknowledge an alert (mark as acknowledged)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.alert import Alert
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
    api_instance = pingera.AlertsApi(api_client)
    alert_id = 'alert_id_example' # str | 

    try:
        # Acknowledge an alert
        api_response = api_instance.v1_alerts_alert_id_acknowledge_post(alert_id)
        print("The response of AlertsApi->v1_alerts_alert_id_acknowledge_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->v1_alerts_alert_id_acknowledge_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  | 

### Return type

[**Alert**](Alert.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request - Only firing alerts can be acknowledged |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**404** | Alert not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alerts_alert_id_get**
> Alert v1_alerts_alert_id_get(alert_id)

Get an alert by ID

Get an alert by ID

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.alert import Alert
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
    api_instance = pingera.AlertsApi(api_client)
    alert_id = 'alert_id_example' # str | 

    try:
        # Get an alert by ID
        api_response = api_instance.v1_alerts_alert_id_get(alert_id)
        print("The response of AlertsApi->v1_alerts_alert_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->v1_alerts_alert_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  | 

### Return type

[**Alert**](Alert.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**404** | Alert not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alerts_alert_id_notifications_get**
> List[AlertNotification] v1_alerts_alert_id_notifications_get(alert_id)

Get all notifications for a specific alert

Get all notifications for a specific alert

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.alert_notification import AlertNotification
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
    api_instance = pingera.AlertsApi(api_client)
    alert_id = 'alert_id_example' # str | 

    try:
        # Get all notifications for a specific alert
        api_response = api_instance.v1_alerts_alert_id_notifications_get(alert_id)
        print("The response of AlertsApi->v1_alerts_alert_id_notifications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->v1_alerts_alert_id_notifications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  | 

### Return type

[**List[AlertNotification]**](AlertNotification.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**404** | Alert not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alerts_alert_id_resolve_post**
> Alert v1_alerts_alert_id_resolve_post(alert_id)

Manually resolve an alert

Manually resolve an alert

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.alert import Alert
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
    api_instance = pingera.AlertsApi(api_client)
    alert_id = 'alert_id_example' # str | 

    try:
        # Manually resolve an alert
        api_response = api_instance.v1_alerts_alert_id_resolve_post(alert_id)
        print("The response of AlertsApi->v1_alerts_alert_id_resolve_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->v1_alerts_alert_id_resolve_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  | 

### Return type

[**Alert**](Alert.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request - Only active alerts can be resolved |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**404** | Alert not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alerts_channels_channel_id_delete**
> v1_alerts_channels_channel_id_delete(channel_id)

Delete an alert channel by ID

Delete an alert channel by ID

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
    api_instance = pingera.AlertsApi(api_client)
    channel_id = 'channel_id_example' # str | 

    try:
        # Delete an alert channel by ID
        api_instance.v1_alerts_channels_channel_id_delete(channel_id)
    except Exception as e:
        print("Exception when calling AlertsApi->v1_alerts_channels_channel_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

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
**400** | Bad Request - Channel is being used by alert rules |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**404** | Alert channel not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alerts_channels_channel_id_get**
> AlertChannel v1_alerts_channels_channel_id_get(channel_id)

Get an alert channel by id

Get an alert channel by id

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.alert_channel import AlertChannel
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
    api_instance = pingera.AlertsApi(api_client)
    channel_id = 'channel_id_example' # str | 

    try:
        # Get an alert channel by id
        api_response = api_instance.v1_alerts_channels_channel_id_get(channel_id)
        print("The response of AlertsApi->v1_alerts_channels_channel_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->v1_alerts_channels_channel_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

### Return type

[**AlertChannel**](AlertChannel.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Bad Request - Validation error |  -  |
**404** | Component not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alerts_channels_channel_id_put**
> AlertChannel v1_alerts_channels_channel_id_put(channel_id, alert_channel1)

Update an alert channel by ID

Update an alert channel by ID

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.alert_channel import AlertChannel
from pingera.models.alert_channel1 import AlertChannel1
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
    api_instance = pingera.AlertsApi(api_client)
    channel_id = 'channel_id_example' # str | 
    alert_channel1 = pingera.AlertChannel1() # AlertChannel1 | 

    try:
        # Update an alert channel by ID
        api_response = api_instance.v1_alerts_channels_channel_id_put(channel_id, alert_channel1)
        print("The response of AlertsApi->v1_alerts_channels_channel_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->v1_alerts_channels_channel_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **alert_channel1** | [**AlertChannel1**](AlertChannel1.md)|  | 

### Return type

[**AlertChannel**](AlertChannel.md)

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
**400** | Bad Request - Validation error |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**404** | Alert channel not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alerts_channels_get**
> List[AlertChannel] v1_alerts_channels_get()

Get all alert channels

Get all alert channels for the current organization

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.alert_channel import AlertChannel
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
    api_instance = pingera.AlertsApi(api_client)

    try:
        # Get all alert channels
        api_response = api_instance.v1_alerts_channels_get()
        print("The response of AlertsApi->v1_alerts_channels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->v1_alerts_channels_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AlertChannel]**](AlertChannel.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alerts_channels_post**
> AlertChannel v1_alerts_channels_post(alert_channel)

Create a new alert channel

Create a new alert channel

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.alert_channel import AlertChannel
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
    api_instance = pingera.AlertsApi(api_client)
    alert_channel = pingera.AlertChannel() # AlertChannel | 

    try:
        # Create a new alert channel
        api_response = api_instance.v1_alerts_channels_post(alert_channel)
        print("The response of AlertsApi->v1_alerts_channels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->v1_alerts_channels_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_channel** | [**AlertChannel**](AlertChannel.md)|  | 

### Return type

[**AlertChannel**](AlertChannel.md)

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
**400** | Bad Request - Validation error |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alerts_get**
> AlertList v1_alerts_get(status=status, check_id=check_id, severity=severity, page=page, per_page=per_page)

Get all alerts

Get all alerts for the organization with optional filtering and pagination

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.alert_list import AlertList
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
    api_instance = pingera.AlertsApi(api_client)
    status = 'status_example' # str | Filter alerts by status (active, firing, resolved, acknowledged, suppressed). (optional)
    check_id = 'check_id_example' # str | Filter alerts by check ID. (optional)
    severity = 'severity_example' # str | Filter alerts by severity level. (optional)
    page = 56 # int | Page number for pagination (default: 1). (optional)
    per_page = 56 # int | Number of alerts per page (default: 20, max: 100). (optional)

    try:
        # Get all alerts
        api_response = api_instance.v1_alerts_get(status=status, check_id=check_id, severity=severity, page=page, per_page=per_page)
        print("The response of AlertsApi->v1_alerts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->v1_alerts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter alerts by status (active, firing, resolved, acknowledged, suppressed). | [optional] 
 **check_id** | **str**| Filter alerts by check ID. | [optional] 
 **severity** | **str**| Filter alerts by severity level. | [optional] 
 **page** | **int**| Page number for pagination (default: 1). | [optional] 
 **per_page** | **int**| Number of alerts per page (default: 20, max: 100). | [optional] 

### Return type

[**AlertList**](AlertList.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request - Invalid filter parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alerts_rules_get**
> List[AlertRule] v1_alerts_rules_get()

Get all alert rules

Get all alert rules for the current organization

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.alert_rule import AlertRule
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
    api_instance = pingera.AlertsApi(api_client)

    try:
        # Get all alert rules
        api_response = api_instance.v1_alerts_rules_get()
        print("The response of AlertsApi->v1_alerts_rules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->v1_alerts_rules_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AlertRule]**](AlertRule.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alerts_rules_post**
> AlertRule v1_alerts_rules_post(alert_rule)

Create a new alert rule

Create a new alert rule

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.alert_rule import AlertRule
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
    api_instance = pingera.AlertsApi(api_client)
    alert_rule = pingera.AlertRule() # AlertRule | 

    try:
        # Create a new alert rule
        api_response = api_instance.v1_alerts_rules_post(alert_rule)
        print("The response of AlertsApi->v1_alerts_rules_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->v1_alerts_rules_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_rule** | [**AlertRule**](AlertRule.md)|  | 

### Return type

[**AlertRule**](AlertRule.md)

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
**400** | Bad Request - Validation error |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**404** | Check or channel not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alerts_rules_rule_id_delete**
> v1_alerts_rules_rule_id_delete(rule_id)

Delete an alert rule by ID

Delete an alert rule by ID

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
    api_instance = pingera.AlertsApi(api_client)
    rule_id = 'rule_id_example' # str | 

    try:
        # Delete an alert rule by ID
        api_instance.v1_alerts_rules_rule_id_delete(rule_id)
    except Exception as e:
        print("Exception when calling AlertsApi->v1_alerts_rules_rule_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

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
**401** | Unauthorized - Invalid or missing authentication |  -  |
**404** | Alert rule not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alerts_rules_rule_id_get**
> AlertRule v1_alerts_rules_rule_id_get(rule_id)

Get an alert rule by ID

Get an alert rule by ID

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.alert_rule import AlertRule
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
    api_instance = pingera.AlertsApi(api_client)
    rule_id = 'rule_id_example' # str | 

    try:
        # Get an alert rule by ID
        api_response = api_instance.v1_alerts_rules_rule_id_get(rule_id)
        print("The response of AlertsApi->v1_alerts_rules_rule_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->v1_alerts_rules_rule_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

### Return type

[**AlertRule**](AlertRule.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**404** | Alert rule not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alerts_rules_rule_id_put**
> AlertRule v1_alerts_rules_rule_id_put(rule_id, alert_rule1)

Update an alert rule by ID

Update an alert rule by ID

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.alert_rule import AlertRule
from pingera.models.alert_rule1 import AlertRule1
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
    api_instance = pingera.AlertsApi(api_client)
    rule_id = 'rule_id_example' # str | 
    alert_rule1 = pingera.AlertRule1() # AlertRule1 | 

    try:
        # Update an alert rule by ID
        api_response = api_instance.v1_alerts_rules_rule_id_put(rule_id, alert_rule1)
        print("The response of AlertsApi->v1_alerts_rules_rule_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->v1_alerts_rules_rule_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 
 **alert_rule1** | [**AlertRule1**](AlertRule1.md)|  | 

### Return type

[**AlertRule**](AlertRule.md)

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
**400** | Bad Request - Validation error |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**404** | Alert rule or referenced channels not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alerts_stats_get**
> AlertStats v1_alerts_stats_get()

Get alert statistics

Get alert statistics and metrics for the organization

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.alert_stats import AlertStats
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
    api_instance = pingera.AlertsApi(api_client)

    try:
        # Get alert statistics
        api_response = api_instance.v1_alerts_stats_get()
        print("The response of AlertsApi->v1_alerts_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->v1_alerts_stats_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AlertStats**](AlertStats.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

