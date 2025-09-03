# MonitorCheckResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The timestamp when the check result was created in ISO format. | [optional] [readonly] 
**response_time** | **int** | The response time of the check in milliseconds. | [optional] 
**status** | **str** | The result status of the check execution. | [optional] 
**check_server_id** | **str** | The identifier of the server that executed this check. | [optional] 
**error_message** | **str** | Error message if the check failed. | [optional] 
**check_server** | [**CheckServer**](CheckServer.md) | Details about the server that executed this check. | [optional] [readonly] 
**check_metadata** | **Dict[str, object]** | Additional metadata collected during the check execution. | [optional] 
**check_id** | **str** | The identifier of the monitor check this result belongs to. | 
**id** | **str** | The unique identifier for the check result. | [optional] [readonly] 

## Example

```python
from pingera.models.monitor_check_result import MonitorCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorCheckResult from a JSON string
monitor_check_result_instance = MonitorCheckResult.from_json(json)
# print the JSON string representation of the object
print(MonitorCheckResult.to_json())

# convert the object into a dict
monitor_check_result_dict = monitor_check_result_instance.to_dict()
# create an instance of MonitorCheckResult from a dict
monitor_check_result_from_dict = MonitorCheckResult.from_dict(monitor_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


