# APIToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_used_at** | **datetime** | The timestamp when the API token was last used in ISO format. Null if never used. | [optional] [readonly] 
**token** | **str** | The actual API token string. Only returned when creating a new token. | [optional] [readonly] 
**name** | **str** | A descriptive name for the API token. Maximum 100 characters. | 
**created_at** | **datetime** | The timestamp when the API token was created in ISO format. | [optional] [readonly] 
**id** | **str** | The unique identifier for the API token. | [optional] [readonly] 

## Example

```python
from pingera.models.api_token import APIToken

# TODO update the JSON string below
json = "{}"
# create an instance of APIToken from a JSON string
api_token_instance = APIToken.from_json(json)
# print the JSON string representation of the object
print(APIToken.to_json())

# convert the object into a dict
api_token_dict = api_token_instance.to_dict()
# create an instance of APIToken from a dict
api_token_from_dict = APIToken.from_dict(api_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


