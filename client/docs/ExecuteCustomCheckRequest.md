# ExecuteCustomCheckRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** | The timeout for each check in seconds. Range: 1-30 seconds. | [optional] 
**name** | **str** | A user-friendly name for the custom check. Max 100 characters. | 
**url** | **str** | The URL to monitor (required for web/api checks). Supports international domain names. | [optional] 
**parameters** | **Dict[str, object]** | Additional parameters specific to the check type. For &#39;synthetic&#39; and &#39;multistep&#39; checks, must include &#39;pw_script&#39; with a valid Playwright script. | [optional] 
**secrets** | **List[Dict[str, str]]** | List of secrets to inject as environment variables during check execution. Each secret must have &#39;secret_id&#39; and &#39;env_variable&#39; keys. | [optional] [default to []]
**type** | **str** | The type of monitoring check to perform. | 
**host** | **str** | The hostname or IP address to monitor (required for TCP/SSL checks). Max 255 characters. | [optional] 
**port** | **int** | The port number to monitor (required for TCP and SSL checks). Range: 1-65535. | [optional] 

## Example

```python
from pingera.models.execute_custom_check_request import ExecuteCustomCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteCustomCheckRequest from a JSON string
execute_custom_check_request_instance = ExecuteCustomCheckRequest.from_json(json)
# print the JSON string representation of the object
print(ExecuteCustomCheckRequest.to_json())

# convert the object into a dict
execute_custom_check_request_dict = execute_custom_check_request_instance.to_dict()
# create an instance of ExecuteCustomCheckRequest from a dict
execute_custom_check_request_from_dict = ExecuteCustomCheckRequest.from_dict(execute_custom_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


