#!/usr/bin/env python
# coding: utf-8

import base64
import json
import os
import requests


class MelaxClient:

    def __init__(self, key_path: str = None):
        self.key_path = key_path
        if key_path is not None:
            # read file key
            key = read_key_file(key_path)
            if key is not None:
                key_obj = verify_key(key)
                self.key = key
                self.url = key_obj['url']
                return
        key = os.environ.get("MELAX_TECH_KEY")
        if key is not None:
            key_obj = verify_key(key)
            self.key = key
            self.url = key_obj['url']

    def invoke(self, text: str):
        payload = "{\"input\":\"" + str(base64.b64encode(text.encode("utf-8")), "utf-8") + "\"}"
        rsp = requests.request('POST', self.url, data=payload, headers=headers(self.key))
        if rsp.status_code == 200:
            return {'status_code': 200, 'output': json.loads(json.loads(rsp.content)['output'])}
        return {'status_code': rsp.status_code, 'content': str(rsp.content, 'utf-8')}


def read_key_file(key_path: str):
    with open(key_path, mode='r') as file_obj:
        content = file_obj.read().splitlines()[0]
        return content
    return None


def verify_key(key: str):
    key_tmp = key.split('.')[1]
    if len(key_tmp) % 2 != 0:
        key_tmp += '='
    return json.loads(base64.b64decode(key_tmp))


def headers(key):
    return {'Content-Type': 'application/json', 'tokenHeader': key}

#
# if __name__ == '__main__':
#     client = MelaxClient('/Users/lvjian/Documents/PycharmProjects/melaxtool/key.txt')
#     response = client.invoke("cancer")
#     print(response)
