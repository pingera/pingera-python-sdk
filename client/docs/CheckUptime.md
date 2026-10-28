# CheckUptime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uptime_data** | [**List[CheckUptimeHour]**](CheckUptimeHour.md) |  | [optional] 
**summary** | [**CheckUptimeSummary**](CheckUptimeSummary.md) |  | [optional] 

## Example

```python
from pingera.models.check_uptime import CheckUptime

# TODO update the JSON string below
json = "{}"
# create an instance of CheckUptime from a JSON string
check_uptime_instance = CheckUptime.from_json(json)
# print the JSON string representation of the object
print(CheckUptime.to_json())

# convert the object into a dict
check_uptime_dict = check_uptime_instance.to_dict()
# create an instance of CheckUptime from a dict
check_uptime_from_dict = CheckUptime.from_dict(check_uptime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


