# CheckJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Error message if the job execution failed. | [optional] [readonly] 
**completed_at** | **datetime** | The timestamp when the check job completed execution in ISO format. | [optional] [readonly] 
**status** | **str** | The current status of the check job execution. | [optional] [readonly] 
**check_id** | **str** | The identifier of the monitor check this job belongs to. | [optional] [readonly] 
**id** | **str** | The unique identifier for the check job. | [optional] [readonly] 
**check_parameters** | **Dict[str, object]** | The parameters used for executing this check job. | [optional] [readonly] 
**result** | **object** | The result data from the completed check job, including server information. | [optional] [readonly] 
**started_at** | **datetime** | The timestamp when the check job started execution in ISO format. | [optional] [readonly] 
**job_type** | **object** | The type of check job being executed. | [optional] [readonly] 
**created_at** | **datetime** | The timestamp when the check job was created in ISO format. | [optional] [readonly] 

## Example

```python
from pingera.models.check_job import CheckJob

# TODO update the JSON string below
json = "{}"
# create an instance of CheckJob from a JSON string
check_job_instance = CheckJob.from_json(json)
# print the JSON string representation of the object
print(CheckJob.to_json())

# convert the object into a dict
check_job_dict = check_job_instance.to_dict()
# create an instance of CheckJob from a dict
check_job_from_dict = CheckJob.from_dict(check_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


