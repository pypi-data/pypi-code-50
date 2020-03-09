"""
Copyright (c) 2019, TransChain.

This source code is licensed under the Apache 2.0 license found in the
LICENSE file in the root directory of this source tree.
"""

from marshmallow import fields
from katena_chain_sdk_py.crypto.ed25519.public_key import PublicKey
from katena_chain_sdk_py.crypto.base_key import KeyField
from katena_chain_sdk_py.entity.certify.common import get_type_certificate_ed25519_v1, get_type_certificate_raw_v1
from katena_chain_sdk_py.entity.tx_data_interface import TxData
from katena_chain_sdk_py.serializer.base_schema import BaseSchema
from katena_chain_sdk_py.serializer.bytes_field import BytesField


class CertificateRawV1(TxData):
    # CertificateRawV1 is the first version of a raw certificate.

    def __init__(self, txid: str, value: bytes):
        self.txid = txid
        self.value = value

    def get_id(self) -> str:
        return self.txid

    def get_value(self) -> bytes:
        return self.value

    def get_type(self) -> str:
        return get_type_certificate_raw_v1()


class CertificateRawV1Schema(BaseSchema):
    # CertificateRawV1Schema allows to serialize and deserialize CertificateRawV1.

    __model__ = CertificateRawV1
    id = fields.Str(attribute="txid")
    value = BytesField()


class CertificateEd25519V1(TxData):
    # CertificateEd25519V1 is the first version of an ed25519 certificate.

    def __init__(self, txid: str, signer: PublicKey, signature: bytes):
        self.txid = txid
        self.signature = signature
        self.signer = signer

    def get_id(self) -> str:
        return self.txid

    def get_signer(self) -> PublicKey:
        return self.signer

    def get_signature(self) -> bytes:
        return self.signature

    def get_type(self) -> str:
        return get_type_certificate_ed25519_v1()


class CertificateEd25519V1Schema(BaseSchema):
    # CertificateEd25519V1Schema allows to serialize and deserialize CertificateEd25519V1.

    __model__ = CertificateEd25519V1
    id = fields.Str(attribute="txid")
    signature = BytesField()
    signer = KeyField(PublicKey)
