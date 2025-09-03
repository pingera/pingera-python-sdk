# AlertChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The timestamp when the alert channel was created in ISO format. | [optional] [readonly] 
**type** | **str** | The type of alert channel. | 
**updated_at** | **datetime** | The timestamp when the alert channel was last updated in ISO format. | [optional] [readonly] 
**last_used_at** | **datetime** | The timestamp when the alert channel was last used to send an alert in ISO format. Null if never used. | [optional] [readonly] 
**enabled** | **bool** | Whether the alert channel is enabled. Defaults to true. | [optional] [default to True]
**id** | **str** | The unique identifier for the alert channel. | [optional] [readonly] 
**configuration** | **Dict[str, object]** | Channel-specific configuration. Structure varies by channel type. | 
**name** | **str** | A user-friendly name for the alert channel. Max 100 characters. | 

## Example

```python
from pingera.models.alert_channel import AlertChannel

# TODO update the JSON string below
json = "{}"
# create an instance of AlertChannel from a JSON string
alert_channel_instance = AlertChannel.from_json(json)
# print the JSON string representation of the object
print(AlertChannel.to_json())

# convert the object into a dict
alert_channel_dict = alert_channel_instance.to_dict()
# create an instance of AlertChannel from a dict
alert_channel_from_dict = AlertChannel.from_dict(alert_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


