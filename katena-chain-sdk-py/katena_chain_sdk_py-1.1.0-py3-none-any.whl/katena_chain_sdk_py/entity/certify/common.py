"""
Copyright (c) 2019, TransChain.

This source code is licensed under the Apache 2.0 license found in the
LICENSE file in the root directory of this source tree.
"""

NAMESPACE = "certify"
TYPE_CERTIFICATE = "certificate"
TYPE_RAW = "raw"
TYPE_ED25519 = "ed25519"
TYPE_SECRET = "secret"
TYPE_NACL_BOX = "nacl_box"


def get_category_certificate() -> str:
    return "{}.{}".format(NAMESPACE, TYPE_CERTIFICATE)


def get_type_certificate_raw_v1() -> str:
    return "{}.{}.{}".format(get_category_certificate(), TYPE_RAW, "v1")


def get_type_certificate_ed25519_v1() -> str:
    return "{}.{}.{}".format(get_category_certificate(), TYPE_ED25519, "v1")


def get_category_secret() -> str:
    return "{}.{}".format(NAMESPACE, TYPE_SECRET)


def get_type_secret_nacl_box_v1() -> str:
    return "{}.{}.{}".format(get_category_secret(), TYPE_NACL_BOX, "v1")
