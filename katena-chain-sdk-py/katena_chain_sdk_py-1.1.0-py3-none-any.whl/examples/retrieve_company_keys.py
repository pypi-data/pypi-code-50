"""
Copyright (c) 2020, TransChain.

This source code is licensed under the Apache 2.0 license found in the
LICENSE file in the root directory of this source tree.
"""

from base64 import b64encode
from examples.common.settings import Settings
from katena_chain_sdk_py.exceptions.api_exception import ApiException
from katena_chain_sdk_py.exceptions.client_exception import ClientException
from katena_chain_sdk_py.transactor import Transactor


def main():
    # Alice wants to retrieve the keys of its company

    # Load yaml configuration file
    settings = Settings('settings.yml')

    # Common Katena network information
    api_url = settings.blockchain.api_url

    # Alice Katena network information
    company_bcid = settings.on_chain.company.bcid

    # Create a Katena API helper
    transactor = Transactor(api_url)

    try:
        # Retrieve the keys from Katena
        keys = transactor.retrieve_company_keys(company_bcid, 1, settings.blockchain.tx_per_page)

        for key in keys:
            print("KeyV1")
            print("  Company bcid : {}".format(key.get_company_bcid()))
            print("  Public key   : {}".format(b64encode(key.get_public_key().get_key()).decode("utf-8")))
            print("  Is active    : {}".format(key.get_is_active()))
            print("  Role         : {}".format(key.get_role()))
            print()
    except (ApiException, ClientException) as e:
        print(e)


main()
