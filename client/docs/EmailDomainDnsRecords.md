# EmailDomainDnsRecords

DNS records to publish; null until the domain is registered

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification** | [**EmailDomainDnsRecord**](EmailDomainDnsRecord.md) | Domain ownership TXT record | [optional] 
**dkim** | [**EmailDomainDnsRecord**](EmailDomainDnsRecord.md) |  | [optional] 
**spf** | [**EmailDomainDnsRecord**](EmailDomainDnsRecord.md) |  | [optional] 
**dmarc** | [**EmailDomainDnsRecord**](EmailDomainDnsRecord.md) |  | [optional] 

## Example

```python
from pingera.models.email_domain_dns_records import EmailDomainDnsRecords

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDomainDnsRecords from a JSON string
email_domain_dns_records_instance = EmailDomainDnsRecords.from_json(json)
# print the JSON string representation of the object
print(EmailDomainDnsRecords.to_json())

# convert the object into a dict
email_domain_dns_records_dict = email_domain_dns_records_instance.to_dict()
# create an instance of EmailDomainDnsRecords from a dict
email_domain_dns_records_from_dict = EmailDomainDnsRecords.from_dict(email_domain_dns_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


