# LinkedOAuthAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**OAuthProvider**](OAuthProvider.md) |  | [optional] [readonly] 
**created_at** | **datetime** | When the OAuth account was linked | [optional] [readonly] 
**id** | **str** | OAuth account link ID | [optional] [readonly] 
**provider_avatar_url** | **str** | Avatar URL from OAuth provider | [optional] [readonly] 
**provider_email** | **str** | Email address from OAuth provider | [optional] [readonly] 
**provider_name** | **str** | Display name from OAuth provider | [optional] [readonly] 
**last_used_at** | **datetime** | When this OAuth account was last used for login | [optional] [readonly] 

## Example

```python
from pingera.models.linked_o_auth_account import LinkedOAuthAccount

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedOAuthAccount from a JSON string
linked_o_auth_account_instance = LinkedOAuthAccount.from_json(json)
# print the JSON string representation of the object
print(LinkedOAuthAccount.to_json())

# convert the object into a dict
linked_o_auth_account_dict = linked_o_auth_account_instance.to_dict()
# create an instance of LinkedOAuthAccount from a dict
linked_o_auth_account_from_dict = LinkedOAuthAccount.from_dict(linked_o_auth_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


