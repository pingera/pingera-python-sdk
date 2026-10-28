# PrivateLocationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_locations** | [**List[PrivateLocation]**](PrivateLocation.md) |  | [optional] 
**limit** | **int** | Maximum number of private locations allowed by the plan | [optional] 
**used** | **int** | Number of private locations in the organization | [optional] 
**approved** | **bool** | Whether private locations are enabled for the organization | [optional] 

## Example

```python
from pingera.models.private_location_list import PrivateLocationList

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateLocationList from a JSON string
private_location_list_instance = PrivateLocationList.from_json(json)
# print the JSON string representation of the object
print(PrivateLocationList.to_json())

# convert the object into a dict
private_location_list_dict = private_location_list_instance.to_dict()
# create an instance of PrivateLocationList from a dict
private_location_list_from_dict = PrivateLocationList.from_dict(private_location_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


