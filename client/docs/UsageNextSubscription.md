# UsageNextSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | [**UsageNextPlan**](UsageNextPlan.md) |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 

## Example

```python
from pingera.models.usage_next_subscription import UsageNextSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of UsageNextSubscription from a JSON string
usage_next_subscription_instance = UsageNextSubscription.from_json(json)
# print the JSON string representation of the object
print(UsageNextSubscription.to_json())

# convert the object into a dict
usage_next_subscription_dict = usage_next_subscription_instance.to_dict()
# create an instance of UsageNextSubscription from a dict
usage_next_subscription_from_dict = UsageNextSubscription.from_dict(usage_next_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


