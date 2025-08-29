# ExecuteExistingCheckResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Human-readable message about the operation result. | 
**job_id** | **str** | The unique identifier for the queued check job. | 
**status** | **str** | The current status of the check job. | 

## Example

```python
from pingera.models.execute_existing_check_response import ExecuteExistingCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteExistingCheckResponse from a JSON string
execute_existing_check_response_instance = ExecuteExistingCheckResponse.from_json(json)
# print the JSON string representation of the object
print(ExecuteExistingCheckResponse.to_json())

# convert the object into a dict
execute_existing_check_response_dict = execute_existing_check_response_instance.to_dict()
# create an instance of ExecuteExistingCheckResponse from a dict
execute_existing_check_response_from_dict = ExecuteExistingCheckResponse.from_dict(execute_existing_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


