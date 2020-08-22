import logging.handlers


class AppLogging:
    log_filename = ".//logs//adoaudit.log"
    auditlogger = logging.getLogger('ADOAudit')
    auditlogger.setLevel(logging.DEBUG)
    logging_format = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
    logfile_handler = logging.handlers.RotatingFileHandler(log_filename,
                                                           maxBytes=100000,
                                                           backupCount=10)
    logfile_handler.setFormatter(logging_format)
    auditlogger.addHandler(logfile_handler)

