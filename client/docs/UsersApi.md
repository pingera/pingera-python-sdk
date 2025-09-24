# pingera.UsersApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_api_tokens_get**](UsersApi.md#v1_api_tokens_get) | **GET** /v1/api-tokens | List API tokens
[**v1_api_tokens_post**](UsersApi.md#v1_api_tokens_post) | **POST** /v1/api-tokens | Create new API token
[**v1_api_tokens_token_id_delete**](UsersApi.md#v1_api_tokens_token_id_delete) | **DELETE** /v1/api-tokens/{token_id} | Delete API token
[**v1_login_post**](UsersApi.md#v1_login_post) | **POST** /v1/login | User login
[**v1_refresh_post**](UsersApi.md#v1_refresh_post) | **POST** /v1/refresh | Refresh access token
[**v1_register_post**](UsersApi.md#v1_register_post) | **POST** /v1/register | Register a new user
[**v1_users_change_password_post**](UsersApi.md#v1_users_change_password_post) | **POST** /v1/users/change-password | Change user password
[**v1_users_get**](UsersApi.md#v1_users_get) | **GET** /v1/users | Get all users
[**v1_users_invite_post**](UsersApi.md#v1_users_invite_post) | **POST** /v1/users/invite | Invite a new user
[**v1_users_onboarding_patch**](UsersApi.md#v1_users_onboarding_patch) | **PATCH** /v1/users/onboarding | Update user onboarding status
[**v1_users_profile_put**](UsersApi.md#v1_users_profile_put) | **PUT** /v1/users/profile | Update user profile information
[**v1_users_request_password_reset_post**](UsersApi.md#v1_users_request_password_reset_post) | **POST** /v1/users/request-password-reset | Request password reset email
[**v1_users_resend_verification_post**](UsersApi.md#v1_users_resend_verification_post) | **POST** /v1/users/resend-verification | Resend email verification
[**v1_users_reset_password_post**](UsersApi.md#v1_users_reset_password_post) | **POST** /v1/users/reset-password | Reset password using token
[**v1_users_roles_get**](UsersApi.md#v1_users_roles_get) | **GET** /v1/users/roles | Get available user roles
[**v1_users_user_id_delete**](UsersApi.md#v1_users_user_id_delete) | **DELETE** /v1/users/{user_id} | Delete user
[**v1_users_user_id_get**](UsersApi.md#v1_users_user_id_get) | **GET** /v1/users/{user_id} | Get user details
[**v1_users_user_id_patch**](UsersApi.md#v1_users_user_id_patch) | **PATCH** /v1/users/{user_id} | Update user
[**v1_users_user_id_put**](UsersApi.md#v1_users_user_id_put) | **PUT** /v1/users/{user_id} | Update user
[**v1_users_user_id_resend_invitation_post**](UsersApi.md#v1_users_user_id_resend_invitation_post) | **POST** /v1/users/{user_id}/resend-invitation | Resend invitation email for a user (admin only)
[**v1_verify_email_token_get**](UsersApi.md#v1_verify_email_token_get) | **GET** /v1/verify-email/{token} | Verify email address


# **v1_api_tokens_get**
> List[APIToken] v1_api_tokens_get()

List API tokens

List all API tokens for the current user. Token values are never returned in list operations.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.api_token import APIToken
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
    api_instance = pingera.UsersApi(api_client)

    try:
        # List API tokens
        api_response = api_instance.v1_api_tokens_get()
        print("The response of UsersApi->v1_api_tokens_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_api_tokens_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[APIToken]**](APIToken.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API tokens retrieved successfully. |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_api_tokens_post**
> APIToken v1_api_tokens_post(api_token)

Create new API token

Create a new API token for the current user. The token will only be returned once during creation.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.api_token import APIToken
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
    api_instance = pingera.UsersApi(api_client)
    api_token = pingera.APIToken() # APIToken | API token creation data

    try:
        # Create new API token
        api_response = api_instance.v1_api_tokens_post(api_token)
        print("The response of UsersApi->v1_api_tokens_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_api_tokens_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | [**APIToken**](APIToken.md)| API token creation data | 

### Return type

[**APIToken**](APIToken.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Validation error |  -  |
**201** | API token created successfully. Token value is only returned once. |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_api_tokens_token_id_delete**
> v1_api_tokens_token_id_delete(token_id)

Delete API token

Delete an API token. This action is irreversible and will immediately invalidate the token.

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
    api_instance = pingera.UsersApi(api_client)
    token_id = 'token_id_example' # str | The unique identifier of the API token to delete.

    try:
        # Delete API token
        api_instance.v1_api_tokens_token_id_delete(token_id)
    except Exception as e:
        print("Exception when calling UsersApi->v1_api_tokens_token_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The unique identifier of the API token to delete. | 

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
**204** | API token deleted successfully |  -  |
**401** | Unauthorized - Authentication required |  -  |
**404** | API token not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_login_post**
> V1LoginPost200Response v1_login_post(login)

User login

Authenticate user credentials and return access and refresh tokens. Requires email verification.

### Example


```python
import pingera
from pingera.models.login import Login
from pingera.models.v1_login_post200_response import V1LoginPost200Response
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
    api_instance = pingera.UsersApi(api_client)
    login = pingera.Login() # Login | User login credentials

    try:
        # User login
        api_response = api_instance.v1_login_post(login)
        print("The response of UsersApi->v1_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | [**Login**](Login.md)| User login credentials | 

### Return type

[**V1LoginPost200Response**](V1LoginPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Validation error |  -  |
**200** | Login successful. Returns access token, refresh token, and user data. |  -  |
**401** | Unauthorized - Invalid credentials |  -  |
**403** | Forbidden - Email not verified |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_refresh_post**
> V1RefreshPost200Response v1_refresh_post(authorization)

Refresh access token

Refresh access token using refresh token from Authorization header

### Example


```python
import pingera
from pingera.models.v1_refresh_post200_response import V1RefreshPost200Response
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
    api_instance = pingera.UsersApi(api_client)
    authorization = 'Bearer <refresh_token>' # str | Bearer token with refresh token

    try:
        # Refresh access token
        api_response = api_instance.v1_refresh_post(authorization)
        print("The response of UsersApi->v1_refresh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_refresh_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer token with refresh token | 

### Return type

[**V1RefreshPost200Response**](V1RefreshPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tokens refreshed successfully. |  -  |
**401** | Unauthorized - Invalid or expired refresh token |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_register_post**
> User v1_register_post(user)

Register a new user

Register a new user account and automatically create an organization with a free plan subscription. Sends email verification and team notification.

### Example


```python
import pingera
from pingera.models.user import User
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
    api_instance = pingera.UsersApi(api_client)
    user = pingera.User() # User | User registration data including email, password, and optional personal details

    try:
        # Register a new user
        api_response = api_instance.v1_register_post(user)
        print("The response of UsersApi->v1_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| User registration data including email, password, and optional personal details | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**201** | User registered successfully. Email verification sent. |  -  |
**400** | Validation error - Invalid request data |  -  |
**409** | Conflict - Email already registered |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_change_password_post**
> V1UsersChangePasswordPost200Response v1_users_change_password_post(v1_users_change_password_post_request)

Change user password

Change the current user password. Requires current password verification.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.v1_users_change_password_post200_response import V1UsersChangePasswordPost200Response
from pingera.models.v1_users_change_password_post_request import V1UsersChangePasswordPostRequest
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
    api_instance = pingera.UsersApi(api_client)
    v1_users_change_password_post_request = pingera.V1UsersChangePasswordPostRequest() # V1UsersChangePasswordPostRequest | Password change data

    try:
        # Change user password
        api_response = api_instance.v1_users_change_password_post(v1_users_change_password_post_request)
        print("The response of UsersApi->v1_users_change_password_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_users_change_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_users_change_password_post_request** | [**V1UsersChangePasswordPostRequest**](V1UsersChangePasswordPostRequest.md)| Password change data | 

### Return type

[**V1UsersChangePasswordPost200Response**](V1UsersChangePasswordPost200Response.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password changed successfully. |  -  |
**400** | Bad Request - Missing required fields |  -  |
**401** | Unauthorized - Current password incorrect |  -  |
**422** | Validation error |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_get**
> List[User] v1_users_get()

Get all users

Get all users in the current organization. Requires authentication.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.user import User
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
    api_instance = pingera.UsersApi(api_client)

    try:
        # Get all users
        api_response = api_instance.v1_users_get()
        print("The response of UsersApi->v1_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_users_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[User]**](User.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users retrieved successfully. |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_invite_post**
> V1UsersChangePasswordPost200Response v1_users_invite_post(v1_users_invite_post_request)

Invite a new user

Invite a new user to the organization with specified role. Sends invitation email with 7-day expiry. Requires admin privileges.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.v1_users_change_password_post200_response import V1UsersChangePasswordPost200Response
from pingera.models.v1_users_invite_post_request import V1UsersInvitePostRequest
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
    api_instance = pingera.UsersApi(api_client)
    v1_users_invite_post_request = pingera.V1UsersInvitePostRequest() # V1UsersInvitePostRequest | User invitation data

    try:
        # Invite a new user
        api_response = api_instance.v1_users_invite_post(v1_users_invite_post_request)
        print("The response of UsersApi->v1_users_invite_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_users_invite_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_users_invite_post_request** | [**V1UsersInvitePostRequest**](V1UsersInvitePostRequest.md)| User invitation data | 

### Return type

[**V1UsersChangePasswordPost200Response**](V1UsersChangePasswordPost200Response.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invitation sent successfully. |  -  |
**400** | Bad Request - Invalid role |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Admin access required |  -  |
**409** | Conflict - User already exists |  -  |
**422** | Validation error |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_onboarding_patch**
> User v1_users_onboarding_patch(v1_users_onboarding_patch_request)

Update user onboarding status

Update user onboarding progress or mark as completed

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.user import User
from pingera.models.v1_users_onboarding_patch_request import V1UsersOnboardingPatchRequest
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
    api_instance = pingera.UsersApi(api_client)
    v1_users_onboarding_patch_request = pingera.V1UsersOnboardingPatchRequest() # V1UsersOnboardingPatchRequest | Onboarding status update

    try:
        # Update user onboarding status
        api_response = api_instance.v1_users_onboarding_patch(v1_users_onboarding_patch_request)
        print("The response of UsersApi->v1_users_onboarding_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_users_onboarding_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_users_onboarding_patch_request** | [**V1UsersOnboardingPatchRequest**](V1UsersOnboardingPatchRequest.md)| Onboarding status update | 

### Return type

[**User**](User.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Onboarding status updated successfully. |  -  |
**400** | Validation error - Invalid onboarding step |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_profile_put**
> User v1_users_profile_put(v1_users_profile_put_request)

Update user profile information

Update user profile information. Only first_name and last_name can be updated.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.user import User
from pingera.models.v1_users_profile_put_request import V1UsersProfilePutRequest
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
    api_instance = pingera.UsersApi(api_client)
    v1_users_profile_put_request = pingera.V1UsersProfilePutRequest() # V1UsersProfilePutRequest | Profile data to update

    try:
        # Update user profile information
        api_response = api_instance.v1_users_profile_put(v1_users_profile_put_request)
        print("The response of UsersApi->v1_users_profile_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_users_profile_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_users_profile_put_request** | [**V1UsersProfilePutRequest**](V1UsersProfilePutRequest.md)| Profile data to update | 

### Return type

[**User**](User.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Validation error |  -  |
**200** | Profile updated successfully. |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_request_password_reset_post**
> V1UsersResendVerificationPost200Response v1_users_request_password_reset_post(v1_users_request_password_reset_post_request)

Request password reset email

Request password reset email with reset token. Token expires in 24 hours.

### Example


```python
import pingera
from pingera.models.v1_users_request_password_reset_post_request import V1UsersRequestPasswordResetPostRequest
from pingera.models.v1_users_resend_verification_post200_response import V1UsersResendVerificationPost200Response
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
    api_instance = pingera.UsersApi(api_client)
    v1_users_request_password_reset_post_request = pingera.V1UsersRequestPasswordResetPostRequest() # V1UsersRequestPasswordResetPostRequest | Email address to send reset link to

    try:
        # Request password reset email
        api_response = api_instance.v1_users_request_password_reset_post(v1_users_request_password_reset_post_request)
        print("The response of UsersApi->v1_users_request_password_reset_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_users_request_password_reset_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_users_request_password_reset_post_request** | [**V1UsersRequestPasswordResetPostRequest**](V1UsersRequestPasswordResetPostRequest.md)| Email address to send reset link to | 

### Return type

[**V1UsersResendVerificationPost200Response**](V1UsersResendVerificationPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reset email sent (if account exists). |  -  |
**400** | Bad Request - Missing email field |  -  |
**422** | Validation error |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_resend_verification_post**
> V1UsersResendVerificationPost200Response v1_users_resend_verification_post(v1_users_resend_verification_post_request)

Resend email verification

Resend email verification link to user. Generates new verification token with 24-hour expiry.

### Example


```python
import pingera
from pingera.models.v1_users_resend_verification_post200_response import V1UsersResendVerificationPost200Response
from pingera.models.v1_users_resend_verification_post_request import V1UsersResendVerificationPostRequest
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
    api_instance = pingera.UsersApi(api_client)
    v1_users_resend_verification_post_request = pingera.V1UsersResendVerificationPostRequest() # V1UsersResendVerificationPostRequest | Email address to resend verification to

    try:
        # Resend email verification
        api_response = api_instance.v1_users_resend_verification_post(v1_users_resend_verification_post_request)
        print("The response of UsersApi->v1_users_resend_verification_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_users_resend_verification_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_users_resend_verification_post_request** | [**V1UsersResendVerificationPostRequest**](V1UsersResendVerificationPostRequest.md)| Email address to resend verification to | 

### Return type

[**V1UsersResendVerificationPost200Response**](V1UsersResendVerificationPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Verification email sent (if account exists and not verified). |  -  |
**400** | Bad Request - Email already verified or missing fields |  -  |
**422** | Validation error |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_reset_password_post**
> V1UsersChangePasswordPost200Response v1_users_reset_password_post(v1_users_reset_password_post_request)

Reset password using token

Reset password using reset token from email or invitation token. Supports both password reset and invitation acceptance.

### Example


```python
import pingera
from pingera.models.v1_users_change_password_post200_response import V1UsersChangePasswordPost200Response
from pingera.models.v1_users_reset_password_post_request import V1UsersResetPasswordPostRequest
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
    api_instance = pingera.UsersApi(api_client)
    v1_users_reset_password_post_request = pingera.V1UsersResetPasswordPostRequest() # V1UsersResetPasswordPostRequest | Password reset data

    try:
        # Reset password using token
        api_response = api_instance.v1_users_reset_password_post(v1_users_reset_password_post_request)
        print("The response of UsersApi->v1_users_reset_password_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_users_reset_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_users_reset_password_post_request** | [**V1UsersResetPasswordPostRequest**](V1UsersResetPasswordPostRequest.md)| Password reset data | 

### Return type

[**V1UsersChangePasswordPost200Response**](V1UsersChangePasswordPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password reset successfully. |  -  |
**400** | Bad Request - Invalid or expired token |  -  |
**422** | Validation error |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_roles_get**
> List[str] v1_users_roles_get()

Get available user roles

Get list of available user roles in the system

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
    api_instance = pingera.UsersApi(api_client)

    try:
        # Get available user roles
        api_response = api_instance.v1_users_roles_get()
        print("The response of UsersApi->v1_users_roles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_users_roles_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available user roles retrieved successfully. |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_user_id_delete**
> v1_users_user_id_delete(user_id)

Delete user

Delete a user from the organization. This action is irreversible. Requires admin privileges.

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
    api_instance = pingera.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user to delete.

    try:
        # Delete user
        api_instance.v1_users_user_id_delete(user_id)
    except Exception as e:
        print("Exception when calling UsersApi->v1_users_user_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user to delete. | 

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
**204** | User deleted successfully |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Admin access required |  -  |
**404** | User not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_user_id_get**
> User v1_users_user_id_get(user_id)

Get user details

Retrieve details of a specific user within the same organization

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.user import User
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
    api_instance = pingera.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user to retrieve.

    try:
        # Get user details
        api_response = api_instance.v1_users_user_id_get(user_id)
        print("The response of UsersApi->v1_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user to retrieve. | 

### Return type

[**User**](User.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User details retrieved successfully. |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - User not in same organization |  -  |
**404** | User not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_user_id_patch**
> User v1_users_user_id_patch(user_id, user1)

Update user

Update user details including role assignment. Requires admin privileges.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.user import User
from pingera.models.user1 import User1
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
    api_instance = pingera.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user to update.
    user1 = pingera.User1() # User1 | User data to update (partial updates supported)

    try:
        # Update user
        api_response = api_instance.v1_users_user_id_patch(user_id, user1)
        print("The response of UsersApi->v1_users_user_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_users_user_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user to update. | 
 **user1** | [**User1**](User1.md)| User data to update (partial updates supported) | 

### Return type

[**User**](User.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | User updated successfully. |  -  |
**400** | Validation error - Invalid role or data |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Admin access required |  -  |
**404** | User not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_user_id_put**
> User v1_users_user_id_put(user_id, user1)

Update user

Update user details including role assignment. Requires admin privileges.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.user import User
from pingera.models.user1 import User1
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
    api_instance = pingera.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user to update.
    user1 = pingera.User1() # User1 | User data to update (partial updates supported)

    try:
        # Update user
        api_response = api_instance.v1_users_user_id_put(user_id, user1)
        print("The response of UsersApi->v1_users_user_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_users_user_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user to update. | 
 **user1** | [**User1**](User1.md)| User data to update (partial updates supported) | 

### Return type

[**User**](User.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | User updated successfully. |  -  |
**400** | Validation error - Invalid role or data |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Admin access required |  -  |
**404** | User not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_user_id_resend_invitation_post**
> V1UsersChangePasswordPost200Response v1_users_user_id_resend_invitation_post(user_id)

Resend invitation email for a user (admin only)

Resend invitation email for a user who was previously invited but has not yet activated their account. Requires admin privileges.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.v1_users_change_password_post200_response import V1UsersChangePasswordPost200Response
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
    api_instance = pingera.UsersApi(api_client)
    user_id = 'user_id_example' # str | The unique identifier of the user to resend invitation to.

    try:
        # Resend invitation email for a user (admin only)
        api_response = api_instance.v1_users_user_id_resend_invitation_post(user_id)
        print("The response of UsersApi->v1_users_user_id_resend_invitation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_users_user_id_resend_invitation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user to resend invitation to. | 

### Return type

[**V1UsersChangePasswordPost200Response**](V1UsersChangePasswordPost200Response.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invitation email sent successfully. |  -  |
**400** | Bad Request - User already active |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Admin access required |  -  |
**404** | User not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_verify_email_token_get**
> V1VerifyEmailTokenGet200Response v1_verify_email_token_get(token)

Verify email address

Verify user email address using verification token. Returns authentication tokens upon successful verification.

### Example


```python
import pingera
from pingera.models.v1_verify_email_token_get200_response import V1VerifyEmailTokenGet200Response
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
    api_instance = pingera.UsersApi(api_client)
    token = 'token_example' # str | The email verification token sent to the user.

    try:
        # Verify email address
        api_response = api_instance.v1_verify_email_token_get(token)
        print("The response of UsersApi->v1_verify_email_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_verify_email_token_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The email verification token sent to the user. | 

### Return type

[**V1VerifyEmailTokenGet200Response**](V1VerifyEmailTokenGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Email verified successfully. Returns access and refresh tokens. |  -  |
**400** | Bad Request - Invalid or expired token |  -  |
**404** | Token not found |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

