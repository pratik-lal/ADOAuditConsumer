import adoclient
import logger
import configparser
import time


class MainProgram:
    @staticmethod
    def main():
        config = configparser.ConfigParser() # Initialize configparser
        config.read(".//adoaudit.config") # Read configuration file

        # Set execution frequency (in seconds) of application.
        # Update execution frequency in configuration file.
        frequency = config.get("ADO_options", "execution_frequency")
        while True:
            logger.AppLogging.auditlogger.info("Application execution frequency (in seconds): " + str(frequency))
            adoclient.ADOClient.query_ado_events()
            time.sleep(float(frequency))

 
if __name__ == '__main__':
    MainProgram.main()
