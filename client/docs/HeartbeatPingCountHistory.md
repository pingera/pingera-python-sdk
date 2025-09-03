# HeartbeatPingCountHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ping_count** | **int** | Number of pings received in this hour bucket. | [optional] [readonly] 
**hour** | **str** | The hour bucket timestamp in GMT format following RFC standard. | [optional] [readonly] 

## Example

```python
from pingera.models.heartbeat_ping_count_history import HeartbeatPingCountHistory

# TODO update the JSON string below
json = "{}"
# create an instance of HeartbeatPingCountHistory from a JSON string
heartbeat_ping_count_history_instance = HeartbeatPingCountHistory.from_json(json)
# print the JSON string representation of the object
print(HeartbeatPingCountHistory.to_json())

# convert the object into a dict
heartbeat_ping_count_history_dict = heartbeat_ping_count_history_instance.to_dict()
# create an instance of HeartbeatPingCountHistory from a dict
heartbeat_ping_count_history_from_dict = HeartbeatPingCountHistory.from_dict(heartbeat_ping_count_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


