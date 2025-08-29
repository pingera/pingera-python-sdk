# HeartbeatPingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_expected_ping** | **datetime** | The timestamp when the next ping is expected in ISO format. | [optional] [readonly] 
**message** | **str** | A message describing the ping result. | [optional] [readonly] 
**status** | **str** | The status of the ping request. | [optional] [readonly] 
**check_id** | **str** | The identifier of the heartbeat check that received the ping. | [optional] [readonly] 

## Example

```python
from pingera.models.heartbeat_ping_response import HeartbeatPingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HeartbeatPingResponse from a JSON string
heartbeat_ping_response_instance = HeartbeatPingResponse.from_json(json)
# print the JSON string representation of the object
print(HeartbeatPingResponse.to_json())

# convert the object into a dict
heartbeat_ping_response_dict = heartbeat_ping_response_instance.to_dict()
# create an instance of HeartbeatPingResponse from a dict
heartbeat_ping_response_from_dict = HeartbeatPingResponse.from_dict(heartbeat_ping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


