# SecretListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | The ID of the user who created the secret. | [optional] [readonly] 
**updated_by** | **str** | The ID of the user who last updated the secret. | [optional] [readonly] 
**secret_value** | **str** | The secret value - not included in list responses for security. | [optional] 
**created_at** | **datetime** | The timestamp when the secret was created in ISO format. | [optional] [readonly] 
**updated_at** | **datetime** | The timestamp when the secret was last updated in ISO format. | [optional] [readonly] 
**secret_name** | **str** | A unique name for the secret within the organization. Max 100 characters. | 
**id** | **str** | The unique identifier for the secret. | [optional] [readonly] 

## Example

```python
from pingera.models.secret_list_item import SecretListItem

# TODO update the JSON string below
json = "{}"
# create an instance of SecretListItem from a JSON string
secret_list_item_instance = SecretListItem.from_json(json)
# print the JSON string representation of the object
print(SecretListItem.to_json())

# convert the object into a dict
secret_list_item_dict = secret_list_item_instance.to_dict()
# create an instance of SecretListItem from a dict
secret_list_item_from_dict = SecretListItem.from_dict(secret_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


