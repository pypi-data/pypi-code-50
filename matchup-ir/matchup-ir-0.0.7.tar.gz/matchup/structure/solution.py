"""
    Solution module basically implements the Solution class
"""

from typing import List

from collections import namedtuple

Result = namedtuple("Result", "document, score")


class Solution:
    """
        The solution class has the function of properly storing and displaying the responses of the queries
    """
    def __init__(self, results: List[Result]):
        self._results = results
        self._idf = None
        self._tf = None

    def __repr__(self):
        string = ""
        if self._results:
            for terms in self._results:
                doc = terms.document.split('/')[-1]
                string += f"\n{doc} : {terms.score}"
        else:
            string += "No results found."
        return string

    def __contains__(self, item: Result):
        return item in self._results

    def expand(self, vocabulary):
        idf = vocabulary.idf
        tf = vocabulary.tf
        self._idf = idf.take(reverse=True)
        self._tf = tf.take(reverse=True)

    def get_dict(self):
        result_list = []
        for terms in self._results:
            doc = terms.document.split('/')[-1]
            result_list.append(Result(doc, terms.score))

        response_dict = {
            'solution': result_list,
            'stats': [
                {'idf': self._idf},
                {'tf': self._tf}
            ]
        }
        return response_dict
