# pingera.StatusPagesIncidentsApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_incident_impacts_get**](StatusPagesIncidentsApi.md#v1_incident_impacts_get) | **GET** /v1/incident-impacts | 
[**v1_incident_statuses_get**](StatusPagesIncidentsApi.md#v1_incident_statuses_get) | **GET** /v1/incident-statuses | 
[**v1_maintenance_statuses_get**](StatusPagesIncidentsApi.md#v1_maintenance_statuses_get) | **GET** /v1/maintenance-statuses | 
[**v1_pages_page_id_incidents_get**](StatusPagesIncidentsApi.md#v1_pages_page_id_incidents_get) | **GET** /v1/pages/{page_id}/incidents | Get incidents for a specific status page
[**v1_pages_page_id_incidents_incident_id_delete**](StatusPagesIncidentsApi.md#v1_pages_page_id_incidents_incident_id_delete) | **DELETE** /v1/pages/{page_id}/incidents/{incident_id} | Delete an incident by ID
[**v1_pages_page_id_incidents_incident_id_get**](StatusPagesIncidentsApi.md#v1_pages_page_id_incidents_incident_id_get) | **GET** /v1/pages/{page_id}/incidents/{incident_id} | Get a specific incident by ID
[**v1_pages_page_id_incidents_incident_id_incident_updates_get**](StatusPagesIncidentsApi.md#v1_pages_page_id_incidents_incident_id_incident_updates_get) | **GET** /v1/pages/{page_id}/incidents/{incident_id}/incident_updates | Get all updates for a specific incident
[**v1_pages_page_id_incidents_incident_id_incident_updates_incident_update_id_patch**](StatusPagesIncidentsApi.md#v1_pages_page_id_incidents_incident_id_incident_updates_incident_update_id_patch) | **PATCH** /v1/pages/{page_id}/incidents/{incident_id}/incident_updates/{incident_update_id} | Update an incident update
[**v1_pages_page_id_incidents_incident_id_incident_updates_incident_update_id_put**](StatusPagesIncidentsApi.md#v1_pages_page_id_incidents_incident_id_incident_updates_incident_update_id_put) | **PUT** /v1/pages/{page_id}/incidents/{incident_id}/incident_updates/{incident_update_id} | Update an incident update
[**v1_pages_page_id_incidents_incident_id_incident_updates_post**](StatusPagesIncidentsApi.md#v1_pages_page_id_incidents_incident_id_incident_updates_post) | **POST** /v1/pages/{page_id}/incidents/{incident_id}/incident_updates | Create a new update for a specific incident
[**v1_pages_page_id_incidents_incident_id_patch**](StatusPagesIncidentsApi.md#v1_pages_page_id_incidents_incident_id_patch) | **PATCH** /v1/pages/{page_id}/incidents/{incident_id} | Update an incident by ID
[**v1_pages_page_id_incidents_incident_id_postmortem_get**](StatusPagesIncidentsApi.md#v1_pages_page_id_incidents_incident_id_postmortem_get) | **GET** /v1/pages/{page_id}/incidents/{incident_id}/postmortem | Get the postmortem for a specific incident
[**v1_pages_page_id_incidents_incident_id_postmortem_publish_put**](StatusPagesIncidentsApi.md#v1_pages_page_id_incidents_incident_id_postmortem_publish_put) | **PUT** /v1/pages/{page_id}/incidents/{incident_id}/postmortem/publish | Publish an incident postmortem
[**v1_pages_page_id_incidents_incident_id_postmortem_put**](StatusPagesIncidentsApi.md#v1_pages_page_id_incidents_incident_id_postmortem_put) | **PUT** /v1/pages/{page_id}/incidents/{incident_id}/postmortem | Create or update an incident postmortem
[**v1_pages_page_id_incidents_incident_id_put**](StatusPagesIncidentsApi.md#v1_pages_page_id_incidents_incident_id_put) | **PUT** /v1/pages/{page_id}/incidents/{incident_id} | Update an incident by ID
[**v1_pages_page_id_incidents_log_past_incident_post**](StatusPagesIncidentsApi.md#v1_pages_page_id_incidents_log_past_incident_post) | **POST** /v1/pages/{page_id}/incidents/log-past-incident | Log an incident that has already occurred in the past with multiple updates
[**v1_pages_page_id_incidents_post**](StatusPagesIncidentsApi.md#v1_pages_page_id_incidents_post) | **POST** /v1/pages/{page_id}/incidents | Create a new incident for a specific status page
[**v1_pages_page_id_incidents_unresolved_get**](StatusPagesIncidentsApi.md#v1_pages_page_id_incidents_unresolved_get) | **GET** /v1/pages/{page_id}/incidents/unresolved | Get unresolved incidents for a specific status page


# **v1_incident_impacts_get**
> v1_incident_impacts_get()

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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)

    try:
        api_instance.v1_incident_impacts_get()
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_incident_impacts_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available incident impacts |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_incident_statuses_get**
> v1_incident_statuses_get()

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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)

    try:
        api_instance.v1_incident_statuses_get()
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_incident_statuses_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available incident statuses |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_maintenance_statuses_get**
> v1_maintenance_statuses_get()

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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)

    try:
        api_instance.v1_maintenance_statuses_get()
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_maintenance_statuses_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available maintenance statuses |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_incidents_get**
> List[Incident] v1_pages_page_id_incidents_get(page_id, component_id=component_id)

Get incidents for a specific status page

Get incidents for a specific status page

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.incident import Incident
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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    component_id = 'component_id_example' # str | Filter incidents by component ID. (optional)

    try:
        # Get incidents for a specific status page
        api_response = api_instance.v1_pages_page_id_incidents_get(page_id, component_id=component_id)
        print("The response of StatusPagesIncidentsApi->v1_pages_page_id_incidents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_pages_page_id_incidents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **component_id** | **str**| Filter incidents by component ID. | [optional] 

### Return type

[**List[Incident]**](Incident.md)

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

# **v1_pages_page_id_incidents_incident_id_delete**
> v1_pages_page_id_incidents_incident_id_delete(page_id, incident_id)

Delete an incident by ID

Delete an incident by ID

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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    incident_id = 'incident_id_example' # str | The ID of the incident.

    try:
        # Delete an incident by ID
        api_instance.v1_pages_page_id_incidents_incident_id_delete(page_id, incident_id)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **incident_id** | **str**| The ID of the incident. | 

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

# **v1_pages_page_id_incidents_incident_id_get**
> Incident v1_pages_page_id_incidents_incident_id_get(page_id, incident_id)

Get a specific incident by ID

Get a specific incident by ID

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.incident import Incident
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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    incident_id = 'incident_id_example' # str | The ID of the incident.

    try:
        # Get a specific incident by ID
        api_response = api_instance.v1_pages_page_id_incidents_incident_id_get(page_id, incident_id)
        print("The response of StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **incident_id** | **str**| The ID of the incident. | 

### Return type

[**Incident**](Incident.md)

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

# **v1_pages_page_id_incidents_incident_id_incident_updates_get**
> List[IncidentUpdate] v1_pages_page_id_incidents_incident_id_incident_updates_get(page_id, incident_id)

Get all updates for a specific incident

Get all updates for a specific incident

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.incident_update import IncidentUpdate
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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    incident_id = 'incident_id_example' # str | The ID of the incident.

    try:
        # Get all updates for a specific incident
        api_response = api_instance.v1_pages_page_id_incidents_incident_id_incident_updates_get(page_id, incident_id)
        print("The response of StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_incident_updates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_incident_updates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **incident_id** | **str**| The ID of the incident. | 

### Return type

[**List[IncidentUpdate]**](IncidentUpdate.md)

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

# **v1_pages_page_id_incidents_incident_id_incident_updates_incident_update_id_patch**
> IncidentUpdate v1_pages_page_id_incidents_incident_id_incident_updates_incident_update_id_patch(page_id, incident_id, incident_update_id, incident_update_edit)

Update an incident update

Update an incident update

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.incident_update import IncidentUpdate
from pingera.models.incident_update_edit import IncidentUpdateEdit
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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    incident_id = 'incident_id_example' # str | The ID of the incident.
    incident_update_id = 'incident_update_id_example' # str | The ID of the incident update.
    incident_update_edit = pingera.IncidentUpdateEdit() # IncidentUpdateEdit | 

    try:
        # Update an incident update
        api_response = api_instance.v1_pages_page_id_incidents_incident_id_incident_updates_incident_update_id_patch(page_id, incident_id, incident_update_id, incident_update_edit)
        print("The response of StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_incident_updates_incident_update_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_incident_updates_incident_update_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **incident_id** | **str**| The ID of the incident. | 
 **incident_update_id** | **str**| The ID of the incident update. | 
 **incident_update_edit** | [**IncidentUpdateEdit**](IncidentUpdateEdit.md)|  | 

### Return type

[**IncidentUpdate**](IncidentUpdate.md)

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

# **v1_pages_page_id_incidents_incident_id_incident_updates_incident_update_id_put**
> IncidentUpdate v1_pages_page_id_incidents_incident_id_incident_updates_incident_update_id_put(page_id, incident_id, incident_update_id, incident_update_edit)

Update an incident update

Update an incident update

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.incident_update import IncidentUpdate
from pingera.models.incident_update_edit import IncidentUpdateEdit
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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    incident_id = 'incident_id_example' # str | The ID of the incident.
    incident_update_id = 'incident_update_id_example' # str | The ID of the incident update.
    incident_update_edit = pingera.IncidentUpdateEdit() # IncidentUpdateEdit | 

    try:
        # Update an incident update
        api_response = api_instance.v1_pages_page_id_incidents_incident_id_incident_updates_incident_update_id_put(page_id, incident_id, incident_update_id, incident_update_edit)
        print("The response of StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_incident_updates_incident_update_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_incident_updates_incident_update_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **incident_id** | **str**| The ID of the incident. | 
 **incident_update_id** | **str**| The ID of the incident update. | 
 **incident_update_edit** | [**IncidentUpdateEdit**](IncidentUpdateEdit.md)|  | 

### Return type

[**IncidentUpdate**](IncidentUpdate.md)

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

# **v1_pages_page_id_incidents_incident_id_incident_updates_post**
> IncidentUpdate v1_pages_page_id_incidents_incident_id_incident_updates_post(page_id, incident_id, incident_update_create)

Create a new update for a specific incident

Create a new update for a specific incident

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.incident_update import IncidentUpdate
from pingera.models.incident_update_create import IncidentUpdateCreate
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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    incident_id = 'incident_id_example' # str | The ID of the incident.
    incident_update_create = pingera.IncidentUpdateCreate() # IncidentUpdateCreate | 

    try:
        # Create a new update for a specific incident
        api_response = api_instance.v1_pages_page_id_incidents_incident_id_incident_updates_post(page_id, incident_id, incident_update_create)
        print("The response of StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_incident_updates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_incident_updates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **incident_id** | **str**| The ID of the incident. | 
 **incident_update_create** | [**IncidentUpdateCreate**](IncidentUpdateCreate.md)|  | 

### Return type

[**IncidentUpdate**](IncidentUpdate.md)

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

# **v1_pages_page_id_incidents_incident_id_patch**
> Incident v1_pages_page_id_incidents_incident_id_patch(page_id, incident_id, incident_update_schema_edit)

Update an incident by ID

Update an incident by ID

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.incident import Incident
from pingera.models.incident_update_schema_edit import IncidentUpdateSchemaEdit
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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    incident_id = 'incident_id_example' # str | The ID of the incident.
    incident_update_schema_edit = pingera.IncidentUpdateSchemaEdit() # IncidentUpdateSchemaEdit | 

    try:
        # Update an incident by ID
        api_response = api_instance.v1_pages_page_id_incidents_incident_id_patch(page_id, incident_id, incident_update_schema_edit)
        print("The response of StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **incident_id** | **str**| The ID of the incident. | 
 **incident_update_schema_edit** | [**IncidentUpdateSchemaEdit**](IncidentUpdateSchemaEdit.md)|  | 

### Return type

[**Incident**](Incident.md)

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

# **v1_pages_page_id_incidents_incident_id_postmortem_get**
> IncidentPostmortem v1_pages_page_id_incidents_incident_id_postmortem_get(page_id, incident_id)

Get the postmortem for a specific incident

Get the postmortem for a specific incident

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.incident_postmortem import IncidentPostmortem
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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    incident_id = 'incident_id_example' # str | The ID of the incident.

    try:
        # Get the postmortem for a specific incident
        api_response = api_instance.v1_pages_page_id_incidents_incident_id_postmortem_get(page_id, incident_id)
        print("The response of StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_postmortem_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_postmortem_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **incident_id** | **str**| The ID of the incident. | 

### Return type

[**IncidentPostmortem**](IncidentPostmortem.md)

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

# **v1_pages_page_id_incidents_incident_id_postmortem_publish_put**
> IncidentPostmortem v1_pages_page_id_incidents_incident_id_postmortem_publish_put(page_id, incident_id)

Publish an incident postmortem

Publish an incident postmortem

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.incident_postmortem import IncidentPostmortem
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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    incident_id = 'incident_id_example' # str | The ID of the incident.

    try:
        # Publish an incident postmortem
        api_response = api_instance.v1_pages_page_id_incidents_incident_id_postmortem_publish_put(page_id, incident_id)
        print("The response of StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_postmortem_publish_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_postmortem_publish_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **incident_id** | **str**| The ID of the incident. | 

### Return type

[**IncidentPostmortem**](IncidentPostmortem.md)

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

# **v1_pages_page_id_incidents_incident_id_postmortem_put**
> IncidentPostmortem v1_pages_page_id_incidents_incident_id_postmortem_put(page_id, incident_id, incident_postmortem)

Create or update an incident postmortem

Create or update an incident postmortem

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.incident_postmortem import IncidentPostmortem
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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    incident_id = 'incident_id_example' # str | The ID of the incident.
    incident_postmortem = pingera.IncidentPostmortem() # IncidentPostmortem | 

    try:
        # Create or update an incident postmortem
        api_response = api_instance.v1_pages_page_id_incidents_incident_id_postmortem_put(page_id, incident_id, incident_postmortem)
        print("The response of StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_postmortem_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_postmortem_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **incident_id** | **str**| The ID of the incident. | 
 **incident_postmortem** | [**IncidentPostmortem**](IncidentPostmortem.md)|  | 

### Return type

[**IncidentPostmortem**](IncidentPostmortem.md)

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

# **v1_pages_page_id_incidents_incident_id_put**
> Incident v1_pages_page_id_incidents_incident_id_put(page_id, incident_id, incident_update_schema_edit)

Update an incident by ID

Update an incident by ID

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.incident import Incident
from pingera.models.incident_update_schema_edit import IncidentUpdateSchemaEdit
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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    incident_id = 'incident_id_example' # str | The ID of the incident.
    incident_update_schema_edit = pingera.IncidentUpdateSchemaEdit() # IncidentUpdateSchemaEdit | 

    try:
        # Update an incident by ID
        api_response = api_instance.v1_pages_page_id_incidents_incident_id_put(page_id, incident_id, incident_update_schema_edit)
        print("The response of StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_pages_page_id_incidents_incident_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **incident_id** | **str**| The ID of the incident. | 
 **incident_update_schema_edit** | [**IncidentUpdateSchemaEdit**](IncidentUpdateSchemaEdit.md)|  | 

### Return type

[**Incident**](Incident.md)

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

# **v1_pages_page_id_incidents_log_past_incident_post**
> Incident v1_pages_page_id_incidents_log_past_incident_post(page_id, log_past_incident)

Log an incident that has already occurred in the past with multiple updates

Log an incident that has already occurred in the past with multiple updates

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.incident import Incident
from pingera.models.log_past_incident import LogPastIncident
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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    log_past_incident = pingera.LogPastIncident() # LogPastIncident | 

    try:
        # Log an incident that has already occurred in the past with multiple updates
        api_response = api_instance.v1_pages_page_id_incidents_log_past_incident_post(page_id, log_past_incident)
        print("The response of StatusPagesIncidentsApi->v1_pages_page_id_incidents_log_past_incident_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_pages_page_id_incidents_log_past_incident_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **log_past_incident** | [**LogPastIncident**](LogPastIncident.md)|  | 

### Return type

[**Incident**](Incident.md)

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

# **v1_pages_page_id_incidents_post**
> Incident v1_pages_page_id_incidents_post(page_id, incident_create)

Create a new incident for a specific status page

Create a new incident for a specific status page

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.incident import Incident
from pingera.models.incident_create import IncidentCreate
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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.
    incident_create = pingera.IncidentCreate() # IncidentCreate | 

    try:
        # Create a new incident for a specific status page
        api_response = api_instance.v1_pages_page_id_incidents_post(page_id, incident_create)
        print("The response of StatusPagesIncidentsApi->v1_pages_page_id_incidents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_pages_page_id_incidents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 
 **incident_create** | [**IncidentCreate**](IncidentCreate.md)|  | 

### Return type

[**Incident**](Incident.md)

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

# **v1_pages_page_id_incidents_unresolved_get**
> List[Incident] v1_pages_page_id_incidents_unresolved_get(page_id)

Get unresolved incidents for a specific status page

Get unresolved incidents for a specific status page

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.incident import Incident
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
    api_instance = pingera.StatusPagesIncidentsApi(api_client)
    page_id = 'page_id_example' # str | The ID of the status page.

    try:
        # Get unresolved incidents for a specific status page
        api_response = api_instance.v1_pages_page_id_incidents_unresolved_get(page_id)
        print("The response of StatusPagesIncidentsApi->v1_pages_page_id_incidents_unresolved_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusPagesIncidentsApi->v1_pages_page_id_incidents_unresolved_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The ID of the status page. | 

### Return type

[**List[Incident]**](Incident.md)

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

