from konker_client.client import Client
from timeit import default_timer as timer
import requests
import logging
import json


class Request(Client):

    def __init__(self, user: str, password: str):
        """Constructor Method for the Request Class

        :param user: The devices username
        :type user: str
        :param password: The devices password
        :type password: str
        """
        self._logger = logging.getLogger(__name__)
        self.url_konker_post = 'http://data.demo.konkerlabs.net:80/pub/'
        self.user = user
        self.password = password

    def send_message(self, channel: str, message: dict) -> bool:
        """Method for posting messages to the Konker Plataform

        :param user: The devices username
        :type user: str
        :param password: The devices password
        :type password: str
        """
        method_start_time = timer()
        self._logger.info("Method post_konker started")

        url = f'{self.url_konker_post}{self.user}/{channel}'
        headers = {'content-type': 'application/json', 'Accept': 'application/json'}
        auth = (self.user, self.password)

        try:
            response = requests.post(url, headers=headers, auth=auth, data=json.dumps(message))
        except Exception:
            method_end_time = timer()
            total_seconds = method_end_time - method_start_time
            self._logger.error(f"Method post_konker finished in {total_seconds:.2} seconds with error", exc_info=1)
            return False

        method_end_time = timer()
        total_seconds = method_end_time - method_start_time
        if response.status_code != 200:
            self._logger.error(f"Method post_konker finished in {total_seconds:.2} seconds with error status != 200")
            return False
        else:
            self._logger.info(f"Method post_konker finished in {total_seconds:.2} seconds")
            return True
