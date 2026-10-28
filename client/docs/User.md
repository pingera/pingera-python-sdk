# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the user account. | [optional] [readonly] 
**email** | **str** | The user&#39;s email address. Must be a valid email format and unique. | 
**password** | **str** | The user&#39;s password. Minimum 6 characters, required on registration. Only used for input, never returned. | [optional] 
**first_name** | **str** | The user&#39;s first name. Maximum 50 characters. | [optional] 
**last_name** | **str** | The user&#39;s last name. Maximum 50 characters. | [optional] 
**org_name** | **str** | Organization name for registration. Used when creating a new organization. Maximum 100 characters. | [optional] 
**role** | **str** | The user&#39;s role within the organization. | [optional] 
**organization_id** | **str** | The ID of the organization the user belongs to. | [optional] [readonly] 
**created_at** | **datetime** | The timestamp when the user account was created in ISO format. | [optional] [readonly] 
**is_first_login** | **bool** | Whether this is the user&#39;s first login to the system. | [optional] [readonly] 
**onboarding_completed** | **bool** | Whether the user has completed the onboarding process. | [optional] [readonly] 
**onboarding_completed_at** | **datetime** | The timestamp when onboarding was completed in ISO format. Null if not completed. | [optional] [readonly] 
**onboarding_step** | **str** | The current step in the onboarding process. Null if onboarding is completed. | [optional] [readonly] 
**email_verified** | **bool** | Whether the user&#39;s email address has been verified. | [optional] [readonly] 
**verification_token_expires** | **object** | The expiration time of the email verification token in ISO format. Null if already verified. | [optional] [readonly] 
**last_login** | **datetime** | The timestamp of the user&#39;s last login in ISO format. Null if never logged in. | [optional] [readonly] 

## Example

```python
from pingera.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


