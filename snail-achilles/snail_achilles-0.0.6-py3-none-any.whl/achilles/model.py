import os
import sys
import requests


class Model(object):
    SERVER_HOST = "achilles.insnail.com"
    PROTOCOL = "https"  # or http

    def __init__(self, project_slug, model_slug, version):
        self.project_slug = project_slug
        self.model_slug = model_slug
        self.version = version

    def get_model_url(self) -> str:
        data = {
            "project_slug": self.project_slug,
            "model_slug": self.model_slug,
            "version": self.version,
        }
        rp = requests.post(self.server_address, data=data)
        if rp.status_code == 200:
            url = rp.json()["url"]
            return url

    def get_model_content(self) -> bytes:
        url = self.get_model_url()
        content = requests.get(url).content
        return content

    def save_model(self, save_path):
        if os.path.exists(save_path):
            sys.stdout.write(f"[{save_path}] exists!")
        else:
            sys.stdout.write(f"model [{self.version}] downloading...")
            with open(save_path, "wb") as f:
                content = self.get_model_content()
                f.write(content)

    @property
    def server_address(self):
        assert self.SERVER_HOST, "Host is Illegal!!!"
        server_address = f"{self.PROTOCOL}://{self.SERVER_HOST}/warehouse/model_url/"
        return server_address
