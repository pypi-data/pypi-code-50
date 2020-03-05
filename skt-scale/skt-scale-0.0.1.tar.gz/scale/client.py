import os
import sys
import time
import fire
import requests
import json
import getpass
from scale.utils import get_job_body, convert_source_file_to_user_command


class Client(object):
    def __init__(self):
        self.config_dir = os.path.join(os.environ.get("HOME", "/tmp"), ".scale")
        if not os.path.exists(self.config_dir):
            os.mkdir(self.config_dir)
        self.config_path = os.path.join(self.config_dir, "config")
        if not os.path.exists(self.config_path):
            with open(self.config_path, "w+") as f:
                default = {"url": None, "token": None, "userId": None}
                json.dump(default, f)

        with open(self.config_path, "r") as f:
            self.conf = json.load(f)

    def config(self, *args):
        self.conf["url"] = args[2]
        with open(self.config_path, "w") as f:
            json.dump(self.conf, f)

    def login(self):
        if not self.conf["url"]:
            print(
                "Please set paas_url using cli ex: scale config set url http://0.0.0.0:13202"
            )
            sys.exit(1)
        paas_id = input("Enter paas id: ")
        paas_paassword = getpass.getpass("Enter paas password: ")
        r = requests.post(
            "{}/api/auth/login".format(self.conf["url"]),
            json={"userId": paas_id, "password": paas_paassword},
        )
        ret = r.json()
        if ret["code"] != 200:
            print("login fail")
            print(ret["message"])
            return
        self.conf["token"] = ret["response"]["token"]
        self.conf["userId"] = paas_id
        with open(self.config_path, "w") as f:
            json.dump(self.conf, f)
        print("login success")

    def create_job(
        self, jobName, imageName, source_file, gpuType=None, gpu=0, cpu=1, mem=1
    ):
        userCmd = convert_source_file_to_user_command(source_file)
        body = get_job_body(
            jobName=jobName,
            imageName=imageName,
            gpuType=gpuType,
            gpu=gpu,
            cpu=cpu,
            mem=mem,
            userCmd=userCmd,
            userId=self.conf["userId"],
        )
        try:
            r = requests.post("{}/api/job".format(self.conf["url"]), json=body)
            if r.status_code != 200:
                print(r.json())
                return
            print("job id: ", r.json()["jobId"])
        except requests.exceptions.RequestException as e:
            print(e)
