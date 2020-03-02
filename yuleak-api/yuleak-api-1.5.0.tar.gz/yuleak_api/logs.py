import logging

logger = logging.getLogger('yuleak-api')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s :: YuleakAPI - %(levelname)s :: %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
