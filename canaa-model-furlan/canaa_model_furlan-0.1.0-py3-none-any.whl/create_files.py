import os

from .create_dto import create_dto
from .create_ms_json import create_ms_json
from .create_ms_model import create_ms_model
from .create_promax_json import create_promax_json
from .create_promax_model import create_promax_model
from .logging import get_logger
from .model_creator import ModelCreator

log = get_logger()


def create_files(model: ModelCreator, destiny_folder: str, **kwargs):

    log.info('Creating model files for {0}'.format(model))

    destiny_folder = os.path.abspath(destiny_folder)

    namespace_promax = "" if not model.info.namespace_promax else model.info.namespace_promax
    namespace_ms = "" if not model.info.namespace_ms else model.info.namespace_ms

    promax_model_folder = os.path.join(
        destiny_folder, 'domain', 'models', 'promax', namespace_promax)
    promax_file = os.path.join(
        promax_model_folder, model.promax_model_file_name)

    ms_model_folder = os.path.join(
        destiny_folder, 'domain', 'models', 'microservice', namespace_ms)
    ms_file = os.path.join(ms_model_folder, model.ms_model_file_name)

    dto_folder = os.path.join(
        destiny_folder, 'domain', 'models', 'dtos', namespace_ms)
    dto_file = os.path.join(dto_folder, model.dto_file_name)
    old_canaa_base = 'old_canaa_base' in kwargs and kwargs['old_canaa_base']

    mock_folder = os.path.join(destiny_folder, 'domain', 'mocks', namespace_ms)

    try:
        folders = []
        for folder in [promax_model_folder, ms_model_folder, dto_folder, mock_folder]:
            if not os.path.isdir(folder):
                os.makedirs(folder)
                create_init(folder)
                folders.append(folder+" [created]")
            else:
                folders.append(folder)
        for folder in folders:
            log.info("Folder: {0}".format(folder))

    except Exception as exc:
        log.error("Folder error: %s", str(exc))
        return False

    return process_files(model, promax_file, ms_file, dto_file, old_canaa_base, mock_folder)


def process_files(model, promax_file, ms_file, dto_file, old_canaa_base, mock_folder):
    processes = {
        "PROMAX": {
            "file": promax_file,
            "method": create_promax_model,
            "json": create_promax_json
        },
        "MICROSERVICE": {
            "file": ms_file,
            "method": create_ms_model,
            "json": create_ms_json
        },
        "DTO": {
            "file": dto_file,
            "method": create_dto,
            "json": lambda x, y: True
        }
    }
    try:
        for process in processes:
            filename = processes[process]['file']
            method = processes[process]['method']
            create_json = processes[process]['json']

            content = method(model, old_canaa_base)
            if os.path.isfile(filename):
                os.remove(filename)

            with open(filename, 'w') as f:
                f.write(content)

            if os.path.isfile(filename):
                log.info('Created %s: %s', process, filename)
            else:
                raise Exception(
                    "File not found after generation: {0}".format(filename))

            create_init(filename)
            create_json(model, mock_folder)

        log.info('Files created successfully!')
        return True

    except Exception as exc:
        log.error('Error on creating %s: %s - %s',
                  process,
                  filename,
                  str(exc))

    return False


def create_init(folder):
    if os.path.isfile(folder):
        folder = os.path.dirname(folder)

    init_file = os.path.join(folder, '__init__.py')
    if not os.path.isfile(init_file):
        with open(init_file, 'w') as f:
            f.write(f'"""{folder}"""\n')
    folder = os.path.dirname(folder)
