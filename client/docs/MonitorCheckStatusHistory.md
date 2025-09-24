# MonitorCheckStatusHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ended_at** | **datetime** | When this status period ended in ISO format. Null if still active. | [optional] 
**started_at** | **datetime** | When this status period started in ISO format. | [optional] 
**status** | **str** | The status during this period. | [optional] 

## Example

```python
from pingera.models.monitor_check_status_history import MonitorCheckStatusHistory

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorCheckStatusHistory from a JSON string
monitor_check_status_history_instance = MonitorCheckStatusHistory.from_json(json)
# print the JSON string representation of the object
print(MonitorCheckStatusHistory.to_json())

# convert the object into a dict
monitor_check_status_history_dict = monitor_check_status_history_instance.to_dict()
# create an instance of MonitorCheckStatusHistory from a dict
monitor_check_status_history_from_dict = MonitorCheckStatusHistory.from_dict(monitor_check_status_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


