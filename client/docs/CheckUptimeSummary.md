# CheckUptimeSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uptime** | **float** | Uptime percentage for the whole period | [optional] 
**avg_response_time** | **int** | Average response time in milliseconds | [optional] 
**checks** | **int** | Number of check executions in the period | [optional] 

## Example

```python
from pingera.models.check_uptime_summary import CheckUptimeSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CheckUptimeSummary from a JSON string
check_uptime_summary_instance = CheckUptimeSummary.from_json(json)
# print the JSON string representation of the object
print(CheckUptimeSummary.to_json())

# convert the object into a dict
check_uptime_summary_dict = check_uptime_summary_instance.to_dict()
# create an instance of CheckUptimeSummary from a dict
check_uptime_summary_from_dict = CheckUptimeSummary.from_dict(check_uptime_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


