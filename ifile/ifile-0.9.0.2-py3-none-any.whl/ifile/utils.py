import uuid
import hashlib


def gen_uuid():
    return str(uuid.uuid4())


def get_md5(stream):
    md5_obj = hashlib.md5()
    md5_obj.update(stream)
    hash_code = md5_obj.hexdigest()

    md5 = str(hash_code).lower()

    return md5
