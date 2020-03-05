import logging
import os
import sys

def get_logger(name='debug', level=10):
    """small method to create loggers with desired setup for module returns a logger. Logs to stdout as well as file
    
    Keyword Arguments:
        level {int} -- [logging level 10 : DEBUG, 20 : INFO, 30: WARNING, 40 : ERROR, 50 : CRITICAL] (default: {10})
        name {str} -- [name for the logger] (default: {'debug'})
    """    
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] : %(message)s')
    # formatter.setlevel(level)
    logger_handler = logging.StreamHandler(sys.stdout)
    logger_handler.setFormatter(formatter)
    logger_handler.setLevel(level)
    logger.addHandler(logger_handler)
    file_handler = logging.FileHandler(f'/home/{os.getlogin()}/monitor/logs/{name}-log.log')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)
    
    return logger