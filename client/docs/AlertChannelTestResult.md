# AlertChannelTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True if the test notification was delivered to every recipient. | [optional] 
**error** | **str** | Delivery error reported by the channel provider, if any. | [optional] 
**results** | [**List[AlertChannelTestDelivery]**](AlertChannelTestDelivery.md) |  | [optional] 

## Example

```python
from pingera.models.alert_channel_test_result import AlertChannelTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of AlertChannelTestResult from a JSON string
alert_channel_test_result_instance = AlertChannelTestResult.from_json(json)
# print the JSON string representation of the object
print(AlertChannelTestResult.to_json())

# convert the object into a dict
alert_channel_test_result_dict = alert_channel_test_result_instance.to_dict()
# create an instance of AlertChannelTestResult from a dict
alert_channel_test_result_from_dict = AlertChannelTestResult.from_dict(alert_channel_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


