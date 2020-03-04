#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function

# import github
# import gitlab
import json

from .tools import http_request


class RepoGitee:
    def __init__(self, token=None):
        self.tokenAccess = token

    def projects(self):
        page = 1
        total_page = 1
        all_json = []
        while page <= total_page:
            url = 'https://gitee.com/api/v5/orgs/yocopen/repos?access_token=%s&type=all&page=%d&per_page=100' % (
                self.tokenAccess, page)
            headers = {'Content-Type': 'application/json;charset=UTF-8'}

            code, data, headers = http_request('GET', url, headers=headers)
            if code == 200:
                total_page = int(headers['total_page'])
                for v in json.loads(data):
                    all_json.append(v['description'])
            page += 1

        return all_json

    def create_project(self, name, description=''):
        url = 'https://gitee.com/api/v5/orgs/yocopen/repos'
        headers = {'Content-Type': 'application/json;charset=UTF-8'}

        data = {
            "access_token": self.tokenAccess,
            "name": name, "has_issues": "true", "has_wiki": "true", "private": "true",
            "description": description,
            # "license_template":"Apache-2.0",
        }
        code, data, _ = http_request('POST', url, json.dumps(data), headers)
        if code == 201:
            v = json.loads(data)
            return v['ssh_url']
        else:
            return self.update_project(name, description)

    def get_project(self, name):
        url = 'https://gitee.com/api/v5/repos/yocopen/%s?access_token=%s' % (
            name, self.tokenAccess)
        headers = {'Content-Type': 'application/json;charset=UTF-8'}

        data = {
            "access_token": self.tokenAccess,
            "name": name, "has_issues": "true", "has_wiki": "true", "private": "true"
        }
        code, data, _ = http_request('GET', url, headers=headers)
        if code == 200:
            v = json.loads(data)
            return v['ssh_url']

    def remove_project(self, name):
        url = 'https://gitee.com/api/v5/repos/yocopen/%s?access_token=%s' % (
            name, self.tokenAccess)

        headers = {'Content-Type': 'application/json;charset=UTF-8'}

        code, data, _ = http_request('DELETE', url, headers=headers)
        if code != 204:
            v = json.loads(data)
            return False, v['message']

        return True, ''

    def branch_to_tag(self, name, branch, tag_name):
        # curl -X POST --header 'Content-Type: application/json;charset=UTF-8'
        # 'https://gitee.com/api/v5/repos/yocopen/newlib/releases'
        # -d '{"access_token":"211f69d3691cd241f123df4d6d98ed80",
        # "tag_name":"v7.2.1","name":"v7.2.1","body":"v7.2.1","target_commitish":"v7.2-dev"}'
        url = 'https://gitee.com/api/v5/repos/yocopen/%s/releases' % name

        headers = {'Content-Type': 'application/json;charset=UTF-8'}

        data = {
            "access_token": self.tokenAccess,
            "tag_name": tag_name,
            "name": tag_name, "body": tag_name,
            "target_commitish": branch
        }
        code, data, _ = http_request('POST', url, json.dumps(data), headers)
        if code == 201:
            v = json.loads(data)
        else:
            v = json.loads(data)
            print(v)

    def update_project(self, name, description=''):
        # curl -X PATCH --header 'Content-Type: application/json;charset=UTF-8'
        # 'https://gitee.com/api/v5/repos/yocopen/yunvoice' -d '{"access_token":"661bc4c24596496dae61a2079288475c","name":"yunvoice",
        # "description":"{\"name\": \"yunvoice\", \"description\": \"yunvoice\", \"versions\": \"v7.2-dev\", \"license\": \"\", \"type\": \"common\", \"depends\": []}",
        # "has_issues":"true","has_wiki":"true"}
        # '

        url = 'https://gitee.com/api/v5/repos/yocopen/' + name
        headers = {'Content-Type': 'application/json;charset=UTF-8'}

        data = {
            "access_token": self.tokenAccess,
            "name": name, "has_issues": "true", "has_wiki": "true", "private": "true",
            "description": description,
            # "license_template":"Apache-2.0",
        }
        code, data, _ = http_request('PATCH', url, json.dumps(data), headers)
        if code == 200:
            v = json.loads(data)
            return v['ssh_url']
        else:
            v = json.loads(data)
            print(v)
            # return self.get_project(name)

# class RepoGithub:
#     def __init__(self, token=None):
#         self.gl = github.Github(token, timeout=30)
#         self.organization = self.gl.get_organization('yoc-components')

#     def projects(self):
#         for repo in self.organization.get_repos():
#             print(repo.name, repo)
#         projects = self.gl.projects.list(
#             owned=True, all=True, namespace_id='6883967')
#         return projects

#     def create_project(self, name):
#         try:
#             project = self.organization.create_repo(name)
#             return project.ssh_url
#         except github.GithubException as e:
#             return 'git@github.com:yoc-components/' + name + '.git'
#             print(e)

#     def branch_to_tag(self, name, branch, tag_name):
#         project = self.organization.get_repo(name)
#         print(project)

#         for tag in project.get_tags():
#             if tag.name == tag_name:
#                 return

#         for br in project.get_branches():
#             if br.name == branch:
#                 print(br)
#                 tag = project.create_git_tag(
#                     tag_name, 'Created from tag %s' % br.name, br.commit.sha, 'commit')
#                 if tag:
#                     project.create_git_ref('refs/tags/%s' % tag_name, tag.sha)
#                 break

# class RepoGitlab:
#     def __init__(self):
#         url = 'https://gitlab.com'
#         token = 'KaPY7CR2Fsu4dm_71Zro'

#         self.gl = gitlab.Gitlab(url, token)

#     def projects(self):
#         projects = self.gl.projects.list(
#             owned=True, all=True, namespace_id='6883967')
#         for p in projects:
#             print(p.name, p.ssh_url_to_repo)

#     def create_project(self, name):
#         try:
#             project = self.gl.projects.create(
#                 {'name': name, 'namespace_id': '6883967'})

#             return project.ssh_url_to_repo

#         except gitlab.GitlabCreateError as e:
#             print(e.error_message)
#             project = self.gl.projects.get('occ-thead/' + name)
#             return project.ssh_url_to_repo
