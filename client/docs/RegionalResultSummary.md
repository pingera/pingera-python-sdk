# RegionalResultSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the check in this region | [optional] 
**response_time** | **int** | Response time in milliseconds (null if check failed) | [optional] 
**result_id** | **str** | Unique identifier of the check result | [optional] 
**created_at** | **datetime** | Timestamp when this regional result was created | [optional] 
**error_message** | **str** | Error message if the check failed | [optional] 
**region** | **str** | Region where this check was executed | [optional] 

## Example

```python
from pingera.models.regional_result_summary import RegionalResultSummary

# TODO update the JSON string below
json = "{}"
# create an instance of RegionalResultSummary from a JSON string
regional_result_summary_instance = RegionalResultSummary.from_json(json)
# print the JSON string representation of the object
print(RegionalResultSummary.to_json())

# convert the object into a dict
regional_result_summary_dict = regional_result_summary_instance.to_dict()
# create an instance of RegionalResultSummary from a dict
regional_result_summary_from_dict = RegionalResultSummary.from_dict(regional_result_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


