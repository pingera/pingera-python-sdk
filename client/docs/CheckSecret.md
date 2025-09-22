# CheckSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The timestamp when the association was created in ISO format. | [optional] [readonly] 
**secret** | [**Secret**](Secret.md) | The secret details (excluding the actual secret value). | [optional] [readonly] 
**secret_id** | **str** | The unique identifier of the secret. | 
**id** | **str** | The unique identifier for the check-secret association. | [optional] [readonly] 
**env_variable** | **str** | The environment variable name for this secret. Max 100 characters. | 

## Example

```python
from pingera.models.check_secret import CheckSecret

# TODO update the JSON string below
json = "{}"
# create an instance of CheckSecret from a JSON string
check_secret_instance = CheckSecret.from_json(json)
# print the JSON string representation of the object
print(CheckSecret.to_json())

# convert the object into a dict
check_secret_dict = check_secret_instance.to_dict()
# create an instance of CheckSecret from a dict
check_secret_from_dict = CheckSecret.from_dict(check_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


