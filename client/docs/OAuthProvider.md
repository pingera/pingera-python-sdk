# OAuthProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_url** | **str** | OAuth authorization endpoint | [optional] [readonly] 
**name** | **str** | Provider identifier | [optional] [readonly] 
**display_name** | **str** | Human-readable provider name | [optional] [readonly] 
**is_active** | **bool** | Whether this provider is currently available | [optional] [readonly] 
**icon_url** | **str** | URL to provider icon/logo for UI | [optional] [readonly] 

## Example

```python
from pingera.models.o_auth_provider import OAuthProvider

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthProvider from a JSON string
o_auth_provider_instance = OAuthProvider.from_json(json)
# print the JSON string representation of the object
print(OAuthProvider.to_json())

# convert the object into a dict
o_auth_provider_dict = o_auth_provider_instance.to_dict()
# create an instance of OAuthProvider from a dict
o_auth_provider_from_dict = OAuthProvider.from_dict(o_auth_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


