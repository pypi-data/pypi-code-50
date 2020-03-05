from ada.base import BaseADA


class UploadImage(BaseADA):
    url = "test-case/"

    def create(self, folder, files):
        return super(UploadImage, self).create_form(folder, files)
