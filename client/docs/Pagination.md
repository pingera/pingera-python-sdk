# Pagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** | Number of items per page | [optional] 
**total_items** | **int** | Total number of items | [optional] 
**page** | **int** | Current page number | [optional] 
**total_pages** | **int** | Total number of pages | [optional] 
**has_prev** | **bool** | Whether there is a previous page | [optional] 
**has_next** | **bool** | Whether there is a next page | [optional] 

## Example

```python
from pingera.models.pagination import Pagination

# TODO update the JSON string below
json = "{}"
# create an instance of Pagination from a JSON string
pagination_instance = Pagination.from_json(json)
# print the JSON string representation of the object
print(Pagination.to_json())

# convert the object into a dict
pagination_dict = pagination_instance.to_dict()
# create an instance of Pagination from a dict
pagination_from_dict = Pagination.from_dict(pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


