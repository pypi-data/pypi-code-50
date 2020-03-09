# -*- coding: utf-8 -*-
#!/usr/bin/env python
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

import pickle
import MySQLdb
import pandas.io.sql as sql
import numpy as np
from .html_preprocessor import HTMLStripper


def strip_html_from_body(doc):
    s = HTMLStripper()
    s.feed(doc)
    return s.get_data()


class EstimatorClassifier(object):
    SELECT_SQL = (
        "SELECT id, first_name, last_name, email, bio FROM users WHERE spam_type = 'None' AND bio IS NOT NULL AND bio <> '';")
    UPDATE_SQL = """UPDATE users set spam_type = %s, active = %s WHERE id = %s"""

    def __init__(self, db_host, db_user, db_user_password, db_name):
        self.db_host = db_host
        self.db_user = db_user
        self.db_user_password = db_user_password
        self.db_name = db_name

    def classify(self, model_file):
        db = None
        cursor = None
        res = []
        try:
            # Open database connection
            db = MySQLdb.connect(self.db_host, self.db_user, self.db_user_password, self.db_name)
            # prepare a cursor object using cursor() method
            cursor = db.cursor()
            df = sql.read_sql(EstimatorClassifier.SELECT_SQL, db)
            x_test = df.replace(np.nan, '', regex=True)
            x_test['bio'] = x_test['bio'].apply(strip_html_from_body)
            if not x_test.empty:
                with open(model_file, 'rb') as f:
                    classifier = pickle.load(f)
                    predicted = classifier.predict(x_test.drop(['id'], axis=1))
                    for item, type in zip(x_test.to_dict(orient='records'), predicted):
                        active = type == 'Ham'
                        cursor.execute(EstimatorClassifier.UPDATE_SQL, (
                            type,
                            active,
                            item['id']
                        ))

                        res.append((item['id'],type))

            db.commit()
        except Exception as e:
            print(e)
            # Rollback in case there is any error
            db.rollback()
            raise
        finally:
            if not (cursor is None):
                cursor.close()
            # disconnect from server
            if not (db is None):
                db.close()
        return res
