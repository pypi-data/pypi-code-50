from secretsmanager.secretsmanager import Secretsmanager
import argparse

def main():
    parser = argparse.ArgumentParser(prog='secretsmanager')
    subparsers = parser.add_subparsers(dest='subcommand')
    ### subcommand create-secret definition ###
    parser_create_secret = subparsers.add_parser('create-secret',help='create a new secret in AWS')
    parser_create_secret.add_argument('--name', required=True, help='the name of the secret stored in AWS')
    parser_create_secret.add_argument('--key', required=True, help='the key of the key/value paired stored by the secret')
    parser_create_secret.add_argument('--value', required=True, help='the value of the key/value paired stored by the secret')
    ### subcommand read-secret-value definition ###
    parser_read_secret_value = subparsers.add_parser('read-secret-value',help='read the content of a secret in aws in AWS')
    parser_read_secret_value.add_argument('--name',required=True, help= 'the name of the secret stored in AWS')
    ### subcommand update-secret definition ###
    parser_update_secret = subparsers.add_parser('update-secret',help='update a secret with a new key/value pair')
    parser_update_secret.add_argument('--name', required=True, help='the name of the secret stored in AWS')
    parser_update_secret.add_argument('--key', required=True, help='the key of the key/value paired stored by the secret')
    parser_update_secret.add_argument('--value', required=True, help='the value of the key/value paired stored by the secret')
    ### subcommand get-keys definition ###
    parser_get_keys = subparsers.add_parser('get-keys',help='get the list of keys for a certain secret')
    parser_get_keys.add_argument('--name', required=True, help='the name of the secret stored in AWS')
    ### subcommand key-present definition ###
    parser_key_present = subparsers.add_parser('key-present',help='check if the secret stores a certain key')
    parser_key_present.add_argument('--name', required=True, help='the name of the secret stored in AWS')
    parser_key_present.add_argument('--key', required=True, help='the key of the key/value paired stored by the secret')
    #### END subcommand definitions ####
    args = parser.parse_args()
    secret_manager = Secretsmanager()
    if args.subcommand == "get-keys":
        print(secret_manager.getKeys(**vars(args)))
    elif args.subcommand == "update-secret":
        print(secret_manager.update(**vars(args)))
    elif args.subcommand == "key-present":
        print(secret_manager.keyPresent(**vars(args)))
    elif args.subcommand == "create-secret":
        print(secret_manager.create(**vars(args)))
    elif args.subcommand == "read-secret-value":
        print(secret_manager.read(**vars(args)))
