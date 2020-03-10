from typing import List
import dataclasses
import json

import requests


@dataclasses.dataclass()
class Client:
    session: requests.Session
    base_url: str


class Workspace:
    def __init__(self, data, client: Client):
        self._data = data
        self._client = client

    def get_name(self) -> str:
        return self._data["attributes"]["name"]

    def get_self_link(self):
        return self._data["links"]["self"]

    def show(self):
        print(json.dumps(self._data["attributes"], indent=2))

    def set_local_execution(self):
        resp = self._client.session.patch(f"{self._client.base_url}/{self.get_self_link()}",
                                   data=json.dumps({"data": {"attributes": {"operations": False}}}))
        if resp.status_code == 200:
            print("Success")
        else:
            print(resp.json())


class Organization:
    def __init__(self, data, client: Client):
        self._data = data
        self._client = client

    def get_name(self) -> str:
        return self._data["id"]

    def get_self_link(self):
        return self._data["links"]["self"]

    def get_workspaces(self) -> List[Workspace]:
        resp = self._client.session.get(f"{self._client.base_url}/{self.get_self_link()}/workspaces")
        return [Workspace(d, self._client) for d in resp.json()["data"]]

    def workspace(self, name) -> Workspace:
        workspaces = self.get_workspaces()
        filtered = [w for w in workspaces if w.get_name() == name]
        if len(filtered) != 1:
            raise LookupError(f"Error finding workspace named {name} (found {len(filtered)})")
        return filtered[0]


class Api:
    def __init__(self, token):
        self._client = Client(requests.Session(), "https://app.terraform.io")
        self._client.session.headers.update(
            {"Content-Type": "application/vnd.api+json", "Authorization": f"Bearer {token}"})

    def get_organizations(self) -> List[Organization]:
        resp = self._client.session.get(f"{self._client.base_url}/api/v2/organizations")
        return [Organization(d, self._client) for d in resp.json()["data"]]

    def organization(self, name) -> Organization:
        organizations = self.get_organizations()
        filtered = [o for o in organizations if o.get_name() == name]
        if len(filtered) != 1:
            raise LookupError(f"Error finding organization named {name} (found {len(filtered)})")

        return filtered[0]
