# CheckGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The timestamp when the group was created in ISO format. | [optional] [readonly] 
**color** | **str** | Hex color code for the group (e.g., #4F46E5). | [optional] 
**position** | **int** | Position for ordering groups (0 &#x3D; first). | [optional] 
**updated_at** | **datetime** | The timestamp when the group was last updated in ISO format. | [optional] [readonly] 
**description** | **str** | Optional description for the check group. Max 500 characters. | [optional] 
**id** | **str** | The unique identifier for the check group. | [optional] [readonly] 
**active** | **bool** | Whether the check group is active. | [optional] 
**name** | **str** | A user-friendly name for the check group. Max 100 characters. | 

## Example

```python
from pingera.models.check_group import CheckGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CheckGroup from a JSON string
check_group_instance = CheckGroup.from_json(json)
# print the JSON string representation of the object
print(CheckGroup.to_json())

# convert the object into a dict
check_group_dict = check_group_instance.to_dict()
# create an instance of CheckGroup from a dict
check_group_from_dict = CheckGroup.from_dict(check_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


