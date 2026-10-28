# OAuthCallback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | OAuth authorization code from provider | 
**state** | **str** | State value returned by the provider, as issued by the authorize endpoint | 
**code_verifier** | **str** | PKCE code_verifier matching the code_challenge sent to the authorize endpoint | 

## Example

```python
from pingera.models.o_auth_callback import OAuthCallback

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthCallback from a JSON string
o_auth_callback_instance = OAuthCallback.from_json(json)
# print the JSON string representation of the object
print(OAuthCallback.to_json())

# convert the object into a dict
o_auth_callback_dict = o_auth_callback_instance.to_dict()
# create an instance of OAuthCallback from a dict
o_auth_callback_from_dict = OAuthCallback.from_dict(o_auth_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


