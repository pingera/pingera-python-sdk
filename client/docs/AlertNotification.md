# AlertNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Error message if the notification failed to send. Null if successful. | [optional] [readonly] 
**channel_id** | **str** | The identifier of the alert channel used for this notification. | [optional] [readonly] 
**status** | **str** | The delivery status of the notification. | [optional] [readonly] 
**alert_id** | **str** | The identifier of the alert this notification belongs to. | [optional] [readonly] 
**id** | **str** | The unique identifier for the alert notification. | [optional] [readonly] 
**sent_at** | **datetime** | The timestamp when the notification was successfully sent in ISO format. Null if not sent. | [optional] [readonly] 
**retry_count** | **int** | The number of retry attempts for this notification. | [optional] [readonly] 
**channel_name** | **object** | The name of the alert channel used for this notification. | [optional] [readonly] 
**notification_type** | **str** | The type of notification sent. | [optional] [readonly] 
**created_at** | **datetime** | The timestamp when the notification was created in ISO format. | [optional] [readonly] 
**channel_type** | **str** | The type of the alert channel used for this notification. | [optional] [readonly] 

## Example

```python
from pingera.models.alert_notification import AlertNotification

# TODO update the JSON string below
json = "{}"
# create an instance of AlertNotification from a JSON string
alert_notification_instance = AlertNotification.from_json(json)
# print the JSON string representation of the object
print(AlertNotification.to_json())

# convert the object into a dict
alert_notification_dict = alert_notification_instance.to_dict()
# create an instance of AlertNotification from a dict
alert_notification_from_dict = AlertNotification.from_dict(alert_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


