"""
Copyright (c) 2019, TransChain.

This source code is licensed under the Apache 2.0 license found in the
LICENSE file in the root directory of this source tree.
"""

from typing import List
from datetime import datetime
from katena_chain_sdk_py.api.handler import Handler
from katena_chain_sdk_py.crypto.nacl.public_key import PublicKey as PublicKeyX25519
from katena_chain_sdk_py.crypto.ed25519.private_key import PrivateKey
from katena_chain_sdk_py.crypto.ed25519.public_key import PublicKey as PublicKeyEd25519
from katena_chain_sdk_py.entity.api.tx_status import TxStatus
from katena_chain_sdk_py.entity.api.tx_wrapper import TxWrapper
from katena_chain_sdk_py.entity.api.tx_wrappers import TxWrappers
from katena_chain_sdk_py.entity.tx_data_interface import TxData
from katena_chain_sdk_py.entity.certify.certificate import CertificateRawV1, CertificateEd25519V1
from katena_chain_sdk_py.entity.certify.secret import SecretNaclBoxV1
from katena_chain_sdk_py.entity.account.keys import KeyV1, KeyCreateV1, KeyRevokeV1
from katena_chain_sdk_py.entity.account.common import get_category_key_create, get_category_key_revoke
from katena_chain_sdk_py.exceptions.client_exception import ClientException
from katena_chain_sdk_py.utils.common import format_txid


class Transactor:
    # Transactor provides methods to hide the complexity of Tx creation, Tx signature and API dialog.

    def __init__(self, api_url: str, chain_id: str = "", company_bcid: str = "", tx_signer: PrivateKey = None):
        self.api_handler = Handler(api_url)
        self.chain_id = chain_id
        self.company_bcid = company_bcid
        self.tx_signer = tx_signer

    def send_certificate_raw_v1(self, uuid: str, value: bytes) -> TxStatus:
        # Creates a CertificateRaw (V1) and sends it to the API.
        certificate = CertificateRawV1(format_txid(self.company_bcid, uuid), value)
        return self.send_tx(certificate)

    def send_certificate_ed25519_v1(self, uuid: str, signer: PublicKeyEd25519, signature: bytes) -> TxStatus:
        # Creates a CertificateEd25519 (V1) and sends it to the API.
        certificate = CertificateEd25519V1(format_txid(self.company_bcid, uuid), signer, signature)
        return self.send_tx(certificate)

    def send_key_create_v1(self, uuid: str, new_key: PublicKeyEd25519, role: str) -> TxStatus:
        # Creates a KeyCreate (V1) and sends it to the API.
        key_create = KeyCreateV1(format_txid(self.company_bcid, uuid), new_key, role)
        return self.send_tx(key_create)

    def send_key_revoke_v1(self, uuid: str, key: PublicKeyEd25519) -> TxStatus:
        # Creates a KeyRevoke (V1) and sends it to the API.
        key_revoke = KeyRevokeV1(format_txid(self.company_bcid, uuid), key)
        return self.send_tx(key_revoke)

    def send_secret_nacl_box_v1(self, uuid: str, sender: PublicKeyX25519, nonce: bytes, content: bytes) -> TxStatus:
        # Creates a SecretNaclBox (V1) and sends it to the API.
        secret = SecretNaclBoxV1(format_txid(self.company_bcid, uuid), content, nonce, sender)
        return self.send_tx(secret)

    def send_tx(self, tx_data: TxData) -> TxStatus:
        # Signs and sends a tx to the Api.
        if self.tx_signer is None or self.chain_id == "":
            raise ClientException("impossible to create txs without a private key or chain id")

        tx = self.api_handler.sign_tx(self.tx_signer, self.chain_id, datetime.utcnow(), tx_data)
        return self.api_handler.send_tx(tx)

    def retrieve_last_certificate(self, company_bcid, uuid: str) -> TxWrapper:
        # Fetches the API to find the corresponding tx and return a tx wrapper.
        return self.api_handler.retrieve_last_certificate(format_txid(company_bcid, uuid))

    def retrieve_certificates(self, company_bcid, uuid: str, page, tx_per_page: int) -> TxWrappers:
        # Fetches the API to find the corresponding txs and returns tx wrappers or an error.
        return self.api_handler.retrieve_certificates(format_txid(company_bcid, uuid), page, tx_per_page)

    def retrieve_key_create_txs(self, company_bcid, uuid: str, page, tx_per_page: int) -> TxWrappers:
        # Fetches the API to find the corresponding txs and returns tx wrappers or an error.
        return self.api_handler.retrieve_txs(get_category_key_create(), format_txid(company_bcid, uuid), page,
                                             tx_per_page)

    def retrieve_key_revoke_txs(self, company_bcid, uuid: str, page, tx_per_page: int) -> TxWrappers:
        # Fetches the API to find the corresponding txs and returns tx wrappers or an error.
        return self.api_handler.retrieve_txs(get_category_key_revoke(), format_txid(company_bcid, uuid), page,
                                             tx_per_page)

    def retrieve_company_keys(self, company_bcid: str, page, tx_per_page: int) -> List[KeyV1]:
        # Fetches the API to find the corresponding txs and returns tx wrappers.
        return self.api_handler.retrieve_company_keys(company_bcid, page, tx_per_page)

    def retrieve_secrets(self, company_bcid, uuid: str, page, tx_per_page: int) -> TxWrappers:
        # Fetches the API to find the corresponding txs and returns tx wrappers.
        return self.api_handler.retrieve_secrets(format_txid(company_bcid, uuid), page, tx_per_page)

    def retrieve_txs(self, tx_category, company_bcid: str, uuid: str, page, tx_per_page: int) -> TxWrappers:
        # Fetches the API to find the corresponding txs and returns tx wrappers.
        return self.api_handler.retrieve_txs(tx_category, format_txid(company_bcid, uuid), page, tx_per_page)
