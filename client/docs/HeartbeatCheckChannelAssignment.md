# HeartbeatCheckChannelAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_ids** | **List[str]** | A list of alert channel IDs to assign to the heartbeat check. | 

## Example

```python
from pingera.models.heartbeat_check_channel_assignment import HeartbeatCheckChannelAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of HeartbeatCheckChannelAssignment from a JSON string
heartbeat_check_channel_assignment_instance = HeartbeatCheckChannelAssignment.from_json(json)
# print the JSON string representation of the object
print(HeartbeatCheckChannelAssignment.to_json())

# convert the object into a dict
heartbeat_check_channel_assignment_dict = heartbeat_check_channel_assignment_instance.to_dict()
# create an instance of HeartbeatCheckChannelAssignment from a dict
heartbeat_check_channel_assignment_from_dict = HeartbeatCheckChannelAssignment.from_dict(heartbeat_check_channel_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


