# RunnerToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Token ID | [optional] 
**name** | **str** | Token name | [optional] 
**token_prefix** | **str** | First characters of the token, for identification | [optional] 
**created_at** | **datetime** |  | [optional] 
**last_used_at** | **datetime** |  | [optional] 
**revoked_at** | **datetime** | Set when the token has been revoked | [optional] 

## Example

```python
from pingera.models.runner_token import RunnerToken

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerToken from a JSON string
runner_token_instance = RunnerToken.from_json(json)
# print the JSON string representation of the object
print(RunnerToken.to_json())

# convert the object into a dict
runner_token_dict = runner_token_instance.to_dict()
# create an instance of RunnerToken from a dict
runner_token_from_dict = RunnerToken.from_dict(runner_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


