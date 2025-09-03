# MonitorCheckResultList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | **Dict[str, object]** | Pagination information for the check results. | [optional] 
**results** | [**List[MonitorCheckResult]**](MonitorCheckResult.md) | List of monitor check results. | [optional] 

## Example

```python
from pingera.models.monitor_check_result_list import MonitorCheckResultList

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorCheckResultList from a JSON string
monitor_check_result_list_instance = MonitorCheckResultList.from_json(json)
# print the JSON string representation of the object
print(MonitorCheckResultList.to_json())

# convert the object into a dict
monitor_check_result_list_dict = monitor_check_result_list_instance.to_dict()
# create an instance of MonitorCheckResultList from a dict
monitor_check_result_list_from_dict = MonitorCheckResultList.from_dict(monitor_check_result_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


