# pingera.OAuthApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_auth_oauth_accounts_get**](OAuthApi.md#v1_auth_oauth_accounts_get) | **GET** /v1/auth/oauth/accounts | Get linked OAuth accounts
[**v1_auth_oauth_provider_name_authorize_get**](OAuthApi.md#v1_auth_oauth_provider_name_authorize_get) | **GET** /v1/auth/oauth/{provider_name}/authorize | Start OAuth sign-in
[**v1_auth_oauth_provider_name_callback_post**](OAuthApi.md#v1_auth_oauth_provider_name_callback_post) | **POST** /v1/auth/oauth/{provider_name}/callback | Complete OAuth sign-in
[**v1_auth_oauth_provider_name_link_complete_post**](OAuthApi.md#v1_auth_oauth_provider_name_link_complete_post) | **POST** /v1/auth/oauth/{provider_name}/link/complete | Complete linking an OAuth account
[**v1_auth_oauth_provider_name_link_post**](OAuthApi.md#v1_auth_oauth_provider_name_link_post) | **POST** /v1/auth/oauth/{provider_name}/link | Start linking an OAuth account
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
> OAuthAuthorizeResponse v1_auth_oauth_provider_name_authorize_get(provider_name, code_challenge)

Start OAuth sign-in

Returns the provider authorization URL for signing in or signing up. The client must send a PKCE S256 code_challenge and keep the matching code_verifier and returned state until the callback.

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
    code_challenge = 'E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM' # str | Base64url-encoded SHA-256 hash of the client's PKCE code_verifier (S256)

    try:
        # Start OAuth sign-in
        api_response = api_instance.v1_auth_oauth_provider_name_authorize_get(provider_name, code_challenge)
        print("The response of OAuthApi->v1_auth_oauth_provider_name_authorize_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->v1_auth_oauth_provider_name_authorize_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | 
 **code_challenge** | **str**| Base64url-encoded SHA-256 hash of the client&#39;s PKCE code_verifier (S256) | 

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
**422** | Unprocessable Entity |  -  |
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_oauth_provider_name_callback_post**
> OAuthLoginResponse v1_auth_oauth_provider_name_callback_post(provider_name, o_auth_callback)

Complete OAuth sign-in

Exchanges the authorization code for Pingera access and refresh tokens. Signs in the user linked to the provider account, links an existing user with the same verified email, or registers a new user and organization.

### Example


```python
import pingera
from pingera.models.o_auth_callback import OAuthCallback
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
    o_auth_callback = pingera.OAuthCallback() # OAuthCallback | 

    try:
        # Complete OAuth sign-in
        api_response = api_instance.v1_auth_oauth_provider_name_callback_post(provider_name, o_auth_callback)
        print("The response of OAuthApi->v1_auth_oauth_provider_name_callback_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->v1_auth_oauth_provider_name_callback_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | 
 **o_auth_callback** | [**OAuthCallback**](OAuthCallback.md)|  | 

### Return type

[**OAuthLoginResponse**](OAuthLoginResponse.md)

### Authorization

No authorization required

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

# **v1_auth_oauth_provider_name_link_complete_post**
> OAuthLinkCompleteResponse v1_auth_oauth_provider_name_link_complete_post(provider_name, o_auth_callback)

Complete linking an OAuth account

Links the provider account that authorized the request to the current user

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.o_auth_callback import OAuthCallback
from pingera.models.o_auth_link_complete_response import OAuthLinkCompleteResponse
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
    o_auth_callback = pingera.OAuthCallback() # OAuthCallback | 

    try:
        # Complete linking an OAuth account
        api_response = api_instance.v1_auth_oauth_provider_name_link_complete_post(provider_name, o_auth_callback)
        print("The response of OAuthApi->v1_auth_oauth_provider_name_link_complete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->v1_auth_oauth_provider_name_link_complete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | 
 **o_auth_callback** | [**OAuthCallback**](OAuthCallback.md)|  | 

### Return type

[**OAuthLinkCompleteResponse**](OAuthLinkCompleteResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

# **v1_auth_oauth_provider_name_link_post**
> OAuthAuthorizeResponse v1_auth_oauth_provider_name_link_post(provider_name, o_auth_authorize_request)

Start linking an OAuth account

Returns the provider authorization URL for linking a provider account to the current user. Finish with POST /auth/oauth/{provider_name}/link/complete.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.o_auth_authorize_request import OAuthAuthorizeRequest
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
    o_auth_authorize_request = pingera.OAuthAuthorizeRequest() # OAuthAuthorizeRequest | 

    try:
        # Start linking an OAuth account
        api_response = api_instance.v1_auth_oauth_provider_name_link_post(provider_name, o_auth_authorize_request)
        print("The response of OAuthApi->v1_auth_oauth_provider_name_link_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->v1_auth_oauth_provider_name_link_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | 
 **o_auth_authorize_request** | [**OAuthAuthorizeRequest**](OAuthAuthorizeRequest.md)|  | 

### Return type

[**OAuthAuthorizeResponse**](OAuthAuthorizeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

