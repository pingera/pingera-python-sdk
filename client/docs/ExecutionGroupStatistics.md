# ExecutionGroupStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_executions** | **int** | Number of completed executions | [optional] 
**max_response_time** | **int** | Slowest response time across regions in milliseconds | [optional] 
**failed_executions** | **int** | Number of failed executions | [optional] 
**total_executions** | **int** | Total number of regional executions expected | [optional] 
**avg_response_time** | **int** | Average response time across all regions in milliseconds | [optional] 
**min_response_time** | **int** | Fastest response time across regions in milliseconds | [optional] 

## Example

```python
from pingera.models.execution_group_statistics import ExecutionGroupStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionGroupStatistics from a JSON string
execution_group_statistics_instance = ExecutionGroupStatistics.from_json(json)
# print the JSON string representation of the object
print(ExecutionGroupStatistics.to_json())

# convert the object into a dict
execution_group_statistics_dict = execution_group_statistics_instance.to_dict()
# create an instance of ExecutionGroupStatistics from a dict
execution_group_statistics_from_dict = ExecutionGroupStatistics.from_dict(execution_group_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


