# LoginOptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**methods** | **List[str]** | Available authentication methods for this email | [optional] [readonly] 
**preferred** | **str** | Preferred authentication method | [optional] [readonly] 
**requires_2fa** | **bool** | Whether 2FA is required for this user | [optional] [readonly] 

## Example

```python
from pingera.models.login_options_response import LoginOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoginOptionsResponse from a JSON string
login_options_response_instance = LoginOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(LoginOptionsResponse.to_json())

# convert the object into a dict
login_options_response_dict = login_options_response_instance.to_dict()
# create an instance of LoginOptionsResponse from a dict
login_options_response_from_dict = LoginOptionsResponse.from_dict(login_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


