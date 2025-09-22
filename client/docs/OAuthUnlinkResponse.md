# OAuthUnlinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Human-readable result message | [optional] [readonly] 
**success** | **bool** | Whether the account was successfully unlinked | [optional] [readonly] 

## Example

```python
from pingera.models.o_auth_unlink_response import OAuthUnlinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthUnlinkResponse from a JSON string
o_auth_unlink_response_instance = OAuthUnlinkResponse.from_json(json)
# print the JSON string representation of the object
print(OAuthUnlinkResponse.to_json())

# convert the object into a dict
o_auth_unlink_response_dict = o_auth_unlink_response_instance.to_dict()
# create an instance of OAuthUnlinkResponse from a dict
o_auth_unlink_response_from_dict = OAuthUnlinkResponse.from_dict(o_auth_unlink_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


