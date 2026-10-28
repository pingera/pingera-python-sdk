# pingera.OrganizationsApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_organizations_get**](OrganizationsApi.md#v1_organizations_get) | **GET** /v1/organizations | Get user organization
[**v1_organizations_org_id_get**](OrganizationsApi.md#v1_organizations_org_id_get) | **GET** /v1/organizations/{org_id} | Get organization
[**v1_organizations_org_id_patch**](OrganizationsApi.md#v1_organizations_org_id_patch) | **PATCH** /v1/organizations/{org_id} | Update organization
[**v1_organizations_org_id_put**](OrganizationsApi.md#v1_organizations_org_id_put) | **PUT** /v1/organizations/{org_id} | Update organization
[**v1_organizations_org_id_subscriptions_get**](OrganizationsApi.md#v1_organizations_org_id_subscriptions_get) | **GET** /v1/organizations/{org_id}/subscriptions | Get subscription history
[**v1_plans_get**](OrganizationsApi.md#v1_plans_get) | **GET** /v1/plans | Get available plans


# **v1_organizations_get**
> List[Organization] v1_organizations_get()

Get user organization

Get user organization

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.organization import Organization
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
    api_instance = pingera.OrganizationsApi(api_client)

    try:
        # Get user organization
        api_response = api_instance.v1_organizations_get()
        print("The response of OrganizationsApi->v1_organizations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organizations_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Organization]**](Organization.md)

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

# **v1_organizations_org_id_get**
> Organization v1_organizations_org_id_get(org_id)

Get organization

Get the current user organization. Requires an admin or billing role.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.organization import Organization
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
    api_instance = pingera.OrganizationsApi(api_client)
    org_id = 'org_id_example' # str | 

    try:
        # Get organization
        api_response = api_instance.v1_organizations_org_id_get(org_id)
        print("The response of OrganizationsApi->v1_organizations_org_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organizations_org_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 

### Return type

[**Organization**](Organization.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_organizations_org_id_patch**
> Organization v1_organizations_org_id_patch(org_id, organization_update)

Update organization

Update the current user organization. Billing users may only change auto_renew and invoice fields; other fields require the admin role.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.organization import Organization
from pingera.models.organization_update import OrganizationUpdate
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
    api_instance = pingera.OrganizationsApi(api_client)
    org_id = 'org_id_example' # str | 
    organization_update = pingera.OrganizationUpdate() # OrganizationUpdate | 

    try:
        # Update organization
        api_response = api_instance.v1_organizations_org_id_patch(org_id, organization_update)
        print("The response of OrganizationsApi->v1_organizations_org_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organizations_org_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **organization_update** | [**OrganizationUpdate**](OrganizationUpdate.md)|  | 

### Return type

[**Organization**](Organization.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated organization |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_organizations_org_id_put**
> Organization v1_organizations_org_id_put(org_id, organization_update)

Update organization

Update the current user organization. Billing users may only change auto_renew and invoice fields; other fields require the admin role.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.organization import Organization
from pingera.models.organization_update import OrganizationUpdate
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
    api_instance = pingera.OrganizationsApi(api_client)
    org_id = 'org_id_example' # str | 
    organization_update = pingera.OrganizationUpdate() # OrganizationUpdate | 

    try:
        # Update organization
        api_response = api_instance.v1_organizations_org_id_put(org_id, organization_update)
        print("The response of OrganizationsApi->v1_organizations_org_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organizations_org_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **organization_update** | [**OrganizationUpdate**](OrganizationUpdate.md)|  | 

### Return type

[**Organization**](Organization.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated organization |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_organizations_org_id_subscriptions_get**
> List[PlanSubscription] v1_organizations_org_id_subscriptions_get(org_id)

Get subscription history

Get organization subscription history

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.plan_subscription import PlanSubscription
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
    api_instance = pingera.OrganizationsApi(api_client)
    org_id = 'org_id_example' # str | 

    try:
        # Get subscription history
        api_response = api_instance.v1_organizations_org_id_subscriptions_get(org_id)
        print("The response of OrganizationsApi->v1_organizations_org_id_subscriptions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organizations_org_id_subscriptions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 

### Return type

[**List[PlanSubscription]**](PlanSubscription.md)

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

# **v1_plans_get**
> List[Plan] v1_plans_get()

Get available plans

Get list of available public plans

### Example


```python
import pingera
from pingera.models.plan import Plan
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
    api_instance = pingera.OrganizationsApi(api_client)

    try:
        # Get available plans
        api_response = api_instance.v1_plans_get()
        print("The response of OrganizationsApi->v1_plans_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_plans_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Plan]**](Plan.md)

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

