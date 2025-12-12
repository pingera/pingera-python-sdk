# PasswordVerificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password_name** | **str** | Name of the matched password (if available) | [optional] 
**token_type** | **str** | Type of the token | [optional] 
**expires_in** | **int** | Token expiration time in seconds | [optional] 
**access_token** | **str** | JWT access token for the page | [optional] 

## Example

```python
from pingera.models.password_verification_response import PasswordVerificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordVerificationResponse from a JSON string
password_verification_response_instance = PasswordVerificationResponse.from_json(json)
# print the JSON string representation of the object
print(PasswordVerificationResponse.to_json())

# convert the object into a dict
password_verification_response_dict = password_verification_response_instance.to_dict()
# create an instance of PasswordVerificationResponse from a dict
password_verification_response_from_dict = PasswordVerificationResponse.from_dict(password_verification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


