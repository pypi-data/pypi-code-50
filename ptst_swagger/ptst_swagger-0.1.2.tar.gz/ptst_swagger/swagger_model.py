__author__ = 'v.denisov'

import json
import os
from ptst_swagger.model.tests_to_swagger import TestsToSwagger


class SwaggerModel:

    def __init__(self):
        _record_test = None
        _record_test_list = None

    @property
    def record_test(self):
        return self._record_test

    @record_test.setter
    def set_record_test(self, value):
        self._record_test = value

    @property
    def record_test_list(self):
        return self._record_test_list

    @record_test_list.setter
    def set_record_test_list(self, r_list):
        self._record_test_list = r_list

    @classmethod
    def record_test_to_list(self, method, path, text):
        if not isinstance(method,str):
            method = str(method)
        if not isinstance(path,str):
            path = str(path)
        if not isinstance(text,str):
            text = str(text)

        if isinstance(self.record_test_list, property):
            self.record_test_list=[]
        r_list = self.record_test_list
        r_l_n = 0
        for r_l in r_list:
            if (r_l.method in method) and (r_l.path in path) and len(r_l.path)==len(path):
                r_list[r_l_n].text = str(int(r_l.text)+1)
                break
            r_l_n = r_l_n + 1
        else:
            r_list.append(TestsToSwagger(method=method, path=path, text=text))
        self.record_test_list = r_list

        file_type = os.path.join(os.getcwd(), 'tests.json')
        with open(file_type, 'w') as out:
            r_test_dict = []
            for r_test in self.record_test_list:
                r_test_dict.append({"method":r_test.method, "path":r_test.path, "text":r_test.text})
            json.dump(r_test_dict, out,  indent=4)
