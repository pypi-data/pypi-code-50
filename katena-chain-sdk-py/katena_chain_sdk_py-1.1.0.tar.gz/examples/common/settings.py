import yaml
import os
from katena_chain_sdk_py.utils.common import DEFAULT_PER_PAGE_PARAM


class Settings:
    # Settings holds the yaml file configuration values
    def __init__(self, file):
        script_dir = os.path.dirname(__file__)

        with open(os.path.join(script_dir, file), 'r') as yamlFile:
            yml_dict = yaml.safe_load(yamlFile)

        self.blockchain = Blockchain(yml_dict['blockchain'])
        self.on_chain = OnChain(yml_dict['on_chain'])
        self.off_chain = OffChain(yml_dict['off_chain'])


class Blockchain:
    # Blockchain communication config
    def __init__(self, yml_dict):
        self.api_url = yml_dict['api_url']
        self.chain_id = yml_dict['chain_id']
        if 'tx_per_page' in yml_dict:
            self.tx_per_page = yml_dict['tx_per_page']
        else:
            self.tx_per_page = DEFAULT_PER_PAGE_PARAM


class OnChain:
    # On chain samples data
    def __init__(self, yml_dict):
        self.tx = Tx(yml_dict['tx'])
        self.company = Company(yml_dict['company'])


class Tx:
    # Common blockchain's transactions infos
    def __init__(self, yml_dict):
        self.uuid = yml_dict['uuid']


class Company:
    # Dummy company abcdef Corp.
    def __init__(self, yml_dict):
        self.bcid = yml_dict['bcid']
        self.ed25519_keys = KeysList(yml_dict['ed25519_keys'])


class OffChain:
    # Off chain samples data
    def __init__(self, yml_dict):
        self.ed25519_keys = KeysList(yml_dict['ed25519_keys'])
        self.x25519_keys = KeysList(yml_dict['x25519_keys'])


class KeysList:
    def __init__(self, yml_dict):
        for item in yml_dict:
            keys_list = list(item.keys())
            setattr(self, keys_list[0], Keys(item[keys_list[0]]))


class Keys:
    def __init__(self, yml_dict):
        self.private_key = yml_dict['private_key']
        self.public_key = yml_dict['public_key']
