# PasswordVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The password to verify | 

## Example

```python
from pingera.models.password_verification import PasswordVerification

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordVerification from a JSON string
password_verification_instance = PasswordVerification.from_json(json)
# print the JSON string representation of the object
print(PasswordVerification.to_json())

# convert the object into a dict
password_verification_dict = password_verification_instance.to_dict()
# create an instance of PasswordVerification from a dict
password_verification_from_dict = PasswordVerification.from_dict(password_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


