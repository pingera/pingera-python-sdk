# ExecutionGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_regions** | **List[str]** | List of regions where execution was requested | [optional] 
**execution_type** | **str** | Type of execution | [optional] 
**status** | **str** | Overall status of the execution group | [optional] 
**regional_summary** | **Dict[str, object]** | Summary of results by region | [optional] 
**started_at** | **datetime** | When the execution started | [optional] 
**triggered_by_user_id** | **str** | ID of user who triggered the execution (null for scheduled) | [optional] 
**check_id** | **str** | ID of the check (null for on-demand custom checks) | [optional] 
**created_at** | **datetime** | When the execution group was created | [optional] 
**organization_id** | **str** | ID of the organization that owns this execution | [optional] 
**statistics** | [**ExecutionGroupStatistics**](ExecutionGroupStatistics.md) | Aggregated statistics for this execution group | [optional] 
**completed_at** | **datetime** | When the execution completed | [optional] 
**id** | **str** | Unique identifier for the execution group | [optional] [readonly] 
**timeout_at** | **datetime** | When to give up waiting for results | [optional] 
**execution_mode** | **str** | Execution mode used | [optional] 

## Example

```python
from pingera.models.execution_group import ExecutionGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionGroup from a JSON string
execution_group_instance = ExecutionGroup.from_json(json)
# print the JSON string representation of the object
print(ExecutionGroup.to_json())

# convert the object into a dict
execution_group_dict = execution_group_instance.to_dict()
# create an instance of ExecutionGroup from a dict
execution_group_from_dict = ExecutionGroup.from_dict(execution_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


