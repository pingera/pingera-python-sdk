# ExecutionGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_groups** | [**List[ExecutionGroup]**](ExecutionGroup.md) | List of execution groups | [optional] 
**pagination** | **Dict[str, object]** | Pagination information | [optional] 

## Example

```python
from pingera.models.execution_group_list import ExecutionGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionGroupList from a JSON string
execution_group_list_instance = ExecutionGroupList.from_json(json)
# print the JSON string representation of the object
print(ExecutionGroupList.to_json())

# convert the object into a dict
execution_group_list_dict = execution_group_list_instance.to_dict()
# create an instance of ExecutionGroupList from a dict
execution_group_list_from_dict = ExecutionGroupList.from_dict(execution_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


