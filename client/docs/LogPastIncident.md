# LogPastIncident


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**impact** | **str** | The impact level of the incident | 
**deliver_notifications** | **bool** | Whether to send notifications | [optional] [default to False]
**name** | **str** | The name of the incident | 
**incident_updates** | [**List[PastIncidentUpdate]**](PastIncidentUpdate.md) | Array of incident updates in chronological order | 

## Example

```python
from pingera.models.log_past_incident import LogPastIncident

# TODO update the JSON string below
json = "{}"
# create an instance of LogPastIncident from a JSON string
log_past_incident_instance = LogPastIncident.from_json(json)
# print the JSON string representation of the object
print(LogPastIncident.to_json())

# convert the object into a dict
log_past_incident_dict = log_past_incident_instance.to_dict()
# create an instance of LogPastIncident from a dict
log_past_incident_from_dict = LogPastIncident.from_dict(log_past_incident_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


