import glob
import os

from create_models.logging import get_logger
from create_models.model_creator import ModelCreator
from create_models.create_files import create_files

log = get_logger()


def create_list_of_files(origin: str):
    try:
        if os.path.isdir(origin):
            files = glob.glob(os.path.join(origin, '*.csv'))
        elif os.path.isfile(origin):
            files = [origin]
        elif '*' in origin or '?' in origin:
            files = glob.glob(origin)
        else:
            raise FileNotFoundError(origin)
    except Exception as exc:
        log.error('Error on get files from %s - %s', origin, str(exc))
        files = []

    return files


def create_list_of_model_creators(origin: str, just_validate: bool, ignore_field_errors: bool):
    models_ok = []
    models_error = []
    try:
        files = create_list_of_files(origin)
        if len(files) == 0:
            log.warning('No models found in %s', origin)
            return []

        for file in files:
            mc = ModelCreator(file_name=file,
                              ignore_field_errors=ignore_field_errors,
                              just_validate=just_validate)
            if mc.is_ok:
                models_ok.append(mc)
            else:
                models_error.append(mc)

        if len(models_ok) > 0:
            models_ok = sorted(
                models_ok, key=lambda x: '1' if x.has_non_primitive_fields else '0')

        if len(models_error) > 0:
            log.warning('Models with errors: %s', models_error)

        if len(models_ok) > 0:
            log.info('Models OK: %s', models_ok)

    except Exception as exc:
        log.error('Error on creating list of models: %s', str(exc))

    return models_ok


def process_files(origin: str, destiny_folder: str, just_validate: bool, ignore_field_errors: bool, old_canaa_base: bool):
    success = False
    try:
        if just_validate:
            ignore_field_errors = False

        file_list = create_list_of_model_creators(
            origin, just_validate, ignore_field_errors)
        if len(file_list) == 0:
            return False
        success = True
        for mc in file_list:
            if mc.is_ok and not just_validate:
                success &= create_files(mc, destiny_folder,
                                        old_canaa_base=old_canaa_base)

    except Exception as exc:
        log.exception('EXCEPTION: %s', exc)
        success = False

    return success
