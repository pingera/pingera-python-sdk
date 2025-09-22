# LinkedOAuthAccountsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[LinkedOAuthAccount]**](LinkedOAuthAccount.md) | List of linked OAuth accounts | [optional] [readonly] 

## Example

```python
from pingera.models.linked_o_auth_accounts_response import LinkedOAuthAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedOAuthAccountsResponse from a JSON string
linked_o_auth_accounts_response_instance = LinkedOAuthAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(LinkedOAuthAccountsResponse.to_json())

# convert the object into a dict
linked_o_auth_accounts_response_dict = linked_o_auth_accounts_response_instance.to_dict()
# create an instance of LinkedOAuthAccountsResponse from a dict
linked_o_auth_accounts_response_from_dict = LinkedOAuthAccountsResponse.from_dict(linked_o_auth_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


