import os
import json
import tempfile

from .logging import get_logger

__cache_folder: str = None

_log = get_logger()


def init():
    global __cache_folder
    if not __cache_folder:
        __cache_folder = os.path.join(os.getcwd(), '.cache')
        if not os.path.isdir(__cache_folder):
            try:
                os.makedirs(__cache_folder)
                _log.info('JSON CACHE: %s', __cache_folder)
            except Exception as exc:
                _log.warning('JSON CACHE CREATION ERROR: %s', str(exc))
                __cache_folder = os.path.join(
                    tempfile.gettempdir(), 'canaa-base-model-creator-cache')

            if not os.path.isdir(__cache_folder):
                try:
                    os.makedirs(__cache_folder)
                    _log.info('JSON CACHE: %s', __cache_folder)
                except Exception as exc:
                    _log.error('JSON CACHE CREATION ERROR: %s', str(exc))
                    __cache_folder = 0

    return isinstance(__cache_folder, str)


def _cache_file(model_type, model_name):
    if init():
        return os.path.join(
            __cache_folder,
            "{0}.{1}.json".format(model_type, model_name))
    return ""


def get_model_json(model_type: str, model_name: str):
    cache_file = _cache_file(model_type, model_name)
    result = None
    if cache_file:
        try:
            with open(cache_file) as f:
                result = json.loads(f.read())
        except Exception as exc:
            _log.error('ERROR ON READ MODEL JSON : %s - %s',
                       cache_file,
                       str(exc))
    return result


def set_model_json(model_type: str, model_name: str, model: dict) -> bool:
    cache_file = _cache_file(model_type, model_name)
    result = False
    if cache_file:
        try:
            with open(cache_file, 'w') as f:
                j = json.dumps(model, default=str)
                result = f.write(j) > 0
        except Exception as exc:
            _log.error('ERROR ON WRITE MODEL JSON : %s - %s',
                       cache_file,
                       str(exc))
    return result
