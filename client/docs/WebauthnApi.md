# pingera.WebauthnApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_auth_passkey_authenticate_begin_post**](WebauthnApi.md#v1_auth_passkey_authenticate_begin_post) | **POST** /v1/auth/passkey/authenticate/begin | Begin passkey authentication
[**v1_auth_passkey_authenticate_complete_post**](WebauthnApi.md#v1_auth_passkey_authenticate_complete_post) | **POST** /v1/auth/passkey/authenticate/complete | Complete passkey authentication
[**v1_auth_passkey_credentials_credential_id_delete**](WebauthnApi.md#v1_auth_passkey_credentials_credential_id_delete) | **DELETE** /v1/auth/passkey/credentials/{credential_id} | Delete passkey credential
[**v1_auth_passkey_credentials_credential_id_put**](WebauthnApi.md#v1_auth_passkey_credentials_credential_id_put) | **PUT** /v1/auth/passkey/credentials/{credential_id} | Update passkey credential
[**v1_auth_passkey_credentials_get**](WebauthnApi.md#v1_auth_passkey_credentials_get) | **GET** /v1/auth/passkey/credentials | Get passkey credentials
[**v1_auth_passkey_register_begin_post**](WebauthnApi.md#v1_auth_passkey_register_begin_post) | **POST** /v1/auth/passkey/register/begin | Begin passkey registration
[**v1_auth_passkey_register_complete_post**](WebauthnApi.md#v1_auth_passkey_register_complete_post) | **POST** /v1/auth/passkey/register/complete | Complete passkey registration


# **v1_auth_passkey_authenticate_begin_post**
> AuthenticationOptionsResponse v1_auth_passkey_authenticate_begin_post(auth_begin_request=auth_begin_request)

Begin passkey authentication

Begin passkey authentication. Supports both usernameless authentication (without user_id) and user-specific authentication (with user_id). Generates WebAuthn authentication options.

### Example


```python
import pingera
from pingera.models.auth_begin_request import AuthBeginRequest
from pingera.models.authentication_options_response import AuthenticationOptionsResponse
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
    api_instance = pingera.WebauthnApi(api_client)
    auth_begin_request = pingera.AuthBeginRequest() # AuthBeginRequest |  (optional)

    try:
        # Begin passkey authentication
        api_response = api_instance.v1_auth_passkey_authenticate_begin_post(auth_begin_request=auth_begin_request)
        print("The response of WebauthnApi->v1_auth_passkey_authenticate_begin_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebauthnApi->v1_auth_passkey_authenticate_begin_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_begin_request** | [**AuthBeginRequest**](AuthBeginRequest.md)|  | [optional] 

### Return type

[**AuthenticationOptionsResponse**](AuthenticationOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | Authentication options generated successfully. |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_passkey_authenticate_complete_post**
> AuthenticationCompleteResponse v1_auth_passkey_authenticate_complete_post(authentication_complete)

Complete passkey authentication

Complete passkey authentication by verifying the credential assertion from the authenticator. Returns access token and user information upon successful authentication.

### Example


```python
import pingera
from pingera.models.authentication_complete import AuthenticationComplete
from pingera.models.authentication_complete_response import AuthenticationCompleteResponse
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
    api_instance = pingera.WebauthnApi(api_client)
    authentication_complete = pingera.AuthenticationComplete() # AuthenticationComplete | 

    try:
        # Complete passkey authentication
        api_response = api_instance.v1_auth_passkey_authenticate_complete_post(authentication_complete)
        print("The response of WebauthnApi->v1_auth_passkey_authenticate_complete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebauthnApi->v1_auth_passkey_authenticate_complete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication_complete** | [**AuthenticationComplete**](AuthenticationComplete.md)|  | 

### Return type

[**AuthenticationCompleteResponse**](AuthenticationCompleteResponse.md)

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
**400** | Bad Request - Validation error |  -  |
**401** | Unauthorized - Authentication failed |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_passkey_credentials_credential_id_delete**
> MessageResponse v1_auth_passkey_credentials_credential_id_delete(credential_id)

Delete passkey credential

Delete a specific passkey credential. Removes the specified passkey from the user's account permanently.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.message_response import MessageResponse
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
    api_instance = pingera.WebauthnApi(api_client)
    credential_id = 'cred-123-456' # str | ID of the credential to delete

    try:
        # Delete passkey credential
        api_response = api_instance.v1_auth_passkey_credentials_credential_id_delete(credential_id)
        print("The response of WebauthnApi->v1_auth_passkey_credentials_credential_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebauthnApi->v1_auth_passkey_credentials_credential_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**| ID of the credential to delete | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credential deleted successfully. |  -  |
**400** | Bad Request - Credential not found or deletion failed |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_passkey_credentials_credential_id_put**
> MessageResponse v1_auth_passkey_credentials_credential_id_put(credential_id, credential_update)

Update passkey credential

Update passkey credential information. Currently supports renaming the device/authenticator for easier identification.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.credential_update import CredentialUpdate
from pingera.models.message_response import MessageResponse
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
    api_instance = pingera.WebauthnApi(api_client)
    credential_id = 'cred-123-456' # str | ID of the credential to update
    credential_update = pingera.CredentialUpdate() # CredentialUpdate | 

    try:
        # Update passkey credential
        api_response = api_instance.v1_auth_passkey_credentials_credential_id_put(credential_id, credential_update)
        print("The response of WebauthnApi->v1_auth_passkey_credentials_credential_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebauthnApi->v1_auth_passkey_credentials_credential_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**| ID of the credential to update | 
 **credential_update** | [**CredentialUpdate**](CredentialUpdate.md)|  | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | Credential updated successfully. |  -  |
**400** | Bad Request - Credential not found or validation error |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_passkey_credentials_get**
> CredentialsListResponse v1_auth_passkey_credentials_get()

Get passkey credentials

Get list of user's registered passkey credentials. Returns information about all passkeys registered to the authenticated user.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.credentials_list_response import CredentialsListResponse
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
    api_instance = pingera.WebauthnApi(api_client)

    try:
        # Get passkey credentials
        api_response = api_instance.v1_auth_passkey_credentials_get()
        print("The response of WebauthnApi->v1_auth_passkey_credentials_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebauthnApi->v1_auth_passkey_credentials_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CredentialsListResponse**](CredentialsListResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credentials retrieved successfully. |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_passkey_register_begin_post**
> RegistrationOptionsResponse v1_auth_passkey_register_begin_post()

Begin passkey registration

Begin passkey registration for authenticated user. This endpoint generates WebAuthn registration options that the client can use to prompt the user to create a new passkey.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.registration_options_response import RegistrationOptionsResponse
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
    api_instance = pingera.WebauthnApi(api_client)

    try:
        # Begin passkey registration
        api_response = api_instance.v1_auth_passkey_register_begin_post()
        print("The response of WebauthnApi->v1_auth_passkey_register_begin_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebauthnApi->v1_auth_passkey_register_begin_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RegistrationOptionsResponse**](RegistrationOptionsResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Registration options generated successfully. |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_passkey_register_complete_post**
> RegistrationCompleteResponse v1_auth_passkey_register_complete_post(registration_complete)

Complete passkey registration

Complete passkey registration by verifying the credential response from the authenticator. This finalizes the registration process and stores the new passkey.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.registration_complete import RegistrationComplete
from pingera.models.registration_complete_response import RegistrationCompleteResponse
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
    api_instance = pingera.WebauthnApi(api_client)
    registration_complete = pingera.RegistrationComplete() # RegistrationComplete | 

    try:
        # Complete passkey registration
        api_response = api_instance.v1_auth_passkey_register_complete_post(registration_complete)
        print("The response of WebauthnApi->v1_auth_passkey_register_complete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebauthnApi->v1_auth_passkey_register_complete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_complete** | [**RegistrationComplete**](RegistrationComplete.md)|  | 

### Return type

[**RegistrationCompleteResponse**](RegistrationCompleteResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | Passkey registered successfully. |  -  |
**400** | Bad Request - Registration failed or validation error |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

