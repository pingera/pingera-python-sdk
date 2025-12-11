# PlanSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | [**Plan**](Plan.md) | The subscribed plan details including pricing and limits. | [optional] [readonly] 
**created_at** | **datetime** | The timestamp when the subscription was created in ISO format. | [optional] 
**id** | **str** | The unique identifier for the plan subscription. | [optional] [readonly] 
**start_date** | **datetime** | The start date of the subscription in ISO format. | [optional] 
**end_date** | **datetime** | The end date of the subscription in ISO format. | [optional] 

## Example

```python
from pingera.models.plan_subscription import PlanSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSubscription from a JSON string
plan_subscription_instance = PlanSubscription.from_json(json)
# print the JSON string representation of the object
print(PlanSubscription.to_json())

# convert the object into a dict
plan_subscription_dict = plan_subscription_instance.to_dict()
# create an instance of PlanSubscription from a dict
plan_subscription_from_dict = PlanSubscription.from_dict(plan_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


