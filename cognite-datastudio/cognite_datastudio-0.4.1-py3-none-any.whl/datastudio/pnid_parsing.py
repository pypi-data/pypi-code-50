import time
from typing import Dict, List

from cognite.datastudio.exceptions import ModelFailedException


def request(client, path, request_type, data=None):
    project = client._config.project
    api_key = client._config.api_key
    url = f"/api/playground/projects/{project}/context/pnid{path}"
    if request_type == "GET":
        response = client._api_client._get(url)
    else:
        response = client._api_client._post(
            url, json=data, headers={"Content-Type": "application/json", "API-Key": api_key}
        )

    return response


class Parser:
    def __init__(self, client):
        self.client = client

    def parse(self, fileId: int, entities: List[str], name_mapping: Dict[str, str] = None):  # TODO: change to file_id
        entities = list(entities)
        request_body = {"fileId": fileId, "entities": entities}
        if name_mapping is not None:
            request_body["nameMapping"] = name_mapping
        response = request(self.client, "/parse", "POST", data=request_body)

        data = response.json()
        job_id = data["jobId"]
        while data["status"] != "Completed":
            response = request(self.client, f"/{job_id}", "GET")
            data = response.json()
            if data["status"] == "Failed":
                raise ModelFailedException(f"model_id: {job_id} error: {data.get('errorMessage')}")
            time.sleep(1)
        return data
