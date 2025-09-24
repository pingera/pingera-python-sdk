# PageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) | Pagination information | [optional] 
**pages** | [**List[Page]**](Page.md) | List of status pages | [optional] 

## Example

```python
from pingera.models.page_list import PageList

# TODO update the JSON string below
json = "{}"
# create an instance of PageList from a JSON string
page_list_instance = PageList.from_json(json)
# print the JSON string representation of the object
print(PageList.to_json())

# convert the object into a dict
page_list_dict = page_list_instance.to_dict()
# create an instance of PageList from a dict
page_list_from_dict = PageList.from_dict(page_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


