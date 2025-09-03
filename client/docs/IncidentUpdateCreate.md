# IncidentUpdateCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The content/message of the incident update. | 
**status** | **str** | The incident status for this update. | 
**deliver_notifications** | **bool** | Whether to send notifications for this update. | [optional] [default to True]

## Example

```python
from pingera.models.incident_update_create import IncidentUpdateCreate

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentUpdateCreate from a JSON string
incident_update_create_instance = IncidentUpdateCreate.from_json(json)
# print the JSON string representation of the object
print(IncidentUpdateCreate.to_json())

# convert the object into a dict
incident_update_create_dict = incident_update_create_instance.to_dict()
# create an instance of IncidentUpdateCreate from a dict
incident_update_create_from_dict = IncidentUpdateCreate.from_dict(incident_update_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


