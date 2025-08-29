# MonitorCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The current status of the monitor check. | [optional] [readonly] 
**parameters** | **Dict[str, object]** | Additional parameters specific to the check type. For &#39;synthetic&#39; and &#39;multistep&#39; checks, must include &#39;pw_script&#39; with a valid Playwright script. | [optional] 
**updated_at** | **datetime** | The timestamp when the monitor check was last updated in ISO format. | [optional] [readonly] 
**port** | **int** | The port number to monitor (required for TCP checks). Range: 1-65535. | [optional] 
**id** | **str** | The unique identifier for the monitor check. 12 chars, alpha-numeric. | [optional] [readonly] 
**type** | **str** | The type of monitoring check to perform. | 
**timeout** | **int** | The timeout for each check in seconds. Range: 1-30 seconds. | [optional] 
**name** | **str** | A user-friendly name for the monitor check. Max 100 characters. | 
**host** | **str** | The hostname or IP address to monitor (required for TCP/SSL checks). Max 255 characters. | [optional] 
**interval** | **int** | The interval between checks in seconds. Range: 30 seconds to 24 hours. | [optional] 
**last_checked_at** | **datetime** | The timestamp when the check was last executed in ISO format. | [optional] [readonly] 
**created_at** | **datetime** | The timestamp when the monitor check was created in ISO format. | [optional] [readonly] 
**url** | **str** | The URL to monitor (required for web/api checks). | [optional] 
**active** | **bool** | Whether the monitor check is active or paused. | [optional] 

## Example

```python
from pingera.models.monitor_check import MonitorCheck

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorCheck from a JSON string
monitor_check_instance = MonitorCheck.from_json(json)
# print the JSON string representation of the object
print(MonitorCheck.to_json())

# convert the object into a dict
monitor_check_dict = monitor_check_instance.to_dict()
# create an instance of MonitorCheck from a dict
monitor_check_from_dict = MonitorCheck.from_dict(monitor_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


