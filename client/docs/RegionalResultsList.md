# RegionalResultsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regional_results** | [**List[RegionalResultSummary]**](RegionalResultSummary.md) | List of results from each region | [optional] 
**execution_group_id** | **str** | ID of the execution group | [optional] 
**statistics** | [**ExecutionGroupStatistics**](ExecutionGroupStatistics.md) | Aggregated statistics | [optional] 

## Example

```python
from pingera.models.regional_results_list import RegionalResultsList

# TODO update the JSON string below
json = "{}"
# create an instance of RegionalResultsList from a JSON string
regional_results_list_instance = RegionalResultsList.from_json(json)
# print the JSON string representation of the object
print(RegionalResultsList.to_json())

# convert the object into a dict
regional_results_list_dict = regional_results_list_instance.to_dict()
# create an instance of RegionalResultsList from a dict
regional_results_list_from_dict = RegionalResultsList.from_dict(regional_results_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


