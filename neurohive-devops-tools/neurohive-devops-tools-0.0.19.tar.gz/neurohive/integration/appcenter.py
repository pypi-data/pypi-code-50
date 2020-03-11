import logging
import sys
import json
import os

import requests
from requests.exceptions import RequestException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class AppCenterWrapperException(Exception):
    pass


class AppCenter:
    def __init__(self, owner: str) -> None:
        self.token = os.environ['APPCENTER_API_TOKEN']
        self.owner = owner
        self.headers = {
            'Content-Type': 'application/json',
            'X-API-Token': self.token
        }
        self.base_url = 'https://api.appcenter.ms'

    def get_new_idids(self, app_name: str, distr_grp_name: str) -> list():
        url = f'{self.base_url}/v0.1/apps/{self.owner}/{app_name}/distribution_groups/{distr_grp_name}/devices'
        try:
            req = requests.get(url, headers=self.headers)
        except RequestException as e:
            logging.error(e)
            sys.exit(1)
        if req.status_code == 200:
            to_provision = [d for d in req.json() if d.get('status') != 'provisioned']
            return to_provision
        else:
            logging.error(req.text)

    def get_apps(self):
        url = f'{self.base_url}/v0.1/apps'
        req = requests.get(url, headers=self.headers)
        print([app['name'] for app in req.json()])

    def cleanup_old_builds(self, app_name, leave_num=30):
        logging.info(f"delete {app_name} builds")
        builds = self._get_builds_for_app(app_name)
        builds = sorted(builds, key=lambda x: x["id"])[0:-leave_num]
        if builds:
            for build in builds:
                self._delete_release_by_id(app_name, build)

    def _get_builds_for_app(self, app_name):
        url = f'{self.base_url}/v0.1/apps/{self.owner}/{app_name}/releases'
        req = requests.get(url, headers=self.headers)
        if req.status_code != 200:
            logger.error(req.text)
            raise AppCenterWrapperException('Error getting builds for app')
        return req.json()

    def _delete_release_by_id(self, app_name, build):
        logging.info(f'delete id:{build["id"]}, ver:{build["short_version"]}')
        url = f'{self.base_url}/v0.1/apps/{self.owner}/{app_name}/releases/{build["id"]}'
        req = requests.delete(url, headers=self.headers)
        if req.status_code != 200:
            raise AppCenterWrapperException("Error delete build")
