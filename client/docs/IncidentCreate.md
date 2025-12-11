# IncidentCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deliver_notifications** | **bool** | Whether to send notifications when creating this incident. | [optional] [default to True]
**scheduled_reminded_at** | **datetime** | The timestamp when reminder notifications were sent for scheduled maintenance (UTC). | [optional] 
**auto_transition_deliver_notifications_at_end** | **bool** | Whether to deliver notifications when auto-transitioning at the end of scheduled maintenance. | [optional] 
**scheduled_for** | **datetime** | For scheduled maintenance, the timestamp when maintenance is scheduled to start (UTC). | [optional] 
**name** | **str** | The name/title of the incident. Must be between 1 and 200 characters. | 
**scheduled_auto_completed** | **bool** | Whether the scheduled maintenance should automatically be marked as completed. | [optional] 
**impact** | **str** | The impact level of the incident. | [optional] 
**auto_transition_to_maintenance_state** | **bool** | Whether to automatically transition components to maintenance state during scheduled maintenance. | [optional] 
**reminder_intervals** | **str** | The intervals at which to send reminder notifications for scheduled maintenance. | [optional] 
**components** | **Dict[str, str]** | A dictionary mapping component IDs to their status during incident creation. | [optional] 
**auto_transition_to_operational_state** | **bool** | Whether to automatically transition components back to operational state after scheduled maintenance. | [optional] 
**scheduled_until** | **datetime** | For scheduled maintenance, the timestamp when maintenance is scheduled to end (UTC). | [optional] 
**scheduled_remind_prior** | **bool** | Whether to send reminder notifications before scheduled maintenance begins. | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata associated with the incident. | [optional] 
**auto_transition_deliver_notifications_at_start** | **bool** | Whether to deliver notifications when auto-transitioning at the start of scheduled maintenance. | [optional] 
**body** | **str** | The initial update body content for the incident. | [optional] 
**scheduled_auto_in_progress** | **bool** | Whether the scheduled maintenance should automatically be marked as in progress. | [optional] 
**status** | **str** | The current status of the incident. | 

## Example

```python
from pingera.models.incident_create import IncidentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentCreate from a JSON string
incident_create_instance = IncidentCreate.from_json(json)
# print the JSON string representation of the object
print(IncidentCreate.to_json())

# convert the object into a dict
incident_create_dict = incident_create_instance.to_dict()
# create an instance of IncidentCreate from a dict
incident_create_from_dict = IncidentCreate.from_dict(incident_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


