# LoginOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address to check authentication options for | 

## Example

```python
from pingera.models.login_options import LoginOptions

# TODO update the JSON string below
json = "{}"
# create an instance of LoginOptions from a JSON string
login_options_instance = LoginOptions.from_json(json)
# print the JSON string representation of the object
print(LoginOptions.to_json())

# convert the object into a dict
login_options_dict = login_options_instance.to_dict()
# create an instance of LoginOptions from a dict
login_options_from_dict = LoginOptions.from_dict(login_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


