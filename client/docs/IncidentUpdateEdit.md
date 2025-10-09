# IncidentUpdateEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The content/message of the incident update. | [optional] 
**created_at** | **datetime** | The timestamp when the update was created in ISO format. | [optional] 

## Example

```python
from pingera.models.incident_update_edit import IncidentUpdateEdit

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentUpdateEdit from a JSON string
incident_update_edit_instance = IncidentUpdateEdit.from_json(json)
# print the JSON string representation of the object
print(IncidentUpdateEdit.to_json())

# convert the object into a dict
incident_update_edit_dict = incident_update_edit_instance.to_dict()
# create an instance of IncidentUpdateEdit from a dict
incident_update_edit_from_dict = IncidentUpdateEdit.from_dict(incident_update_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


