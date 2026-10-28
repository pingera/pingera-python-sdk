# Secret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the secret. | [optional] [readonly] 
**secret_name** | **str** | A unique name for the secret within the organization. Max 100 characters. | 
**created_at** | **datetime** | The timestamp when the secret was created in ISO format. | [optional] [readonly] 
**updated_at** | **datetime** | The timestamp when the secret was last updated in ISO format. | [optional] [readonly] 
**created_by** | **str** | The ID of the user who created the secret. | [optional] [readonly] 
**updated_by** | **str** | The ID of the user who last updated the secret. | [optional] [readonly] 

## Example

```python
from pingera.models.secret import Secret

# TODO update the JSON string below
json = "{}"
# create an instance of Secret from a JSON string
secret_instance = Secret.from_json(json)
# print the JSON string representation of the object
print(Secret.to_json())

# convert the object into a dict
secret_dict = secret_instance.to_dict()
# create an instance of Secret from a dict
secret_from_dict = Secret.from_dict(secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


