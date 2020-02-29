from pymongo import MongoClient
from gridfs import GridFS

from ifile.storage.base import FileApiBase
from ifile.utils import gen_uuid


class GridFsApi(FileApiBase):

    def __init__(self, uri, collection):
        client = MongoClient(uri)
        database = client.get_database()
        self._gridfs = GridFS(database, collection)

    def get(self, uuid):
        """Get a file by uuid"""
        grid_file = self._gridfs.find_one({"uuid": uuid})
        return grid_file

    def add(self, bdata, uuid=None):
        """Insert bdata"""
        if uuid is None:
            uuid = gen_uuid()

        object_id = self._gridfs.put(bdata, uuid=uuid)
        grid_file = self._gridfs.get(object_id)
        return grid_file

    def destroy(self, uuid):
        """Destroy file"""
        grid_file = self.get(uuid)
        self._gridfs.delete(grid_file._id)

    def get_bdata_by_uuid(self, uuid):
        """Get bdata by uuid"""
        grid_file = self.gridfs_api.get(uuid)
        bdata = grid_file.read()

        return bdata
