# AlertStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_channels** | **int** | Total number of enabled alert channels. | [optional] [readonly] 
**severity_breakdown** | **Dict[str, object]** | Count of alerts by severity level in the last 30 days. | [optional] [readonly] 
**total_rules** | **int** | Total number of enabled alert rules. | [optional] [readonly] 
**active_alerts** | **int** | Number of currently active alerts (firing or acknowledged). | [optional] [readonly] 
**recent_alerts** | **int** | Number of alerts fired in the last 30 days. | [optional] [readonly] 

## Example

```python
from pingera.models.alert_stats import AlertStats

# TODO update the JSON string below
json = "{}"
# create an instance of AlertStats from a JSON string
alert_stats_instance = AlertStats.from_json(json)
# print the JSON string representation of the object
print(AlertStats.to_json())

# convert the object into a dict
alert_stats_dict = alert_stats_instance.to_dict()
# create an instance of AlertStats from a dict
alert_stats_from_dict = AlertStats.from_dict(alert_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


