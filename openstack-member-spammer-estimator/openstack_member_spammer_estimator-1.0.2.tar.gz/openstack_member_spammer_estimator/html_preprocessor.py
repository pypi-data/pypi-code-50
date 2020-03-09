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

from html.parser import HTMLParser
from sklearn.base import TransformerMixin


class StripHTMLTransformer(TransformerMixin):

    def transform(self, x, **transform_params):
        return [
            self.stripHtmlOff(doc) for doc in x
        ]

    def stripHtmlOff(self, document):
        if document == '':
            return document
        s = HTMLStripper()
        s.feed(document)
        strip = s.get_data()
        return strip

    def fit(self, X, y=None, **fit_params):
        return self


class HTMLStripper(HTMLParser):

    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)
