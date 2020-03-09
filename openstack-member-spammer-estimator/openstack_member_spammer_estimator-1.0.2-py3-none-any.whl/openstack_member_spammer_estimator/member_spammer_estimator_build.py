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
import MySQLdb
import pandas.io.sql as sql
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import HashingVectorizer, CountVectorizer, TfidfTransformer
import pickle
from sklearn.pipeline import Pipeline, FeatureUnion
from .data_frame_column_extracter import DataFrameColumnExtracter
from .html_preprocessor import StripHTMLTransformer
import json
import datetime


class EstimatorBuilder(object):

    SELECT_SQL = "SELECT email, first_name, last_name, bio, spam_type FROM users_spam_estimator_feed;"
    TRUNCATE_SQL = "TRUNCATE TABLE users_spam_estimator_feed;"
    INSERT_SQL_SPAM =  """INSERT INTO users_spam_estimator_feed (created_at, updated_at, first_name, last_name, email, bio, spam_type)
      VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    INSERT_SQL_HAM = """INSERT INTO users_spam_estimator_feed
(created_at, updated_at, first_name, last_name, email, bio, spam_type)
SELECT UTC_TIMESTAMP(), UTC_TIMESTAMP() ,first_name, last_name, email, bio , spam_type FROM users 
WHERE users.spam_type = 'Ham' LIMIT 0, 500;"""

    def __init__(self, filename , db_host, db_user, db_user_password, db_name):
        self.db_host = db_host
        self.db_user = db_user
        self.db_user_password = db_user_password
        self.db_name = db_name
        self.filename = filename

    def populate(self, file):
        db = None
        cursor = None
        try:
            with open(file, 'r') as f:
                loaded_json = json.load(f)

            db = MySQLdb.connect(self.db_host, self.db_user, self.db_user_password, self.db_name)
            cursor = db.cursor()
            now = datetime.datetime.utcnow()
            cursor.execute(EstimatorBuilder.TRUNCATE_SQL)
            # spam sample
            for user in loaded_json:
                cursor.execute(EstimatorBuilder.INSERT_SQL_SPAM,(
                    now.strftime('%Y-%m-%d %H:%M:%S'),
                    now.strftime('%Y-%m-%d %H:%M:%S'),
                    user['FirstName'],
                    user['Surname'],
                    user['Email'],
                    user['Bio'],
                    'Spam',
                ))

            # ham sample

            cursor.execute(EstimatorBuilder.INSERT_SQL_HAM)

            db.commit()

        except Exception as e:
            print(e)
            # Rollback in case there is any error
            if not (db is None):
                db.rollback()
            raise

        finally:
            if not (cursor is None):
                cursor.close()
            # disconnect from server
            if not (db is None):
                db.close()

    def build(self):
        cursor = None
        db = None
        try:
            db = MySQLdb.connect(self.db_host, self.db_user, self.db_user_password, self.db_name)
            # Open database connection
            # prepare a cursor object using cursor() method
            cursor = db.cursor()
            pd = sql.read_sql(EstimatorBuilder.SELECT_SQL, db)
            data = pd.replace(np.nan, '', regex=True)
            labels = pd.spam_type
            trainData = data.drop(['spam_type'], axis=1)

            email_pipe = Pipeline([
                ('data', DataFrameColumnExtracter('email')),
                ('vectorizer', HashingVectorizer(alternate_sign=False))
            ])

            fname_pipe = Pipeline([
                ('data', DataFrameColumnExtracter('first_name')),
                ('vectorizer', HashingVectorizer(alternate_sign=False))
            ])

            lname_pipe = Pipeline([
                ('data', DataFrameColumnExtracter('last_name')),
                ('vectorizer', HashingVectorizer(alternate_sign=False))
            ])

            bio_pipe = Pipeline([
                ('data', DataFrameColumnExtracter('bio')),
                ('preprocessor', StripHTMLTransformer()),
                ('vectorizer', CountVectorizer(strip_accents='unicode', stop_words='english', ngram_range=(1, 3))),
                ('tfidf', TfidfTransformer())
            ])

            features = FeatureUnion(
                n_jobs=1,
                transformer_list=[
                    ('email_pipe', email_pipe),
                    ('fname_pipe', fname_pipe),
                    ('lname_pipe', lname_pipe),
                    ('bio_pipe', bio_pipe)
                ],
                transformer_weights=None)

            classifier = Pipeline([
                ('features', features),
                ('model', MultinomialNB(alpha=0.0001, fit_prior=True))
            ])

            classifier.fit(trainData, labels)

            pickle.dump(classifier, open(self.filename, 'wb'))
            db.commit()

        except Exception as e:
            print(e)
            # Rollback in case there is any error
            if not (db is None):
                db.rollback()
            raise

        finally:

            if not (cursor is None):
                cursor.close()
            # disconnect from server
            if not (db is None):
                db.close()
