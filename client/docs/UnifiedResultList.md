# UnifiedResultList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[UnifiedResult]**](UnifiedResult.md) |  | [optional] 
**pagination** | **Dict[str, object]** |  | [optional] 

## Example

```python
from pingera.models.unified_result_list import UnifiedResultList

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedResultList from a JSON string
unified_result_list_instance = UnifiedResultList.from_json(json)
# print the JSON string representation of the object
print(UnifiedResultList.to_json())

# convert the object into a dict
unified_result_list_dict = unified_result_list_instance.to_dict()
# create an instance of UnifiedResultList from a dict
unified_result_list_from_dict = UnifiedResultList.from_dict(unified_result_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


