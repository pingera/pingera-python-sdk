# EnhancedLogin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User&#39;s email address | 
**method** | **str** | Authentication method to use | [optional] [default to 'password']
**password** | **str** | Password (required when method is &#39;password&#39;) | [optional] 

## Example

```python
from pingera.models.enhanced_login import EnhancedLogin

# TODO update the JSON string below
json = "{}"
# create an instance of EnhancedLogin from a JSON string
enhanced_login_instance = EnhancedLogin.from_json(json)
# print the JSON string representation of the object
print(EnhancedLogin.to_json())

# convert the object into a dict
enhanced_login_dict = enhanced_login_instance.to_dict()
# create an instance of EnhancedLogin from a dict
enhanced_login_from_dict = EnhancedLogin.from_dict(enhanced_login_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


