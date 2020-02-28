from pyupdater.core.uploader import BaseUploader
from pyupdater.utils.exceptions import UploaderError

import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


class AzureBlobStorageUploader(BaseUploader):

    name = "azure-blob"
    author = "Tom Hill"

    def init_config(self, config):

        # get the connection string
        # TODO: put this into environent variable
        self.connection_string = config["connection_string"]
        if self.connection_string is None:
            raise UploaderError("Missing connection_string", expected=True)

        # get the blob container name
        self.blob_container_name = config["blob_container_name"]
        if self.blob_container_name is None:
            raise UploaderError("Missing blob_container_name", expected=True)

        self._connect()

    def set_config(self, config):
        config["connection_string"] = self.get_answer(
            "Please enter Azure Storage connection string\n--> "
        )
        config["blob_container_name"] = self.get_answer(
            "Please enter the blob container name\n--> "
        )

    def _connect(self):
        self.blob_service_client = BlobServiceClient.from_connection_string(
            self.connection_string
        )
        self.container_client = self.blob_service_client.get_container_client(
            self.blob_container_name
        )

    def upload_file(self, filename):
        """Uploads a file to Azure Blob storage"""

        filename_only = os.path.basename(filename)

        # if file already exists
        for b in self.container_client.list_blobs(name_starts_with=filename_only):
            self.container_client.delete_blob(filename_only, delete_snapshots="include")
            break  # there will be only one

        # create the blob
        blob = self.blob_service_client.get_blob_client(
            container=self.blob_container_name, blob=filename_only
        )

        try:
            with open(filename, "rb") as data:
                blob.upload_blob(data)

            print("Uploaded", filename_only)
            return True
        except Exception as err:
            print("Failed to upload", filename_only)
            print(err)

            self._connect()

            return False
