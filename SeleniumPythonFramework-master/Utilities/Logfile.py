import inspect
import logging


def customLogger(logLevel):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    fileHandler = logging.FileHandler('Logs\logfile.log', mode='w')
    # fileHandler = logging.FileHandler('Logs\{0}.log'.format(loggerName), mode='w')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler object

    logger.setLevel(logging.DEBUG)
    return logger
