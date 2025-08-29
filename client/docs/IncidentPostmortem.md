# IncidentPostmortem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **datetime** | The timestamp when the postmortem was last updated. | [optional] [readonly] 
**body_draft_updated_at** | **datetime** | The timestamp when the draft postmortem body was last updated. | [optional] 
**notify_subscribers** | **bool** | Whether to notify subscribers when the postmortem is published. | [optional] 
**id** | **str** | The unique identifier for the incident postmortem. | [optional] [readonly] 
**body** | **str** | The published content of the postmortem in Markdown format. | [optional] 
**published_at** | **datetime** | The timestamp when the postmortem was published and made publicly available. | [optional] 
**preview_key** | **str** | A unique key that allows public access to preview the postmortem before it&#39;s published. | [optional] 
**incident_id** | **str** | The unique identifier of the incident this postmortem belongs to. | [optional] [readonly] 
**body_updated_at** | **datetime** | The timestamp when the published postmortem body was last updated. | [optional] 
**created_at** | **datetime** | The timestamp when the postmortem was created. | [optional] [readonly] 
**body_draft** | **str** | The draft content of the postmortem that hasn&#39;t been published yet. | [optional] 

## Example

```python
from pingera.models.incident_postmortem import IncidentPostmortem

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentPostmortem from a JSON string
incident_postmortem_instance = IncidentPostmortem.from_json(json)
# print the JSON string representation of the object
print(IncidentPostmortem.to_json())

# convert the object into a dict
incident_postmortem_dict = incident_postmortem_instance.to_dict()
# create an instance of IncidentPostmortem from a dict
incident_postmortem_from_dict = IncidentPostmortem.from_dict(incident_postmortem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


