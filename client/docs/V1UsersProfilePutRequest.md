# V1UsersProfilePutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | User first name | [optional] 
**last_name** | **str** | User last name | [optional] 

## Example

```python
from pingera.models.v1_users_profile_put_request import V1UsersProfilePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UsersProfilePutRequest from a JSON string
v1_users_profile_put_request_instance = V1UsersProfilePutRequest.from_json(json)
# print the JSON string representation of the object
print(V1UsersProfilePutRequest.to_json())

# convert the object into a dict
v1_users_profile_put_request_dict = v1_users_profile_put_request_instance.to_dict()
# create an instance of V1UsersProfilePutRequest from a dict
v1_users_profile_put_request_from_dict = V1UsersProfilePutRequest.from_dict(v1_users_profile_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


