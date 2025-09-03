# IncidentCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The current status of the incident. | 
**body** | **str** | The initial update body content for the incident. | [optional] 
**impact** | **str** | The impact level of the incident. | [optional] 
**deliver_notifications** | **bool** | Whether to send notifications when creating this incident. | [optional] [default to True]
**components** | **Dict[str, str]** | A dictionary mapping component IDs to their status during incident creation. | [optional] 
**name** | **str** | The name/title of the incident. Must be between 1 and 200 characters. | 

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


