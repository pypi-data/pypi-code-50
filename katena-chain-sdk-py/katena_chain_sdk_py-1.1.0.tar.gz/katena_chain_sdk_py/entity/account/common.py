"""
Copyright (c) 2020, TransChain.

This source code is licensed under the Apache 2.0 license found in the
LICENSE file in the root directory of this source tree.
"""

NAMESPACE = "account"
TYPE_KEY = "key"
TYPE_CREATE = "create"
TYPE_REVOKE = "revoke"
DEFAULT_ROLE_ID = "default"
COMPANY_ADMIN_ROLE_ID = "company_admin"


def get_category_key_create() -> str:
    return "{}.{}.{}".format(NAMESPACE, TYPE_KEY, TYPE_CREATE)


def get_category_key_revoke() -> str:
    return "{}.{}.{}".format(NAMESPACE, TYPE_KEY, TYPE_REVOKE)


def get_type_key_create_v1() -> str:
    return "{}.{}".format(get_category_key_create(), "v1")


def get_type_key_revoke_v1() -> str:
    return "{}.{}".format(get_category_key_revoke(), "v1")
