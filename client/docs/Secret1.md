# Secret1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | The ID of the user who created the secret. | [optional] [readonly] 
**id** | **str** | The unique identifier for the secret. | [optional] [readonly] 
**updated_at** | **datetime** | The timestamp when the secret was last updated in ISO format. | [optional] [readonly] 
**secret_name** | **str** | A unique name for the secret within the organization. Max 100 characters. | 
**created_at** | **datetime** | The timestamp when the secret was created in ISO format. | [optional] [readonly] 
**updated_by** | **str** | The ID of the user who last updated the secret. | [optional] [readonly] 
**secret_value** | **str** | The secret value. This will be encrypted in storage but returned in API responses. | 

## Example

```python
from pingera.models.secret1 import Secret1

# TODO update the JSON string below
json = "{}"
# create an instance of Secret1 from a JSON string
secret1_instance = Secret1.from_json(json)
# print the JSON string representation of the object
print(Secret1.to_json())

# convert the object into a dict
secret1_dict = secret1_instance.to_dict()
# create an instance of Secret1 from a dict
secret1_from_dict = Secret1.from_dict(secret1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


