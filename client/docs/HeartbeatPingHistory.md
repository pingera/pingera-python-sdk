# HeartbeatPingHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | **Dict[str, object]** | Pagination metadata for the ping history. | [optional] [readonly] 
**pings** | [**List[HeartbeatPing]**](HeartbeatPing.md) |  | [optional] [readonly] 

## Example

```python
from pingera.models.heartbeat_ping_history import HeartbeatPingHistory

# TODO update the JSON string below
json = "{}"
# create an instance of HeartbeatPingHistory from a JSON string
heartbeat_ping_history_instance = HeartbeatPingHistory.from_json(json)
# print the JSON string representation of the object
print(HeartbeatPingHistory.to_json())

# convert the object into a dict
heartbeat_ping_history_dict = heartbeat_ping_history_instance.to_dict()
# create an instance of HeartbeatPingHistory from a dict
heartbeat_ping_history_from_dict = HeartbeatPingHistory.from_dict(heartbeat_ping_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


