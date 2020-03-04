import json
import threading
import time
import uuid
from queue import PriorityQueue

from scrybe.internal.commons.queue_item import PriorityQueueItem
from scrybe.internal.uploader import DataUploader

shared_queue = PriorityQueue()


def data_generator():
    while True:
        print('datagen queue size %s' % shared_queue.qsize())
        dataset_obj = {
            'data_type': 'dataset',
            'client_id': str(uuid.uuid4()),
            'created_in_run': False,
            'client_watermark': 1,
            'name': 'some_training_dataset',
            'description': 'some_description',
            'location': 'some_location'
        }
        json_data = json.dumps(dataset_obj)
        qi = PriorityQueueItem(priority_number=1, created_timestamp_micros=int(time.time()*1000), datastr=json_data)
        shared_queue.put(qi)
        time.sleep(5)


gen_thread = threading.Thread(target=data_generator)
gen_thread.start()

du = DataUploader(shared_queue=shared_queue,
                  data_upload_config={},
                  ingestion_server_url='localhost:5001',
                  project_id=5, project_name='fight trolls',
                  user_id=1, user_name='himanshu')
uploader_thread = threading.Thread(target=du.upload)
uploader_thread.start()

