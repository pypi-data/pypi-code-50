#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .params import Params


def makeParamsFromArguments(*args, **kwargs):
    if 'params' in kwargs:
        x = kwargs.pop('params', None)
        if isinstance(x, (Params,)):
            params = x
        elif isinstance(x, (dict,)):
            params = Params()
            for k, v in x.items():
                params[k] = v
        else:
            raise TypeError('Invalid type of params')
    else:
        params = Params()

    for idx, x in enumerate(args):
        if isinstance(x, (Params,)):
            for k, v in x.items():
                params[k] = v
        else:
            params['arg_{}'.format(idx)] = x

    for k, v in kwargs.items():
        params[k] = v

    return params


def ensure_unicode(x):
    import sys
    if sys.version_info < (3, 0):
        if isinstance(x, (unicode,)):
            return x
        elif isinstance(x, (str,)):
            return x.decode('utf-8')
        return unicode(x)
    else:
        if isinstance(x, (bytes,)):
            return x.decode('utf-8')
        return x


def has_pyflink():
    try:
        import pkg_resources
        pkg_resources.get_distribution("pyalink-flink-1.9")
    except:
        return True
    return False


def get_alink_lib_path() -> str:
    import pyalink
    import os
    for path in pyalink.__path__:
        lib_path = os.path.join(path, "lib")
        if os.path.isdir(lib_path):
            return lib_path
    raise Exception("Cannot find pyalink Java libraries, please check your installation.")


def get_pyflink_path() -> str:
    if has_pyflink():
        import pyflink
        import os
        for path in pyflink.__path__:
            if os.path.isdir(path):
                return path
    else:
        alink_lib_path = get_alink_lib_path()
        import os
        for f in os.listdir(alink_lib_path):
            path = os.path.join(alink_lib_path, f)
            if f.startswith("flink-") and os.path.isdir(path):
                return path
    print("Cannot find pyflink path, if you're not running using 'flink run', please check if PyFlink is installed correctly.")
