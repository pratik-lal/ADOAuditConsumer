# Azure DevOps Audit Events Consumer (ADOAuditConsumer)
An application to consume audit events from Azure DevOps audit service.

## Application: ADOAuditConsumer Use cases
- Security Monitoring & Analytics
- Collect Audit events for compliance

## Pre-requisites
- It is recommended to set the host's timezone in UTC.
- PAT (personal access token) with read-only privilege from Azure DevOps instance to query audit events.
- [Microsoft DOCS - How to create PAT](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=preview-page)

## Install Azure DevOps Audit Events Consumer (ADOAuditConsumer)
- Download ADOAuditConsumer release
- Configuation file: adoaudit.config required three parameters
  1. organization_url - e.g. https://auditservice.dev.azure.com/enter_you_org_name
  2. personal_access_token -  some random hexadeciman characters
  3. execution_frequency - Frequency (schedule) (in seconds) to query Azure DevOps instance. Change the frequency as oer your need. Default is 600 seconds (10 minutes)
