# OAuthLinkCompleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**LinkedOAuthAccount**](LinkedOAuthAccount.md) |  | [optional] [readonly] 

## Example

```python
from pingera.models.o_auth_link_complete_response import OAuthLinkCompleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthLinkCompleteResponse from a JSON string
o_auth_link_complete_response_instance = OAuthLinkCompleteResponse.from_json(json)
# print the JSON string representation of the object
print(OAuthLinkCompleteResponse.to_json())

# convert the object into a dict
o_auth_link_complete_response_dict = o_auth_link_complete_response_instance.to_dict()
# create an instance of OAuthLinkCompleteResponse from a dict
o_auth_link_complete_response_from_dict = OAuthLinkCompleteResponse.from_dict(o_auth_link_complete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


