# Page


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**css_greens** | **str** | Green color used for operational status in HEX format | [optional] 
**id** | **str** | Unique identifier for the status page | [optional] [readonly] 
**allow_incident_subscribers** | **bool** | Whether to allow users to subscribe to incident updates | [optional] 
**country** | **str** | Country where your organization is located | [optional] 
**css_no_data** | **str** | Color used when no data is available in HEX format | [optional] 
**transactional_logo** | **str** | URL to the logo used in transactional emails | [optional] 
**ip_restrictions** | **str** | IP address restrictions for viewing the page | [optional] 
**allow_sms_subscribers** | **bool** | Whether to allow SMS subscriptions | [optional] 
**css_font_color** | **str** | Primary font color in HEX format | [optional] 
**css_border_color** | **str** | Border color for page elements in HEX format | [optional] 
**city** | **str** | City where your organization is located | [optional] 
**viewers_must_be_team_members** | **bool** | Whether only team members can view this page. In other words if page is public or not. | [optional] 
**yandex_metrica_id** | **str** | Yandex Metrica counter ID for analytics tracking | [optional] 
**time_zone** | **str** | Timezone for displaying dates and times on the status page | [optional] 
**css_graph_color** | **str** | Color used for graphs and charts in HEX format | [optional] 
**email_logo** | **str** | URL to the logo used in email notifications | [optional] 
**template** | **object** | Name of the template used for this page | [optional] [readonly] 
**css_spinner_color** | **str** | Loading spinner color in HEX format | [optional] 
**favicon_logo** | **str** | URL to the favicon image | [optional] 
**template_id** | **str** | ID of the template used for this page | [optional] 
**allow_webhook_subscribers** | **bool** | Whether to allow webhook subscriptions | [optional] 
**support_url** | **str** | URL to your support or contact page | [optional] 
**domain** | **str** | Custom domain for the status page | [optional] 
**css_reds** | **str** | Red color used for major outage status in HEX format | [optional] 
**css_oranges** | **str** | Orange color used for partial outage status in HEX format | [optional] 
**password_protected** | **bool** | Whether this page is protected by password(s). When true, users must enter a valid password to access the page. | [optional] 
**state** | **str** | State/region where your organization is located | [optional] 
**css_link_color** | **str** | Color for links in HEX format | [optional] 
**company_logo** | **str** | URL to the company logo | [optional] 
**notifications_from_email** | **str** | Email address used as sender for notifications | [optional] 
**css_button_border_color** | **str** | Button border color in HEX format | [optional] 
**subdomain** | **str** | Subdomain for accessing the status page (e.g., &#39;mycompany&#39; for mycompany.pingera.ru) | [optional] 
**language** | **str** | Language for the status page interface | [optional] 
**hidden_from_search** | **bool** | Whether to hide this page from search engines | [optional] 
**url** | **str** | Company URL - users will be redirected there when clicking on the logo | [optional] 
**allow_page_subscribers** | **bool** | Whether to allow users to subscribe to page updates | [optional] 
**created_at** | **datetime** | Timestamp when the page was created | [optional] [readonly] 
**headline** | **str** | Headline text displayed on the status page | [optional] 
**css_button_color** | **str** | Button background color in HEX format | [optional] 
**google_analytics_id** | **str** | Google Analytics measurement ID (e.g., G-XXXXXXXXXX or UA-XXXXXXXXX-X) | [optional] 
**css_light_font_color** | **str** | Light font color for secondary text in HEX format | [optional] 
**page_description** | **str** | Brief description of what this status page monitors | [optional] 
**css_button_hover_color** | **str** | Button color on hover in HEX format | [optional] 
**css_body_background_color** | **str** | Background color for the page body in HEX format | [optional] 
**css_button_text_color** | **str** | Button text color in HEX format | [optional] 
**hero_cover** | **str** | URL to the hero cover image | [optional] 
**organization_id** | **str** | ID of the organization this page belongs to | [optional] [readonly] 
**updated_at** | **datetime** | Timestamp when the page was last updated | [optional] [readonly] 
**name** | **str** | Display name of the status page | 
**allow_rss_atom_feeds** | **bool** | Whether to provide RSS/Atom feeds | [optional] 
**css_yellows** | **str** | Yellow color used for degraded status in HEX format | [optional] 
**css_blues** | **str** | Blue color used for maintenance status in HEX format | [optional] 
**activity_score** | **int** | Internal activity score for the page | [optional] 
**allow_email_subscribers** | **bool** | Whether to allow email subscriptions | [optional] 
**notifications_email_footer** | **str** | Footer text included in notification emails | [optional] 

## Example

```python
from pingera.models.page import Page

# TODO update the JSON string below
json = "{}"
# create an instance of Page from a JSON string
page_instance = Page.from_json(json)
# print the JSON string representation of the object
print(Page.to_json())

# convert the object into a dict
page_dict = page_instance.to_dict()
# create an instance of Page from a dict
page_from_dict = Page.from_dict(page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


