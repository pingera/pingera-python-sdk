# pingera.StatusPagesIncidentTemplatesApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_pages_page_id_incident_templates_get**](StatusPagesIncidentTemplatesApi.md#v1_pages_page_id_incident_templates_get) | **GET** /v1/pages/{page_id}/incident-templates | List incident templates
[**v1_pages_page_id_incident_templates_post**](StatusPagesIncidentTemplatesApi.md#v1_pages_page_id_incident_templates_post) | **POST** /v1/pages/{page_id}/incident-templates | Create an incident template
[**v1_pages_page_id_incident_templates_template_id_delete**](StatusPagesIncidentTemplatesApi.md#v1_pages_page_id_incident_templates_template_id_delete) | **DELETE** /v1/pages/{page_id}/incident-templates/{template_id} | Delete an incident template
[**v1_pages_page_id_incident_templates_template_id_get**](StatusPagesIncidentTemplatesApi.md#v1_pages_page_id_incident_templates_template_id_get) | **GET** /v1/pages/{page_id}/incident-templates/{template_id} | Get an incident template
[**v1_pages_page_id_incident_templates_template_id_patch**](StatusPagesIncidentTemplatesApi.md#v1_pages_page_id_incident_templates_template_id_patch) | **PATCH** /v1/pages/{page_id}/incident-templates/{template_id} | Update an incident template


# **v1_pages_page_id_incident_templates_get**
> List[IncidentTemplate] v1_pages_page_id_incident_templates_get(page_id, type=type)

List incident templates

List incident and maintenance templates for a status page, ordered by name.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.incident_template import IncidentTemplate
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
    api_instance = pingera.StatusPagesIncidentTemplatesApi(api_client)
    page_id = 'page_id_example' # str | 
    type = 'type_example' # str | Only return templates of this type. (optional)

    try:
        # List incident templates
        api_response = api_instance.v1_pages_page_id_incident_templates_get(page_id, type=type)
        print("The response of StatusPagesIncidentTemplatesApi->v1_pages_page_id_incident_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentTemplatesApi->v1_pages_page_id_incident_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **type** | **str**| Only return templates of this type. | [optional] 

### Return type

[**List[IncidentTemplate]**](IncidentTemplate.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

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

# **v1_pages_page_id_incident_templates_post**
> IncidentTemplate v1_pages_page_id_incident_templates_post(page_id, incident_template)

Create an incident template

Create an incident or maintenance template. A page can have at most 50 templates.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.incident_template import IncidentTemplate
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
    api_instance = pingera.StatusPagesIncidentTemplatesApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    incident_template = pingera.IncidentTemplate() # IncidentTemplate | 

    try:
        # Create an incident template
        api_response = api_instance.v1_pages_page_id_incident_templates_post(page_id, incident_template)
        print("The response of StatusPagesIncidentTemplatesApi->v1_pages_page_id_incident_templates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentTemplatesApi->v1_pages_page_id_incident_templates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **incident_template** | [**IncidentTemplate**](IncidentTemplate.md)|  | 

### Return type

[**IncidentTemplate**](IncidentTemplate.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

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

# **v1_pages_page_id_incident_templates_template_id_delete**
> v1_pages_page_id_incident_templates_template_id_delete(page_id, template_id)

Delete an incident template

Delete an incident or maintenance template. Incidents created from it are not affected.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

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

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with pingera.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pingera.StatusPagesIncidentTemplatesApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    template_id = 'template_id_example' # str | The ID of the template.

    try:
        # Delete an incident template
        api_instance.v1_pages_page_id_incident_templates_template_id_delete(page_id, template_id)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentTemplatesApi->v1_pages_page_id_incident_templates_template_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **template_id** | **str**| The ID of the template. | 

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_incident_templates_template_id_get**
> IncidentTemplate v1_pages_page_id_incident_templates_template_id_get(page_id, template_id)

Get an incident template

Get a single incident or maintenance template.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.incident_template import IncidentTemplate
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
    api_instance = pingera.StatusPagesIncidentTemplatesApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    template_id = 'template_id_example' # str | The ID of the template.

    try:
        # Get an incident template
        api_response = api_instance.v1_pages_page_id_incident_templates_template_id_get(page_id, template_id)
        print("The response of StatusPagesIncidentTemplatesApi->v1_pages_page_id_incident_templates_template_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentTemplatesApi->v1_pages_page_id_incident_templates_template_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **template_id** | **str**| The ID of the template. | 

### Return type

[**IncidentTemplate**](IncidentTemplate.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_incident_templates_template_id_patch**
> IncidentTemplate v1_pages_page_id_incident_templates_template_id_patch(page_id, template_id, incident_template1)

Update an incident template

Update fields of an incident or maintenance template. Omitted fields are left unchanged.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (apiKeyHeader):

```python
import pingera
from pingera.models.incident_template import IncidentTemplate
from pingera.models.incident_template1 import IncidentTemplate1
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
    api_instance = pingera.StatusPagesIncidentTemplatesApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    template_id = 'template_id_example' # str | The ID of the template.
    incident_template1 = pingera.IncidentTemplate1() # IncidentTemplate1 | 

    try:
        # Update an incident template
        api_response = api_instance.v1_pages_page_id_incident_templates_template_id_patch(page_id, template_id, incident_template1)
        print("The response of StatusPagesIncidentTemplatesApi->v1_pages_page_id_incident_templates_template_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentTemplatesApi->v1_pages_page_id_incident_templates_template_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **template_id** | **str**| The ID of the template. | 
 **incident_template1** | [**IncidentTemplate1**](IncidentTemplate1.md)|  | 

### Return type

[**IncidentTemplate**](IncidentTemplate.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth), [apiKeyHeader](../README.md#apiKeyHeader)

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

