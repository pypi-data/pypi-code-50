"""
Copyright (c) 2020, TransChain.

This source code is licensed under the Apache 2.0 license found in the
LICENSE file in the root directory of this source tree.
"""

from base64 import b64encode
from examples.common.settings import Settings
from katena_chain_sdk_py.entity.certify.common import get_type_certificate_raw_v1, get_type_certificate_ed25519_v1
from katena_chain_sdk_py.exceptions.api_exception import ApiException
from katena_chain_sdk_py.exceptions.client_exception import ClientException
from katena_chain_sdk_py.transactor import Transactor


def main():
    # Alice wants to retrieve a certificate

    # Load yaml configuration file
    settings = Settings('settings.yml')

    # Common Katena network information
    api_url = settings.blockchain.api_url

    # Alice Katena network information
    company_bcid = settings.on_chain.company.bcid

    # Certificate id Alice wants to retrieve
    certificate_uuid = settings.on_chain.tx.uuid

    # Create a Katena API helper
    transactor = Transactor(api_url)

    try:
        # Retrieve a certificate, version 1, from Katena
        tx_wrapper = transactor.retrieve_last_certificate(company_bcid, certificate_uuid)
        tx_data = tx_wrapper.get_tx().get_data()

        print("Transaction status")
        print("  Code    : {}".format(tx_wrapper.get_status().get_code()))
        print("  Message : {}".format(tx_wrapper.get_status().get_message()))

        if tx_data.get_type() == get_type_certificate_raw_v1():
            print("CertificateRawV1")
            print("  Id    : {}".format(tx_data.get_id()))
            print("  Value : {}".format(tx_data.get_value().decode("utf-8")))

        if tx_data.get_type() == get_type_certificate_ed25519_v1():
            print("CertificateEd25519V1")
            print("  Id             : {}".format(tx_data.get_id()))
            print("  Data signer    : {}".format(b64encode(tx_data.get_signer().get_key()).decode("utf-8")))
            print("  Data signature : {}".format(b64encode(tx_data.get_signature()).decode("utf-8")))

            """
                In case of ed25519 certificate, we might want to check the certification
                We can achieve this by using:
                1) The signer public key (sender)
                2) The signed data (off-chain data)
                3) The signature from the blockchain

                If the signature of data (2) made with the signer key (1) provides the same value than (3), the certification is valid

                # Create a public key object from the signer key, then verify the certification
                signer_public_key = create_public_key_ed25519_from_base64(b64encode(tx_data.get_signer().get_key()))
                is_valid = signer_public_key.verify("off_chain_data_raw_signature_from_py".encode("utf-8"), tx_data.get_signature())
                print("  Certificate status : {}".format(is_valid))
            """

    except (ApiException, ClientException) as e:
        print(e)


main()
