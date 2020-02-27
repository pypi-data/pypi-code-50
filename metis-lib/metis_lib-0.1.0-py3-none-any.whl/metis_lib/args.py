import json
import os


def loads(default=None):
    args = os.environ.get('METIS_ARGS', None)
    args = args if args else default or '{}'

    return json.loads(args) if isinstance(args, str) else args
