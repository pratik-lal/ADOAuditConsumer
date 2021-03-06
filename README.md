# Azure DevOps Audit Events Consumer (ADOAuditConsumer)
An application to query/download audit events from Azure DevOps audit service

## Application Components
- **adoauditconsumer.exe**: main application - Windows executable
- **adoaudit.config**: ADOAuditConsumer configuration file. This is place to configure the application
- **last_processed_time**: file that tracks last query time to Azure DevOps audit service
- **output**: Directory wherein, output files containing audit events are saved
- **logs**: Directory contains application logs (INFO, WARN, ERROR). Max log filesize is 1 MB and 10 log files would be kept as backup. Refer [logger.py](https://github.com/pratik-lal/ADOAuditConsumer/blob/master/logger.py)
- **tmp**: Directory to analyze output received from  Azure DevOps audit service

## Application: ADOAuditConsumer Use Cases
- Security Monitoring & Analytics
- Collect Audit events for compliance

## Pre-requisites
- It is recommended to set the host's timezone in UTC
- PAT (personal access token) with read-only privilege from Azure DevOps instance to query audit events
- [Microsoft Docs - How to create PAT](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=preview-page)

## Install Azure DevOps Audit Events Consumer (ADOAuditConsumer)
- [Download ADOAuditConsumer Windows Executable](https://github.com/pratik-lal/ADOAuditConsumer/releases/download/v1.0beta/ADOAuditConsumer.zip)
- Configuation file: adoaudit.config requires three parameters
  - **organization_url** - e.g. https://auditservice.dev.azure.com/enter_you_org_name
  - **personal_access_token**
  - **execution_frequency** - Frequency (schedule) (in seconds) to query Azure DevOps instance. Change the frequency as per your need. Default is 600 seconds (10 minutes)
  
- Intsall as Windows Service:
  - Open cmd.exe with Administrator privilege
  - Navigate to ADOAuditConsumer\nssm-2.24\win64 directory
  - Execute command *nssm install service_name*. Replace service_name with name of your service
  - In NSSM gui window, navigate to ADOAuditConsumer\adoauditconsumer.exe
  - Click Install service
  - Open Windows Service (services.msc) and start ADOAuditConsumer service

## Download
- [ADOAuditConsumer v1.0beta - Windows Executable](https://github.com/pratik-lal/ADOAuditConsumer/releases)
- File: ADOAuditConsumer.zip

  
