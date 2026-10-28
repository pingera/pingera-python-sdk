# PagePasswordUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Optional name/label for the password | [optional] 
**password** | **str** | The password (minimum 8 characters). Only used for input, never returned. | [optional] 
**password_hint** | **str** | Optional hint for the password | [optional] 
**active** | **bool** | Whether the password is active | [optional] 
**expires_at** | **datetime** | Optional expiration date for the password. Accepts ISO format, partial dates (YYYY-MM-DD), or flexible date strings | [optional] 

## Example

```python
from pingera.models.page_password_update import PagePasswordUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PagePasswordUpdate from a JSON string
page_password_update_instance = PagePasswordUpdate.from_json(json)
# print the JSON string representation of the object
print(PagePasswordUpdate.to_json())

# convert the object into a dict
page_password_update_dict = page_password_update_instance.to_dict()
# create an instance of PagePasswordUpdate from a dict
page_password_update_from_dict = PagePasswordUpdate.from_dict(page_password_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


