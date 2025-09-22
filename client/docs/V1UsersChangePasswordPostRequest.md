# V1UsersChangePasswordPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_password** | **str** | Current password for verification | 
**new_password** | **str** | New password to set | 

## Example

```python
from pingera.models.v1_users_change_password_post_request import V1UsersChangePasswordPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UsersChangePasswordPostRequest from a JSON string
v1_users_change_password_post_request_instance = V1UsersChangePasswordPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1UsersChangePasswordPostRequest.to_json())

# convert the object into a dict
v1_users_change_password_post_request_dict = v1_users_change_password_post_request_instance.to_dict()
# create an instance of V1UsersChangePasswordPostRequest from a dict
v1_users_change_password_post_request_from_dict = V1UsersChangePasswordPostRequest.from_dict(v1_users_change_password_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


