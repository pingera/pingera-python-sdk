# pingera.AuditApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_audit_get**](AuditApi.md#v1_audit_get) | **GET** /v1/audit | List audit trail entries


# **v1_audit_get**
> AuditList v1_audit_get(action=action, entity_type=entity_type, user_id=user_id, start_date=start_date, end_date=end_date, page=page, per_page=per_page)

List audit trail entries

Return the organization audit trail (logins, invitations, and create/update/delete of checks, status pages and components), newest first. Requires an admin or billing role and a plan with audit logs enabled. Supports filtering by action, entity type, actor and date range.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.audit_list import AuditList
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
    api_instance = pingera.AuditApi(api_client)
    action = 'action_example' # str | Filter by action (create, update, delete, login, invite, invite_accepted). (optional)
    entity_type = 'entity_type_example' # str | Filter by entity type (e.g. check, status_page, component, user). (optional)
    user_id = 'user_id_example' # str | Filter by actor user id. (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Only include entries at or after this ISO datetime. (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Only include entries at or before this ISO datetime. (optional)
    page = 56 # int | Page number for pagination (default: 1). (optional)
    per_page = 56 # int | Items per page (default: 50, max: 100). (optional)

    try:
        # List audit trail entries
        api_response = api_instance.v1_audit_get(action=action, entity_type=entity_type, user_id=user_id, start_date=start_date, end_date=end_date, page=page, per_page=per_page)
        print("The response of AuditApi->v1_audit_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditApi->v1_audit_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Filter by action (create, update, delete, login, invite, invite_accepted). | [optional] 
 **entity_type** | **str**| Filter by entity type (e.g. check, status_page, component, user). | [optional] 
 **user_id** | **str**| Filter by actor user id. | [optional] 
 **start_date** | **datetime**| Only include entries at or after this ISO datetime. | [optional] 
 **end_date** | **datetime**| Only include entries at or before this ISO datetime. | [optional] 
 **page** | **int**| Page number for pagination (default: 1). | [optional] 
 **per_page** | **int**| Items per page (default: 50, max: 100). | [optional] 

### Return type

[**AuditList**](AuditList.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audit trail entries |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

