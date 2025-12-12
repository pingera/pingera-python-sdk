# pingera.OAuthApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_auth_oauth_accounts_get**](OAuthApi.md#v1_auth_oauth_accounts_get) | **GET** /v1/auth/oauth/accounts | Get linked OAuth accounts
[**v1_auth_oauth_provider_name_authorize_get**](OAuthApi.md#v1_auth_oauth_provider_name_authorize_get) | **GET** /v1/auth/oauth/{provider_name}/authorize | Initiate OAuth authorization
[**v1_auth_oauth_provider_name_callback_get**](OAuthApi.md#v1_auth_oauth_provider_name_callback_get) | **GET** /v1/auth/oauth/{provider_name}/callback | Handle OAuth callback
[**v1_auth_oauth_provider_name_link_post**](OAuthApi.md#v1_auth_oauth_provider_name_link_post) | **POST** /v1/auth/oauth/{provider_name}/link | Link OAuth account to existing user
[**v1_auth_oauth_provider_name_unlink_delete**](OAuthApi.md#v1_auth_oauth_provider_name_unlink_delete) | **DELETE** /v1/auth/oauth/{provider_name}/unlink | Unlink OAuth account
[**v1_auth_oauth_providers_get**](OAuthApi.md#v1_auth_oauth_providers_get) | **GET** /v1/auth/oauth/providers | Get available OAuth providers


# **v1_auth_oauth_accounts_get**
> LinkedOAuthAccountsResponse v1_auth_oauth_accounts_get()

Get linked OAuth accounts

Retrieve all OAuth accounts linked to the current user

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.linked_o_auth_accounts_response import LinkedOAuthAccountsResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = pingera.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pingera.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pingera.OAuthApi(api_client)

    try:
        # Get linked OAuth accounts
        api_response = api_instance.v1_auth_oauth_accounts_get()
        print("The response of OAuthApi->v1_auth_oauth_accounts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->v1_auth_oauth_accounts_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LinkedOAuthAccountsResponse**](LinkedOAuthAccountsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_oauth_provider_name_authorize_get**
> OAuthAuthorizeResponse v1_auth_oauth_provider_name_authorize_get(provider_name)

Initiate OAuth authorization

Start OAuth authorization flow for the specified provider

### Example


```python
import pingera
from pingera.models.o_auth_authorize_response import OAuthAuthorizeResponse
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
    api_instance = pingera.OAuthApi(api_client)
    provider_name = 'provider_name_example' # str | 

    try:
        # Initiate OAuth authorization
        api_response = api_instance.v1_auth_oauth_provider_name_authorize_get(provider_name)
        print("The response of OAuthApi->v1_auth_oauth_provider_name_authorize_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->v1_auth_oauth_provider_name_authorize_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | 

### Return type

[**OAuthAuthorizeResponse**](OAuthAuthorizeResponse.md)

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

# **v1_auth_oauth_provider_name_callback_get**
> OAuthLoginResponse v1_auth_oauth_provider_name_callback_get(provider_name, code, state, error_description=error_description, error=error)

Handle OAuth callback

Handle OAuth provider callback and complete authentication

### Example


```python
import pingera
from pingera.models.o_auth_login_response import OAuthLoginResponse
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
    api_instance = pingera.OAuthApi(api_client)
    provider_name = 'provider_name_example' # str | 
    code = 'def456ghi789' # str | OAuth authorization code from provider
    state = 'abc123def456' # str | OAuth state parameter for CSRF validation
    error_description = 'User denied access' # str | Human-readable error description (optional)
    error = 'access_denied' # str | OAuth error code if authorization failed (optional)

    try:
        # Handle OAuth callback
        api_response = api_instance.v1_auth_oauth_provider_name_callback_get(provider_name, code, state, error_description=error_description, error=error)
        print("The response of OAuthApi->v1_auth_oauth_provider_name_callback_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->v1_auth_oauth_provider_name_callback_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | 
 **code** | **str**| OAuth authorization code from provider | 
 **state** | **str**| OAuth state parameter for CSRF validation | 
 **error_description** | **str**| Human-readable error description | [optional] 
 **error** | **str**| OAuth error code if authorization failed | [optional] 

### Return type

[**OAuthLoginResponse**](OAuthLoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_oauth_provider_name_link_post**
> OAuthAuthorizeResponse v1_auth_oauth_provider_name_link_post(provider_name)

Link OAuth account to existing user

Initiate OAuth flow to link an account to the currently authenticated user

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.o_auth_authorize_response import OAuthAuthorizeResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = pingera.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pingera.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pingera.OAuthApi(api_client)
    provider_name = 'provider_name_example' # str | 

    try:
        # Link OAuth account to existing user
        api_response = api_instance.v1_auth_oauth_provider_name_link_post(provider_name)
        print("The response of OAuthApi->v1_auth_oauth_provider_name_link_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->v1_auth_oauth_provider_name_link_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | 

### Return type

[**OAuthAuthorizeResponse**](OAuthAuthorizeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_oauth_provider_name_unlink_delete**
> OAuthUnlinkResponse v1_auth_oauth_provider_name_unlink_delete(provider_name)

Unlink OAuth account

Remove OAuth account link from the current user

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.o_auth_unlink_response import OAuthUnlinkResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = pingera.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pingera.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pingera.OAuthApi(api_client)
    provider_name = 'provider_name_example' # str | 

    try:
        # Unlink OAuth account
        api_response = api_instance.v1_auth_oauth_provider_name_unlink_delete(provider_name)
        print("The response of OAuthApi->v1_auth_oauth_provider_name_unlink_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->v1_auth_oauth_provider_name_unlink_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | 

### Return type

[**OAuthUnlinkResponse**](OAuthUnlinkResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_oauth_providers_get**
> OAuthProvidersResponse v1_auth_oauth_providers_get()

Get available OAuth providers

Retrieve a list of all available OAuth providers for authentication

### Example


```python
import pingera
from pingera.models.o_auth_providers_response import OAuthProvidersResponse
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
    api_instance = pingera.OAuthApi(api_client)

    try:
        # Get available OAuth providers
        api_response = api_instance.v1_auth_oauth_providers_get()
        print("The response of OAuthApi->v1_auth_oauth_providers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->v1_auth_oauth_providers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OAuthProvidersResponse**](OAuthProvidersResponse.md)

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

