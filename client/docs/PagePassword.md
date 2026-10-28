# PagePassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the page password | [optional] [readonly] 
**name** | **str** | Optional name/label for the password | [optional] 
**password** | **str** | The password (minimum 8 characters). Only used for input, never returned. | [optional] 
**password_hint** | **str** | Optional hint for the password | [optional] 
**active** | **bool** | Whether the password is active | [optional] 
**expires_at** | **datetime** | Optional expiration date for the password. Accepts ISO format, partial dates (YYYY-MM-DD), or flexible date strings | [optional] 
**created_at** | **datetime** | Timestamp when the password was created | [optional] [readonly] 
**updated_at** | **datetime** | Timestamp when the password was last updated | [optional] [readonly] 
**created_by** | **str** | ID of the user who created this password | [optional] [readonly] 
**is_expired** | **bool** | Whether the password is expired | [optional] [readonly] 

## Example

```python
from pingera.models.page_password import PagePassword

# TODO update the JSON string below
json = "{}"
# create an instance of PagePassword from a JSON string
page_password_instance = PagePassword.from_json(json)
# print the JSON string representation of the object
print(PagePassword.to_json())

# convert the object into a dict
page_password_dict = page_password_instance.to_dict()
# create an instance of PagePassword from a dict
page_password_from_dict = PagePassword.from_dict(page_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


