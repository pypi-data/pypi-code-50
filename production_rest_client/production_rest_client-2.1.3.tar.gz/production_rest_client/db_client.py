# coding=utf-8
# pylint: disable=wrong-import-position, relative-import, import-error
from .resources.benchmark_db_resource import BenchmarkDBResource


class PerfDBClient(object):

    def __init__(self):
        self.benchmark_db = BenchmarkDBResource(db_name="performance_test")

    def search(self, test_key=None, project_name=None, begin_time=None, end_time=None, test_name=None):
        """
        :param project_name: project name, like tahoe, alpha
        :param begin_time: format: '%Y%m%d', e.g. 20170601
        :param end_time: format: '%Y%m%d', e.g. 201901101
        :param test_name:
        :param test_key:
        :return:
        """
        test_results = list()
        if test_key is None:
            search_str = self.benchmark_db.get_search_match_string(test_key, project_name, begin_time, end_time, test_name)
            results = self.benchmark_db.execute_sql_command(search_str)
            group_key_list = [item[4] for item in results if item[4] is not None]
            group_key_list = list(set(group_key_list))
        else:
            group_key_list = test_key
        for group_key in group_key_list:
            results = self.benchmark_db.search_tests_by_group_key(group_key)
            test = {
                "name": results[0][2],
                "project_name": results[0][3],
                "start_time": results[0][11],
                "end_time": results[0][12],
                "tester": results[0][14],
                "test_key": group_key,
                "environment": self.benchmark_db.get_env_by_index(results[0][0]),
                "confirm": results[0][15]
            }
            test_results.append(test)
        return test_results

    def get_test_detail_information(self, test_key):
        results = self.benchmark_db.search_tests_by_group_key(test_key)
        test_steps = list()
        for item in results:
            step = {
                "index":item[0],
                "name":item[1],
                "group_name": item[2],
                "key":item[10],
                "start_time":item[11],
                "end_time":item[12],
                "state":item[13],
                "duration": self.benchmark_db.get_duration(item[11], item[12]),
                "environment": self.benchmark_db.get_env_by_index(item[0]),
                "summary_report": self.benchmark_db.get_summary_report_by_index(item[0]),
                "configuration": self.benchmark_db.get_test_config(item[0])}
            test_steps.append(step)
        return test_steps

    def get_step_detail_information(self, step_key):
        result = self.benchmark_db.search_step_by_key(step_key)[0]
        step = {
            "index":result[0],
            "name":result[1],
            "group_name": result[2],
            "key":result[10],
            "start_time":result[11],
            "end_time":result[12],
            "state":result[13],
            "duration":self.benchmark_db.get_duration(result[11], result[12]),
            "environment": self.benchmark_db.get_env_by_index(result[0]),
            "summary_report": self.benchmark_db.get_summary_report_by_index(result[0]),
            "configuration": self.benchmark_db.get_test_config(result[0])}
        return step

    def get_real_time_results(self, key, mini_index=None):
        """

        :param key: the test which want to get the real time
        :param mini_index: get the real time data index more then the mini_index
        :return:
        """
        index = self.benchmark_db.get_index_by_key(key)
        result = self.benchmark_db.get_real_time_results(index, mini_index)
        return result

    def get_test_state(self, key):
        index = self.benchmark_db.get_index_by_key(key)
        return self.benchmark_db.get_test_state(index)

    def get_index_by_key(self, key):
        return self.benchmark_db.get_index_by_key(key)

    def confirm_test(self, key):
        self.benchmark_db.confirm_test(key)
#
# if __name__ == '__main__':
#     P = PerfDBClient()
#     # TESTS = P.search(test_key=["20191112163727_eHvhCh5eNg"])
#     # for TEST in TESTS:
#     A = P.get_real_time_results("bESbBodFVf")
#         # for item in A:
#         #     D = P.get_step_detail_information(item["key"])
#         #     C = P.get_real_time_results(item["key"], 1000)
#         #     pass
