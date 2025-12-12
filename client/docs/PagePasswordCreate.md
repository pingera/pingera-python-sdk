# PagePasswordCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Optional name/label for the password | [optional] 
**password_hint** | **str** | Optional hint for the password | [optional] 
**expires_at** | **datetime** | Optional expiration date for the password. Accepts ISO format, partial dates (YYYY-MM-DD), or flexible date strings | [optional] 
**password** | **str** | The password (minimum 8 characters). Only used for input, never returned. | 

## Example

```python
from pingera.models.page_password_create import PagePasswordCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PagePasswordCreate from a JSON string
page_password_create_instance = PagePasswordCreate.from_json(json)
# print the JSON string representation of the object
print(PagePasswordCreate.to_json())

# convert the object into a dict
page_password_create_dict = page_password_create_instance.to_dict()
# create an instance of PagePasswordCreate from a dict
page_password_create_from_dict = PagePasswordCreate.from_dict(page_password_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


