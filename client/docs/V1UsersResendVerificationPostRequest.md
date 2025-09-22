# V1UsersResendVerificationPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address to resend verification to | 

## Example

```python
from pingera.models.v1_users_resend_verification_post_request import V1UsersResendVerificationPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UsersResendVerificationPostRequest from a JSON string
v1_users_resend_verification_post_request_instance = V1UsersResendVerificationPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1UsersResendVerificationPostRequest.to_json())

# convert the object into a dict
v1_users_resend_verification_post_request_dict = v1_users_resend_verification_post_request_instance.to_dict()
# create an instance of V1UsersResendVerificationPostRequest from a dict
v1_users_resend_verification_post_request_from_dict = V1UsersResendVerificationPostRequest.from_dict(v1_users_resend_verification_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


