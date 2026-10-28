# AuthenticationCompleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | A JWT access token for authenticating subsequent requests. | [optional] [readonly] 
**refresh_token** | **str** | A JWT refresh token for generating new access tokens. | [optional] [readonly] 
**user** | [**User**](User.md) | Information about the authenticated user. | [optional] [readonly] 
**auth_method** | **str** | The authentication method used. | [optional] [readonly] 
**is_first_login** | **bool** | Indicates if this is the user&#39;s first successful authentication. | [optional] [readonly] 

## Example

```python
from pingera.models.authentication_complete_response import AuthenticationCompleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationCompleteResponse from a JSON string
authentication_complete_response_instance = AuthenticationCompleteResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticationCompleteResponse.to_json())

# convert the object into a dict
authentication_complete_response_dict = authentication_complete_response_instance.to_dict()
# create an instance of AuthenticationCompleteResponse from a dict
authentication_complete_response_from_dict = AuthenticationCompleteResponse.from_dict(authentication_complete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


