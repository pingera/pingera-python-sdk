# pingera.AuthEnhancedApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_auth_login_options_post**](AuthEnhancedApi.md#v1_auth_login_options_post) | **POST** /v1/auth/login/options | Get authentication options
[**v1_auth_login_post**](AuthEnhancedApi.md#v1_auth_login_post) | **POST** /v1/auth/login | Enhanced login
[**v1_auth_preferences_get**](AuthEnhancedApi.md#v1_auth_preferences_get) | **GET** /v1/auth/preferences | Get authentication preferences
[**v1_auth_preferences_put**](AuthEnhancedApi.md#v1_auth_preferences_put) | **PUT** /v1/auth/preferences | Update authentication preferences
[**v1_auth_setup_check_get**](AuthEnhancedApi.md#v1_auth_setup_check_get) | **GET** /v1/auth/setup/check | Check authentication setup
[**v1_auth_setup_recommend_get**](AuthEnhancedApi.md#v1_auth_setup_recommend_get) | **GET** /v1/auth/setup/recommend | Get authentication recommendations


# **v1_auth_login_options_post**
> LoginOptionsResponse v1_auth_login_options_post(login_options)

Get authentication options

Get available authentication methods for an email address. This endpoint checks what authentication options are available for a given email address, including password, passkey, and OAuth providers.

### Example


```python
import pingera
from pingera.models.login_options import LoginOptions
from pingera.models.login_options_response import LoginOptionsResponse
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
    api_instance = pingera.AuthEnhancedApi(api_client)
    login_options = pingera.LoginOptions() # LoginOptions | 

    try:
        # Get authentication options
        api_response = api_instance.v1_auth_login_options_post(login_options)
        print("The response of AuthEnhancedApi->v1_auth_login_options_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthEnhancedApi->v1_auth_login_options_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_options** | [**LoginOptions**](LoginOptions.md)|  | 

### Return type

[**LoginOptionsResponse**](LoginOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Validation error - Invalid email format |  -  |
**200** | Authentication options retrieved successfully. |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_login_post**
> LoginResponse v1_auth_login_post(enhanced_login)

Enhanced login

Enhanced login endpoint supporting multiple authentication methods. Currently supports password authentication with plans for passkey and OAuth integration.

### Example


```python
import pingera
from pingera.models.enhanced_login import EnhancedLogin
from pingera.models.login_response import LoginResponse
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
    api_instance = pingera.AuthEnhancedApi(api_client)
    enhanced_login = pingera.EnhancedLogin() # EnhancedLogin | 

    try:
        # Enhanced login
        api_response = api_instance.v1_auth_login_post(enhanced_login)
        print("The response of AuthEnhancedApi->v1_auth_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthEnhancedApi->v1_auth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enhanced_login** | [**EnhancedLogin**](EnhancedLogin.md)|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | User authenticated successfully. |  -  |
**400** | Bad Request - Missing fields or unsupported method |  -  |
**401** | Unauthorized - Authentication failed |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_preferences_get**
> AuthPreferences v1_auth_preferences_get()

Get authentication preferences

Get user authentication preferences including preferred method, 2FA requirements, and passkey-only mode.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.auth_preferences import AuthPreferences
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
    api_instance = pingera.AuthEnhancedApi(api_client)

    try:
        # Get authentication preferences
        api_response = api_instance.v1_auth_preferences_get()
        print("The response of AuthEnhancedApi->v1_auth_preferences_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthEnhancedApi->v1_auth_preferences_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthPreferences**](AuthPreferences.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authentication preferences retrieved successfully. |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_preferences_put**
> AuthPreferences v1_auth_preferences_put(auth_preferences1)

Update authentication preferences

Update user authentication preferences. Allows users to set their preferred authentication method, enable/disable 2FA requirements, and configure passkey-only mode.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.auth_preferences import AuthPreferences
from pingera.models.auth_preferences1 import AuthPreferences1
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
    api_instance = pingera.AuthEnhancedApi(api_client)
    auth_preferences1 = pingera.AuthPreferences1() # AuthPreferences1 | 

    try:
        # Update authentication preferences
        api_response = api_instance.v1_auth_preferences_put(auth_preferences1)
        print("The response of AuthEnhancedApi->v1_auth_preferences_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthEnhancedApi->v1_auth_preferences_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_preferences1** | [**AuthPreferences1**](AuthPreferences1.md)|  | 

### Return type

[**AuthPreferences**](AuthPreferences.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | Authentication preferences updated successfully. |  -  |
**400** | Bad Request - Invalid authentication method or validation error |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_setup_check_get**
> AuthSetupStatus v1_auth_setup_check_get()

Check authentication setup

Check user's authentication setup status. Returns information about configured authentication methods including passwords, passkeys, OAuth providers, and 2FA status.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.auth_setup_status import AuthSetupStatus
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
    api_instance = pingera.AuthEnhancedApi(api_client)

    try:
        # Check authentication setup
        api_response = api_instance.v1_auth_setup_check_get()
        print("The response of AuthEnhancedApi->v1_auth_setup_check_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthEnhancedApi->v1_auth_setup_check_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthSetupStatus**](AuthSetupStatus.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authentication setup status retrieved successfully. |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_setup_recommend_get**
> AuthRecommendations v1_auth_setup_recommend_get()

Get authentication recommendations

Get authentication setup recommendations for user. Provides personalized suggestions for improving account security based on current authentication configuration.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.auth_recommendations import AuthRecommendations
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
    api_instance = pingera.AuthEnhancedApi(api_client)

    try:
        # Get authentication recommendations
        api_response = api_instance.v1_auth_setup_recommend_get()
        print("The response of AuthEnhancedApi->v1_auth_setup_recommend_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthEnhancedApi->v1_auth_setup_recommend_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthRecommendations**](AuthRecommendations.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authentication recommendations retrieved successfully. |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

