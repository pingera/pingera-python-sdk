# EmailDomainDnsRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DNS record type | [optional] 
**name** | **str** | DNS record name | [optional] 
**value** | **str** | DNS record value | [optional] 

## Example

```python
from pingera.models.email_domain_dns_record import EmailDomainDnsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDomainDnsRecord from a JSON string
email_domain_dns_record_instance = EmailDomainDnsRecord.from_json(json)
# print the JSON string representation of the object
print(EmailDomainDnsRecord.to_json())

# convert the object into a dict
email_domain_dns_record_dict = email_domain_dns_record_instance.to_dict()
# create an instance of EmailDomainDnsRecord from a dict
email_domain_dns_record_from_dict = EmailDomainDnsRecord.from_dict(email_domain_dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


