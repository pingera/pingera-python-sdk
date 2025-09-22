# V1UsersInvitePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address of user to invite | 
**role** | **str** | Role to assign to invited user | [optional] [default to 'viewer']

## Example

```python
from pingera.models.v1_users_invite_post_request import V1UsersInvitePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UsersInvitePostRequest from a JSON string
v1_users_invite_post_request_instance = V1UsersInvitePostRequest.from_json(json)
# print the JSON string representation of the object
print(V1UsersInvitePostRequest.to_json())

# convert the object into a dict
v1_users_invite_post_request_dict = v1_users_invite_post_request_instance.to_dict()
# create an instance of V1UsersInvitePostRequest from a dict
v1_users_invite_post_request_from_dict = V1UsersInvitePostRequest.from_dict(v1_users_invite_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


