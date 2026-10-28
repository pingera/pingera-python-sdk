# AlertChannelTestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the alert channel. | [optional] [readonly] 
**name** | **str** | Optional channel name used in the test message. | [optional] 
**type** | **str** | The type of alert channel. | 
**enabled** | **bool** | Whether the alert channel is enabled. Defaults to true. | [optional] [default to True]
**configuration** | **Dict[str, object]** | Channel-specific configuration. Structure varies by channel type. | 
**created_at** | **datetime** | The timestamp when the alert channel was created in ISO format. | [optional] [readonly] 
**updated_at** | **datetime** | The timestamp when the alert channel was last updated in ISO format. | [optional] [readonly] 
**last_used_at** | **datetime** | The timestamp when the alert channel was last used to send an alert in ISO format. Null if never used. | [optional] [readonly] 

## Example

```python
from pingera.models.alert_channel_test_request import AlertChannelTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AlertChannelTestRequest from a JSON string
alert_channel_test_request_instance = AlertChannelTestRequest.from_json(json)
# print the JSON string representation of the object
print(AlertChannelTestRequest.to_json())

# convert the object into a dict
alert_channel_test_request_dict = alert_channel_test_request_instance.to_dict()
# create an instance of AlertChannelTestRequest from a dict
alert_channel_test_request_from_dict = AlertChannelTestRequest.from_dict(alert_channel_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


