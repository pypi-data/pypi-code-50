import json
import requests


class ApiAsana:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            'Accept': '/',
            'Accept-Encoding': 'gzip, deflate',
            'Authorization': token,
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json'
        }

    def get_workspaces(self, fields: list = []) -> list:
        url = f'{self.base_url}/workspaces'
        response = requests.get(url=url, headers=self.headers, params={'opt_fields': fields})
        return response.json().get('data', [])

    def get_teams(self, workspace, fields: list = []) -> list:
        url = f'{self.base_url}/organizations/{workspace}/teams'
        response = requests.get(url=url, headers=self.headers, params={'opt_fields': fields})
        return response.json().get('data', [])

    def get_projects(self, worspace, team, fields: list = []) -> list:
        url = f'{self.base_url}/projects'
        params = {
            'workspace': worspace,
            'team': team,
            'opt_fields': fields
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        return response.json().get('data', [])

    def get_tasks(self, project: int, fields: list = []) -> list:
        url = f'{self.base_url}/tasks'
        params = {
            'project': project,
            'opt_fields': fields
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        return response.json().get('data', [])

    def get_task_by_id(self, task_gid, fields: list = []) -> dict:
        url = f'{self.base_url}/tasks/{task_gid}'
        response = requests.get(url=url, headers=self.headers, params={'opt_fields': fields})
        return response.json().get('data', {})

    def get_events(self, resource, sync='') -> tuple:
        url = f'{self.base_url}/events'
        params = {
            'resource': resource,
            'sync': sync
        }
        response = requests.get(url, params=params, headers=self.headers)
        obj = response.json()
        return obj.get('data', []), obj.get('sync', '')

    def patch_task(self, task_gid: int, data: dict) -> tuple:
        url = f'{self.base_url}/tasks/{task_gid}'
        response = requests.put(url=url, data=json.dumps({'data': data}), headers=self.headers)
        return response.ok, response.json().get('data', {})

    def add_custom_field_to_project(self, project_gid: int, custom_field: int) -> bool:
        url = f'{self.base_url}/projects/{project_gid}/addCustomFieldSetting'
        response = requests.post(url=url, data=json.dumps({}), params={'custom_field': custom_field},
                                 headers=self.headers)
        return response.ok

    def get_webhooks(self, workspace: int, fields: list = []) -> list:
        url = f'{self.base_url}/webhooks'
        params = {
            'workspace': workspace,
            'opt_fields': fields
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        return response.json().get('data', [])

    def post_webhook(self, resource: str, target: str) -> tuple:
        url = f'{self.base_url}/webhooks'
        response = requests.post(
            url=url,
            headers=self.headers,
            data=json.dumps({
                'data': {
                    'resource': resource,
                    'target': target
                }
            })
        )
        return response.ok, response.json()

    def get_user_mail(self, gid) -> str:
        url = f'{self.base_url}/users/{gid}'
        response = requests.get(url=url, headers=self.headers)
        return response.json().get('data', {}).get('email', '')
