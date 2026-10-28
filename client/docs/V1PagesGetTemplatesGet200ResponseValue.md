# V1PagesGetTemplatesGet200ResponseValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Template ID | [optional] 
**name** | **str** | Template name | [optional] 
**preview_url** | **str** | URL of the template preview image | [optional] 

## Example

```python
from pingera.models.v1_pages_get_templates_get200_response_value import V1PagesGetTemplatesGet200ResponseValue

# TODO update the JSON string below
json = "{}"
# create an instance of V1PagesGetTemplatesGet200ResponseValue from a JSON string
v1_pages_get_templates_get200_response_value_instance = V1PagesGetTemplatesGet200ResponseValue.from_json(json)
# print the JSON string representation of the object
print(V1PagesGetTemplatesGet200ResponseValue.to_json())

# convert the object into a dict
v1_pages_get_templates_get200_response_value_dict = v1_pages_get_templates_get200_response_value_instance.to_dict()
# create an instance of V1PagesGetTemplatesGet200ResponseValue from a dict
v1_pages_get_templates_get200_response_value_from_dict = V1PagesGetTemplatesGet200ResponseValue.from_dict(v1_pages_get_templates_get200_response_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


