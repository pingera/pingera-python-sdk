# ReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the report. | [optional] [readonly] 
**status** | **str** | Report generation status: pending, generating, completed, or failed. | [optional] [readonly] 
**check_ids** | **List[str]** | List of check IDs included in the report. Null means all active checks. | [optional] [readonly] 
**start_date** | **datetime** | Start date of the report period. | [optional] [readonly] 
**end_date** | **datetime** | End date of the report period. | [optional] [readonly] 
**download_url** | **str** | Presigned URL to download the PDF report. Only available when status is &#39;completed&#39;. Expires after 1 hour. | [optional] [readonly] 
**created_at** | **datetime** | Timestamp when the report was requested. | [optional] [readonly] 
**completed_at** | **datetime** | Timestamp when the report generation completed. | [optional] [readonly] 
**error_message** | **str** | Error message if report generation failed. | [optional] [readonly] 

## Example

```python
from pingera.models.report_response import ReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportResponse from a JSON string
report_response_instance = ReportResponse.from_json(json)
# print the JSON string representation of the object
print(ReportResponse.to_json())

# convert the object into a dict
report_response_dict = report_response_instance.to_dict()
# create an instance of ReportResponse from a dict
report_response_from_dict = ReportResponse.from_dict(report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


