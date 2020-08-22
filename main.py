import adoclient
import logger
import configparser
import time


class MainProgram:
    @staticmethod
    def main():
        config = configparser.ConfigParser()
        config.read(".//adoaudit.config")
        frequency = config.get("ADO_options", "execution_frequency")
        while True:
            logger.AppLogging.auditlogger.info("Application execution frequency (in seconds): " + str(frequency))
            adoclient.ADOClient.query_ado_events()
            time.sleep(float(frequency))


if __name__ == '__main__':
    MainProgram.main()
