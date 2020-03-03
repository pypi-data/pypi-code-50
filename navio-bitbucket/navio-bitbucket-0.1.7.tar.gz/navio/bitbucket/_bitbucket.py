import os
from requests.auth import HTTPBasicAuth
from requests import Request, Session

import requests


class Bitbucket():

    def __init__(self, **kwargs):
        pass

    def is_bitbucket(self):
        if os.environ.get('CI', 'false') == 'true':
            return True
        else:
            return False

    def is_pull_request(self):
        if self.is_bitbucket() and os.environ.get('BITBUCKET_PR_ID', None) is not None:
            return True
        else:
            return False

    def branch(self):
        if self.is_bitbucket():
            return os.environ.get('BITBUCKET_BRANCH')
        else:
            return 'master'

    def commit_hash(self):
        return os.environ.get('BITBUCKET_COMMIT', '0' * 30)

    def short_commit_hash(self):
        return os.environ.get('BITBUCKET_COMMIT', '0' * 30)[:7]

    def tag(self):
        return os.environ.get('BITBUCKET_TAG', None)

    def is_tag(self):
        if os.environ.get('BITBUCKET_TAG', False):
            return True
        else:
            return False

    def home_dir(self):
        return os.environ.get('HOME', '/dev/null')

    def build_dir(self):
        return os.environ.get('BITBUCKET_CLONE_DIR', '/dev/null')

    def find_pipeline_down(self, branch, number):
        s = Session()
        while number > 1:
            number = number - 1
            prep = self._api_get('/pipelines/{number}'.format(number=number))
            r = s.send(prep).json()
            if (r['target']['ref_type'] == 'branch' and
                    r['target']['ref_name'] == branch and
                    r['state']['name'] == 'IN_PROGRESS'):
                return number

        return None

    def find_pipeline_up(self, branch, number):
        s = Session()
        while True:
            number = number + 1
            prep = self._api_get('/pipelines/{number}'.format(number=number))
            resp = s.send(prep)
            if resp.status_code == 404:
                return None

            r = resp.json()
            if (r['target']['ref_type'] == 'branch' and
                    r['target']['ref_name'] == branch and
                    r['state']['name'] == 'IN_PROGRESS'):
                return number

    def stop_pipeline(self, number):
        s = Session()
        prep = self._api_post('/pipelines/{number}/stopPipeline'.format(number=number))
        resp = s.send(prep)
        if resp.status_code != 204:
            raise Exception("Wasn't able to stop pipeline {}: {}: {}".format(number, r.status_code, r.content))

    def _api_post(self, url):
        if not url.startswith('/'):
            url = '/' + url
        return Request('POST', 'https://api.bitbucket.org/2.0/repositories/{team}/{repo_name}{url}'.format(
            team=os.environ.get('BITBUCKET_WORKSPACE'),
            repo_name=os.environ.get('BITBUCKET_REPO_SLUG'),
            url=url
        ),
            headers={'Authorization': 'JWT {jwt_token}'.format(jwt_token=os.environ.get('PIPELINES_JWT_TOKEN'))},
            # auth=HTTPBasicAuth(os.environ.get('BITBUCKET_USERNAME'), os.environ.get('BITBUCKET_PASSWORD'))
        ).prepare()

    def _api_get(self, url):
        if not url.startswith('/'):
            url = '/' + url
        return Request('GET', 'https://api.bitbucket.org/2.0/repositories/{team}/{repo_name}{url}'.format(
            team=os.environ.get('BITBUCKET_WORKSPACE'),
            repo_name=os.environ.get('BITBUCKET_REPO_SLUG'),
            url=url
        ),
            headers={'Authorization': 'JWT {jwt_token}'.format(jwt_token=os.environ.get('PIPELINES_JWT_TOKEN'))},
            # auth=HTTPBasicAuth(os.environ.get('BITBUCKET_USERNAME'), os.environ.get('BITBUCKET_PASSWORD'))
        ).prepare()
