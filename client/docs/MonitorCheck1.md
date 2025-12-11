# MonitorCheck1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets** | [**List[CheckSecretInput]**](CheckSecretInput.md) | Secrets to associate with this check during creation. Each secret must have secret_id and env_variable fields. | [optional] [default to []]
**parameters** | **Dict[str, object]** | Additional parameters specific to the check type. May include &#39;regions&#39; (list of region IDs) and &#39;multi_region_execution&#39; (configuration object). | [optional] 
**status** | **str** | The current status of the monitor check. | [optional] [readonly] 
**updated_at** | **datetime** | The timestamp when the monitor check was last updated in ISO format. | [optional] [readonly] 
**type** | **str** | The type of monitoring check to perform. | [optional] 
**created_at** | **datetime** | The timestamp when the monitor check was created in ISO format. | [optional] [readonly] 
**id** | **str** | The unique identifier for the monitor check. 12 chars, alpha-numeric. | [optional] [readonly] 
**group_id** | **str** | The ID of the group this check belongs to (optional). | [optional] 
**timeout** | **int** | The timeout for each check in seconds. Range: 1-30 seconds for most checks, up to 180 seconds for portscan checks. | [optional] 
**last_checked_at** | **datetime** | The timestamp when the check was last executed in ISO format. | [optional] [readonly] 
**host** | **str** | The hostname or IP address to monitor (required for TCP/SSL checks). Max 255 characters. | [optional] 
**group** | [**CheckGroup**](CheckGroup.md) | The group this check belongs to (if any). | [optional] [readonly] 
**port** | **int** | The port number to monitor (required for TCP checks). Range: 1-65535. | [optional] 
**position** | **int** | Position for ordering checks within groups or ungrouped (0 &#x3D; first). | [optional] 
**name** | **str** | A user-friendly name for the monitor check. Max 100 characters. | [optional] 
**uptime_data** | **List[Dict[str, object]]** | Uptime data breakdown by hour (only included when include_uptime&#x3D;true) | [optional] [readonly] 
**active** | **bool** | Whether the monitor check is active or paused. | [optional] 
**url** | **str** | The URL to monitor (required for web/api checks). Supports international domain names. | [optional] 
**interval** | **int** | The interval between checks in seconds. Range: 30 seconds to 24 hours. | [optional] 
**uptime_summary** | **Dict[str, object]** | Uptime summary statistics (only included when include_uptime&#x3D;true) | [optional] [readonly] 

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


