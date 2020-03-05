# Copyright 2014, Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Authors:
#   Martin Krizek <mkrizek@redhat.com>

import resultsdb_api

import json

import pytest
import requests
from dingus import patch


class TestAPI():
    def setup_method(self, method):
        self.rdb_url = "http://0.0.0.0:5000/api/v1.0"
        self.ref_url = "http://example.com/someref"
        self.ref_status = "SCHEDULED"
        self.ref_testcase_name = "testcase"
        self.ref_testcase_url = "http://fedoraqa.fedoraproject.org/testcase"
        self.ref_outcome = "PASSED"
        self.ref_content_type = "application/json"
        self.ref_accept = "text/plain"
        self.ref_job_id = 1
        self.ref_result_id = 1

        self.helper = resultsdb_api.ResultsDBapi(self.rdb_url)

    @patch('requests.post')
    def test_create_testcase(self):
        self.helper.create_testcase(self.ref_testcase_name, self.ref_testcase_url)

        post_calls = requests.post.calls()

        rdb_url = post_calls[0][1][0]
        headers = post_calls[0][2]['headers']
        data = json.loads(post_calls[0][2]['data'])

        assert rdb_url == "%s/testcases" % self.rdb_url
        assert headers['Content-type'] == self.ref_content_type
        assert headers['Accept'] == self.ref_accept
        assert data['url'] == self.ref_testcase_url
        assert data['name'] == self.ref_testcase_name

    @patch('requests.put')
    def test_update_testcase(self):
        self.helper.update_testcase(self.ref_testcase_name, self.ref_testcase_url)

        put_calls = requests.put.calls()

        rdb_url = put_calls[0][1][0]
        headers = put_calls[0][2]['headers']
        data = json.loads(put_calls[0][2]['data'])

        assert rdb_url == "%s/testcases/%s" % (self.rdb_url, self.ref_testcase_name)
        assert headers['Content-type'] == self.ref_content_type
        assert headers['Accept'] == self.ref_accept
        assert data['url'] == self.ref_testcase_url

    @patch('requests.get')
    def test_get_testcase(self):
        self.helper.get_testcase(self.ref_testcase_name)

        get_calls = requests.get.calls()

        rdb_url = get_calls[0][1][0]

        assert rdb_url == "%s/testcases/%s" % (self.rdb_url, self.ref_testcase_name)

    @patch('requests.get')
    def test_get_testcases(self):
        self.helper.get_testcases()

        get_calls = requests.get.calls()

        rdb_url = get_calls[0][1][0]

        assert rdb_url == "%s/testcases" % self.rdb_url

    @patch('requests.post')
    def test_create_job(self):
        self.helper.create_job(self.ref_url)

        post_calls = requests.post.calls()

        rdb_url = post_calls[0][1][0]
        headers = post_calls[0][2]['headers']
        data = json.loads(post_calls[0][2]['data'])

        assert rdb_url == "%s/jobs" % self.rdb_url
        assert headers['Content-type'] == self.ref_content_type
        assert headers['Accept'] == self.ref_accept
        assert data['ref_url'] == self.ref_url

    @patch('requests.put')
    def test_update_job(self):
        self.helper.update_job(id=self.ref_job_id, status=self.ref_status)

        put_calls = requests.put.calls()

        rdb_url = put_calls[0][1][0]
        headers = put_calls[0][2]['headers']
        data = json.loads(put_calls[0][2]['data'])

        assert rdb_url == "%s/jobs/%s" % (self.rdb_url, self.ref_job_id)
        assert headers['Content-type'] == self.ref_content_type
        assert headers['Accept'] == self.ref_accept
        assert data['status'] == self.ref_status

    def test_update_job_invalid(self):
        with pytest.raises(TypeError):
            self.helper.update_job()

    @patch('requests.get')
    def test_get_job(self):
        self.helper.get_job(self.ref_job_id)

        get_calls = requests.get.calls()

        rdb_url = get_calls[0][1][0]

        assert rdb_url == "%s/jobs/%s" % (self.rdb_url, self.ref_job_id)

    def test_get_job_invalid(self):
        with pytest.raises(TypeError):
            self.helper.get_job()

    @patch('requests.get')
    def test_get_jobs(self):
        self.helper.get_jobs()

        get_calls = requests.get.calls()

        rdb_url = get_calls[0][1][0]

        assert rdb_url == "%s/jobs" % self.rdb_url

    @patch('requests.get')
    def test_get_jobs_params(self):
        self.helper.get_jobs(status=self.ref_status)

        get_calls = requests.get.calls()

        rdb_url = get_calls[0][1][0]
        params = get_calls[0][2]['params']

        assert rdb_url == "%s/jobs" % self.rdb_url
        assert params['status'] == self.ref_status

    @patch('requests.post')
    def test_create_result(self):
        self.helper.create_result(self.ref_job_id, self.ref_testcase_name, self.ref_outcome)

        post_calls = requests.post.calls()

        rdb_url = post_calls[0][1][0]
        headers = post_calls[0][2]['headers']
        data = json.loads(post_calls[0][2]['data'])

        assert rdb_url == "%s/results" % self.rdb_url
        assert headers['Content-type'] == self.ref_content_type
        assert headers['Accept'] == self.ref_accept
        assert data['job_id'] == self.ref_job_id
        assert data['testcase_name'] == self.ref_testcase_name
        assert data['outcome'] == self.ref_outcome

    @patch('requests.get')
    def test_get_result(self):
        self.helper.get_result(self.ref_result_id)

        get_calls = requests.get.calls()

        rdb_url = get_calls[0][1][0]

        assert rdb_url == "%s/results/%s" % (self.rdb_url, self.ref_job_id)

    def test_get_result_invalid(self):
        with pytest.raises(TypeError):
            self.helper.get_result()

    @patch('requests.get')
    def test_get_results(self):
        self.helper.get_results()

        get_calls = requests.get.calls()

        rdb_url = get_calls[0][1][0]

        assert rdb_url == "%s/results" % self.rdb_url

    @patch('requests.get')
    def test_get_results_params(self):
        self.helper.get_results(testcase_name=self.ref_testcase_name, job_id=self.ref_job_id)

        get_calls = requests.get.calls()

        rdb_url = get_calls[0][1][0]
        params = get_calls[0][2]['params']

        assert rdb_url == "%s/results" % self.rdb_url
        assert params['testcase_name'] == self.ref_testcase_name
        assert params['job_id'] == str(self.ref_job_id)
