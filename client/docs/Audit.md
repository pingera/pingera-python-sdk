# Audit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the audit entry. | [optional] [readonly] 
**action** | **object** | Action performed (e.g. create, update, delete, login, invite). | [optional] [readonly] 
**entity_type** | **str** | Type of the affected entity (e.g. check, status_page, component, user). | [optional] [readonly] 
**entity_id** | **str** | Identifier of the affected entity. | [optional] [readonly] 
**entity_name** | **str** | Human-readable name of the affected entity at the time of the action. | [optional] [readonly] 
**user_id** | **str** | Identifier of the actor, if still present. | [optional] [readonly] 
**actor_email** | **str** | Email of the actor at the time of the action. | [optional] [readonly] 
**actor_name** | **str** | Name of the actor at the time of the action. | [optional] [readonly] 
**ip_address** | **str** | Client IP address of the actor. | [optional] [readonly] 
**user_agent** | **str** | Client user-agent of the actor. | [optional] [readonly] 
**metadata** | **object** | Additional context for the action. | [optional] [readonly] 
**created_at** | **datetime** | When the action occurred (UTC). | [optional] [readonly] 

## Example

```python
from pingera.models.audit import Audit

# TODO update the JSON string below
json = "{}"
# create an instance of Audit from a JSON string
audit_instance = Audit.from_json(json)
# print the JSON string representation of the object
print(Audit.to_json())

# convert the object into a dict
audit_dict = audit_instance.to_dict()
# create an instance of Audit from a dict
audit_from_dict = Audit.from_dict(audit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


