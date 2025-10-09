# PasswordHintsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**List[PasswordHint]**](PasswordHint.md) | List of available password hints | [optional] 

## Example

```python
from pingera.models.password_hints_response import PasswordHintsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordHintsResponse from a JSON string
password_hints_response_instance = PasswordHintsResponse.from_json(json)
# print the JSON string representation of the object
print(PasswordHintsResponse.to_json())

# convert the object into a dict
password_hints_response_dict = password_hints_response_instance.to_dict()
# create an instance of PasswordHintsResponse from a dict
password_hints_response_from_dict = PasswordHintsResponse.from_dict(password_hints_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


