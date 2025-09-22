# JobListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[CheckJob]**](CheckJob.md) | List of check jobs for the organization. | [optional] 
**pagination** | **Dict[str, object]** | Pagination information for the job results. | [optional] 

## Example

```python
from pingera.models.job_list_response import JobListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobListResponse from a JSON string
job_list_response_instance = JobListResponse.from_json(json)
# print the JSON string representation of the object
print(JobListResponse.to_json())

# convert the object into a dict
job_list_response_dict = job_list_response_instance.to_dict()
# create an instance of JobListResponse from a dict
job_list_response_from_dict = JobListResponse.from_dict(job_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


