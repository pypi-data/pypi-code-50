# Copyright (c) 2017 Santosh Philip
# =======================================================================
#  Distributed under the MIT License.
#  (See accompanying file LICENSE or copy at
#  http://opensource.org/licenses/MIT)
# =======================================================================

"""get the environmental variables
will get the heroku env vars or the local env files"""
# Extract the Environmental variables as a defaultdict
from collections import defaultdict
import os


def getenvars(fhandle=None, defvalue=None, remoteKV=None, defaultfilename='.env'):
    """get the environmental variables
    will get the heroku env vars or the local env files"""
    if remoteKV is None:
        remoteKV = ("ENV_NOW", "production")
    # -
    osdct = os.environ
    try:
        if osdct[remoteKV[0]] == remoteKV[1]:
            keyval = [(key, value) for key, value in osdct.items()]
    except KeyError:
        if not fhandle:
            try:
                fhandle = open(defaultfilename, 'r')
            except FileNotFoundError as e:
                dct = defaultdict(lambda: defvalue)
                return dct
        lines = [line.split('#')[0].strip() for line in fhandle.readlines()]
        lines = [line for line in lines if line]
        keyval = [line.split("=") for line in lines]
        keyval = [(key.strip(), value.strip()) for key, value in keyval]
    # -
    # from https://www.accelebrate.com/blog/using-defaultdict-python/
    dct = defaultdict(lambda: defvalue)
    for key, value in keyval:
        dct[key] = value
    return dct


def dictvalue(dct, key, defvalue=None):
    """return the value of the dct given the key.
    return default value if key does not exist"""
    return dct.setdefault(key, defvalue)
