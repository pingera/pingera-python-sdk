# IncidentTemplate1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the template. | [optional] [readonly] 
**page_id** | **str** | The status page the template belongs to. | [optional] [readonly] 
**type** | **str** | Whether the template is used for incidents or scheduled maintenance. | [optional] 
**name** | **str** | Internal label shown in the template picker. Not visible on the status page. | [optional] 
**title** | **str** | Pre-fills the incident or maintenance title. | [optional] 
**body** | **str** | Pre-fills the update message. Defaults to an empty string. | [optional] 
**status** | **str** | Incident status to apply. Only for incident templates; always null for maintenance templates. | [optional] 
**components** | **Dict[str, str]** | Components to pre-select, mapped to the status they should be set to. For maintenance templates the status is always under_maintenance. | [optional] 
**duration_minutes** | **int** | Default maintenance window length in minutes. Only for maintenance templates. | [optional] 
**created_at** | **datetime** | When the template was created (UTC). | [optional] [readonly] 
**updated_at** | **datetime** | When the template was last updated (UTC). | [optional] [readonly] 

## Example

```python
from pingera.models.incident_template1 import IncidentTemplate1

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentTemplate1 from a JSON string
incident_template1_instance = IncidentTemplate1.from_json(json)
# print the JSON string representation of the object
print(IncidentTemplate1.to_json())

# convert the object into a dict
incident_template1_dict = incident_template1_instance.to_dict()
# create an instance of IncidentTemplate1 from a dict
incident_template1_from_dict = IncidentTemplate1.from_dict(incident_template1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


