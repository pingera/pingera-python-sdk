# ComponentUptime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Component ID | [optional] [readonly] 
**name** | **str** | Component name | [optional] [readonly] 
**range_start** | **str** | Start date of the uptime calculation period (YYYY-MM-DD) | [optional] [readonly] 
**range_end** | **str** | End date of the uptime calculation period (YYYY-MM-DD) | [optional] [readonly] 
**uptime_percentage** | **float** | Uptime percentage for the specified period | [optional] [readonly] 
**major_outage** | **int** | Total seconds of major outages during the period | [optional] [readonly] 
**partial_outage** | **int** | Total seconds of partial outages during the period | [optional] [readonly] 
**warnings** | **List[str]** | List of warnings about the calculation | [optional] [readonly] 
**related_events** | [**ComponentUptimeEvents**](ComponentUptimeEvents.md) | Events that affected this component during the period | [optional] [readonly] 

## Example

```python
from pingera.models.component_uptime import ComponentUptime

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentUptime from a JSON string
component_uptime_instance = ComponentUptime.from_json(json)
# print the JSON string representation of the object
print(ComponentUptime.to_json())

# convert the object into a dict
component_uptime_dict = component_uptime_instance.to_dict()
# create an instance of ComponentUptime from a dict
component_uptime_from_dict = ComponentUptime.from_dict(component_uptime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


