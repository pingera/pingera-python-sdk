# pingera.CheckSecretsApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_checks_check_id_secrets_get**](CheckSecretsApi.md#v1_checks_check_id_secrets_get) | **GET** /v1/checks/{check_id}/secrets | Get all secrets for a check
[**v1_checks_check_id_secrets_post**](CheckSecretsApi.md#v1_checks_check_id_secrets_post) | **POST** /v1/checks/{check_id}/secrets | Add secret to check
[**v1_checks_check_id_secrets_put**](CheckSecretsApi.md#v1_checks_check_id_secrets_put) | **PUT** /v1/checks/{check_id}/secrets | Update all secrets for a check
[**v1_checks_check_id_secrets_secret_id_delete**](CheckSecretsApi.md#v1_checks_check_id_secrets_secret_id_delete) | **DELETE** /v1/checks/{check_id}/secrets/{secret_id} | Remove secret from check


# **v1_checks_check_id_secrets_get**
> List[CheckSecret] v1_checks_check_id_secrets_get(check_id)

Get all secrets for a check

Get all secrets associated with a specific check

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.check_secret import CheckSecret
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
    api_instance = pingera.CheckSecretsApi(api_client)
    check_id = 'check_id_example' # str | The unique identifier of the monitor check.

    try:
        # Get all secrets for a check
        api_response = api_instance.v1_checks_check_id_secrets_get(check_id)
        print("The response of CheckSecretsApi->v1_checks_check_id_secrets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckSecretsApi->v1_checks_check_id_secrets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The unique identifier of the monitor check. | 

### Return type

[**List[CheckSecret]**](CheckSecret.md)

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

# **v1_checks_check_id_secrets_post**
> CheckSecret v1_checks_check_id_secrets_post(check_id, check_secret)

Add secret to check

Associate a secret with a check using an environment variable name

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.check_secret import CheckSecret
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
    api_instance = pingera.CheckSecretsApi(api_client)
    check_id = 'check_id_example' # str | The unique identifier of the monitor check.
    check_secret = pingera.CheckSecret() # CheckSecret | 

    try:
        # Add secret to check
        api_response = api_instance.v1_checks_check_id_secrets_post(check_id, check_secret)
        print("The response of CheckSecretsApi->v1_checks_check_id_secrets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckSecretsApi->v1_checks_check_id_secrets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The unique identifier of the monitor check. | 
 **check_secret** | [**CheckSecret**](CheckSecret.md)|  | 

### Return type

[**CheckSecret**](CheckSecret.md)

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

# **v1_checks_check_id_secrets_put**
> List[CheckSecret] v1_checks_check_id_secrets_put(check_id, check_secret)

Update all secrets for a check

Replace all secret associations for a check. This will remove existing associations and create new ones.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.check_secret import CheckSecret
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
    api_instance = pingera.CheckSecretsApi(api_client)
    check_id = 'check_id_example' # str | The unique identifier of the monitor check.
    check_secret = [pingera.CheckSecret()] # List[CheckSecret] | 

    try:
        # Update all secrets for a check
        api_response = api_instance.v1_checks_check_id_secrets_put(check_id, check_secret)
        print("The response of CheckSecretsApi->v1_checks_check_id_secrets_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckSecretsApi->v1_checks_check_id_secrets_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The unique identifier of the monitor check. | 
 **check_secret** | [**List[CheckSecret]**](CheckSecret.md)|  | 

### Return type

[**List[CheckSecret]**](CheckSecret.md)

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

# **v1_checks_check_id_secrets_secret_id_delete**
> v1_checks_check_id_secrets_secret_id_delete(check_id, secret_id)

Remove secret from check

Remove a secret association from a check

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
    api_instance = pingera.CheckSecretsApi(api_client)
    check_id = 'check_id_example' # str | The unique identifier of the monitor check.
    secret_id = 'secret_id_example' # str | The unique identifier of the secret.

    try:
        # Remove secret from check
        api_instance.v1_checks_check_id_secrets_secret_id_delete(check_id, secret_id)
    except Exception as e:
        print("Exception when calling CheckSecretsApi->v1_checks_check_id_secrets_secret_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| The unique identifier of the monitor check. | 
 **secret_id** | **str**| The unique identifier of the secret. | 

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

