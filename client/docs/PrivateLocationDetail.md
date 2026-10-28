# PrivateLocationDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Private location ID | [optional] 
**region_id** | **str** | Region ID to use in a check&#39;s regions to run it from this location | [optional] 
**name** | **str** |  | [optional] 
**country** | **str** | ISO 3166-1 alpha-2 country code | [optional] 
**check_types** | **List[str]** | Check types run from this location: api, dns, icmp, multistep, portscan, ssl, synthetic, tcp, web | [optional] 
**enabled** | **bool** |  | [optional] 
**status** | **str** | Connection status: online, offline or never_connected | [optional] 
**runners_online** | **int** | Number of runners currently online | [optional] 
**last_seen_at** | **datetime** | Last heartbeat from any runner in the last 24 hours | [optional] 
**created_at** | **datetime** |  | [optional] 
**runners** | [**List[PrivateLocationRunner]**](PrivateLocationRunner.md) | Runners seen in the last 24 hours | [optional] 
**tokens** | [**List[RunnerToken]**](RunnerToken.md) |  | [optional] 

## Example

```python
from pingera.models.private_location_detail import PrivateLocationDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateLocationDetail from a JSON string
private_location_detail_instance = PrivateLocationDetail.from_json(json)
# print the JSON string representation of the object
print(PrivateLocationDetail.to_json())

# convert the object into a dict
private_location_detail_dict = private_location_detail_instance.to_dict()
# create an instance of PrivateLocationDetail from a dict
private_location_detail_from_dict = PrivateLocationDetail.from_dict(private_location_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


