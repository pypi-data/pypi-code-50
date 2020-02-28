from .Storage import Storage, DataNotFound


class FileStorage(Storage):
    def read(self, path):
        try:
            file = open(self.getPath(path), "rb")
            return file.read()
        except FileNotFoundError:
            raise DataNotFound("Data was not found:" + path)

    def write(self, path, data):
        file = open(self.getPath(path), "wb")
        file.write(data)
        file.close()
