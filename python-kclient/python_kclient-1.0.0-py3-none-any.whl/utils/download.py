import shutil
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def download(client, link, target):
    http = urllib3.PoolManager()
    link = client.configuration.host + link
    headers = {}
    auth_settings = client.configuration.auth_settings()
    for s in auth_settings:
        if auth_settings[s]['in'] == 'header':
            headers[auth_settings[s]['key']] = auth_settings[s]['value']
    with http.request('GET', link, preload_content=False, headers=headers) as resp, open(target, 'wb') as out_file:
        shutil.copyfileobj(resp, out_file)
    resp.release_conn()