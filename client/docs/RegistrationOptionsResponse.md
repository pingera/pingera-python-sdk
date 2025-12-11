# RegistrationOptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge_id** | **str** | The unique challenge ID for this registration attempt. Must be sent back in the completion step. | [optional] [readonly] 
**options** | **Dict[str, object]** | The W3C standard PublicKeyCredentialCreationOptions to be passed to navigator.credentials.create(). | [optional] [readonly] 

## Example

```python
from pingera.models.registration_options_response import RegistrationOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationOptionsResponse from a JSON string
registration_options_response_instance = RegistrationOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(RegistrationOptionsResponse.to_json())

# convert the object into a dict
registration_options_response_dict = registration_options_response_instance.to_dict()
# create an instance of RegistrationOptionsResponse from a dict
registration_options_response_from_dict = RegistrationOptionsResponse.from_dict(registration_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


