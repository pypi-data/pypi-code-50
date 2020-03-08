import os
import logging
import hashlib

from ifile.storage.base import FileApiBase
from ifile.utils import gen_uuid, gen_data_path
from ifile import setting as conf

logger = logging.getLogger(__name__)


class FileMetaData(object):
    def __init__(self, uuid):

        self.uuid = uuid

        data_path = gen_data_path()
        self.path = os.path.join(data_path, uuid)

    def read(self):
        bdata = None
        with open(self.path, 'rb') as f:
            bdata = f.read()
        return bdata

    @property
    def stream(self):
        return self.read()

    @property
    def md5(self):
        hash_obj = hashlib.md5()
        hash_obj.update(self.stream)

        return hash_obj.hexdigest()

    @property
    def is_exist(self):
        return os.path.exists(self.path)

    def destroy(self):
        if self.is_exist is True:
            os.remove(self.path)


class DiskApi(FileApiBase):

    def __init__(self):
        self.data_path = gen_data_path()

    def get(self, uuid):
        metadata = FileMetaData(uuid)
        if metadata.is_exist is False:
            return None
        return metadata

    def add(self, bdata, uuid=None):
        if uuid is None:
            uuid = gen_uuid()

        metadata = FileMetaData(uuid)
        logger.info(f"writing file {uuid}, path: {metadata.path}")

        with open(metadata.path, 'wb') as f:
            if type(bdata) == bytes:
                f.write(bdata)
            else:
                f.write(bdata.read())

        return metadata

    def destroy(self, uuid):
        metadata = FileMetaData(uuid)
        if metadata.is_exist is False:
            raise

        metadata.destroy()

    def get_bdata_by_uuid(self, uuid):
        metadata = FileMetaData(uuid)
        if metadata.is_exist is False:
            raise

        return metadata.stream
