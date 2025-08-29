# AlertChannel1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the alert channel is enabled. Defaults to true. | [optional] [default to True]
**updated_at** | **datetime** | The timestamp when the alert channel was last updated in ISO format. | [optional] [readonly] 
**id** | **str** | The unique identifier for the alert channel. | [optional] [readonly] 
**type** | **str** | The type of alert channel. | [optional] 
**last_used_at** | **datetime** | The timestamp when the alert channel was last used to send an alert in ISO format. Null if never used. | [optional] [readonly] 
**name** | **str** | A user-friendly name for the alert channel. Max 100 characters. | [optional] 
**configuration** | **Dict[str, object]** | Channel-specific configuration. Structure varies by channel type. | [optional] 
**created_at** | **datetime** | The timestamp when the alert channel was created in ISO format. | [optional] [readonly] 

## Example

```python
from pingera.models.alert_channel1 import AlertChannel1

# TODO update the JSON string below
json = "{}"
# create an instance of AlertChannel1 from a JSON string
alert_channel1_instance = AlertChannel1.from_json(json)
# print the JSON string representation of the object
print(AlertChannel1.to_json())

# convert the object into a dict
alert_channel1_dict = alert_channel1_instance.to_dict()
# create an instance of AlertChannel1 from a dict
alert_channel1_from_dict = AlertChannel1.from_dict(alert_channel1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


