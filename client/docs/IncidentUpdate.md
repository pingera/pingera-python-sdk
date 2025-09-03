# IncidentUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The content of the incident update. | [optional] 
**created_at** | **datetime** | The timestamp when the incident update was created. | [optional] [readonly] 
**incident_id** | **str** | The ID of the incident this update belongs to. | [optional] [readonly] 
**updated_at** | **datetime** | The timestamp when the incident update was last updated. | [optional] [readonly] 
**deliver_notifications** | **bool** | Whether to send notifications for this update. | [optional] [default to True]
**components** | **object** | Components affected by this incident update. | [optional] [readonly] 
**id** | **str** | The unique identifier for the incident update. | [optional] [readonly] 
**status** | **str** | The status of the incident update. | [optional] 

## Example

```python
from pingera.models.incident_update import IncidentUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentUpdate from a JSON string
incident_update_instance = IncidentUpdate.from_json(json)
# print the JSON string representation of the object
print(IncidentUpdate.to_json())

# convert the object into a dict
incident_update_dict = incident_update_instance.to_dict()
# create an instance of IncidentUpdate from a dict
incident_update_from_dict = IncidentUpdate.from_dict(incident_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


