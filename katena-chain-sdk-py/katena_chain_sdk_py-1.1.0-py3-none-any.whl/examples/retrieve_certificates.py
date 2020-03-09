"""
Copyright (c) 2019, TransChain.

This source code is licensed under the Apache 2.0 license found in the
LICENSE file in the root directory of this source tree.
"""

from base64 import b64encode
from katena_chain_sdk_py.entity.certify.common import get_type_certificate_raw_v1, get_type_certificate_ed25519_v1
from katena_chain_sdk_py.exceptions.api_exception import ApiException
from katena_chain_sdk_py.exceptions.client_exception import ClientException
from katena_chain_sdk_py.transactor import Transactor
from examples.common.settings import Settings


def main():
    # Alice wants to retrieve certificates

    # Load yaml configuration file
    settings = Settings('settings.yml')

    # Common Katena network information
    api_url = settings.blockchain.api_url

    # Alice Katena network information
    company_bcid = settings.on_chain.company.bcid

    # Create a Katena API helper
    transactor = Transactor(api_url)

    # Certificate uuid Alice wants to retrieve
    certificate_uuid = settings.on_chain.tx.uuid

    try:
        # Retrieve version 1 of certificates from Katena
        tx_wrappers = transactor.retrieve_certificates(company_bcid, certificate_uuid, 1,
                                                       settings.blockchain.tx_per_page)

        for tx_wrapper in tx_wrappers.get_txs():
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

            print()
    except (ApiException, ClientException) as e:
        print(e)


main()
