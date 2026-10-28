# PrivateLocationUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**country** | **str** | ISO 3166-1 alpha-2 country code | [optional] 
**check_types** | **List[str]** | Check types to run from this location | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from pingera.models.private_location_update import PrivateLocationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateLocationUpdate from a JSON string
private_location_update_instance = PrivateLocationUpdate.from_json(json)
# print the JSON string representation of the object
print(PrivateLocationUpdate.to_json())

# convert the object into a dict
private_location_update_dict = private_location_update_instance.to_dict()
# create an instance of PrivateLocationUpdate from a dict
private_location_update_from_dict = PrivateLocationUpdate.from_dict(private_location_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


