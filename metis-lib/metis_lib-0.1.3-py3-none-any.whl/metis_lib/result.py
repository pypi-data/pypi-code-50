import sys
import json
import os


def success(msg):
    if isinstance(msg, list) or isinstance(msg, dict):
        msg = json.dumps(msg, ensure_ascii=False)

    sys.stdout.write('__METIS_SUCCESS_LOG__' + msg + os.linesep + '__METIS_SUCCESS_LOG__')
    sys.stdout.flush()


def error(msg):
    if isinstance(msg, list) or isinstance(msg, dict):
        msg = json.dumps(msg, ensure_ascii=False)

    sys.stderr.write('__METIS_ERROR_LOG__' + msg + os.linesep + '__METIS_ERROR_LOG__')
    sys.stderr.flush()
