# HeartbeatPingCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **Dict[str, object]** | Summary statistics for the time period. | [optional] [readonly] 
**ping_counts** | [**List[HeartbeatPingCountHistory]**](HeartbeatPingCountHistory.md) | List of hourly ping counts. | [optional] [readonly] 

## Example

```python
from pingera.models.heartbeat_ping_count_response import HeartbeatPingCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HeartbeatPingCountResponse from a JSON string
heartbeat_ping_count_response_instance = HeartbeatPingCountResponse.from_json(json)
# print the JSON string representation of the object
print(HeartbeatPingCountResponse.to_json())

# convert the object into a dict
heartbeat_ping_count_response_dict = heartbeat_ping_count_response_instance.to_dict()
# create an instance of HeartbeatPingCountResponse from a dict
heartbeat_ping_count_response_from_dict = HeartbeatPingCountResponse.from_dict(heartbeat_ping_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


