# RegistrationCompleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**Credential**](Credential.md) | Information about the newly created credential. | [optional] [readonly] 
**success** | **bool** | Indicates if the registration was successful. | [optional] [readonly] 

## Example

```python
from pingera.models.registration_complete_response import RegistrationCompleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationCompleteResponse from a JSON string
registration_complete_response_instance = RegistrationCompleteResponse.from_json(json)
# print the JSON string representation of the object
print(RegistrationCompleteResponse.to_json())

# convert the object into a dict
registration_complete_response_dict = registration_complete_response_instance.to_dict()
# create an instance of RegistrationCompleteResponse from a dict
registration_complete_response_from_dict = RegistrationCompleteResponse.from_dict(registration_complete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


