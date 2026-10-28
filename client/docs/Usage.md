# Usage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | [**UsagePlan**](UsagePlan.md) | Current subscription plan | [optional] 
**usage** | **Dict[str, object]** | Usage per plan limit, keyed by resource (e.g. checks, monitors, statuspages, sms, credits). Countable resources contain used, limit, percent and unlimited. | [optional] 
**last_calculated** | **datetime** | When usage was last calculated | [optional] 
**next_subscription** | [**UsageNextSubscription**](UsageNextSubscription.md) | Scheduled next subscription, if any | [optional] 
**message** | **str** | Only present when there is no active subscription | [optional] 
**code** | **str** | Only present when there is no active subscription | [optional] 
**subscription_status** | **str** | Only present when there is no active subscription: expired or none | [optional] 

## Example

```python
from pingera.models.usage import Usage

# TODO update the JSON string below
json = "{}"
# create an instance of Usage from a JSON string
usage_instance = Usage.from_json(json)
# print the JSON string representation of the object
print(Usage.to_json())

# convert the object into a dict
usage_dict = usage_instance.to_dict()
# create an instance of Usage from a dict
usage_from_dict = Usage.from_dict(usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


