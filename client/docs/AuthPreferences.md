# AuthPreferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**require_2fa** | **bool** | Whether to require 2FA for this user | [optional] 
**preferred_auth_method** | **str** | Preferred authentication method | [optional] 
**passkey_only** | **bool** | Whether to allow only passkey authentication | [optional] 

## Example

```python
from pingera.models.auth_preferences import AuthPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPreferences from a JSON string
auth_preferences_instance = AuthPreferences.from_json(json)
# print the JSON string representation of the object
print(AuthPreferences.to_json())

# convert the object into a dict
auth_preferences_dict = auth_preferences_instance.to_dict()
# create an instance of AuthPreferences from a dict
auth_preferences_from_dict = AuthPreferences.from_dict(auth_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


