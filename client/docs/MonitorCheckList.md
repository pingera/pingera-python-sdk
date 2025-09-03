# MonitorCheckList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checks** | [**List[MonitorCheck]**](MonitorCheck.md) | List of monitor checks for the organization. | [optional] 
**pagination** | **Dict[str, object]** | Pagination information for the check results. | [optional] 

## Example

```python
from pingera.models.monitor_check_list import MonitorCheckList

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorCheckList from a JSON string
monitor_check_list_instance = MonitorCheckList.from_json(json)
# print the JSON string representation of the object
print(MonitorCheckList.to_json())

# convert the object into a dict
monitor_check_list_dict = monitor_check_list_instance.to_dict()
# create an instance of MonitorCheckList from a dict
monitor_check_list_from_dict = MonitorCheckList.from_dict(monitor_check_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


