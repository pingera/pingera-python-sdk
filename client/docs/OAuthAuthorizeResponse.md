# OAuthAuthorizeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_url** | **str** | URL to redirect user to for OAuth authorization | [optional] [readonly] 
**state** | **str** | OAuth state parameter for CSRF protection | [optional] [readonly] 

## Example

```python
from pingera.models.o_auth_authorize_response import OAuthAuthorizeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthAuthorizeResponse from a JSON string
o_auth_authorize_response_instance = OAuthAuthorizeResponse.from_json(json)
# print the JSON string representation of the object
print(OAuthAuthorizeResponse.to_json())

# convert the object into a dict
o_auth_authorize_response_dict = o_auth_authorize_response_instance.to_dict()
# create an instance of OAuthAuthorizeResponse from a dict
o_auth_authorize_response_from_dict = OAuthAuthorizeResponse.from_dict(o_auth_authorize_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


