# pingera.SecretsApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_secrets_get**](SecretsApi.md#v1_secrets_get) | **GET** /v1/secrets | Get all organization secrets
[**v1_secrets_post**](SecretsApi.md#v1_secrets_post) | **POST** /v1/secrets | Create a new secret
[**v1_secrets_secret_id_delete**](SecretsApi.md#v1_secrets_secret_id_delete) | **DELETE** /v1/secrets/{secret_id} | Delete a secret
[**v1_secrets_secret_id_get**](SecretsApi.md#v1_secrets_secret_id_get) | **GET** /v1/secrets/{secret_id} | Get a specific secret
[**v1_secrets_secret_id_patch**](SecretsApi.md#v1_secrets_secret_id_patch) | **PATCH** /v1/secrets/{secret_id} | Update a secret


# **v1_secrets_get**
> SecretList v1_secrets_get(page=page, page_size=page_size)

Get all organization secrets

Get all secrets for current organization with pagination. Secret values are excluded from list responses for security.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.secret_list import SecretList
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
    api_instance = pingera.SecretsApi(api_client)
    page = 1 # int | Page number for pagination (default: 1). (optional) (default to 1)
    page_size = 20 # int | Number of items per page (default: 20, max: 100). (optional) (default to 20)

    try:
        # Get all organization secrets
        api_response = api_instance.v1_secrets_get(page=page, page_size=page_size)
        print("The response of SecretsApi->v1_secrets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->v1_secrets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number for pagination (default: 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default: 20, max: 100). | [optional] [default to 20]

### Return type

[**SecretList**](SecretList.md)

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

# **v1_secrets_post**
> Secret1 v1_secrets_post(secret1)

Create a new secret

Create a new organization secret. The secret value will be encrypted in storage.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.secret1 import Secret1
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
    api_instance = pingera.SecretsApi(api_client)
    secret1 = pingera.Secret1() # Secret1 | 

    try:
        # Create a new secret
        api_response = api_instance.v1_secrets_post(secret1)
        print("The response of SecretsApi->v1_secrets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->v1_secrets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret1** | [**Secret1**](Secret1.md)|  | 

### Return type

[**Secret1**](Secret1.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |
**201** | Created |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_secrets_secret_id_delete**
> v1_secrets_secret_id_delete(secret_id)

Delete a secret

Delete a secret. This action cannot be undone.

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
    api_instance = pingera.SecretsApi(api_client)
    secret_id = 'secret_id_example' # str | The unique identifier of the secret to delete.

    try:
        # Delete a secret
        api_instance.v1_secrets_secret_id_delete(secret_id)
    except Exception as e:
        print("Exception when calling SecretsApi->v1_secrets_secret_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **str**| The unique identifier of the secret to delete. | 

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

# **v1_secrets_secret_id_get**
> Secret1 v1_secrets_secret_id_get(secret_id)

Get a specific secret

Get a specific secret by ID. The secret value is included only for editor and admin roles.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.secret1 import Secret1
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
    api_instance = pingera.SecretsApi(api_client)
    secret_id = 'secret_id_example' # str | The unique identifier of the secret.

    try:
        # Get a specific secret
        api_response = api_instance.v1_secrets_secret_id_get(secret_id)
        print("The response of SecretsApi->v1_secrets_secret_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->v1_secrets_secret_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **str**| The unique identifier of the secret. | 

### Return type

[**Secret1**](Secret1.md)

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

# **v1_secrets_secret_id_patch**
> Secret1 v1_secrets_secret_id_patch(secret_id, secret2)

Update a secret

Update a secret. Only the secret value can be updated, not the name.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.secret1 import Secret1
from pingera.models.secret2 import Secret2
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
    api_instance = pingera.SecretsApi(api_client)
    secret_id = 'secret_id_example' # str | The unique identifier of the secret to update.
    secret2 = pingera.Secret2() # Secret2 | 

    try:
        # Update a secret
        api_response = api_instance.v1_secrets_secret_id_patch(secret_id, secret2)
        print("The response of SecretsApi->v1_secrets_secret_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->v1_secrets_secret_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **str**| The unique identifier of the secret to update. | 
 **secret2** | [**Secret2**](Secret2.md)|  | 

### Return type

[**Secret1**](Secret1.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

