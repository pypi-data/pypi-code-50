"""
Copyright (c) 2020, TransChain.

This source code is licensed under the Apache 2.0 license found in the
LICENSE file in the root directory of this source tree.
"""

from base64 import b64encode
from katena_chain_sdk_py.exceptions.api_exception import ApiException
from katena_chain_sdk_py.exceptions.client_exception import ClientException
from katena_chain_sdk_py.transactor import Transactor
from katena_chain_sdk_py.utils.crypto import create_private_key_ed25519_from_base64, \
    create_public_key_ed25519_from_base64
from examples.common.settings import Settings
from katena_chain_sdk_py.entity.account.common import DEFAULT_ROLE_ID


def main():
    # Alice wants to create a key for its company

    # Load yaml configuration file
    settings = Settings('settings.yml')

    # Common Katena network information
    api_url = settings.blockchain.api_url
    chain_id = settings.blockchain.chain_id

    # Alice Katena network information
    company_bcid = settings.on_chain.company.bcid
    alice_sign_private_key = create_private_key_ed25519_from_base64(
        settings.on_chain.company.ed25519_keys.alice.private_key)

    # Information Alice want to send
    key_create_uuid = settings.on_chain.tx.uuid
    new_public_key = create_public_key_ed25519_from_base64("gaKih+STp93wMuKmw5tF5NlQvOlrGsahpSmpr/KwOiw=")

    # Role assigned to the key
    new_role = DEFAULT_ROLE_ID

    # Create a Katena API helper
    transactor = Transactor(api_url, chain_id, company_bcid, alice_sign_private_key)

    try:
        # Send a version 1 of a key create on Katena
        tx_status = transactor.send_key_create_v1(key_create_uuid, new_public_key, new_role)

        print("Transaction status")
        print("  Code    : {}".format(tx_status.get_code()))
        print("  Message : {}".format(tx_status.get_message()))
    except (ApiException, ClientException) as e:
        print(e)


main()
