# CheckUptimeHour


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hour** | **datetime** | Start of the hour (UTC) | [optional] 
**status** | **str** | Aggregated check status for the hour | [optional] 
**uptime** | **float** | Uptime percentage for the hour | [optional] 

## Example

```python
from pingera.models.check_uptime_hour import CheckUptimeHour

# TODO update the JSON string below
json = "{}"
# create an instance of CheckUptimeHour from a JSON string
check_uptime_hour_instance = CheckUptimeHour.from_json(json)
# print the JSON string representation of the object
print(CheckUptimeHour.to_json())

# convert the object into a dict
check_uptime_hour_dict = check_uptime_hour_instance.to_dict()
# create an instance of CheckUptimeHour from a dict
check_uptime_hour_from_dict = CheckUptimeHour.from_dict(check_uptime_hour_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


