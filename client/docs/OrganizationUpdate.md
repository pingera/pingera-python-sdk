# OrganizationUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Organization name | [optional] 
**timezone** | **str** | Organization timezone for cron scheduling (IANA time zone name) | [optional] 
**invoice_email** | **str** | Email address for invoice delivery | [optional] 
**invoice_company_name** | **str** | Legal company name for invoices | [optional] 
**invoice_tax_id** | **str** | Tax ID / INN for invoice | [optional] 
**invoice_address** | **str** | Full legal address for invoices | [optional] 
**auto_renew** | **bool** | Automatically renew the subscription. Can only be enabled when the organization has a payment method. | [optional] 

## Example

```python
from pingera.models.organization_update import OrganizationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationUpdate from a JSON string
organization_update_instance = OrganizationUpdate.from_json(json)
# print the JSON string representation of the object
print(OrganizationUpdate.to_json())

# convert the object into a dict
organization_update_dict = organization_update_instance.to_dict()
# create an instance of OrganizationUpdate from a dict
organization_update_from_dict = OrganizationUpdate.from_dict(organization_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


