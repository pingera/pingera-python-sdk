# Incident


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The main description/body content of the incident. | [optional] 
**created_at** | **datetime** | The timestamp when the incident was created in ISO format. | [optional] [readonly] 
**monitoring_at** | **datetime** | The timestamp when the incident status was changed to monitoring. | [optional] 
**scheduled_for** | **datetime** | For scheduled maintenance, the timestamp when maintenance is scheduled to start. | [optional] 
**incident_updates** | **object** | List of all updates posted for this incident, sorted by creation time (newest first). | [optional] [readonly] 
**components** | **object** | List of components affected by this incident with their current status. | [optional] 
**impact** | **str** | The impact level of the incident. | [optional] 
**status** | **str** | The current status of the incident. | 
**auto_transition_deliver_notifications_at_start** | **bool** | Whether to deliver notifications when auto-transitioning at the start of scheduled maintenance. | [optional] 
**scheduled_auto_completed** | **bool** | Whether the scheduled maintenance should automatically be marked as completed. | [optional] 
**postmortem_body** | **object** | The content of the incident postmortem, if published. | [optional] [readonly] 
**name** | **str** | The name/title of the incident. Must be between 1 and 200 characters. | 
**deliver_notifications** | **bool** | Whether to send notifications when creating or updating this incident. | [optional] 
**auto_transition_to_maintenance_state** | **bool** | Whether to automatically transition components to maintenance state during scheduled maintenance. | [optional] 
**auto_transition_to_operational_state** | **bool** | Whether to automatically transition components back to operational state after scheduled maintenance. | [optional] 
**postmortem_body_last_updated_at** | **object** | The timestamp when the postmortem body was last updated. | [optional] [readonly] 
**reminder_intervals** | **str** | The intervals at which to send reminder notifications for scheduled maintenance. | [optional] 
**postmortem_published_at** | **object** | The timestamp when the postmortem was published. | [optional] [readonly] 
**resolved_at** | **object** | The timestamp when the incident was resolved, derived from the latest update with &#39;resolved&#39; status. | [optional] [readonly] 
**scheduled_reminded_at** | **datetime** | The timestamp when reminder notifications were sent for scheduled maintenance. | [optional] 
**scheduled_until** | **datetime** | For scheduled maintenance, the timestamp when maintenance is scheduled to end. | [optional] 
**updated_at** | **datetime** | The timestamp when the incident was last updated in ISO format. | [optional] [readonly] 
**page_id** | **str** | The unique identifier of the status page this incident belongs to. | [optional] [readonly] 
**metadata** | **Dict[str, object]** | Additional metadata associated with the incident. | [optional] 
**id** | **str** | The unique identifier for the incident. | [optional] [readonly] 
**scheduled_remind_prior** | **bool** | Whether to send reminder notifications before scheduled maintenance begins. | [optional] 
**scheduled_auto_in_progress** | **bool** | Whether the scheduled maintenance should automatically be marked as in progress. | [optional] 
**auto_transition_deliver_notifications_at_end** | **bool** | Whether to deliver notifications when auto-transitioning at the end of scheduled maintenance. | [optional] 

## Example

```python
from pingera.models.incident import Incident

# TODO update the JSON string below
json = "{}"
# create an instance of Incident from a JSON string
incident_instance = Incident.from_json(json)
# print the JSON string representation of the object
print(Incident.to_json())

# convert the object into a dict
incident_dict = incident_instance.to_dict()
# create an instance of Incident from a dict
incident_from_dict = Incident.from_dict(incident_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


