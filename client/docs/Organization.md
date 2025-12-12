# Organization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The timestamp when the organization was created in ISO format. | [optional] [readonly] 
**name** | **str** | The name of the organization. Maximum 100 characters. | 
**id** | **str** | The unique identifier for the organization. | [optional] [readonly] 
**auto_renew** | **bool** | Whether the subscription will automatically renew at the end of the billing period. | [optional] 
**current_subscription** | [**PlanSubscription**](PlanSubscription.md) | The current active subscription for the organization. | [optional] [readonly] 

## Example

```python
from pingera.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print(Organization.to_json())

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_from_dict = Organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


