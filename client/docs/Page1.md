# Page1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_rss_atom_feeds** | **bool** | Whether to provide RSS/Atom feeds | [optional] 
**created_at** | **datetime** | Timestamp when the page was created | [optional] [readonly] 
**css_graph_color** | **str** | Color used for graphs and charts in HEX format | [optional] 
**support_url** | **str** | URL to your support or contact page | [optional] 
**country** | **str** | Country where your organization is located | [optional] 
**allow_page_subscribers** | **bool** | Whether to allow users to subscribe to page updates | [optional] 
**css_button_text_color** | **str** | Button text color in HEX format | [optional] 
**state** | **str** | State/region where your organization is located | [optional] 
**css_button_hover_color** | **str** | Button color on hover in HEX format | [optional] 
**time_zone** | **str** | Timezone for displaying dates and times on the status page | [optional] 
**organization_id** | **str** | ID of the organization this page belongs to | [optional] [readonly] 
**css_greens** | **str** | Green color used for operational status in HEX format | [optional] 
**ip_restrictions** | **str** | IP address restrictions for viewing the page | [optional] 
**name** | **str** | Display name of the status page | [optional] 
**allow_email_subscribers** | **bool** | Whether to allow email subscriptions | [optional] 
**css_oranges** | **str** | Orange color used for partial outage status in HEX format | [optional] 
**template_id** | **str** | ID of the template used for this page | [optional] 
**css_border_color** | **str** | Border color for page elements in HEX format | [optional] 
**hero_cover** | **str** | URL to the hero cover image | [optional] 
**allow_webhook_subscribers** | **bool** | Whether to allow webhook subscriptions | [optional] 
**hidden_from_search** | **bool** | Whether to hide this page from search engines | [optional] 
**notifications_from_email** | **str** | Email address used as sender for notifications | [optional] 
**template** | **object** | Name of the template used for this page | [optional] [readonly] 
**transactional_logo** | **str** | URL to the logo used in transactional emails | [optional] 
**css_blues** | **str** | Blue color used for maintenance status in HEX format | [optional] 
**company_logo** | **str** | URL to the company logo | [optional] 
**url** | **str** | Company URL - users will be redirected there when clicking on the logo | [optional] 
**language** | **str** | Language for the status page interface | [optional] 
**email_logo** | **str** | URL to the logo used in email notifications | [optional] 
**viewers_must_be_team_members** | **bool** | Whether only team members can view this page. In other words if page is public or not. | [optional] 
**css_button_color** | **str** | Button background color in HEX format | [optional] 
**css_body_background_color** | **str** | Background color for the page body in HEX format | [optional] 
**css_font_color** | **str** | Primary font color in HEX format | [optional] 
**subdomain** | **str** | Subdomain for accessing the status page (e.g., &#39;mycompany&#39; for mycompany.pingera.ru) | [optional] 
**domain** | **str** | Custom domain for the status page | [optional] 
**activity_score** | **int** | Internal activity score for the page | [optional] 
**css_yellows** | **str** | Yellow color used for degraded status in HEX format | [optional] 
**css_reds** | **str** | Red color used for major outage status in HEX format | [optional] 
**css_link_color** | **str** | Color for links in HEX format | [optional] 
**css_no_data** | **str** | Color used when no data is available in HEX format | [optional] 
**css_spinner_color** | **str** | Loading spinner color in HEX format | [optional] 
**css_light_font_color** | **str** | Light font color for secondary text in HEX format | [optional] 
**updated_at** | **datetime** | Timestamp when the page was last updated | [optional] [readonly] 
**allow_sms_subscribers** | **bool** | Whether to allow SMS subscriptions | [optional] 
**css_button_border_color** | **str** | Button border color in HEX format | [optional] 
**notifications_email_footer** | **str** | Footer text included in notification emails | [optional] 
**page_description** | **str** | Brief description of what this status page monitors | [optional] 
**city** | **str** | City where your organization is located | [optional] 
**headline** | **str** | Headline text displayed on the status page | [optional] 
**id** | **str** | Unique identifier for the status page | [optional] [readonly] 
**allow_incident_subscribers** | **bool** | Whether to allow users to subscribe to incident updates | [optional] 
**favicon_logo** | **str** | URL to the favicon image | [optional] 

## Example

```python
from pingera.models.page1 import Page1

# TODO update the JSON string below
json = "{}"
# create an instance of Page1 from a JSON string
page1_instance = Page1.from_json(json)
# print the JSON string representation of the object
print(Page1.to_json())

# convert the object into a dict
page1_dict = page1_instance.to_dict()
# create an instance of Page1 from a dict
page1_from_dict = Page1.from_dict(page1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


