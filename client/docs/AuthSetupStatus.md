# AuthSetupStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_password** | **bool** | Whether user has a password set | [optional] [readonly] 
**passkey_count** | **int** | Number of registered passkeys | [optional] [readonly] 
**oauth_providers** | **List[str]** | Connected OAuth providers | [optional] [readonly] 
**two_factor_enabled** | **bool** | Whether 2FA is enabled | [optional] [readonly] 
**setup_complete** | **bool** | Whether authentication setup is complete | [optional] [readonly] 

## Example

```python
from pingera.models.auth_setup_status import AuthSetupStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AuthSetupStatus from a JSON string
auth_setup_status_instance = AuthSetupStatus.from_json(json)
# print the JSON string representation of the object
print(AuthSetupStatus.to_json())

# convert the object into a dict
auth_setup_status_dict = auth_setup_status_instance.to_dict()
# create an instance of AuthSetupStatus from a dict
auth_setup_status_from_dict = AuthSetupStatus.from_dict(auth_setup_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


