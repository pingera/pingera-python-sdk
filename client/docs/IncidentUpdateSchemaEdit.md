# IncidentUpdateSchemaEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The update body content for the incident. | [optional] 
**name** | **str** | The name/title of the incident. Must be between 1 and 200 characters. | [optional] 
**components** | **Dict[str, str]** | A dictionary mapping component IDs to their status during incident update. | [optional] 
**deliver_notifications** | **bool** | Whether to send notifications when updating this incident. | [optional] [default to True]
**impact** | **str** | The impact level of the incident. | [optional] 
**status** | **str** | The current status of the incident. | [optional] 

## Example

```python
from pingera.models.incident_update_schema_edit import IncidentUpdateSchemaEdit

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentUpdateSchemaEdit from a JSON string
incident_update_schema_edit_instance = IncidentUpdateSchemaEdit.from_json(json)
# print the JSON string representation of the object
print(IncidentUpdateSchemaEdit.to_json())

# convert the object into a dict
incident_update_schema_edit_dict = incident_update_schema_edit_instance.to_dict()
# create an instance of IncidentUpdateSchemaEdit from a dict
incident_update_schema_edit_from_dict = IncidentUpdateSchemaEdit.from_dict(incident_update_schema_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


