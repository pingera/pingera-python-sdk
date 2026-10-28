# PrivateLocationRunner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Runner instance ID | [optional] 
**name** | **str** | Runner key reported by the runner | [optional] 
**version** | **str** | Runner version | [optional] 
**check_types** | **List[str]** | Check types the runner executes | [optional] 
**max_concurrency** | **int** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**online** | **bool** | Whether the runner sent a heartbeat in the last 2 minutes | [optional] 
**last_heartbeat_at** | **datetime** |  | [optional] 

## Example

```python
from pingera.models.private_location_runner import PrivateLocationRunner

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateLocationRunner from a JSON string
private_location_runner_instance = PrivateLocationRunner.from_json(json)
# print the JSON string representation of the object
print(PrivateLocationRunner.to_json())

# convert the object into a dict
private_location_runner_dict = private_location_runner_instance.to_dict()
# create an instance of PrivateLocationRunner from a dict
private_location_runner_from_dict = PrivateLocationRunner.from_dict(private_location_runner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


