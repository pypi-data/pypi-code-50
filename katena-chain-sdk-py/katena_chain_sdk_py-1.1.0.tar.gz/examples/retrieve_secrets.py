"""
Copyright (c) 2019, TransChain.

This source code is licensed under the Apache 2.0 license found in the
LICENSE file in the root directory of this source tree.
"""

from katena_chain_sdk_py.entity.certify.common import get_type_secret_nacl_box_v1
from katena_chain_sdk_py.exceptions.api_exception import ApiException
from katena_chain_sdk_py.exceptions.client_exception import ClientException
from katena_chain_sdk_py.transactor import Transactor
from katena_chain_sdk_py.utils.crypto import create_private_key_x25519_from_base64
from base64 import b64encode
from examples.common.settings import Settings


def main():
    # Bob wants to read a nacl box secret from Alice to decrypt an off-chain data

    # Load yaml configuration file
    settings = Settings('settings.yml')

    # Common Katena network information
    api_url = settings.blockchain.api_url

    # Alice Katena network information
    company_bcid = settings.on_chain.company.bcid

    # Nacl box information
    bob_decrypt_private_key = create_private_key_x25519_from_base64(
        settings.off_chain.x25519_keys.bob.private_key)

    # Secret uuid Bob wants to retrieve
    secret_uuid = settings.on_chain.tx.uuid

    # Create a Katena API helper
    transactor = Transactor(api_url)

    try:
        # Retrieve version 1 of secrets from Katena
        tx_wrappers = transactor.retrieve_secrets(company_bcid, secret_uuid, 1, settings.blockchain.tx_per_page)

        for tx_wrapper in tx_wrappers.get_txs():
            tx_data = tx_wrapper.get_tx().get_data()

            print("Transaction status")
            print("  Code    : {}".format(tx_wrapper.get_status().get_code()))
            print("  Message : {}".format(tx_wrapper.get_status().get_message()))

            if tx_data.get_type() == get_type_secret_nacl_box_v1():
                print("SecretNaclBoxV1")
                print("  Id                : {}".format(tx_data.get_id()))
                print("  Data sender       : {}".format(b64encode(tx_data.get_sender().get_key()).decode("utf-8")))
                print("  Data nonce        : {}".format(b64encode(tx_data.get_nonce()).decode("utf-8")))
                print("  Data content      : {}".format(b64encode(tx_data.get_content()).decode("utf-8")))

            # Bob will use its private key and the sender's public key (needs to be Alice's) to decrypt a message
            decrypted_content = bob_decrypt_private_key.open(tx_data.get_content(), tx_data.get_sender(),
                                                             tx_data.get_nonce()).decode("utf-8")

            if decrypted_content == "":
                decrypted_content = "Unable to decrypt"

            print("  Decrypted content : {}".format(decrypted_content))
            print()
    except (ApiException, ClientException) as e:
        print(e)


main()
