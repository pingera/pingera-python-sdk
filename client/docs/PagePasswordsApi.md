# pingera.PagePasswordsApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_pages_page_id_password_hints_get**](PagePasswordsApi.md#v1_pages_page_id_password_hints_get) | **GET** /v1/pages/{page_id}/password-hints | Get password hints for page
[**v1_pages_page_id_passwords_get**](PagePasswordsApi.md#v1_pages_page_id_passwords_get) | **GET** /v1/pages/{page_id}/passwords | List page passwords
[**v1_pages_page_id_passwords_password_id_delete**](PagePasswordsApi.md#v1_pages_page_id_passwords_password_id_delete) | **DELETE** /v1/pages/{page_id}/passwords/{password_id} | Delete page password
[**v1_pages_page_id_passwords_password_id_put**](PagePasswordsApi.md#v1_pages_page_id_passwords_password_id_put) | **PUT** /v1/pages/{page_id}/passwords/{password_id} | Update page password
[**v1_pages_page_id_passwords_post**](PagePasswordsApi.md#v1_pages_page_id_passwords_post) | **POST** /v1/pages/{page_id}/passwords | Create page password
[**v1_pages_page_id_verify_password_post**](PagePasswordsApi.md#v1_pages_page_id_verify_password_post) | **POST** /v1/pages/{page_id}/verify-password | Verify password for page access


# **v1_pages_page_id_password_hints_get**
> PasswordHintsResponse v1_pages_page_id_password_hints_get(page_id)

Get password hints for page

Get available password hints for a password-protected page

### Example


```python
import pingera
from pingera.models.password_hints_response import PasswordHintsResponse
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
    api_instance = pingera.PagePasswordsApi(api_client)
    page_id = 'page_id_example' # str | 

    try:
        # Get password hints for page
        api_response = api_instance.v1_pages_page_id_password_hints_get(page_id)
        print("The response of PagePasswordsApi->v1_pages_page_id_password_hints_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagePasswordsApi->v1_pages_page_id_password_hints_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 

### Return type

[**PasswordHintsResponse**](PasswordHintsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password hints retrieved successfully |  -  |
**404** | Page not found or not password-protected |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_passwords_get**
> List[PagePassword] v1_pages_page_id_passwords_get(page_id)

List page passwords

Get all passwords for a page (admin only)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.page_password import PagePassword
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
    api_instance = pingera.PagePasswordsApi(api_client)
    page_id = 'page_id_example' # str | 

    try:
        # List page passwords
        api_response = api_instance.v1_pages_page_id_passwords_get(page_id)
        print("The response of PagePasswordsApi->v1_pages_page_id_passwords_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagePasswordsApi->v1_pages_page_id_passwords_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 

### Return type

[**List[PagePassword]**](PagePassword.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Passwords retrieved successfully |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied |  -  |
**404** | Page not found |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_passwords_password_id_delete**
> v1_pages_page_id_passwords_password_id_delete(page_id, password_id)

Delete page password

Delete a password for a page

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
    api_instance = pingera.PagePasswordsApi(api_client)
    page_id = 'page_id_example' # str | 
    password_id = 'password_id_example' # str | 

    try:
        # Delete page password
        api_instance.v1_pages_page_id_passwords_password_id_delete(page_id, password_id)
    except Exception as e:
        print("Exception when calling PagePasswordsApi->v1_pages_page_id_passwords_password_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **password_id** | **str**|  | 

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
**204** | Password deleted successfully |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied |  -  |
**404** | Password not found |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_passwords_password_id_put**
> PagePassword v1_pages_page_id_passwords_password_id_put(page_id, password_id, page_password_update)

Update page password

Update an existing password for a page

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.page_password import PagePassword
from pingera.models.page_password_update import PagePasswordUpdate
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
    api_instance = pingera.PagePasswordsApi(api_client)
    page_id = 'page_id_example' # str | 
    password_id = 'password_id_example' # str | 
    page_password_update = pingera.PagePasswordUpdate() # PagePasswordUpdate | 

    try:
        # Update page password
        api_response = api_instance.v1_pages_page_id_passwords_password_id_put(page_id, password_id, page_password_update)
        print("The response of PagePasswordsApi->v1_pages_page_id_passwords_password_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagePasswordsApi->v1_pages_page_id_passwords_password_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **password_id** | **str**|  | 
 **page_password_update** | [**PagePasswordUpdate**](PagePasswordUpdate.md)|  | 

### Return type

[**PagePassword**](PagePassword.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |
**200** | Password updated successfully |  -  |
**400** | Bad Request - Invalid data |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied |  -  |
**404** | Password not found |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_passwords_post**
> PagePassword v1_pages_page_id_passwords_post(page_id, page_password_create)

Create page password

Create a new password for a page

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.page_password import PagePassword
from pingera.models.page_password_create import PagePasswordCreate
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
    api_instance = pingera.PagePasswordsApi(api_client)
    page_id = 'page_id_example' # str | 
    page_password_create = pingera.PagePasswordCreate() # PagePasswordCreate | 

    try:
        # Create page password
        api_response = api_instance.v1_pages_page_id_passwords_post(page_id, page_password_create)
        print("The response of PagePasswordsApi->v1_pages_page_id_passwords_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagePasswordsApi->v1_pages_page_id_passwords_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **page_password_create** | [**PagePasswordCreate**](PagePasswordCreate.md)|  | 

### Return type

[**PagePassword**](PagePassword.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |
**201** | Password created successfully |  -  |
**400** | Bad Request - Invalid data |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied |  -  |
**404** | Page not found |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_verify_password_post**
> PasswordVerificationResponse v1_pages_page_id_verify_password_post(page_id, password_verification)

Verify password for page access

Verify a password for accessing a password-protected page. Returns a temporary access token on success.

### Example


```python
import pingera
from pingera.models.password_verification import PasswordVerification
from pingera.models.password_verification_response import PasswordVerificationResponse
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
    api_instance = pingera.PagePasswordsApi(api_client)
    page_id = 'page_id_example' # str | 
    password_verification = pingera.PasswordVerification() # PasswordVerification | 

    try:
        # Verify password for page access
        api_response = api_instance.v1_pages_page_id_verify_password_post(page_id, password_verification)
        print("The response of PagePasswordsApi->v1_pages_page_id_verify_password_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagePasswordsApi->v1_pages_page_id_verify_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **password_verification** | [**PasswordVerification**](PasswordVerification.md)|  | 

### Return type

[**PasswordVerificationResponse**](PasswordVerificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |
**200** | Password verified successfully, access token returned |  -  |
**400** | Bad Request - Missing or invalid password |  -  |
**401** | Unauthorized - Incorrect password |  -  |
**404** | Page not found or not password-protected |  -  |
**429** | Too many attempts - Rate limit exceeded |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

