from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from datetime import datetime
import time
import os
import shutil
import configparser
import logger


class ADOClient:
    # initializing configparser
    config = configparser.ConfigParser()
    try:
        config.read(".\\adoaudit.config")
        logger.AppLogging.auditlogger.info("Reading configuration file adoaudit.config")
        personal_access_token = config.get("ADO_options", "personal_access_token")
        organization_url = config.get("ADO_options", "organization_url")
        logger.AppLogging.auditlogger.info("Successfully retrieved PAT & Organization URL " + organization_url)
    except configparser.NoOptionError as ex:
        logger.AppLogging.auditlogger.error("Unable to retrieve configuration from adoaudit.config")
        logger.AppLogging.auditlogger.error(str(ex))

    @staticmethod
    def query_ado_events():
        try:
            start_time_file = open(".//last_processed_time", "r")
            get_start_time = start_time_file.read()
            logger.AppLogging.auditlogger.info("Reading last_processed_time file to get last audit event collection"
                                               " time: " + str(get_start_time))
            start_time_file.close()
        except FileNotFoundError as ex:
            logger.AppLogging.auditlogger.error("File last_processed_time not found. File last_processed_time must "
                                                "exist ")
            logger.AppLogging.auditlogger.error(str(ex))
        try:
            credentials = BasicAuthentication('', ADOClient.personal_access_token)
            connection = Connection(base_url=ADOClient.organization_url, creds=credentials)
            logger.AppLogging.auditlogger.info("Using BasicAuthentication to Authenticate against ADO "
                                               + str(credentials))
            logger.AppLogging.auditlogger.info("Establishing connection to ADO Audit Service " + str(connection))
        except AttributeError as ex:
            logger.AppLogging.auditlogger.error(str(ex))
        try:
            ado_client = connection.clients_v6_0.get_audit_client()
            logger.AppLogging.auditlogger.info("Initializing clients_v6_0.get_audit_client() " + str(ado_client))
            get_audit_response = ado_client.query_log(start_time=get_start_time, skip_aggregation=True)
            logger.AppLogging.auditlogger.info("Ready to receive response from server " + str(get_audit_response))
        except NameError as ex:
            logger.AppLogging.auditlogger.error(str(ex))

        update_last_processed_time = datetime.utcnow().astimezone().isoformat()
        try:
            with open(".//last_processed_time", 'w') as filetowrite:
                filetowrite.write(update_last_processed_time)
                filetowrite.close()
                logger.AppLogging.auditlogger.info("Successfully updated new last_processed_time: "
                                                   + str(update_last_processed_time))
                for items in [get_audit_response.decorated_audit_log_entries]:
                    f = open(".//tmp//adoaudit_output"+time.strftime("%Y%m%d-%H%M%S")+".log", "w")
                    for item in range(len(items)):
                        out = items[item]
                        f.write(str(out))
                        logger.AppLogging.auditlogger.info("Checking for Audit events. Using tmp directory.")
        except RuntimeError as ex:
            logger.AppLogging.auditlogger.error(str(ex))
        try:
            if os.stat(f.name).st_size == 0:
                f.close()
                os.remove(f.name)
                logger.AppLogging.auditlogger.info("No audit event was found in previous execution")
            else:
                f.close()
                shutil.move(f.name, ".//output")
                logger.AppLogging.auditlogger.info("Audit events were found in previous execution")
                logger.AppLogging.auditlogger.info("New output file created in output directory " + str(f.name))
        except RuntimeError as ex:
            logger.AppLogging.auditlogger.error(str(ex))





