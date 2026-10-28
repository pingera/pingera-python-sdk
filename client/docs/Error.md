# Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** | Machine-readable error code (e.g. &#39;validation_error&#39;, &#39;resource_not_found&#39;), or the HTTP status code for generic errors. | [optional] 
**message** | **object** | Human-readable message. For validation errors this is an object with per-field messages, e.g. {\&quot;fields\&quot;: {\&quot;name\&quot;: [\&quot;Missing data\&quot;]}}. | [optional] 
**status** | **str** | HTTP reason phrase (generic errors only). | [optional] 
**errors** | **Dict[str, object]** | Additional error details (generic errors only). | [optional] 

## Example

```python
from pingera.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


