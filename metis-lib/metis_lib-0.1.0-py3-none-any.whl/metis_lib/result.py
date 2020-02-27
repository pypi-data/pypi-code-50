import sys
import json
import os


def success(msg):
    if isinstance(msg, list) or isinstance(msg, dict):
        msg = json.dumps(msg, ensure_ascii=False)

    sys.stdout.write(msg + os.linesep)
    sys.stdout.flush()


def error(msg):
    if isinstance(msg, list) or isinstance(msg, dict):
        msg = json.dumps(msg, ensure_ascii=False)

    sys.stderr.write(msg + os.linesep)
    sys.stderr.flush()
