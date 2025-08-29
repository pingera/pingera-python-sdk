# HeartbeatCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grace_seconds** | **int** | A grace period in seconds to wait before marking the check as &#39;down&#39;. Defaults to 3600. | [optional] [default to 3600]
**next_expected_ping** | **datetime** | The timestamp when the next ping is expected in ISO format. | [optional] [readonly] 
**last_ping_at** | **datetime** | The timestamp of the last received ping in ISO format. | [optional] [readonly] 
**status** | **str** | The current status of the heartbeat check. | [optional] [readonly] 
**updated_at** | **datetime** | The timestamp when the heartbeat check was last updated in ISO format. | [optional] [readonly] 
**id** | **str** | The unique identifier for the heartbeat check. 12 chars, alpha-numeric. | [optional] [readonly] 
**name** | **str** | A user-friendly name for the heartbeat check. Max 100 symbols. | 
**period_seconds** | **int** | The expected interval between pings, in seconds. Minimum is 60. | 
**ping_url** | **str** | The unique URL to which the monitored service should send GET or POST requests. Auto-generated. | [optional] [readonly] 
**created_at** | **datetime** | The timestamp when the heartbeat check was created in ISO format. | [optional] [readonly] 
**active** | **bool** | Whether the heartbeat check is active or paused. Defaults to true. | [optional] [default to True]

## Example

```python
from pingera.models.heartbeat_check import HeartbeatCheck

# TODO update the JSON string below
json = "{}"
# create an instance of HeartbeatCheck from a JSON string
heartbeat_check_instance = HeartbeatCheck.from_json(json)
# print the JSON string representation of the object
print(HeartbeatCheck.to_json())

# convert the object into a dict
heartbeat_check_dict = heartbeat_check_instance.to_dict()
# create an instance of HeartbeatCheck from a dict
heartbeat_check_from_dict = HeartbeatCheck.from_dict(heartbeat_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


