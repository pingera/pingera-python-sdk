# HeartbeatCheckList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | **Dict[str, object]** | Pagination metadata for the list of checks. | [optional] [readonly] 
**checks** | [**List[HeartbeatCheck]**](HeartbeatCheck.md) |  | [optional] [readonly] 

## Example

```python
from pingera.models.heartbeat_check_list import HeartbeatCheckList

# TODO update the JSON string below
json = "{}"
# create an instance of HeartbeatCheckList from a JSON string
heartbeat_check_list_instance = HeartbeatCheckList.from_json(json)
# print the JSON string representation of the object
print(HeartbeatCheckList.to_json())

# convert the object into a dict
heartbeat_check_list_dict = heartbeat_check_list_instance.to_dict()
# create an instance of HeartbeatCheckList from a dict
heartbeat_check_list_from_dict = HeartbeatCheckList.from_dict(heartbeat_check_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


