# CheckGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | **Dict[str, object]** | Pagination information for the groups. | [optional] 
**groups** | [**List[CheckGroup1]**](CheckGroup1.md) | List of check groups for the organization. | [optional] 

## Example

```python
from pingera.models.check_group_list import CheckGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of CheckGroupList from a JSON string
check_group_list_instance = CheckGroupList.from_json(json)
# print the JSON string representation of the object
print(CheckGroupList.to_json())

# convert the object into a dict
check_group_list_dict = check_group_list_instance.to_dict()
# create an instance of CheckGroupList from a dict
check_group_list_from_dict = CheckGroupList.from_dict(check_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


