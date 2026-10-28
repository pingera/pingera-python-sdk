# ReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Start date for the report period (ISO 8601 format). | 
**end_date** | **datetime** | End date for the report period (ISO 8601 format). | 
**check_ids** | **List[str]** | List of check IDs to include in the report. If omitted or null, all active checks in the organization will be included. | [optional] 

## Example

```python
from pingera.models.report_request import ReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportRequest from a JSON string
report_request_instance = ReportRequest.from_json(json)
# print the JSON string representation of the object
print(ReportRequest.to_json())

# convert the object into a dict
report_request_dict = report_request_instance.to_dict()
# create an instance of ReportRequest from a dict
report_request_from_dict = ReportRequest.from_dict(report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


