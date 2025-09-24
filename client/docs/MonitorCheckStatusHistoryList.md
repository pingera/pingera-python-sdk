# MonitorCheckStatusHistoryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | **Dict[str, object]** | Pagination information for the status history. | [optional] 
**status_history** | [**List[MonitorCheckStatusHistory]**](MonitorCheckStatusHistory.md) | List of status history records for the check. | [optional] 

## Example

```python
from pingera.models.monitor_check_status_history_list import MonitorCheckStatusHistoryList

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorCheckStatusHistoryList from a JSON string
monitor_check_status_history_list_instance = MonitorCheckStatusHistoryList.from_json(json)
# print the JSON string representation of the object
print(MonitorCheckStatusHistoryList.to_json())

# convert the object into a dict
monitor_check_status_history_list_dict = monitor_check_status_history_list_instance.to_dict()
# create an instance of MonitorCheckStatusHistoryList from a dict
monitor_check_status_history_list_from_dict = MonitorCheckStatusHistoryList.from_dict(monitor_check_status_history_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


