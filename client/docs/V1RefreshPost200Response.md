# V1RefreshPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | New JWT access token | [optional] 
**refresh_token** | **str** | New JWT refresh token | [optional] 

## Example

```python
from pingera.models.v1_refresh_post200_response import V1RefreshPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1RefreshPost200Response from a JSON string
v1_refresh_post200_response_instance = V1RefreshPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1RefreshPost200Response.to_json())

# convert the object into a dict
v1_refresh_post200_response_dict = v1_refresh_post200_response_instance.to_dict()
# create an instance of V1RefreshPost200Response from a dict
v1_refresh_post200_response_from_dict = V1RefreshPost200Response.from_dict(v1_refresh_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


