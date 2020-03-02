import logging

def configure_and_get_logger(logger_name, stream_level=logging.WARNING):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    c_handler = logging.StreamHandler()
    fdebug_handler = logging.FileHandler('gf_debug.log')
    fprod_handler = logging.FileHandler('gf_prod.log')
    
    c_handler.setLevel(stream_level)
    fdebug_handler.setLevel(logging.DEBUG)
    fprod_handler.setLevel(logging.ERROR)

    c_fmt = logging.Formatter('%(name)s - %(funcName)s - %(levelname)s - %(message)s')
    fdebug_fmt = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
    fprod_fmt = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')

    c_handler.setFormatter(c_fmt)
    fdebug_handler.setFormatter(fdebug_fmt)
    fprod_handler.setFormatter(fprod_fmt)

    logger.addHandler(c_handler)
    logger.addHandler(fdebug_handler)
    logger.addHandler(fprod_handler)
    
    return logger
