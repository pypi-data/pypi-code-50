import re
import os
import sys
import time
import fire
import requests
import json
import getpass
from scale.utils import get_job_body, convert_source_file_to_user_command
from scale.receive_log import get_log_from_container


class Client(object):
    def __init__(self, user_id=None, url=None, token=None):
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
        if user_id:
            self.conf["userId"] = user_id
        if url:
            self.conf["url"] = url
        if token:
            self.conf["token"] = token

    def _config_check(self):
        for k in self.conf:
            if not self.conf[k]:
                print("need to login to create job\nex) scalecli login")
                sys.exit(1)

    def config(self, *args):
        self.conf["url"] = args[2]
        with open(self.config_path, "w") as f:
            json.dump(self.conf, f)
        print("Updated config")

    def login(self):
        if not self.conf["url"]:
            print(
                "Please set paas_url using cli\nex) scalecli config set url http://0.0.0.0:13202"
            )
            sys.exit(1)
        if sys.version_info[0] == 2:
            paas_id = raw_input("Enter paas id: ")
        else:
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
        self,
        job_name,
        image_name,
        source_file,
        gpu_type=None,
        gpu=0,
        cpu=1,
        mem=1,
    ):
        self._config_check()
        user_cmd = convert_source_file_to_user_command(source_file)
        body = get_job_body(
            job_name=job_name,
            image_name=image_name,
            gpu_type=gpu_type,
            gpu=gpu,
            cpu=cpu,
            mem=mem,
            user_cmd=user_cmd,
            user_id=self.conf["userId"],
        )
        try:
            r = requests.post("{}/api/job".format(self.conf["url"]), json=body)
            if r.status_code != 200:
                print(r.text)
                return
            job_id = r.json()["jobId"]
            print("job id: ", job_id)
            m = re.search(r"http://(.*):\d+", self.conf["url"])
            redis_host = m.group(1)
            print("wait for container to start")
            get_log_from_container(redis_host, job_id)

        except requests.exceptions.RequestException as e:
            print(e)
