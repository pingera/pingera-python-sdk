# Plan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **Dict[str, object]** | Pricing information for the plan in different currencies. | [optional] 
**description** | **str** | A detailed description of the plan features and benefits. | [optional] 
**name** | **str** | The name of the subscription plan. Maximum 100 characters. | 
**id** | **str** | The unique identifier for the subscription plan. | [optional] [readonly] 
**duration** | **int** | The duration of the plan subscription in days. Minimum is 1 day. | [optional] 
**limits** | **Dict[str, object]** | Usage limits and quotas for the plan features. | [optional] 

## Example

```python
from pingera.models.plan import Plan

# TODO update the JSON string below
json = "{}"
# create an instance of Plan from a JSON string
plan_instance = Plan.from_json(json)
# print the JSON string representation of the object
print(Plan.to_json())

# convert the object into a dict
plan_dict = plan_instance.to_dict()
# create an instance of Plan from a dict
plan_from_dict = Plan.from_dict(plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


