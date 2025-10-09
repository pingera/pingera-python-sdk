# OAuthLoginResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | JWT access token for authenticated requests | [optional] [readonly] 
**linked_account** | **bool** | Whether OAuth account was linked to existing user | [optional] [readonly] 
**is_new_user** | **bool** | Whether this was a new user registration | [optional] [readonly] 
**auth_method** | **str** | Authentication method used | [optional] [readonly] 
**user** | [**User**](User.md) | User information | [optional] [readonly] 
**refresh_token** | **str** | Refresh token for obtaining new access tokens | [optional] [readonly] 

## Example

```python
from pingera.models.o_auth_login_response import OAuthLoginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthLoginResponse from a JSON string
o_auth_login_response_instance = OAuthLoginResponse.from_json(json)
# print the JSON string representation of the object
print(OAuthLoginResponse.to_json())

# convert the object into a dict
o_auth_login_response_dict = o_auth_login_response_instance.to_dict()
# create an instance of OAuthLoginResponse from a dict
o_auth_login_response_from_dict = OAuthLoginResponse.from_dict(o_auth_login_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


