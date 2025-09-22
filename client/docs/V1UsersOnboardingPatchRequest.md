# V1UsersOnboardingPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**onboarding_completed** | **bool** | Mark onboarding as completed | [optional] 
**onboarding_step** | **str** | Current onboarding step | [optional] 

## Example

```python
from pingera.models.v1_users_onboarding_patch_request import V1UsersOnboardingPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UsersOnboardingPatchRequest from a JSON string
v1_users_onboarding_patch_request_instance = V1UsersOnboardingPatchRequest.from_json(json)
# print the JSON string representation of the object
print(V1UsersOnboardingPatchRequest.to_json())

# convert the object into a dict
v1_users_onboarding_patch_request_dict = v1_users_onboarding_patch_request_instance.to_dict()
# create an instance of V1UsersOnboardingPatchRequest from a dict
v1_users_onboarding_patch_request_from_dict = V1UsersOnboardingPatchRequest.from_dict(v1_users_onboarding_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


