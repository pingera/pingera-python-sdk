# PasswordHint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the password (if available) | [optional] 
**hint** | **str** | The password hint | [optional] 

## Example

```python
from pingera.models.password_hint import PasswordHint

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordHint from a JSON string
password_hint_instance = PasswordHint.from_json(json)
# print the JSON string representation of the object
print(PasswordHint.to_json())

# convert the object into a dict
password_hint_dict = password_hint_instance.to_dict()
# create an instance of PasswordHint from a dict
password_hint_from_dict = PasswordHint.from_dict(password_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


