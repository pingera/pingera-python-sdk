# UsagePlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**auto_renew** | **bool** |  | [optional] 

## Example

```python
from pingera.models.usage_plan import UsagePlan

# TODO update the JSON string below
json = "{}"
# create an instance of UsagePlan from a JSON string
usage_plan_instance = UsagePlan.from_json(json)
# print the JSON string representation of the object
print(UsagePlan.to_json())

# convert the object into a dict
usage_plan_dict = usage_plan_instance.to_dict()
# create an instance of UsagePlan from a dict
usage_plan_from_dict = UsagePlan.from_dict(usage_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


