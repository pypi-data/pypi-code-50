import unittest
from time import sleep
import os
import random
import requests
from datetime import datetime, timezone, timedelta
from myoperator.apm.decorators import collect_external_io_metrics, collect_function_duration_metrics
from myoperator.apm.metrics import create_external_io_duration_metric_name
from myoperator.apm.metrics import create_function_duration_metric_name

PROMETHEUS_API_URL = os.environ.get('PROMETHEUS_API_URL', 'http://localhost:9090/api/v1/query')
METRIC_PREFIX = 'myoperator'

def get_prometheus_data(params):
    return requests.get(PROMETHEUS_API_URL,
                params = params
            )


class TestDecorators(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_collect_external_io_metrics_decrator(self):

        @collect_external_io_metrics(METRIC_PREFIX, service_name='test_service')
        def dummy_func():
            choice = [True, False]
            sel_choice = random.choice(choice)
            if sel_choice:
                raise RuntimeError('Error')
            sleep(1)

        dt = datetime.now()
        start_time = dt.replace(tzinfo=timezone.utc).timestamp()
        try:
            dummy_func()
            sleep(1)
        except RuntimeError:
            pass

        end_time = (dt + timedelta(seconds=1)).replace(tzinfo=timezone.utc).timestamp()
        expected_metric_name = create_external_io_duration_metric_name(METRIC_PREFIX) + '_count'
        response = get_prometheus_data({
                'query': expected_metric_name ,
                'start': start_time,
                'end': end_time
            })

        data = response.json()
        self.assertTrue(response.ok)
        self.assertTrue(data['data']['result'])

        result = data['data']['result']
        for item in result:
            self.assertEqual(item['metric']['service_name'], 'test_service')

    def test_collect_function_metrics_decorator(self):
        @collect_function_duration_metrics(METRIC_PREFIX, function_name='test_dummy_func')
        def dummy_func():
            choice = [True, False]
            sel_choice = random.choice(choice)
            if sel_choice:
                raise RuntimeError('Error')
            sleep(1)

        dt = datetime.now()
        start_time = dt.replace(tzinfo=timezone.utc).timestamp()
        try:
            dummy_func()
        except RuntimeError:
            pass

        end_time = (dt + timedelta(seconds=0.1)).replace(tzinfo=timezone.utc).timestamp()
        expected_metric_name = create_external_io_duration_metric_name(METRIC_PREFIX) + '_count'
        response = get_prometheus_data({
                'query': expected_metric_name ,
                'start': start_time,
                'end': end_time
            })

        data = response.json()
        self.assertTrue(response.ok)
        self.assertTrue(data['data']['result'])

        result = data['data']['result']
        for item in result:
            self.assertEqual(item['metric']['service_name'], 'test_service')

if __name__ == '__main__':
    unittest.main()

