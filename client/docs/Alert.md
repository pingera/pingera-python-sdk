# Alert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | A short, descriptive title for the alert. | [optional] [readonly] 
**severity** | **str** | The severity level of the alert. | [optional] [readonly] 
**rule_id** | **str** | The identifier of the alert rule that triggered this alert. | [optional] [readonly] 
**check_name** | **object** | The name of the monitor check that triggered this alert. | [optional] [readonly] 
**acknowledged_at** | **datetime** | The timestamp when the alert was acknowledged in ISO format. Null if not acknowledged. | [optional] [readonly] 
**resolved_at** | **datetime** | The timestamp when the alert was resolved in ISO format. Null if not resolved. | [optional] [readonly] 
**check_id** | **str** | The identifier of the monitor check that triggered this alert. | [optional] [readonly] 
**description** | **str** | A detailed description of the alert condition. | [optional] [readonly] 
**last_notification_at** | **datetime** | The timestamp when the last notification was sent in ISO format. Null if no notifications sent. | [optional] [readonly] 
**duration** | **object** | The duration of the alert in seconds. For active alerts, this is time since firing. | [optional] [readonly] 
**fired_at** | **datetime** | The timestamp when the alert was first triggered in ISO format. | [optional] [readonly] 
**rule_name** | **object** | The name of the alert rule that triggered this alert. | [optional] [readonly] 
**acknowledged_by_id** | **str** | The identifier of the user who acknowledged the alert. Null if not acknowledged. | [optional] [readonly] 
**notification_count** | **int** | The number of notifications sent for this alert. | [optional] [readonly] 
**id** | **str** | The unique identifier for the alert. | [optional] [readonly] 
**is_active** | **object** | Whether the alert is currently active (firing or acknowledged). | [optional] [readonly] 
**status** | **str** | The current status of the alert. | [optional] [readonly] 
**alert_metadata** | **Dict[str, object]** | Additional context and metadata about what triggered the alert. | [optional] [readonly] 

## Example

```python
from pingera.models.alert import Alert

# TODO update the JSON string below
json = "{}"
# create an instance of Alert from a JSON string
alert_instance = Alert.from_json(json)
# print the JSON string representation of the object
print(Alert.to_json())

# convert the object into a dict
alert_dict = alert_instance.to_dict()
# create an instance of Alert from a dict
alert_from_dict = Alert.from_dict(alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


