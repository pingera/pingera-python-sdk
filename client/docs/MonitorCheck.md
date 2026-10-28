# MonitorCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the monitor check. 12 chars, alpha-numeric. | [optional] [readonly] 
**name** | **str** | A user-friendly name for the monitor check. Max 100 characters. | 
**type** | **str** | The type of monitoring check to perform. | 
**url** | **str** | The URL to monitor (required for web/api checks). Supports international domain names. | [optional] 
**host** | **str** | The hostname or IP address to monitor (required for TCP/SSL checks). Max 255 characters. | [optional] 
**port** | **int** | The port number to monitor (required for TCP checks). Range: 1-65535. | [optional] 
**interval** | **int** | The interval between checks in seconds. Range: 30 seconds to 24 hours. Required when scheduling_type is &#39;interval&#39;. | [optional] 
**scheduling_type** | **str** | The scheduling type for this check. &#39;interval&#39; uses fixed intervals, &#39;cron&#39; uses cron expressions. | [optional] [default to 'interval']
**cron_schedule** | **str** | Cron expression for scheduling (required when scheduling_type is &#39;cron&#39;). Uses standard cron format. | [optional] 
**timeout** | **int** | The timeout for each check in seconds. Range: 1-30 seconds for most checks, up to 120 seconds for synthetic checks (the whole run, including browser start) and up to 180 seconds for portscan and multistep checks. | [optional] 
**parameters** | **Dict[str, object]** | Additional parameters specific to the check type. May include &#39;regions&#39; (list of region IDs) and &#39;multi_region_execution&#39; (configuration object). | [optional] 
**active** | **bool** | Whether the monitor check is active or paused. | [optional] 
**group_id** | **str** | The ID of the group this check belongs to (optional). | [optional] 
**group** | [**CheckGroup**](CheckGroup.md) | The group this check belongs to (if any). | [optional] [readonly] 
**position** | **int** | Position for ordering checks within groups or ungrouped (0 &#x3D; first). | [optional] 
**status** | **str** | The current status of the monitor check. | [optional] [readonly] 
**credit_throttled** | **object** | True when the organization is out of credits and the check runs at a reduced frequency until credits reset or the plan is upgraded. | [optional] [readonly] 
**effective_interval** | **object** | The interval in seconds the check actually runs at. Equals &#39;interval&#39; unless the check is credit-throttled. | [optional] [readonly] 
**last_checked_at** | **datetime** | The timestamp when the check was last executed in ISO format. | [optional] [readonly] 
**created_at** | **datetime** | The timestamp when the monitor check was created in ISO format. | [optional] [readonly] 
**updated_at** | **datetime** | The timestamp when the monitor check was last updated in ISO format. | [optional] [readonly] 
**secrets** | [**List[CheckSecret]**](CheckSecret.md) | Secrets injected into the check as environment variables. On create/update, each item needs secret_id and env_variable. | [optional] [default to []]
**uptime_data** | **List[Dict[str, object]]** | Uptime data breakdown by hour (only included when include_uptime&#x3D;true) | [optional] [readonly] 
**uptime_summary** | **Dict[str, object]** | Uptime summary statistics (only included when include_uptime&#x3D;true) | [optional] [readonly] 

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


