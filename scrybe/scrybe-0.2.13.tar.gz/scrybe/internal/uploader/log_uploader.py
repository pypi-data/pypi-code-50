import gzip
import json
import time

import requests
from retrying import retry


class LogUploader(object):

    def __init__(self, log_queue, log_upload_config, ingestion_server_url, project_id, user_id):
        """

        :param queue.Queue log_queue:
        :param {} log_upload_config:
        :param str ingestion_server_url:
        :param int project_id:
        :param int user_id:
        """
        self.log_queue = log_queue
        self.log_upload_config = log_upload_config
        self.ingestion_server_url = ingestion_server_url
        self.project_id = project_id
        self.user_id = user_id

    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=3000)
    def _send_data(self, log_records):
        """

        :param [] log_records:
        :return:
        """
        if len(log_records) > 0:
            payload = gzip.compress(json.dumps(log_records).encode('utf-8'))
            # FIXME - http -> https
            ingestion_server = 'http://%s' % self.ingestion_server_url
            if self.ingestion_server_url == 'ingestionapi.scrybetool.com':
                ingestion_server = 'https://%s' % self.ingestion_server_url
            url = '%s/v1/project/%s/uploadlogs' % (ingestion_server, self.project_id)
            requests.post(url=url,
                          data=payload,
                          headers={'Content-Type': 'application/octet-stream', 'user-id': str(self.user_id)})

    def _get_data_for_upload(self):
        sum_len_log_records = 0
        log_records = []
        queue_empty = False
        while True:
            try:
                log_record = self.log_queue.get(block=False)
                self.log_queue.task_done()
                sum_len_log_records += len(log_record)
                log_records.append(log_record)
                if sum_len_log_records > 1048576:
                    break
            except:
                queue_empty = True
                break
        return log_records, queue_empty

    def upload_remaining(self):
        while True:
            log_records, queue_empty = self._get_data_for_upload()
            try:
                self._send_data(log_records=log_records)
            except:
                # TODO (himanshu) try sending to S3
                pass
            if queue_empty:
                break

    def upload(self):
        """

        :return:
        """
        while True:
            try:
                log_records, _ = self._get_data_for_upload()
                try:
                    self._send_data(log_records=log_records)
                except:
                    for log_record in log_records:
                        self.log_queue.put(log_record)
                time.sleep(2)
            except:
                pass

