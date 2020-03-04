import os
from requests.auth import HTTPBasicAuth
import requests
from datetime import datetime, timedelta


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
        page = 0
        created_on_not_later = datetime.utcnow() - timedelta(hours=1)
        created_on_not_later = created_on_not_later.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        result = list()
        while True:
            page = page + 1
            resp = self._api_get('/pipelines/?sort=-created_on&page={page}'.format(page=page))

            if resp['pagelen'] == 0:
                print('No more results returned form API')
                return result

            for val in resp['values']:
                if val['created_on'] < created_on_not_later:
                    print('Stopping on (1 hour diff): {}: {}'.format(val['build_number'], val['created_on']))
                    return result
                if val['build_number'] > number:
                    print('Skipping (number higher): {}: {}'.format(val['build_number'], val['created_on']))
                    continue

                if (val['target']['ref_type'] == 'branch' and
                        val['target']['ref_name'] == branch and
                        val['state']['name'] == 'IN_PROGRESS'):
                    print('Adding to results {}: {}'.format(val['build_number'], val['created_on']))
                    result.append(val['build_number'])

        return None

    def find_pipeline_up(self, branch, number):
        page = 0
        result = list()
        while True:
            page = page + 1
            resp = self._api_get('/pipelines/?sort=-created_on&page={page}'.format(page=page))

            if resp['pagelen'] == 0:
                print('No more results returned form API')
                return result

            for val in resp['values']:
                if val['build_number'] < number:
                    print('Stopping on (number lower): {}: {}'.format(val['build_number'], val['created_on']))
                    return result

                if (val['target']['ref_type'] == 'branch' and
                        val['target']['ref_name'] == branch and
                        val['state']['name'] == 'IN_PROGRESS'):
                    print('Adding to results {}: {}'.format(val['build_number'], val['created_on']))
                    result.append(val['build_number'])

        return None

    def stop_pipeline(self, number):
        resp = self._api_post('/pipelines/{number}/stopPipeline'.format(number=number))

        if resp.status_code != 204:
            raise Exception("Wasn't able to stop pipeline {}: {}: {}".format(number, r.status_code, r.content))

    def _api_post(self, url):
        if not url.startswith('/'):
            url = '/' + url

        resp = requests.post('https://api.bitbucket.org/2.0/repositories/{team}/{repo_name}{url}'.format(
            team=os.environ.get('BITBUCKET_WORKSPACE'),
            repo_name=os.environ.get('BITBUCKET_REPO_SLUG'),
            url=url
        ),
            headers={'Authorization': 'JWT {jwt_token}'.format(jwt_token=os.environ.get('PIPELINES_JWT_TOKEN'))},
            # auth=HTTPBasicAuth(os.environ.get('BITBUCKET_USERNAME'), os.environ.get('BITBUCKET_PASSWORD'))
        )

        if resp.status_code >= 400:
            resp.raise_for_status()

        return resp.json()

    def _api_get(self, url):
        if not url.startswith('/'):
            url = '/' + url

        resp = requests.get('https://api.bitbucket.org/2.0/repositories/{team}/{repo_name}{url}'.format(
            team=os.environ.get('BITBUCKET_WORKSPACE'),
            repo_name=os.environ.get('BITBUCKET_REPO_SLUG'),
            url=url
        ),
            headers={'Authorization': 'JWT {jwt_token}'.format(jwt_token=os.environ.get('PIPELINES_JWT_TOKEN'))},
            # auth=HTTPBasicAuth(os.environ.get('BITBUCKET_USERNAME'), os.environ.get('BITBUCKET_PASSWORD'))
        )

        if resp.status_code >= 400:
            resp.raise_for_status()

        return resp.json()
