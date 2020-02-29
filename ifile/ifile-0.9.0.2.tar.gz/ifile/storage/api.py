from ifile.storage.mongo import GridFsApi
from ifile.storage.disk import DiskApi
from ifile.db.sqlalchemy import api as db_api
from ifile.common.constant import StorageType
from ifile.exception import NotFound
from ifile import setting as conf


class File(object):
    def __init__(self, id):
        self._id = id
        _file = self._get()

        self.uuid = _file["uuid"]
        self.name = _file["name"]
        self.md5 = _file["md5"]
        self.size = _file["size"]

        storage_type = conf.STORAGE_TYPE

        if storage_type == "mongodb":
            mongo_uri = conf.MONGO_URI
            self.storage = GridFsApi(mongo_uri, "files")

        if storage_type == "disk":
            self.storage = DiskApi()

    def _get(self):
        _file = db_api.get_file(self._id)
        return _file

    @property
    def id(self):
        return self._id

    @property
    def stream(self):
        # TODO 优化异常捕获
        try:
            _file = db_api.get_file(self._id)
            metadata = self.storage.get(_file["uuid"])
            stream = metadata.read()
        except NotFound as e:
            raise NotFound(str(e))

        return stream

    def destroy(self):
        self.storage.destroy(self.uuid)
        db_api.destory_file(self._id)

    def add_stream(self, stream):
        fs = self.storage.add(stream)
        values = {
            "uuid": fs.uuid,
            "md5": fs.md5
        }
        _file = db_api.update_file(self._id, values)
        return _file

    def to_json(self):
        _file = {
            "id": self._id,
            "uuid": self.uuid,
            "name": self.name,
            "md5": self.md5,
            "size": self.size
        }
        return _file


class Files(object):
    def __init__(self):
        self._files = None
        self._refresh()

    def _get_all_from_db(self):
        files_db = db_api.get_files()
        return files_db

    def _refresh(self):
        files_db = self._get_all_from_db()
        self._files = {file_db["id"]: File(file_db["id"])
                       for file_db in files_db}

    def add(self, name, stream):
        file_db = db_api.add_file(name)
        _file = File(file_db.id)
        _file.add_stream(stream)

        self._refresh()
        return _file

    def _destroy(self, id):
        try:
            _file = self._files[id]
            _file.destroy()
        except NotFound as e:
            raise NotFound(str(e))

        self._refresh()

    def to_json(self):
        files = []
        for _, f in self._files.items():
            files.append(f.to_json())
        return files

    def __len__(self):
        return len(self._files)

    def __getitem__(self, id):
        return self._files[id]

    def __delitem__(self, id):
        self._destroy(id)

    def __iter__(self):
        return iter(self._files)
