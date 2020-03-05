import time
import os
import re
from ada.features import Execution, TestCase, UploadImage


def get_keyword_failed(data, keyword=""):

    for func in data:
        if func["status"] != "PASS":
            if keyword:
                keyword += "."
            keyword += func["kwname"]
            keyword = get_keyword_failed(func["functions"], keyword)
            break
    return keyword


class BaseListener:
    ROBOT_LISTENER_API_VERSION = 2
    API_KEY = ""
    PROJECT_ID = ""

    def __init__(self):
        """Is used to init variables, objects, ... to support for generating report

        Args:
            sampleVar: TBD

        Returns:
            NA

        """
        self.execution = None
        self.dict_exe = {}
        self.arr_exe = []
        self.step = {}

    def start_suite(self, name, attrs):
        """This event will be trigger at the beginning of test suite.

        Args:
            name: TCs name
            attrs: Attribute of test case can be query as dictionary type

        Returns:
            NA

        """
        self.image = []
        self.name = name
        self.index = -1
        parent = None
        if self.arr_exe:
            functions = []
            id_parent = self.arr_exe[-1]
            parent = self.dict_exe[id_parent]
            if id_parent in self.step and self.step[id_parent]:
                functions = self.step[id_parent][0]
            i = 0
            while i < 30:
                try:
                    Execution(self.API_KEY).up_log(
                        parent, functions=functions
                    )
                    break
                except Exception as e:
                    print(e)
                    time.sleep(2)
                    i += 1
        i = 0
        while i < 30:
            try:
                self.execution = Execution(self.API_KEY).create(
                    attrs["longname"], self.PROJECT_ID, attrs["totaltests"],
                    parent=parent, starttime=attrs["starttime"], endtime="",
                    doc=attrs["doc"], source=attrs["source"]
                )
                break
            except Exception as e:
                print(e)
                time.sleep(2)
                i += 1
        self.dict_exe[attrs["id"]] = self.execution
        self.step[attrs["id"]] = {}
        self.arr_exe.append(attrs["id"])

    def end_suite(self, name, attrs):

        function = []
        if attrs["id"] in self.step and self.step[attrs["id"]]:
            function = self.step[attrs["id"]][0]
        i = 0
        while i < 30:
            try:
                Execution(self.API_KEY).up_log(
                    self.dict_exe[attrs["id"]], log_teardown="this is log teardown",
                    status="complete", functions=function, duration=attrs["elapsedtime"],
                    endtime=attrs["endtime"]
                )
                break
            except Exception as e:
                print(e)
                time.sleep(2)
                i += 1
        del self.arr_exe[-1]

    def start_test(self, name, attrs):
        self.image = []
        self.step[name] = {}
        self.index = -1
        self.start_time = time.time()
        self.arr_exe.append(name)

    def end_test(self, name, attrs):
        failed_keyword = ""
        if attrs['status'] == 'PASS':
            status = "passed"
        else:
            status = "failed"
            failed_keyword = get_keyword_failed(self.step[name][0])
        i = 0
        result = None
        while i < 30:
            try:
                if not result:
                    result = TestCase(self.API_KEY).create(
                        name, status, attrs["elapsedtime"], self.execution,
                        failed_reason=attrs["message"], functions=self.step[name][0],
                        starttime=attrs["starttime"], endtime=attrs["endtime"],
                        failed_keyword=failed_keyword
                    )
                if result and self.image:
                    print(self.image)
                    UploadImage(self.API_KEY).create(result, self.image)
                break
            except Exception as e:
                time.sleep(2)
                i += 1
                print("test_case:", e)
        self.step[name] = {}
        del self.arr_exe[-1]
        self.image = []

    def start_keyword(self, name, attrs):
        self.log_test = []
        self.index += 1
        self.step[self.arr_exe[-1]].setdefault(self.index, [])

    def end_keyword(self, name, attrs):
        # print("end key ", attrs)

        attrs["functions"] = []
        attrs["log"] = self.log_test
        index = self.index + 1
        key = self.arr_exe[-1]
        if index in self.step[key] and self.step[key][index]:
            attrs["functions"] = self.step[key][index]
            self.step[key][index] = []
        self.step[key][self.index].append(attrs)
        self.index -= 1
        self.log_test = []
        self.check = True

    def log_message(self, msg):
        message = msg["message"]
        result = re.search("(([<]([\w\W\-.\/]+\.(png|jpg))[>])|([\w-]+\.(png|jpg)))", message)
        real_image = None
        if result:
            data = result.group(1).strip("<>")
            if "/" in data or "\\" in data:
                image_path = data
                if "/" in data:
                    image = data.split("/")[-1]
                else:
                    image = data.split("\\")[-1]
            else:
                image_path = os.path.join(os.getcwd(), data.strip())
                image = data
            try:
                if os.path.isfile(image_path):
                    self.image.append(('screenshot', open(image_path, "rb")))
                    real_image = image
            except:
                pass
        msg["image"] = real_image
        self.log_test.append(msg)

    # def message(self, msg):
    #     print('\n Listener detect message: %s' %(msg))

    def close(self):
        print('\n Close Suite')