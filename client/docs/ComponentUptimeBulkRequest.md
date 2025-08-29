# ComponentUptimeBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_ids** | **List[str]** | List of component IDs to calculate uptime for | 

## Example

```python
from pingera.models.component_uptime_bulk_request import ComponentUptimeBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentUptimeBulkRequest from a JSON string
component_uptime_bulk_request_instance = ComponentUptimeBulkRequest.from_json(json)
# print the JSON string representation of the object
print(ComponentUptimeBulkRequest.to_json())

# convert the object into a dict
component_uptime_bulk_request_dict = component_uptime_bulk_request_instance.to_dict()
# create an instance of ComponentUptimeBulkRequest from a dict
component_uptime_bulk_request_from_dict = ComponentUptimeBulkRequest.from_dict(component_uptime_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


