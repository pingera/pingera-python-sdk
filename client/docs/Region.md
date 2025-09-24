# Region


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The human-readable display name for the region. | [optional] 
**available_check_types** | **List[str]** | List of check types available in this region. | [optional] 
**id** | **str** | The unique identifier for the region. | [optional] 

## Example

```python
from pingera.models.region import Region

# TODO update the JSON string below
json = "{}"
# create an instance of Region from a JSON string
region_instance = Region.from_json(json)
# print the JSON string representation of the object
print(Region.to_json())

# convert the object into a dict
region_dict = region_instance.to_dict()
# create an instance of Region from a dict
region_from_dict = Region.from_dict(region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


