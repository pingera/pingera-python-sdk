# ComponentUptimeEvents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **List[str]** | List of incident IDs that affected this component during the period | [optional] [readonly] 

## Example

```python
from pingera.models.component_uptime_events import ComponentUptimeEvents

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentUptimeEvents from a JSON string
component_uptime_events_instance = ComponentUptimeEvents.from_json(json)
# print the JSON string representation of the object
print(ComponentUptimeEvents.to_json())

# convert the object into a dict
component_uptime_events_dict = component_uptime_events_instance.to_dict()
# create an instance of ComponentUptimeEvents from a dict
component_uptime_events_from_dict = ComponentUptimeEvents.from_dict(component_uptime_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


