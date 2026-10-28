# pingera.ReportsApi

All URIs are relative to *https://api.pingera.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_reports_get**](ReportsApi.md#v1_reports_get) | **GET** /v1/reports | List reports
[**v1_reports_post**](ReportsApi.md#v1_reports_post) | **POST** /v1/reports | Request a new report
[**v1_reports_report_id_get**](ReportsApi.md#v1_reports_report_id_get) | **GET** /v1/reports/{report_id} | Get report status and download URL


# **v1_reports_get**
> ReportList v1_reports_get(page=page, page_size=page_size)

List reports

List all reports for the current organization, ordered by creation date (newest first).

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.report_list import ReportList
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
    api_instance = pingera.ReportsApi(api_client)
    page = 1 # int | Page number (default: 1) (optional) (default to 1)
    page_size = 20 # int | Number of reports per page (default: 20, max: 100) (optional) (default to 20)

    try:
        # List reports
        api_response = api_instance.v1_reports_get(page=page, page_size=page_size)
        print("The response of ReportsApi->v1_reports_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->v1_reports_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (default: 1) | [optional] [default to 1]
 **page_size** | **int**| Number of reports per page (default: 20, max: 100) | [optional] [default to 20]

### Return type

[**ReportList**](ReportList.md)

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

# **v1_reports_post**
> ReportResponse v1_reports_post(report_request)

Request a new report

Request generation of a PDF report for monitoring checks. If check_ids is omitted or null, the report will include all active checks in the organization. The report is generated asynchronously. Poll GET /v1/reports/<id> for status and download URL.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.report_request import ReportRequest
from pingera.models.report_response import ReportResponse
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
    api_instance = pingera.ReportsApi(api_client)
    report_request = pingera.ReportRequest() # ReportRequest | 

    try:
        # Request a new report
        api_response = api_instance.v1_reports_post(report_request)
        print("The response of ReportsApi->v1_reports_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->v1_reports_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_request** | [**ReportRequest**](ReportRequest.md)|  | 

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |
**202** | Accepted |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_reports_report_id_get**
> ReportResponse v1_reports_report_id_get(report_id)

Get report status and download URL

Get a single report by ID. When the report is completed, a presigned download URL (valid for 1 hour) will be included.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import pingera
from pingera.models.report_response import ReportResponse
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
    api_instance = pingera.ReportsApi(api_client)
    report_id = 'report_id_example' # str | The unique identifier of the report.

    try:
        # Get report status and download URL
        api_response = api_instance.v1_reports_report_id_get(report_id)
        print("The response of ReportsApi->v1_reports_report_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->v1_reports_report_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The unique identifier of the report. | 

### Return type

[**ReportResponse**](ReportResponse.md)

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

