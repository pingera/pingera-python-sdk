# CheckServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_metadata** | **Dict[str, object]** | Additional metadata about the server configuration. | [optional] 
**region** | **str** | The geographical region where the server is located. | [optional] 
**country** | **str** | The country where the server is located. | [optional] 
**id** | **str** | The unique identifier for the check server. | [optional] [readonly] 
**ip_address** | **str** | The IP address of the check server. | [optional] 

## Example

```python
from pingera.models.check_server import CheckServer

# TODO update the JSON string below
json = "{}"
# create an instance of CheckServer from a JSON string
check_server_instance = CheckServer.from_json(json)
# print the JSON string representation of the object
print(CheckServer.to_json())

# convert the object into a dict
check_server_dict = check_server_instance.to_dict()
# create an instance of CheckServer from a dict
check_server_from_dict = CheckServer.from_dict(check_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


