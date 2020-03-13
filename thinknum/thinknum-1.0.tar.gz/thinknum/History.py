import requests
import json
import httplib
import os
import unicodecsv
import io
import gzip
import shutil


class History(object):

    _BASE_URL = 'https://data.thinknum.com'

    def __init__(self, client_id, client_secret):
        self._client_id = client_id
        self._client_secret = client_secret

        self._token = None
        self._authenticate()
        self._headers = {
            "Authorization": "token {token}".format(token=self._token),
            "X-API-Version": "20151130",
            "Accept": "application/json"
        }

        self._dataset_id = None

    def _authenticate(self):
        response = requests.post(
            '{base_url}/api/authorize'.format(base_url=self._BASE_URL), 
            data={
                "version": "20151130",
                "client_id": self._client_id,
                "client_secret": self._client_secret
            }
        )
        if response.status_code != httplib.OK:
            raise Exception('Invalid autentication')
        self._token = json.loads(response.text)['auth_token']

    def get_history_list(self, dataset_id):
        if not dataset_id:
            raise Exception('Invalid dataset_id')

        response = requests.get(
            '{base_url}/datasets/{dataset_id}/history/'.format(
                base_url=self._BASE_URL,
                dataset_id=dataset_id
            ),
            headers=self._headers
        )
        history = json.loads(response.text)['history']
        return history

    def get_history_metadata(self, dataset_id, history_date):
        if not dataset_id:
            raise Exception('Invalid dataset_id')

        if not history_date:
            raise Exception('Invalid history_date')

        response = requests.get(
            '{base_url}/datasets/{dataset_id}/history/{history_date}'.format(
                base_url=self._BASE_URL,
                dataset_id=dataset_id,
                history_date=history_date
            ),
            headers=self._headers
        )
        return json.loads(response.text)

    def download(self, dataset_id, history_date, download_path=None):
        if not dataset_id:
            raise Exception('Invalid dataset_id')

        if not history_date:
            raise Exception('Invalid history_date')

        if not download_path:
            download_path = os.path.abspath(os.getcwd())

        with requests.get(
            '{base_url}/datasets/{dataset_id}/history/{history_date}'.format(
                base_url=self._BASE_URL,
                dataset_id=dataset_id,
                history_date=history_date
            ),
            headers=dict(
                self._headers,
                **{
                    "Accept": "text/csv",
                    "Accept-Encoding": "gzip"
                }
            ),
            stream=True
        ) as r:
            gz_filepath = '{download_path}/{dataset_id}_{history_date}.csv.gz'.format(
                download_path=download_path,
                dataset_id=dataset_id,
                history_date=history_date,
            )
            csv_filepath = '{download_path}/{dataset_id}_{history_date}.csv'.format(
                download_path=download_path,
                dataset_id=dataset_id,
                history_date=history_date,
            )

            with open(gz_filepath, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            
            with gzip.open(gz_filepath, 'rb') as f_in:
                with open(csv_filepath, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            os.remove(gz_filepath)

            return csv_filepath
