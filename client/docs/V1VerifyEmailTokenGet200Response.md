# V1VerifyEmailTokenGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | JWT access token | [optional] 
**refresh_token** | **str** | JWT refresh token | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**message** | **str** | Success message | [optional] 

## Example

```python
from pingera.models.v1_verify_email_token_get200_response import V1VerifyEmailTokenGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1VerifyEmailTokenGet200Response from a JSON string
v1_verify_email_token_get200_response_instance = V1VerifyEmailTokenGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1VerifyEmailTokenGet200Response.to_json())

# convert the object into a dict
v1_verify_email_token_get200_response_dict = v1_verify_email_token_get200_response_instance.to_dict()
# create an instance of V1VerifyEmailTokenGet200Response from a dict
v1_verify_email_token_get200_response_from_dict = V1VerifyEmailTokenGet200Response.from_dict(v1_verify_email_token_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


