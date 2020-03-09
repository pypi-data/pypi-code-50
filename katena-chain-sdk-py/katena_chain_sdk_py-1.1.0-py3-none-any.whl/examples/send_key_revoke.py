"""
Copyright (c) 2020, TransChain.

This source code is licensed under the Apache 2.0 license found in the
LICENSE file in the root directory of this source tree.
"""

from katena_chain_sdk_py.exceptions.api_exception import ApiException
from katena_chain_sdk_py.exceptions.client_exception import ClientException
from katena_chain_sdk_py.transactor import Transactor
from katena_chain_sdk_py.utils.crypto import create_private_key_ed25519_from_base64, \
    create_public_key_ed25519_from_base64
from examples.common.settings import Settings


def main():
    # Alice wants to revoke a key for its company

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
    key_revoke_uuid = settings.on_chain.tx.uuid
    public_key = create_public_key_ed25519_from_base64("gaKih+STp93wMuKmw5tF5NlQvOlrGsahpSmpr/KwOiw=")

    # Create a Katena API helper
    transactor = Transactor(api_url, chain_id, company_bcid, alice_sign_private_key)

    try:
        # Send a key revoke, version 1, to Katena
        tx_status = transactor.send_key_revoke_v1(key_revoke_uuid, public_key)

        print("Transaction status")
        print("  Code    : {}".format(tx_status.get_code()))
        print("  Message : {}".format(tx_status.get_message()))
    except (ApiException, ClientException) as e:
        print(e)


main()
