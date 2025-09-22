# V1UsersRequestPasswordResetPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address to send reset link to | 

## Example

```python
from pingera.models.v1_users_request_password_reset_post_request import V1UsersRequestPasswordResetPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UsersRequestPasswordResetPostRequest from a JSON string
v1_users_request_password_reset_post_request_instance = V1UsersRequestPasswordResetPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1UsersRequestPasswordResetPostRequest.to_json())

# convert the object into a dict
v1_users_request_password_reset_post_request_dict = v1_users_request_password_reset_post_request_instance.to_dict()
# create an instance of V1UsersRequestPasswordResetPostRequest from a dict
v1_users_request_password_reset_post_request_from_dict = V1UsersRequestPasswordResetPostRequest.from_dict(v1_users_request_password_reset_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


