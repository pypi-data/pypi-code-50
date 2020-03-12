import argparse
import sys
import os

from create_models.create_files import create_files
from create_models.example import print_example
from create_models.logging import get_logger
from create_models.model_creator import ModelCreator
from create_models.process_files import process_files, create_list_of_files

from . import __version__, __description__

_usage = """

Gets an metadata model example:
    canaa-model --example

Validates an metadata model
    canaa-model --source metadata_model.csv --just-validate

Generates models from metadata model
    canaa-model --source metadata_model.csv --destiny output_folder

    canaa-model --source metadata_models_folder --destiny output_folder

"""
_testing_args = None


def create_parser():
    parser = argparse.ArgumentParser(
        description='{0} v{1}'.format(__description__, __version__),
        usage=_usage)
    parser.add_argument('--source', '-s',
                        dest='source',
                        help='model metadata file (csv) or folder with csv files (you can use * and ? masks)',
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument('--destiny', '-d',
                        dest='destiny_folder',
                        help='Path to create "model" folder and DTO, Promax and Microservice python files and JSON mocks (default = current directory)',
                        required=(
                            '--source' in sys.argv or '-s' in sys.argv) and not('--just-validate' in sys.argv),
                        type=lambda x: is_valid_folder(parser, x))
    parser.add_argument('--ignore-field-errors',
                        dest='ignore_field_errors',
                        action='store_true',
                        help='Don´t stop process when detect error on field definition')
    parser.add_argument('--just-validate',
                        dest='just_validate',
                        action='store_true',
                        help='Just validate model metadata file')
    parser.add_argument('--example', '-e',
                        dest='example',
                        action='store_true',
                        help='print example of metadata file')
    parser.add_argument('--version', '-v',
                        dest='version',
                        action='store_true')
    parser.add_argument('--foo',
                        action="store_true",
                        help=argparse.SUPPRESS)
    parser.set_defaults(ignore_field_errors=False,
                        just_validate=False,
                        example=False,
                        old_canaa_base=False,
                        version=False,
                        destiny_folder='.')

    return parser


def is_valid_file(parser, arg):
    files = create_list_of_files(arg)
    if len(files) == 0:
        if _testing_args:
            raise FileNotFoundError(arg)
        sys.exit(2)
    else:
        return arg


def is_valid_folder(parser, arg):
    if not os.path.isdir(arg):
        if _testing_args:
            raise FileNotFoundError(arg)
        parser.error("The folder %s does not exist!" % arg)
    else:
        return os.path.abspath(arg)


def show_version(_testing_args):
    print(f'{__description__} v{__version__}')
    if _testing_args:
        return True
    exit(0)


def main():
    # print(f'{__description__} v{__version__}')

    parser = create_parser()

    if _testing_args:
        args = parser.parse_args(_testing_args)
        sys.argv.append(_testing_args)
    else:
        args = parser.parse_args()

    if args.example:
        return print_example(_testing_args)

    if args.version:
        return show_version(_testing_args)

    if not args.source:
        parser.print_help()
        if _testing_args:
            return False
        exit(1)

    if not args.just_validate and not args.destiny_folder:
        if _testing_args:
            return False
        parser.error("")

    source = args.source
    destiny_folder = args.destiny_folder

    return process_files(source, destiny_folder, args.just_validate,
                         args.ignore_field_errors, args.old_canaa_base)


if __name__ == "__main__":
    main()
