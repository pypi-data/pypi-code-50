import json
import requests

from ada.config import ADA_API_URL, DEFAULT_HEADERS


class Request(object):
    def __init__(self, token):
        self.token = token

    def send_request(self, api_path, data, method):
        url = ADA_API_URL + api_path + "?api-key=" + self.token
        main_data = json.dumps(data)
        headers = DEFAULT_HEADERS
        if method == "POST":
            response = requests.post(
                url, data=main_data, headers=headers
            )
        elif method == "PATCH":
            response = requests.patch(
                url, data=main_data, headers=headers
            )
        else:
            raise Exception("method is not supported")
        if response.status_code == 201 or response.status_code == 200:
            return response.json()
        raise Exception(response.text)

    def send_request_form(self, api_path, folder, method, files):
        url = ADA_API_URL + api_path + folder + "/upload/?api-key=" + self.token
        if method == "POST":
            response = requests.post(
                url, files=files
            )
        elif method == "PATCH":
            response = requests.patch(
                url, files=files
            )
        else:
            raise Exception("method is not supported")
        if response.status_code == 201 or response.status_code == 200:
            return response.json()
        raise Exception(response.text)


class BaseADA(Request):
    url = None

    def create(self, kwargs):
        reps = self.send_request(self.url, data=kwargs, method="POST")
        return reps["_id"]["$oid"]

    def create_form(self, folder, files):
        reps = self.send_request_form(self.url, folder=folder, method="POST", files=files)
        return reps
