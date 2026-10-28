# AlertChannelTestDelivery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient** | **str** | Recipient the test was sent to (email, URL or chat id). | [optional] 
**success** | **bool** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from pingera.models.alert_channel_test_delivery import AlertChannelTestDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of AlertChannelTestDelivery from a JSON string
alert_channel_test_delivery_instance = AlertChannelTestDelivery.from_json(json)
# print the JSON string representation of the object
print(AlertChannelTestDelivery.to_json())

# convert the object into a dict
alert_channel_test_delivery_dict = alert_channel_test_delivery_instance.to_dict()
# create an instance of AlertChannelTestDelivery from a dict
alert_channel_test_delivery_from_dict = AlertChannelTestDelivery.from_dict(alert_channel_test_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


