# HeartbeatPing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**received_at** | **datetime** | The timestamp when the ping was received in ISO format. | [optional] [readonly] 
**user_agent** | **str** | The User-Agent header from the ping request. | [optional] [readonly] 
**ping_data** | **Dict[str, object]** | Additional JSON data sent with the ping request. | [optional] [readonly] 
**source_ip** | **str** | The IP address from which the ping was sent. | [optional] [readonly] 
**check_id** | **str** | The identifier of the heartbeat check this ping belongs to. | [optional] [readonly] 
**id** | **str** | The unique identifier for the heartbeat ping. | [optional] [readonly] 

## Example

```python
from pingera.models.heartbeat_ping import HeartbeatPing

# TODO update the JSON string below
json = "{}"
# create an instance of HeartbeatPing from a JSON string
heartbeat_ping_instance = HeartbeatPing.from_json(json)
# print the JSON string representation of the object
print(HeartbeatPing.to_json())

# convert the object into a dict
heartbeat_ping_dict = heartbeat_ping_instance.to_dict()
# create an instance of HeartbeatPing from a dict
heartbeat_ping_from_dict = HeartbeatPing.from_dict(heartbeat_ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


