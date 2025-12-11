# UnifiedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_group_id** | **str** | ID of the execution group if this result is part of a multi-region execution. Null for single-region checks. | [optional] [readonly] 
**execution_id** | **str** | Unique identifier for this specific check execution. Null for legacy results. | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**check_name** | **str** | The name of the check. | [optional] [readonly] 
**id** | **str** | The unique identifier for the result or job. | [optional] [readonly] 
**response_time** | **int** | The response time in milliseconds. | [optional] 
**triggered_alerts** | **List[Dict[str, object]]** | Alerts that were triggered by this check result. | [optional] [readonly] 
**error_message** | **str** | Error message if the check failed. | [optional] 
**check_type** | **str** | The type of check performed (e.g., web, api, ssl, icmp, dns). | [optional] [readonly] 
**execution_group** | **Dict[str, object]** | Execution group details if this result is part of a multi-region execution. | [optional] [readonly] 
**check_server** | [**CheckServer**](CheckServer.md) |  | [optional] [readonly] 
**check_id** | **str** | The identifier of the monitor check, if applicable. | [optional] 
**check_metadata** | **Dict[str, object]** | Additional metadata from the check. | [optional] 
**region** | **str** | The region where the check was executed from. | [optional] [readonly] 
**check_server_id** | **str** |  | [optional] 
**result_type** | **str** | Type of the result. | [optional] [readonly] 
**status** | **str** | The result status of the check execution. | [optional] 

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


