# RegionsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_regions** | **int** | Total number of available regions. | [optional] 
**regions** | [**List[Region]**](Region.md) | List of available regions for serverless check execution. | [optional] 

## Example

```python
from pingera.models.regions_list import RegionsList

# TODO update the JSON string below
json = "{}"
# create an instance of RegionsList from a JSON string
regions_list_instance = RegionsList.from_json(json)
# print the JSON string representation of the object
print(RegionsList.to_json())

# convert the object into a dict
regions_list_dict = regions_list_instance.to_dict()
# create an instance of RegionsList from a dict
regions_list_from_dict = RegionsList.from_dict(regions_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


