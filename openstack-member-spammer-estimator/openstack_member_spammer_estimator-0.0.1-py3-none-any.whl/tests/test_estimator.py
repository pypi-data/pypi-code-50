# -*- coding: utf-8 -*-
# !/usr/bin/env python
#
# Copyright (c) 2020 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
import openstack_member_spammer_estimator
import os


class EstimatorBuildTest(unittest.TestCase):

    def setUp(self):
        self.db_host = os.getenv("DB_TEST_HOST")
        self.db_user = os.getenv("DB_TEST_USER")
        self.db_user_password = os.getenv("DB_TEST_USER_PASSWORD")
        self.db_name = os.getenv("DB_TEST")

        if not self.db_host:
            self.skipTest("No DB_TEST_HOST set")
        if not self.db_user:
            self.skipTest("No DB_TEST_USER set")
        if not self.db_user_password:
            self.skipTest("No DB_TEST_USER_PASSWORD set")
        if not self.db_name:
            self.skipTest("No DB_TEST set")

    def test_model_builder_from_zero(self):

        builder = openstack_member_spammer_estimator.EstimatorBuilder(
            host=self.db_host,
            user=self.db_user,
            password=self.db_user_password,
            db=self.db_name
        )
        script_dir = os.path.dirname(__file__)
        pickle_file = os.path.join(script_dir, 'member_classifier.pickle')

        if os.path.exists(pickle_file):
            os.remove(pickle_file)

        builder.populate(os.path.join(script_dir, '../openstack_member_spammer_estimator/initial_spam_feed.json'))
        builder.build()

        self.assertTrue(os.path.exists(pickle_file))

    def test_complete(self):

        builder = openstack_member_spammer_estimator.EstimatorBuilder(
            host=self.db_host,
            user=self.db_user,
            password=self.db_user_password,
            db=self.db_name
        )

        script_dir = os.path.dirname(__file__)
        pickle_file = os.path.join(script_dir, 'member_classifier.pickle')

        if os.path.exists(pickle_file):
            os.remove(pickle_file)

        builder.populate(os.path.join(script_dir, '../openstack_member_spammer_estimator/initial_spam_feed.json'))
        builder.build()

        self.assertTrue(os.path.exists(pickle_file))

        classifier = openstack_member_spammer_estimator.EstimatorClassifier(
            host=self.db_host,
            user=self.db_user,
            password=self.db_user_password,
            db=self.db_name
        )

        res = classifier.classify(pickle_file)

        self.assertTrue(len(res) > 0 )


if __name__ == '__main__':
    unittest.main()
