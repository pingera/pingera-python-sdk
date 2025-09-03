# UnifiedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**result_type** | **str** | Type of the result. | [optional] [readonly] 
**check_metadata** | **Dict[str, object]** | Additional metadata from the check. | [optional] 
**check_name** | **str** | The name of the check. | [optional] [readonly] 
**response_time** | **int** | The response time in milliseconds. | [optional] 
**check_server_id** | **str** |  | [optional] 
**check_id** | **str** | The identifier of the monitor check, if applicable. | [optional] 
**region** | **str** | The region where the check was executed from. | [optional] [readonly] 
**check_type** | **str** | The type of check performed (e.g., web, api, ssl). | [optional] [readonly] 
**check_server** | [**CheckServer**](CheckServer.md) |  | [optional] [readonly] 
**id** | **str** | The unique identifier for the result or job. | [optional] [readonly] 
**status** | **str** | The result status of the check execution. | [optional] 
**error_message** | **str** | Error message if the check failed. | [optional] 

## Example

```python
from pingera.models.unified_result import UnifiedResult

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedResult from a JSON string
unified_result_instance = UnifiedResult.from_json(json)
# print the JSON string representation of the object
print(UnifiedResult.to_json())

# convert the object into a dict
unified_result_dict = unified_result_instance.to_dict()
# create an instance of UnifiedResult from a dict
unified_result_from_dict = UnifiedResult.from_dict(unified_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


