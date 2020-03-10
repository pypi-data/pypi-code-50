# -*- coding: UTF-8 -*-

import oss2

import xcli
from xcli import PyCliConfig


def get_bucket_name(config: PyCliConfig):
    service = oss2.Service(config.auth, config.endpoint)
    bucket_list = [b.name for b in oss2.BucketIterator(service)]

    return bucket_list


def get_bucket(config: PyCliConfig):
    return oss2.Bucket(config.auth, config.endpoint, config.bucket)


def publish(oss_key, apk_abspath):
    """
    上传apk文件到OSS上

    :param oss_key: oss key
    :param apk_abspath: apk绝对路径
    :return:
    """
    # 上传OSS
    config = xcli.load_config()
    config.auth = oss2.Auth(config.access_key_id, config.access_key_secret)
    oss_bucket = get_bucket(config)

    oss_bucket.put_object_from_file(oss_key, apk_abspath)
    with open(apk_abspath, 'rb') as apk_file_object:
        # 验证上传的文件与本地文件是否一致
        verify_result = oss_bucket.get_object(oss_key).read() == apk_file_object.read()

    return verify_result
