"""
Copyright (c) 2020, TransChain.

This source code is licensed under the Apache 2.0 license found in the
LICENSE file in the root directory of this source tree.
"""

from http import HTTPStatus
from typing import List
from datetime import datetime
from katena_chain_sdk_py.api.client import Client
from katena_chain_sdk_py.entity.api.tx_status import TxStatusSchema, TxStatus
from katena_chain_sdk_py.entity.api.tx_wrapper import TxWrapperSchema, TxWrapper
from katena_chain_sdk_py.entity.api.tx_wrappers import TxWrappersSchema, TxWrappers
from katena_chain_sdk_py.entity.tx import Tx
from katena_chain_sdk_py.entity.tx import TxSchema
from katena_chain_sdk_py.entity.tx_data_interface import TxData
from katena_chain_sdk_py.entity.tx_data_state import TxDataState, TxDataStateSchema
from katena_chain_sdk_py.exceptions.api_exception import ApiExceptionSchema
from katena_chain_sdk_py.entity.account.keys import KeyV1Schema, KeyV1
from katena_chain_sdk_py.utils.common import get_pagination_query_params
from katena_chain_sdk_py.crypto.ed25519.private_key import PrivateKey


class Handler:
    # Handler provides helper methods to send and retrieve tx without directly interacting with the HTTP Client.
    CERTIFICATES_PATH = "certificates"
    SECRET_PATH = "secrets"
    LAST_PATH = "last"
    TXS_PATH = "txs"
    COMPANIES_PATH = "companies"
    KEYS_PATH = "keys"

    def __init__(self, api_url: str):
        self.api_client = Client(api_url)
        self.tx_schema = TxSchema()
        self.tx_status_schema = TxStatusSchema()
        self.tx_wrapper_schema = TxWrapperSchema()
        self.tx_wrappers_schema = TxWrappersSchema()
        self.api_exception_schema = ApiExceptionSchema()
        self.key_v1_schema = KeyV1Schema()
        self.tx_data_state_schema = TxDataStateSchema()

    def send_tx(self, tx: Tx) -> TxStatus:
        # Accept a Tx and sends it to the API, returns its status or throws an error.
        response = self.api_client.post(self.TXS_PATH, body=self.tx_schema.dumps(tx))
        json_body = response.get_body().decode("utf-8")
        if response.get_status_code() == HTTPStatus.ACCEPTED:
            return self.tx_status_schema.loads(json_body)
        else:
            raise self.api_exception_schema.loads(json_body, unknown="EXCLUDE")

    def retrieve_last_certificate(self, id: str) -> TxWrapper:
        # Fetches the API and returns a tx wrapper.
        response = self.api_client.get("{}/{}/{}".format(self.CERTIFICATES_PATH, id, self.LAST_PATH))
        json_body = response.get_body().decode("utf-8")
        if response.get_status_code() == HTTPStatus.OK:
            return self.tx_wrapper_schema.loads(json_body)
        else:
            raise self.api_exception_schema.loads(json_body, unknown="EXCLUDE")

    def retrieve_certificates(self, id: str, page, tx_per_page: int) -> TxWrappers:
        # Fetches the API and returns a tx wrappers.
        query_params = get_pagination_query_params(page, tx_per_page)
        response = self.api_client.get("{}/{}".format(self.CERTIFICATES_PATH, id), query_params)
        json_body = response.get_body().decode("utf-8")
        if response.get_status_code() == HTTPStatus.OK:
            return self.tx_wrappers_schema.loads(json_body)
        else:
            raise self.api_exception_schema.loads(json_body, unknown="EXCLUDE")

    def retrieve_secrets(self, id: str, page, tx_per_page: int) -> TxWrappers:
        # Fetches the API and returns a tx wrapper list.
        query_params = get_pagination_query_params(page, tx_per_page)
        response = self.api_client.get("{}/{}".format(self.SECRET_PATH, id), query_params)
        json_body = response.get_body().decode("utf-8")
        if response.get_status_code() == HTTPStatus.OK:
            return self.tx_wrappers_schema.loads(json_body)
        else:
            raise self.api_exception_schema.loads(json_body, unknown="EXCLUDE")

    def retrieve_txs(self, tx_category, id: str, page, tx_per_page: int) -> TxWrappers:
        # Fetches the API and returns a tx wrapper list.
        query_params = get_pagination_query_params(page, tx_per_page)
        response = self.api_client.get("{}/{}/{}".format(self.TXS_PATH, tx_category, id), query_params)
        json_body = response.get_body().decode("utf-8")
        if response.get_status_code() == HTTPStatus.OK:
            return self.tx_wrappers_schema.loads(json_body)
        else:
            raise self.api_exception_schema.loads(json_body, unknown="EXCLUDE")

    def retrieve_company_keys(self, company_bcid: str, page, tx_per_page: int) -> List[KeyV1]:
        # Fetches the API and returns a tx wrapper list.
        query_params = get_pagination_query_params(page, tx_per_page)
        response = self.api_client.get("{}/{}/{}".format(self.COMPANIES_PATH, company_bcid, self.KEYS_PATH),
                                       query_params)
        json_body = response.get_body().decode("utf-8")
        if response.get_status_code() == HTTPStatus.OK:
            return self.key_v1_schema.loads(json_body, many=True)
        else:
            raise self.api_exception_schema.loads(json_body, unknown="EXCLUDE")

    def sign_tx(self, private_key: PrivateKey, chain_id: str, nonce_time: datetime, tx_data: TxData) -> Tx:
        # Creates a tx data state, signs it and returns a tx ready to encode and send.
        tx_data_state = self.get_tx_data_state(chain_id, nonce_time, tx_data)
        tx_signature = private_key.sign(tx_data_state)
        return Tx(nonce_time, tx_data, private_key.get_public_key(), tx_signature)

    def get_tx_data_state(self, chain_id: str, nonce_time: datetime, tx_data: TxData) -> bytes:
        # Returns the sorted and marshaled json representation of a TxData ready to be signed.
        tx_data_state = TxDataState(chain_id, nonce_time, tx_data)
        return self.tx_data_state_schema.dumps(tx_data_state).encode("utf-8")
