# Secret2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_value** | **str** | The secret value. This will be encrypted in storage but returned in API responses. | [optional] 
**created_at** | **datetime** | The timestamp when the secret was created in ISO format. | [optional] [readonly] 
**created_by** | **str** | The ID of the user who created the secret. | [optional] [readonly] 
**updated_by** | **str** | The ID of the user who last updated the secret. | [optional] [readonly] 
**updated_at** | **datetime** | The timestamp when the secret was last updated in ISO format. | [optional] [readonly] 
**id** | **str** | The unique identifier for the secret. | [optional] [readonly] 
**secret_name** | **str** | A unique name for the secret within the organization. Max 100 characters. | [optional] 

## Example

```python
from pingera.models.secret2 import Secret2

# TODO update the JSON string below
json = "{}"
# create an instance of Secret2 from a JSON string
secret2_instance = Secret2.from_json(json)
# print the JSON string representation of the object
print(Secret2.to_json())

# convert the object into a dict
secret2_dict = secret2_instance.to_dict()
# create an instance of Secret2 from a dict
secret2_from_dict = Secret2.from_dict(secret2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


