# RunnerTokenCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Token ID | [optional] 
**name** | **str** | Token name | [optional] 
**token_prefix** | **str** | First characters of the token, for identification | [optional] 
**created_at** | **datetime** |  | [optional] 
**last_used_at** | **datetime** |  | [optional] 
**revoked_at** | **datetime** | Set when the token has been revoked | [optional] 
**token** | **str** | Token value. It is only returned once, store it securely. | [optional] 

## Example

```python
from pingera.models.runner_token_created import RunnerTokenCreated

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerTokenCreated from a JSON string
runner_token_created_instance = RunnerTokenCreated.from_json(json)
# print the JSON string representation of the object
print(RunnerTokenCreated.to_json())

# convert the object into a dict
runner_token_created_dict = runner_token_created_instance.to_dict()
# create an instance of RunnerTokenCreated from a dict
runner_token_created_from_dict = RunnerTokenCreated.from_dict(runner_token_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


