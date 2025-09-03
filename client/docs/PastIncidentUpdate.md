# PastIncidentUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The content of the incident update. | 
**created_at** | **datetime** | When this update was posted (ISO format). | 
**components** | **Dict[str, str]** | Component statuses at time of update | [optional] 
**status** | **str** | The incident status at the time of this update. | 

## Example

```python
from pingera.models.past_incident_update import PastIncidentUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PastIncidentUpdate from a JSON string
past_incident_update_instance = PastIncidentUpdate.from_json(json)
# print the JSON string representation of the object
print(PastIncidentUpdate.to_json())

# convert the object into a dict
past_incident_update_dict = past_incident_update_instance.to_dict()
# create an instance of PastIncidentUpdate from a dict
past_incident_update_from_dict = PastIncidentUpdate.from_dict(past_incident_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


