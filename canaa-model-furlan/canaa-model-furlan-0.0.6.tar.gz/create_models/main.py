import argparse
import sys

from create_models.create_files import create_files
from create_models.example import print_example
from create_models.logging import get_logger
from create_models.model_creator import ModelCreator

from . import __version__, __description__

_usage = """

Get an metadata model example:
    canaa-model --example

Validate an metadata model
    canaa-model -f metadata_model.csv --just-validate

Generate models from metadata model
    canaa-model -f metadata_model.csv -d output_folder

"""
_testing_args = None


def main():
    print(f'\n{__description__} v{__version__}\n')

    parser = argparse.ArgumentParser(
        description='{0} v{1}'.format(__description__, __version__),
        usage=_usage)
    parser.add_argument('--file', '-f',
                        dest='file_name',
                        help='model metadata file (csv)')
    parser.add_argument('--destiny', '-d',
                        dest='destiny_folder',
                        help='destiny folder',
                        required=('--file' in sys.argv or '-f' in sys.argv) and not('--just-validate' in sys.argv))
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
    parser.add_argument('--old-canaa-base',
                        dest='old_canaa_base',
                        action='store_true',
                        help='used for old versions of canaa_base (<0.4.8)')
    parser.set_defaults(ignore_field_errors=False,
                        just_validate=False,
                        example=False,
                        old_canaa_base=False)

    if _testing_args:
        args = parser.parse_args(_testing_args)
    else:
        args = parser.parse_args()
    if args.example:
        print(print_example())
        if _testing_args:
            return
        exit(0)

    if not args.file_name or not args.destiny_folder:
        parser.print_help()
        if _testing_args:
            return
        exit(0)

    log = get_logger()
    try:
        if args.just_validate:
            args.ignore_field_errors = False
        mc = ModelCreator(
            file_name=args.file_name,
            ignore_field_errors=args.ignore_field_errors,
            just_validate=args.just_validate)
        if mc.is_ok and not args.just_validate:

            create_files(mc, args.destiny_folder,
            old_canaa_base=args.old_canaa_base)
    except Exception as exc:
        log.exception('EXCEPTION: %s', exc)


if __name__ == "__main__":
    main()
