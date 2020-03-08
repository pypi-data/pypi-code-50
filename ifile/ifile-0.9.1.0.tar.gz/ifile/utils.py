import os
import uuid
import hashlib

from ifile import setting as conf


def gen_uuid():
    return str(uuid.uuid4())


def get_md5(filename):
    myhash = hashlib.md5()
    f = open(filename, 'rb')

    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    hash_code = myhash.hexdigest()
    f.close()

    md5 = str(hash_code).lower()
    return md5


def gen_data_path():
    data_path = conf.DATA_PATH
    if data_path is None:
        data_path = os.path.join(conf.APP_HOME, 'data/')

    if not os.path.exists(data_path):
        os.makedirs(data_path)

    return data_path
