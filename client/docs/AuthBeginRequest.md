# AuthBeginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Optional user ID to hint which user is trying to authenticate. Enables usernameless login if omitted. | [optional] 

## Example

```python
from pingera.models.auth_begin_request import AuthBeginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthBeginRequest from a JSON string
auth_begin_request_instance = AuthBeginRequest.from_json(json)
# print the JSON string representation of the object
print(AuthBeginRequest.to_json())

# convert the object into a dict
auth_begin_request_dict = auth_begin_request_instance.to_dict()
# create an instance of AuthBeginRequest from a dict
auth_begin_request_from_dict = AuthBeginRequest.from_dict(auth_begin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


