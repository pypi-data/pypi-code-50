import os

from kisters.water.rest_client import RESTClient
from kisters.water.rest_client.auth import OpenIDConnect


client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]
auth = OpenIDConnect(client_id, client_secret)
client = RESTClient(
    url="https://dev.hydraulic-network.kisters.cloud/", authentication=auth,
)


def test_get_str():
    networks = client.get("rest/networks")
    assert isinstance(networks, list)


def test_get_iter():
    networks = client.get(["rest", "networks"])
    assert isinstance(networks, list)


# def test_put():
#     client.put(["rest", "networks", "tmp"], data={"nodes": [], "links": []})


# def test_post():
#     client.post(["rest", "networks", "tmp", "metadata"], data={"datum": "EPSG:4269"})


# def test_delete():
#     client.delete(["rest", "networks", "tmp"])
