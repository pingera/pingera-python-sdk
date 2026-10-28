# UsageNextPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from pingera.models.usage_next_plan import UsageNextPlan

# TODO update the JSON string below
json = "{}"
# create an instance of UsageNextPlan from a JSON string
usage_next_plan_instance = UsageNextPlan.from_json(json)
# print the JSON string representation of the object
print(UsageNextPlan.to_json())

# convert the object into a dict
usage_next_plan_dict = usage_next_plan_instance.to_dict()
# create an instance of UsageNextPlan from a dict
usage_next_plan_from_dict = UsageNextPlan.from_dict(usage_next_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


