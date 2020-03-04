import logging
from queue import Queue

from .memory_logging_handler import MemoryQueueHandler


def init_internal_logging(logger_name: str, log_queue: Queue):
    mem_handler = MemoryQueueHandler(log_queue=log_queue)
    formatter = logging.Formatter('%(asctime)s %(levelname)s : %(message)s')
    mem_handler.setFormatter(formatter)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logger.addHandler(mem_handler)

