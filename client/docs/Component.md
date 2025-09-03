# Component


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp when the component was created | [optional] [readonly] 
**page_id** | **str** | ID of the status page this component belongs to | [optional] [readonly] 
**only_show_if_degraded** | **bool** | Whether to show this component only when it&#39;s not operational | [optional] 
**start_date** | **datetime** | Date when monitoring for this component started | [optional] 
**position** | **int** | Display order position of the component on the status page | [optional] 
**status** | **str** | Current operational status of the component | [optional] 
**group_id** | **str** | ID of the group this component belongs to (if any) | [optional] 
**showcase** | **bool** | Whether to prominently display this component on the status page | [optional] 
**updated_at** | **datetime** | Timestamp when the component was last updated | [optional] [readonly] 
**group** | **bool** | Whether this component is a group container for other components | [optional] [default to False]
**description** | **str** | Detailed description of the component | [optional] 
**id** | **str** | Unique identifier for the component | [optional] [readonly] 
**name** | **str** | Display name of the component | 

## Example

```python
from pingera.models.component import Component

# TODO update the JSON string below
json = "{}"
# create an instance of Component from a JSON string
component_instance = Component.from_json(json)
# print the JSON string representation of the object
print(Component.to_json())

# convert the object into a dict
component_dict = component_instance.to_dict()
# create an instance of Component from a dict
component_from_dict = Component.from_dict(component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


