import json
import requests
from requests.models import Response

from typing import Tuple, Union

from retrying import retry


@retry(stop_max_attempt_number=3, wait_random_min=1000, wait_random_max=3000)
def __auth(host_url: str, project_name: str, user_access_key: str) -> Response:
    # TODO(himanshu): http->https
    auth_server = 'http://%s' % host_url
    if host_url == 'ingestionapi.scrybetool.com':
        auth_server = 'https://%s' % host_url
    url = '%s/v1/scrybeinit?project_name=%s' % (auth_server, project_name)
    resp = requests.get(url=url, headers={'Content-Type': 'application/json', 'user-access-key': str(user_access_key)})
    resp.raise_for_status()
    return resp


def authenticate(host_url: str, user_access_key: str, project_name: str) -> Union[None, Tuple]:
    try:
        resp = __auth(host_url=host_url, project_name=project_name, user_access_key=user_access_key)
        json_resp = json.loads(resp.content.decode('utf-8'))
        return json_resp['project'], json_resp['user'], json_resp.get('dashboard_server_addr')
    except requests.exceptions.HTTPError as err:
        print(err.response.content)
        return None


