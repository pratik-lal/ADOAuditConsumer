import logging.handlers

# Application logging module

class AppLogging:
    log_filename = ".//logs//adoaudit.log" # All the log file will be saved in Logs directory with filename adoaudit.log
    auditlogger = logging.getLogger('ADOAudit')
    auditlogger.setLevel(logging.DEBUG)
    logging_format = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s") # Setting time format for logging

    # Using RotatingFileHandler class.
    # Log file will be rotated after reasching 1 MB in size.
    # Keep 10 logs files from past.
    logfile_handler = logging.handlers.RotatingFileHandler(log_filename,
                                                           maxBytes=100000,
                                                           backupCount=10)
    logfile_handler.setFormatter(logging_format)
    auditlogger.addHandler(logfile_handler)

