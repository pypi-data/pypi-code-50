import gzip
import json
import logging
import time

import requests
from retrying import retry

from ..commons.queue_item import PriorityQueueItem

logger = logging.getLogger(__name__)


class DataUploader(object):

    def __init__(self, shared_queue, data_upload_config, ingestion_server_url, project_id, project_name, user_id,
                 user_name):
        """

        :param queue.Queue shared_queue:
        :param {} data_upload_config:
        :param str ingestion_server_url:
        :param int project_id:
        :param str project_name:
        :param int user_id:
        :param str user_name:
        """
        self.shared_queue = shared_queue
        self.data_upload_config = data_upload_config
        self.ingestion_server_url = ingestion_server_url
        self.project_id = project_id
        self.project_name = project_name
        self.user_id = user_id
        self.user_name = user_name

    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=3000)
    def _send_data(self, json_data_list):
        """

        :param [] json_data_list:
        :return:
        """
        if len(json_data_list) > 0:
            payload = gzip.compress(json.dumps(json_data_list).encode('utf-8'))
            ingestion_server = 'http://%s' % self.ingestion_server_url
            if self.ingestion_server_url == 'ingestionapi.scrybetool.com':
                ingestion_server = 'https://%s' % self.ingestion_server_url
            url = '%s/v1/project/%s/upload' % (ingestion_server, self.project_id)
            requests.post(url=url,
                          data=payload,
                          headers={'Content-Type': 'application/octet-stream', 'user-id': str(self.user_id)})

    def _get_data_for_upload(self):
        json_data_list = []
        sum_len_json_data = 0
        queue_empty = False
        while True:
            try:
                queue_item = self.shared_queue.get(block=False)
                json_data = queue_item.datastr
                self.shared_queue.task_done()
                sum_len_json_data += len(json_data)
                json_data_list.append(json_data)
                # limit payload to 200KB
                if sum_len_json_data > 204800:
                    break
            except:
                queue_empty = True
                break
        return json_data_list, queue_empty

    def upload_remaining(self):
        while True:
            json_data_list, queue_empty = self._get_data_for_upload()
            try:
                self._send_data(json_data_list=json_data_list)
            except:
                # TODO (himanshu) try sending to S3
                logger.error('_send_data failed', exc_info=True)
            if queue_empty:
                break

    def upload(self):
        """

        :return:
        """
        while True:
            try:
                json_data_list, _ = self._get_data_for_upload()
                try:
                    self._send_data(json_data_list=json_data_list)
                except:
                    logger.error('_send_data failed', exc_info=True)
                    for json_data in json_data_list:
                        self.shared_queue.put(PriorityQueueItem(priority_number=0,
                                                                created_timestamp_micros=int(time.time()*1000000),
                                                                datastr=json_data))
                time.sleep(2)
            except:
                logger.error('some problem occured getting data from queue and while uploading it', exc_info=True)

