import atexit
import threading

from queue import Queue, PriorityQueue
from typing import Dict

from .data_receiver import DataReceiver
from .data_uploader import DataUploader
from .log_uploader import LogUploader
from scrybe.internal.config import Config

DATA_UPLOADER = None
LOG_QUEUE = None
LOG_UPLOADER = None


def init_data_uploader(ingestion_server_url: str, project_id: int, project_name: str,
                       user_id: int, user_name: str) -> (PriorityQueue, DataUploader):
    upload_queue = PriorityQueue()
    du = DataUploader(shared_queue=upload_queue,
                      data_upload_config={},
                      ingestion_server_url=ingestion_server_url,
                      project_id=project_id,
                      project_name=project_name,
                      user_id=user_id,
                      user_name=user_name)
    uploader_thread = threading.Thread(target=du.upload)
    uploader_thread.setDaemon(True)
    uploader_thread.start()
    return upload_queue, du


def init_log_uploader(ingestion_server_url: str, project_id: int, user_id: int) -> (Queue, LogUploader):
    log_queue = Queue()
    lu = LogUploader(log_queue=log_queue,
                     log_upload_config={},
                     ingestion_server_url=ingestion_server_url,
                     project_id=project_id,
                     user_id=user_id)
    uploader_thread = threading.Thread(target=lu.upload)
    uploader_thread.setDaemon(True)
    uploader_thread.start()
    return log_queue, lu


def init_module(host_url: str, project_info: Dict, user_info: Dict):
    global DATA_UPLOADER
    data_queue, DATA_UPLOADER = \
        init_data_uploader(ingestion_server_url=host_url,
                           project_id=project_info['id'],
                           project_name=project_info['name'],
                           user_id=user_info['id'],
                           user_name=user_info['username'])
    DataReceiver.INTERNAL_RECEIVER = DataReceiver.InternalReceiver(shared_queue=data_queue)
    global LOG_QUEUE
    global LOG_UPLOADER
    LOG_QUEUE, LOG_UPLOADER = init_log_uploader(ingestion_server_url=host_url,
                                                project_id=project_info['id'],
                                                user_id=user_info['id'])


@atexit.register
def teardown():
    Config.has_exited = True
    global DATA_UPLOADER
    global LOG_UPLOADER
    if DATA_UPLOADER:
        DATA_UPLOADER.upload_remaining()
    if LOG_UPLOADER:
        LOG_UPLOADER.upload_remaining()
