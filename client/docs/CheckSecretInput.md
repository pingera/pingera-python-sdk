# CheckSecretInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env_variable** | **str** | The environment variable name for this secret. Max 100 characters. | 
**secret_id** | **str** | The unique identifier of the secret. | 

## Example

```python
from pingera.models.check_secret_input import CheckSecretInput

# TODO update the JSON string below
json = "{}"
# create an instance of CheckSecretInput from a JSON string
check_secret_input_instance = CheckSecretInput.from_json(json)
# print the JSON string representation of the object
print(CheckSecretInput.to_json())

# convert the object into a dict
check_secret_input_dict = check_secret_input_instance.to_dict()
# create an instance of CheckSecretInput from a dict
check_secret_input_from_dict = CheckSecretInput.from_dict(check_secret_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


