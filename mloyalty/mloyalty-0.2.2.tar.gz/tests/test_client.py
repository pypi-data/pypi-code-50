from mloyalty.client import Client
from mloyalty.base import ApiException
import pytest


class TestClient:
    def test_get_client_info_phone(self):
        client = Client()
        resp = client.get_client_info(phone='9043482856')
        assert isinstance(resp, dict)

    def test_get_client_info_phone_fail(self):
        client = Client()
        with pytest.raises(ApiException):
            client.get_client_info(phone='1234567890')

    def test_get_client_info_card(self):
        client = Client()
        resp = client.get_client_info(card=25809824)
        assert isinstance(resp, dict)

    def test_get_client_info_card_fail(self):
        client = Client()
        with pytest.raises(ApiException):
            client.get_client_info(card=1234567890)
