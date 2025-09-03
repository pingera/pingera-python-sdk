# MonitorCheck1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The timestamp when the monitor check was created in ISO format. | [optional] [readonly] 
**type** | **str** | The type of monitoring check to perform. | [optional] 
**last_checked_at** | **datetime** | The timestamp when the check was last executed in ISO format. | [optional] [readonly] 
**position** | **int** | Position for ordering checks within groups or ungrouped (0 &#x3D; first). | [optional] 
**port** | **int** | The port number to monitor (required for TCP checks). Range: 1-65535. | [optional] 
**status** | **str** | The current status of the monitor check. | [optional] [readonly] 
**group_id** | **str** | The ID of the group this check belongs to (optional). | [optional] 
**updated_at** | **datetime** | The timestamp when the monitor check was last updated in ISO format. | [optional] [readonly] 
**parameters** | **Dict[str, object]** | Additional parameters specific to the check type. For &#39;synthetic&#39; and &#39;multistep&#39; checks, must include &#39;pw_script&#39; with a valid Playwright script. | [optional] 
**url** | **str** | The URL to monitor (required for web/api checks). Supports international domain names. | [optional] 
**timeout** | **int** | The timeout for each check in seconds. Range: 1-30 seconds. | [optional] 
**host** | **str** | The hostname or IP address to monitor (required for TCP/SSL checks). Max 255 characters. | [optional] 
**group** | [**CheckGroup**](CheckGroup.md) | The group this check belongs to (if any). | [optional] [readonly] 
**id** | **str** | The unique identifier for the monitor check. 12 chars, alpha-numeric. | [optional] [readonly] 
**active** | **bool** | Whether the monitor check is active or paused. | [optional] 
**interval** | **int** | The interval between checks in seconds. Range: 30 seconds to 24 hours. | [optional] 
**name** | **str** | A user-friendly name for the monitor check. Max 100 characters. | [optional] 

## Example

```python
from pingera.models.monitor_check1 import MonitorCheck1

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorCheck1 from a JSON string
monitor_check1_instance = MonitorCheck1.from_json(json)
# print the JSON string representation of the object
print(MonitorCheck1.to_json())

# convert the object into a dict
monitor_check1_dict = monitor_check1_instance.to_dict()
# create an instance of MonitorCheck1 from a dict
monitor_check1_from_dict = MonitorCheck1.from_dict(monitor_check1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


