# Changelog

All notable changes to `pingera-sdk` are documented here. The project follows
[Semantic Versioning](https://semver.org/).

## 1.2.0

Regenerated from the Pingera API after the backend made its OpenAPI spec match the API's real
responses (pingera/pingera-backend#96). Backward compatible with 1.1.0 except for the removal of the
unused `CheckSecretInput` model.

### Fixed

- Responses that 1.1.0 failed to parse with a `ValidationError`:
  - alert rules (`AlertRule.channel_ids` is now returned by the API),
  - alert notifications (`notification_type`, `status` and `channel_type` enums now match the API),
  - page passwords and users (`password` is no longer required in responses),
  - secrets viewed by non-editors (`Secret1.secret_value` is optional).
- Email domain responses no longer fail with `RecursionError`: `EmailDomainDnsRecords` is now a regular
  model with `verification`, `dkim`, `spf` and `dmarc` fields instead of a broken union wrapper.
- The update models `AlertRule1`, `AlertChannel1`, `MonitorCheck1` and `Component1` no longer have
  default values, so updates only send the fields you set instead of resetting others (for example a
  rule's `enabled`, `cooldown_period` and `auto_resolve`).
- `MonitorCheck.secrets` can be set when creating or updating a check.
- Fields the API can return as `null` are typed as optional, and `Error` matches the API's error body
  (`code` is a string or an int, `message` a string or an object).

### Added

- Query parameters: `show_deleted` and `show_groups` on `v1_pages_page_id_components_get`,
  `show_deleted` on `v1_pages_page_id_component_groups_get`, and `start`/`end` on component uptime
  (`v1_pages_page_id_components_component_id_uptime_get`, `v1_pages_page_id_components_uptime_post`).
- `apiKeyHeader` authentication: send the API token in the `X-API-KEY` header.

### Removed

- `CheckSecretInput`, which no operation used.

## 1.1.0

Regenerated from the current Pingera API with OpenAPI Generator 7.26.0.

### Added

- `PrivateLocationsApi`: manage private locations and runner tokens for self-hosted runners.
- `ReportsApi`: request and download PDF reports.
- `AuditApi`: read the organization audit trail.
- `AlertsApi.v1_alerts_channels_test_post` and `v1_alerts_channels_channel_id_test_post` to send test notifications.
- `StatusPagesApi` custom sender email domain endpoints (`v1_pages_page_id_email_domain_*`).
- `StatusPagesIncidentsApi.v1_pages_page_id_incidents_incident_id_incident_updates_incident_update_id_delete`.
- `OAuthApi.v1_auth_oauth_provider_name_link_complete_post`.
- New model fields, including cron scheduling on checks (`scheduling_type`, `cron_schedule`,
  `effective_interval`, `credit_throttled`), organization `timezone` and invoice details, page email
  domain settings, private region flags on `Region`, and components on incident update edits.
- Typed responses for endpoints that previously returned nothing useful: organization details,
  usage, check uptime, page templates, component/incident/maintenance statuses and bulk component uptime.
- Request bodies for `OrganizationsApi.v1_organizations_org_id_put`/`_patch` (`OrganizationUpdate`).

### Fixed

- Alert channels and notifications of type `sms` and `max` raised a `ValidationError`.
- The package no longer installs `pytest`, `pytest-cov`, `pytest-asyncio`, `setuptools` and `httpx`
  as runtime dependencies.
- `python -m build` works with build isolation.
- Requests now send a `pingera-sdk/<version>/python` user agent.

### Changed

- Python 3.10 or newer is required (Python 3.9 is end-of-life). Dependencies are now
  `urllib3>=2.7`, `pydantic>=2.11`.
- `OAuthApi.v1_auth_oauth_provider_name_callback_get` was replaced by
  `v1_auth_oauth_provider_name_callback_post`, matching the API. `OAuthProvider.authorization_url`
  was removed from the API.
- `OAuthApi.v1_auth_oauth_provider_name_authorize_get` accepts `code_challenge`, and
  `v1_auth_oauth_provider_name_link_post` takes an `OAuthAuthorizeRequest` body.
- Optional query parameters of `v1_checks_all_results_get`, `v1_checks_status_history_get` and
  `v1_checks_check_id_response_times_get` were reordered to match the API; pass them as keyword arguments.

## 1.0.15 and earlier

See the [git history](https://github.com/pingera/pingera-python-sdk/commits/main).
