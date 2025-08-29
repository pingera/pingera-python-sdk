# pingera.StatusPagesApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_pages_by_domain_domain_get**](StatusPagesApi.md#v1_pages_by_domain_domain_get) | **GET** /v1/pages/by-domain/{domain} | Get page by domain
[**v1_pages_get**](StatusPagesApi.md#v1_pages_get) | **GET** /v1/pages | Get all status pages
[**v1_pages_get_templates_get**](StatusPagesApi.md#v1_pages_get_templates_get) | **GET** /v1/pages/get-templates | Get available templates
[**v1_pages_page_id_delete**](StatusPagesApi.md#v1_pages_page_id_delete) | **DELETE** /v1/pages/{page_id} | Delete status page
[**v1_pages_page_id_get**](StatusPagesApi.md#v1_pages_page_id_get) | **GET** /v1/pages/{page_id} | Get status page by ID
[**v1_pages_page_id_patch**](StatusPagesApi.md#v1_pages_page_id_patch) | **PATCH** /v1/pages/{page_id} | Update status page
[**v1_pages_page_id_put**](StatusPagesApi.md#v1_pages_page_id_put) | **PUT** /v1/pages/{page_id} | Update status page
[**v1_pages_post**](StatusPagesApi.md#v1_pages_post) | **POST** /v1/pages | Create a new status page


# **v1_pages_by_domain_domain_get**
> Page v1_pages_by_domain_domain_get(domain)

Get page by domain

Get a page by its domain or subdomain

### Example


```python
import pingera
from pingera.models.page import Page
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
    api_instance = pingera.StatusPagesApi(api_client)
    domain = 'domain_example' # str | 

    try:
        # Get page by domain
        api_response = api_instance.v1_pages_by_domain_domain_get(domain)
        print("The response of StatusPagesApi->v1_pages_by_domain_domain_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesApi->v1_pages_by_domain_domain_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | 

### Return type

[**Page**](Page.md)

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

# **v1_pages_get**
> PageList v1_pages_get(page=page, page_size=page_size)

Get all status pages

Retrieve all status pages for the authenticated organization with pagination support. Returns a paginated list of all status pages including their configuration, branding settings, and metadata. This endpoint provides complete information about each page including custom domains, CSS styling, and notification preferences.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.page_list import PageList
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
    api_instance = pingera.StatusPagesApi(api_client)
    page = 1 # int | Page number (starting from 1) (optional) (default to 1)
    page_size = 20 # int | Number of items per page (1-100) (optional) (default to 20)

    try:
        # Get all status pages
        api_response = api_instance.v1_pages_get(page=page, page_size=page_size)
        print("The response of StatusPagesApi->v1_pages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesApi->v1_pages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (starting from 1) | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (1-100) | [optional] [default to 20]

### Return type

[**PageList**](PageList.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | List of status pages retrieved successfully with pagination. |  -  |
**400** | Bad Request - Invalid pagination parameters |  -  |
**401** | Unauthorized - Authentication required |  -  |
**500** | Internal Server Error - Database error occurred |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_get_templates_get**
> Error v1_pages_get_templates_get()

Get available templates

Get available templates with their preview URLs

### Example


```python
import pingera
from pingera.models.error import Error
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
    api_instance = pingera.StatusPagesApi(api_client)

    try:
        # Get available templates
        api_response = api_instance.v1_pages_get_templates_get()
        print("The response of StatusPagesApi->v1_pages_get_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesApi->v1_pages_get_templates_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Error**](Error.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_delete**
> v1_pages_page_id_delete(page_id)

Delete status page

Permanently delete a status page and all its associated data including components, incidents, subscribers, and historical data. This action cannot be undone. Only users from the same organization as the page can perform this operation.

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
    api_instance = pingera.StatusPagesApi(api_client)
    page_id = 'page_id_example' # str | 

    try:
        # Delete status page
        api_instance.v1_pages_page_id_delete(page_id)
    except Exception as e:
        print("Exception when calling StatusPagesApi->v1_pages_page_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 

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
**204** | Status page deleted successfully. No content returned. |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied to this page |  -  |
**404** | Status page not found |  -  |
**500** | Internal Server Error - Database error occurred |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_get**
> Page v1_pages_page_id_get(page_id)

Get status page by ID

Retrieve a specific status page by its unique identifier. Returns complete page configuration including branding, domain settings, CSS customization, and notification preferences.

    **Security Details:**
    * **Public Pages:** If a page is configured for public access (viewers_must_be_team_members=false), it can be accessed **without any authentication token**. In this case, providing a bearer token or API key is **optional** and is primarily used to identify the requesting user for analytics or to apply user-specific preferences (if applicable).
    * **Private Pages:** For pages that are not public, authentication is **mandatory**. You must provide either a `bearerAuth` token (JWT) or an `Authorization: <API_TOKEN>` header. Access will be granted only if the authenticated user belongs to the same organization as the requested page.
    

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.page import Page
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
    api_instance = pingera.StatusPagesApi(api_client)
    page_id = 'page_id_example' # str | 

    try:
        # Get status page by ID
        api_response = api_instance.v1_pages_page_id_get(page_id)
        print("The response of StatusPagesApi->v1_pages_page_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesApi->v1_pages_page_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 

### Return type

[**Page**](Page.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status page retrieved successfully. |  -  |
**401** | Unauthorized - Authentication required for private pages |  -  |
**403** | Forbidden - Access denied to this page |  -  |
**404** | Status page not found |  -  |
**500** | Internal Server Error - Database error occurred |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_patch**
> Page v1_pages_page_id_patch(page_id, page1)

Update status page

Update a status page with new configuration settings. This endpoint supports both partial updates (PATCH) and full updates (PUT). You can update page branding, domain settings, CSS styling, notification preferences, and upload logo files. File uploads for logos should be sent as multipart/form-data, while other updates should be sent as JSON.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.page import Page
from pingera.models.page1 import Page1
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
    api_instance = pingera.StatusPagesApi(api_client)
    page_id = 'page_id_example' # str | 
    page1 = pingera.Page1() # Page1 | 

    try:
        # Update status page
        api_response = api_instance.v1_pages_page_id_patch(page_id, page1)
        print("The response of StatusPagesApi->v1_pages_page_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesApi->v1_pages_page_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **page1** | [**Page1**](Page1.md)|  | 

### Return type

[**Page**](Page.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | Status page updated successfully. |  -  |
**400** | Bad Request - Validation error, invalid domain, subdomain, timezone, or file format |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied or plan limit exceeded |  -  |
**404** | Status page not found |  -  |
**500** | Internal Server Error - Database error occurred |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_put**
> Page v1_pages_page_id_put(page_id, page1)

Update status page

Update a status page with new configuration settings. This endpoint supports both partial updates (PATCH) and full updates (PUT). You can update page branding, domain settings, CSS styling, notification preferences, and upload logo files. File uploads for logos should be sent as multipart/form-data, while other updates should be sent as JSON.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.page import Page
from pingera.models.page1 import Page1
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
    api_instance = pingera.StatusPagesApi(api_client)
    page_id = 'page_id_example' # str | 
    page1 = pingera.Page1() # Page1 | 

    try:
        # Update status page
        api_response = api_instance.v1_pages_page_id_put(page_id, page1)
        print("The response of StatusPagesApi->v1_pages_page_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesApi->v1_pages_page_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **page1** | [**Page1**](Page1.md)|  | 

### Return type

[**Page**](Page.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | Status page updated successfully. |  -  |
**400** | Bad Request - Validation error, invalid domain, subdomain, timezone, or file format |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Access denied or plan limit exceeded |  -  |
**404** | Status page not found |  -  |
**500** | Internal Server Error - Database error occurred |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_post**
> Page v1_pages_post(page)

Create a new status page

Create a new status page for the organization. This endpoint allows you to create a status page with custom branding, domain configuration, and notification settings. The page can be configured as public or private, and supports custom CSS styling and subscriber management.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.page import Page
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
    api_instance = pingera.StatusPagesApi(api_client)
    page = pingera.Page() # Page | 

    try:
        # Create a new status page
        api_response = api_instance.v1_pages_post(page)
        print("The response of StatusPagesApi->v1_pages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesApi->v1_pages_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**Page**](Page.md)|  | 

### Return type

[**Page**](Page.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | Status page created successfully. |  -  |
**400** | Bad Request - Validation error, invalid subdomain, or invalid domain |  -  |
**401** | Unauthorized - Authentication required |  -  |
**403** | Forbidden - Plan limit exceeded for status pages, domains, CSS, or templates |  -  |
**500** | Internal Server Error - Database error occurred |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

