# EmailDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notifications_from_email** | **str** |  | [optional] 
**notifications_from_name** | **str** |  | [optional] 
**email_domain** | **str** |  | [optional] 
**email_domain_verified** | **bool** |  | [optional] 
**email_domain_status** | **str** | Verification status, e.g. pending or confirmed | [optional] 
**dns_records** | [**EmailDomainDnsRecords**](EmailDomainDnsRecords.md) |  | [optional] 

## Example

```python
from pingera.models.email_domain import EmailDomain

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDomain from a JSON string
email_domain_instance = EmailDomain.from_json(json)
# print the JSON string representation of the object
print(EmailDomain.to_json())

# convert the object into a dict
email_domain_dict = email_domain_instance.to_dict()
# create an instance of EmailDomain from a dict
email_domain_from_dict = EmailDomain.from_dict(email_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


