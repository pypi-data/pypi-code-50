import os
import json
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

from gradefast.result import ResultGroup

class Upload: # pragma: no cover

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    # TODO: Add support for result_group csv
    @staticmethod
    def make_result_group(result_group):
        if isinstance(result_group, ResultGroup):
            return result_group
        elif isinstance(result_group, str):
            if os.path.isfile(result_group):
                extension = Path(result_group).suffix[1:]
                if extension == 'json':
                    return ResultGroup.from_json(result_group)
                elif extension == 'csv':
                    return ResultGroup.from_csv(result_group)
        raise Exception("")

    @staticmethod
    def upload(result_group, cookie, upload_url='', task_no=''):
        result_group = Upload.make_result_group(result_group)
        base_url = 'http://portal.e-yantra.org/admin/grade/'
        if upload_url == None or upload_url == '':
            upload_url = base_url + result_group.task.lower()
            penalty_url = base_url + 'penalty' + task.lower()
            marks_url = base_url + 'marksTask' + task.lower()


class Uploader:
    pass

class DefaultUploader:
    pass
