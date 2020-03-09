"""
Copyright (c) 2019, TransChain.

This source code is licensed under the Apache 2.0 license found in the
LICENSE file in the root directory of this source tree.
"""

from katena_chain_sdk_py.exceptions.api_exception import ApiException
from katena_chain_sdk_py.exceptions.client_exception import ClientException
from katena_chain_sdk_py.transactor import Transactor
from katena_chain_sdk_py.utils.crypto import create_private_key_ed25519_from_base64, \
    create_private_key_x25519_from_base64, create_public_key_x25519_from_base64
from examples.common.settings import Settings


def main():
    # Alice wants to send a nacl box secret to Bob to encrypt an off-chain data

    # Load yaml configuration file
    settings = Settings('settings.yml')

    # Common Katena network information
    api_url = settings.blockchain.api_url
    chain_id = settings.blockchain.chain_id

    # Alice Katena network information
    company_bcid = settings.on_chain.company.bcid
    alice_sign_private_key = create_private_key_ed25519_from_base64(
        settings.on_chain.company.ed25519_keys.alice.private_key)

    # Nacl box information
    alice_encrypt_private_key = create_private_key_x25519_from_base64(
        settings.off_chain.x25519_keys.alice.private_key)
    bob_decrypt_public_key = create_public_key_x25519_from_base64(
        settings.off_chain.x25519_keys.bob.public_key)

    # Off-chain information Alice wants to send to Bob
    secret_uuid = settings.on_chain.tx.uuid
    content = "off_chain_secret_to_crypt_from_py"

    # Alice uses its private key and Bob's public key to encrypt the message
    encrypted_message, nonce = alice_encrypt_private_key.seal(content.encode("utf-8"), bob_decrypt_public_key)

    # Create a Katena API helper
    transactor = Transactor(api_url, chain_id, company_bcid, alice_sign_private_key)

    try:
        # Send a version 1 of a secret nacl box on Katena
        tx_status = transactor.send_secret_nacl_box_v1(secret_uuid, alice_encrypt_private_key.get_public_key(), nonce,
                                                       encrypted_message)

        print("Transaction status")
        print("  Code    : {}".format(tx_status.get_code()))
        print("  Message : {}".format(tx_status.get_message()))
    except (ApiException, ClientException) as e:
        print(e)


main()
