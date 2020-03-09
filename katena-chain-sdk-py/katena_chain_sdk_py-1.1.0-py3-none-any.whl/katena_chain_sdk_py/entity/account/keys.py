"""
Copyright (c) 2020, TransChain.

This source code is licensed under the Apache 2.0 license found in the
LICENSE file in the root directory of this source tree.
"""

from marshmallow import fields
from katena_chain_sdk_py.crypto.ed25519.public_key import PublicKey
from katena_chain_sdk_py.crypto.base_key import KeyField
from katena_chain_sdk_py.entity.tx_data_interface import TxData
from katena_chain_sdk_py.serializer.base_schema import BaseSchema
from katena_chain_sdk_py.entity.account.common import get_type_key_create_v1, get_type_key_revoke_v1


class KeyV1:
    # KeyV1 is the version 1 of a key message

    def __init__(self, company_bcid: str, public_key: PublicKey, is_active: bool, role: str):
        self.company_bcid = company_bcid
        self.public_key = public_key
        self.is_active = is_active
        self.role = role

    def get_company_bcid(self) -> str:
        return self.company_bcid

    def get_public_key(self) -> PublicKey:
        return self.public_key

    def get_is_active(self) -> bool:
        return self.is_active

    def get_role(self) -> str:
        return self.role


class KeyV1Schema(BaseSchema):
    # KeyV1Schema allows to serialize and deserialize KeyV1.

    __model__ = KeyV1
    company_bcid = fields.Str()
    public_key = KeyField(PublicKey)
    is_active = fields.Bool()
    role = fields.Str()


class KeyCreateV1(TxData):
    # KeyCreateV1 is the version 1 of a key create message

    def __init__(self, txid: str, public_key: PublicKey, role: str):
        self.txid = txid
        self.public_key = public_key
        self.role = role

    def get_id(self) -> str:
        return self.txid

    def get_public_key(self) -> PublicKey:
        return self.public_key

    def get_role(self) -> str:
        return self.role

    def get_type(self) -> str:
        return get_type_key_create_v1()


class KeyCreateV1Schema(BaseSchema):
    # KeyCreateV1Schema allows to serialize and deserialize KeyCreateV1.

    __model__ = KeyCreateV1
    id = fields.Str(attribute="txid")
    public_key = KeyField(PublicKey)
    role = fields.Str()


class KeyRevokeV1(TxData):
    # KeyRevokeV1 is the version 1 of a key revoke message

    def __init__(self, txid: str, public_key: PublicKey):
        self.txid = txid
        self.public_key = public_key

    def get_id(self) -> str:
        return self.txid

    def get_public_key(self) -> PublicKey:
        return self.public_key

    def get_type(self) -> str:
        return get_type_key_revoke_v1()


class KeyRevokeV1Schema(BaseSchema):
    # KeyRevokeV1Schema allows to serialize and deserialize KeyRevokeV1.

    __model__ = KeyRevokeV1
    id = fields.Str(attribute="txid")
    public_key = KeyField(PublicKey)
