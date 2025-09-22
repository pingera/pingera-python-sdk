# V1UsersResetPasswordPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Reset token from email or invitation | 
**new_password** | **str** | New password to set | 

## Example

```python
from pingera.models.v1_users_reset_password_post_request import V1UsersResetPasswordPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UsersResetPasswordPostRequest from a JSON string
v1_users_reset_password_post_request_instance = V1UsersResetPasswordPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1UsersResetPasswordPostRequest.to_json())

# convert the object into a dict
v1_users_reset_password_post_request_dict = v1_users_reset_password_post_request_instance.to_dict()
# create an instance of V1UsersResetPasswordPostRequest from a dict
v1_users_reset_password_post_request_from_dict = V1UsersResetPasswordPostRequest.from_dict(v1_users_reset_password_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


