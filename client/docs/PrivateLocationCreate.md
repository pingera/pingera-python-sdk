# PrivateLocationCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**country** | **str** | ISO 3166-1 alpha-2 country code | [optional] 
**check_types** | **List[str]** | Check types to run from this location | [optional] 

## Example

```python
from pingera.models.private_location_create import PrivateLocationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateLocationCreate from a JSON string
private_location_create_instance = PrivateLocationCreate.from_json(json)
# print the JSON string representation of the object
print(PrivateLocationCreate.to_json())

# convert the object into a dict
private_location_create_dict = private_location_create_instance.to_dict()
# create an instance of PrivateLocationCreate from a dict
private_location_create_from_dict = PrivateLocationCreate.from_dict(private_location_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


