# AuthenticationOptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge_id** | **str** | The unique challenge ID for this authentication attempt. Must be sent back in the completion step. | [optional] [readonly] 
**options** | **Dict[str, object]** | The W3C standard PublicKeyCredentialRequestOptions to be passed to navigator.credentials.get(). | [optional] [readonly] 

## Example

```python
from pingera.models.authentication_options_response import AuthenticationOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationOptionsResponse from a JSON string
authentication_options_response_instance = AuthenticationOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticationOptionsResponse.to_json())

# convert the object into a dict
authentication_options_response_dict = authentication_options_response_instance.to_dict()
# create an instance of AuthenticationOptionsResponse from a dict
authentication_options_response_from_dict = AuthenticationOptionsResponse.from_dict(authentication_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


