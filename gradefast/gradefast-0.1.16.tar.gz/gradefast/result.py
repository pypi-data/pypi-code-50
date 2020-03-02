"""
Contains :class:`~gradefast.result.Result` and :class:`~gradefast.result.ResultGroup` classes
that represent result of a :class:`~gradefast.test.GFTest` or :class:`~gradefast.evaluate.Evaluate`
"""
import os
import re
import csv
import copy
import json
import logging
import traceback
import collections
from pathlib import Path
from typing import Union

import numpy as np
import pandas as pd

from gradefast import utils
from gradefast.exceptions import *
from gradefast import logconfig

logger = logconfig.configure_and_get_logger(__name__)

# TODO: Include exception inside result object itself
# TODO: CopyFrom result method to copy a result from
# existing one and add new fields to it
class Result:
    """
    Represents `result` of a :class:`~gradefast.test.GFTest`

    A `result` is output of a :class:`~gradefast.test.GFTest` identified by ``team_id`` 
    and the ``file`` the test was run on. The marks are stored as `dictionary` in 
    ``result_dict`` in which `keys` are the `parameters` and `values` are the `marks`.
    
    Parameters
    -----------
    team_id: int
        Identifier of the team whose result is under consideration

    file: str
        Item which was tested. ``e.g. 'zip' or 'png2'``

    result_dict: dict
        Contains parameters and marks. ``e.g. {sum: 10, divsion: [1, 5]}``

    exec_time: int
        Time it took for the result_dict to generate

    pkg_path: str, optional
        If TestType.PYTHON was selected, pkg_path should be specified
        
    comment: Union[str, list], optional
        Comment is a text feedback. Can be optionally returned from a :class:`~gradefast.test.GFTest` 

    error: Union[str, list], optional
        Error is the stack trace or list of stack traces. Can be optionally returned from 
        a :class:`~gradefast.test.GFTest` 
    
    Attributes
    ----------
    team_id: int
    file: str
    result_dict: dict
    exec_time: float
    pkg_path: str
    comment: Union[str, list]
    error: Union[str, list]
    
    Examples
    --------
    .. doctest::

        >>> team_id = 987
        >>> file = 'py'
        >>> result_dict = {'loss': 30, 'activation': 25, 'sgd': [14, -5, 10]}
        >>> Result(team_id, file, result_dict)
        Result(team_id: 987, file: py, result_dict: {'loss': 30, 'activation': 25,
        'sgd': [14, -5, 10]}, exec_time: 0, pkg_path: , comment: )

    """
    def __init__(self, team_id: int, file: str, result_dict: dict, exec_time=0, 
    pkg_path: str = '', comment: Union[str, list] = '', error: Union[str, list] = ''):

        # identified by team id
        if type(team_id) in [str, int] and utils.is_string_number(team_id):
            self.team_id = int(team_id)
        else:
            raise TypeError("team_id should be a integer")

        # which file did the test run on?
        self.file = file
        # which package to mount?
        # dictionary of parameters and marks
        if not isinstance(result_dict, dict):
            raise TypeError("Result should be a dict")
        self.result_dict = result_dict
        self.pkg_path = pkg_path
        self.exec_time = exec_time
        self.comment = comment
        self.error = error

    def __eq__(self, value):
        # this method doesnt not consider private fields and functions
        # when evaluating equals
        return utils.object_equality(self, value)

    def __ne__(self, value):
        return not self.__eq__(value)

    def __repr__(self):
        return "Result(team_id: {}, file: {}, result_dict: {}, ".format(self.team_id, 
        self.file, self.result_dict) \
        + "exec_time: {}, pkg_path: {}, comment: {}, error: {})".format(self.exec_time, 
        self.pkg_path, self.comment, self.error)

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def from_submission_test(submission, test, result_dict: dict, 
    exec_time: Union[int, float]=0, comment: Union[str, list]='', 
    error: Union[str, list]=''):
        """
        Creates a :class:`Result`

        Parameters
        -----------
        submission: :class:`~gradefast.submission.Submission`
        test: :class:`~gradefast.test.GFTest`
        result_dict: dict
        exec_time: float
        comment: Union[str, list]
        error: Union[str, list]

        Returns
        --------
        :class:`Result`
 
        Examples
        --------
        .. doctest:: 

            >>> # submission with team_id 5
            >>> # test with file_item_to_test 'zip' 
            >>> Result.from_submission_test(submission, test, {'marks': 10})
            Result(team_id: 5, file: 'zip', result_dict: {'marks': 10}, exec_time: 0,
            pkg_path: , comment: )
        """
        return Result(submission.team_id, test.file_item_to_test, result_dict, 
        exec_time=exec_time, pkg_path=test.pkg_path, comment=comment, error=error)

    @staticmethod
    def from_dict(result):
        """
        Creates a :class:`Result` from a :class:`dict`.

        Parameters
        ----------
        result: dict
            Should contain `keys` `team_id`, `file` and `result_dict`. Can optionally contain
            `comment`, `error` and `pkg_path`. 

        Returns
        -------
        :class:`Result`
            A :class:`Result` built from the result dictionary

        Examples
        --------
        .. doctest::

            >>> dict_repr_result = {'team_id': 987, 'file': 'py', 'pkg_path': '', 'result_dict':
            ... {'loss': 30, 'activation': 25, 'sgd': [14, -5, 10]}, 'exec_time': 0, 'comment': ''}
            >>> Result.from_dict(dict_repr_result)
            Result(team_id: 987, file: py, result_dict: {'loss': 30, 'activation': 25, 
            'sgd': [14, -5, 10]}, exec_time: , pkg_path: , comment: )
        
        """

        # if 'team_id' in result:
        #     team_id = result['team_id']
        # if 'file' in result:
        #     file = result['file']
        # if 'result_dict' in result:
        #     result_dict = result['result_dict']
        # if 'exec_time' in result:
        #     exec_time = result['exec_time']
        # if 'pkg_path' in result:
        #     pkg_path = result['pkg_path']
        # if 'comment' in result:
        #     comment = result['comment']
        # if 'error' in result:
        #     error = result['error']

        result_obj = Result(result['team_id'], result['file'], result['result_dict'])
        return Result.copy_from(result_obj, **result)

    def to_dict(self):
        """
        Converts from :class:`Result` to a :class:`dict`

        Returns
        -------
        dict

        Examples
        --------
        .. doctest::

            >>> result = Result(987, 'py', {'loss': 30, 'activation': 25, 'sgd': [14, -5, 10]}, 
            ... exec_time=0.5, pkg_path='', comment='Hello')
            >>> result.to_dict()
            {'team_id': 987, 'file': 'py', 'pkg_path': '', 'result_dict': {'loss': 30,
            'activation': 25, 'sgd': [14, -5, 10]}, 'exec_time': 0.5, 'comment': 'Hello'}
        """
        return self.__dict__

    def to_flat_dict(self, result_params_prefix='result_param'):
        """
        Returns a flat (or non-nested) :class:`dict` representation of :class:`Result`

        The method is a utility used to serialize a result into a flat structure like a csv file. 
        The parameters and marks inside the result_dict are copied in the root dictionary along 
        with team_id, file and other optional parameters.  
        
        Returns
        -------
        dict

        Examples
        --------
        .. doctest::

            >>> r = Result(31, 'zip', {'add': 5, 'subtract': [1, 3]})
            >>> r.to_flat_dict()
            {'team_id': 31, 'file': 'zip', 'pkg_path': '', 'add': 5, 'subtract': [1, 3], 
            'comment': ''}

        """

        # return {'team_id': self.team_id, 'file': self.file, 
        # 'exec_time': self.exec_time, 'pkg_path': self.pkg_path,
        # **self.result_dict, 'comment': self.comment}

        flattened_dict = utils.flatten({result_params_prefix: self.result_dict})
        
        return {'team_id': self.team_id, 'file': self.file, 
        'exec_time': self.exec_time, 'pkg_path': self.pkg_path,
        **flattened_dict, 'comment': self.comment, 'error': self.error}

    def flat_result(self, average=True):
        """
        Add or average list of marks, if present, inside `result_dict` 

        A result_dict may have marks either as float (int) or as a list of floats (ints).
        In the latter case, it means marks for multiple test cases were given. The method 
        allows us to add or average such lists of marks

        Parameters
        ----------
        average: bool, optional
            Whether to average or add the marks from multiple `test cases` (Default 
            is True i.e. Average)

        Returns
        --------
        :class:`Result`

        Examples
        --------
        .. doctest::

            >>> r = Result(5, 'png', {'a': 5, 'b': [3, 10], 'c': [5]})
            >>> r.flat_result()
            Result(team_id: 5, file: png, result_dict: {'a': 5, 'b': 6.5, 'c': 5.0},
            pkg_path: , comment: )

        With ``average=False``, the method just adds the marks
            
            >>> r = Result(5, 'png', {'a': 5, 'b': [3, 10], 'c': [5]})
            >>> r.flat_result(average=False)
            Result(team_id: 5, file: png, result_dict: {'a': 5, 'b': 13, 'c': 5},
            pkg_path: , comment: )

        """
        result_copy = copy.deepcopy(self.result_dict)
        total = 0
        for key, value in result_copy.items():
            if value != np.nan:
                if type(value) == list:
                    result_copy[key] = self._aggregate_test_cases(value, average)
                else:
                    result_copy[key] = value
        return Result.copy_from(self, result_dict=result_copy)

    def add(self, average=True):
        """
        Add marks from `result_dict` and return a :class:`Result` with result_dict containing 
        the `total`

        The method adds values from all keys in result_dict and returns a :class:`Result` 
        whose ``result_dict`` contains only `total` key. You can choose to add or average 
        test cases from within this method itself

        Parameters
        ----------
        average: bool, optional
            Whether to average or add the marks from multiple `test cases` (Default 
            is True i.e. Average)

        Returns
        --------
        :class:`Result`
            Result obtained after adding values corresponding to each grading parameter

        Examples
        --------
        .. doctest::

            >>> r = Result(5, 'png', {'a': 5, 'b': [3, 10], 'c': [5]})
            >>> r.add()
            Result(team_id: 5, file: png, result_dict: {'total': 16.5}, pkg_path: , comment: )

        With ``average=False``, the method simply adds the marks
            
            >>> r = Result(5, 'png', {'a': 5, 'b': [3, 10], 'c': [5]})
            >>> r.add(average=False)
            Result(team_id: 5, file: png, result_dict: {'total': 23}, pkg_path: , comment: )

        """
        result_copy = copy.deepcopy(self.result_dict)
        total = 0
        for key, value in result_copy.items():
            if value != np.nan:
                if type(value) == list:
                    total += self._aggregate_test_cases(value, average)
                else: 
                    total += value

        return Result.copy_from(self, result_dict={'total': total})

    @staticmethod
    def copy_from(result, **kwargs):
        """
        Returns a new :class:`Result` by adding properties from a base
        :class:`Result` and :attr:`Result.copy_from.kwargs`
        
        Parameters
        ----------
        result: :class:`Result`
            A base result to copy properties from
        kwargs: tuple
            A variable number of key=value pairs. **Key** represents names of
            member fields to be set to given **value**.

        Returns
        -------
        :class:`Result`

        """
        new_result = copy.deepcopy(result) 
        for key, value in kwargs.items():
            setattr(new_result, key, value)
        return new_result

    @staticmethod
    def multiply_list(marks, weightage):
        final_marks = []
        for idx, value in enumerate(marks):
            if type(value) not in [int, float]:
                raise Exception('Test cases marks should be numbers')

            if type(weightage) not in [list, int, float]:
                raise Exception('Weightages should be number or list of numbers')

            if type(weightage) == list and (len(weightage) != len(marks)):
                raise Exception("Either specify a single multiplier or all multiplers"  \
                    "for weightages")
            elif type(weightage) == list and (len(weightage) == len(marks)):
                result = value * weightage[idx]
            else:
                result = value * weightage
            final_marks.append(result)
        return final_marks

    def multiply(self, weightages: dict):
        """
        Multiply marks in ``result_dict`` with weights or factors specified in ``weightages``
        dict

        Returns a :class:`Result` obtained by multiplying weights present in ``weightages``
        dict with those corresponding to parameters present in ``result_dict``

        Parameters
        ----------
        weightages: dict
            :class:`dict` of weights. Keys present should correspond to those in ``result_dict``. 
            Values should be ``float`` or ``int``

        Returns
        -------
        :class:`Result`
            :class:`Result` obtained after applying weights

        Examples
        --------
        .. doctest::

            >>> result = Result(987, 'py', {'loss': 30, 'activation': 25, 'backprop': [5, 6],
            ... 'sgd': [14, -5, 10]}, exec_time=0.5, pkg_path='', comment='Hello')
            >>> weightages = {'loss': 0.5, 'activation': 1.5, 'backprop': 2, 'sgd': [0.5, 1, 2]}
            >>> result.multiply(weightages)
            Result(team_id: 987, file: py, result_dict: {'loss': 15.0, 'activation': 37.5,
            'backprop': [10, 12], 'sgd': [7.0, -5, 20]}, exec_time: 0.5, pkg_path: , comment: Hello)

        """
        result_copy = copy.deepcopy(self.result_dict)
        total = 0
        for param, marks in self.result_dict.items():
            if param not in weightages:
                continue
            if marks != np.nan:
                if type(marks) == list:
                    result_copy[param] = Result.multiply_list(marks, weightages[param])
                elif type(marks) in [int, float] and type(weightages[param]) in [int, float]:
                    result_copy[param] = marks * weightages[param]
                else:
                    raise Exception("Marks and weightages for a parameter should be a number or"    \
                        "number list. Marks cannot be a single number and weightages a list for"    \
                        "same parameter.")
            else:
                raise Exception('Marks for a parameter should be either a number or number list\
                    and not NaN')
        return Result.copy_from(self, result_dict=result_copy)

    def _aggregate_test_cases(self, result_of_test_cases, average):
        '''
            A test cased result will be a list and not a float/int value
        '''
        total = 0
        for value in result_of_test_cases:
            if type(value) == str and utils.is_string_number(value):
                total += utils.is_string_number(value)
            else:
                total += value
        if average:
            total = float(total / len(result_of_test_cases))
        return total

    @staticmethod
    def rename(mapping, result):
        new_result = copy.deepcopy(result)
        renamed_result_dict = {}
        for key in new_result.result_dict.keys():
            if key in mapping.keys():
                renamed_result_dict[mapping[key]] = new_result.result_dict[key]
            else:
                renamed_result_dict[key] = new_result.result_dict[key]
        return Result.copy_from(new_result, result_dict=renamed_result_dict)

    @staticmethod
    def join(*results):
        """
        Concatenates ``result_dict`` from mutiple :class:`Result` objects

        Joins or concatenates multiple results. The resultant ``result_dict`` will include 
        unique `keys` (parameters) from all the Result objects, thereby creating a union 
        of results. For this method to work, ``team_id`` of results should be same. ``file``, 
        ``pkg_path`` and ``comment`` are appended as lists.


        Parameters
        ----------
        results: tuple
            A tuple of :class:`Result`. Any number of result objects can be provided

        Returns
        -------
        :class:`Result`
            Result representing union of results

        Raises
        -------
        Exception
            If ``team_id`` of results don't match

        Examples
        --------
        .. doctest::

            >>> result1 = Result(725, 'py', {'loss': 10, 'activation': 5, 'sgd': [4, 5, '6']},
            ... exec_time=10, pkg_path='', comment='Hello')
            >>> result2 = Result(725, 'py2', {'cnn': 30, 'object_detect': 25}, exec_time=15, 
            ... pkg_path='./cnn/', comment='world')
            >>> Result.join(result1, result2)
            Result(team_id: 725, file: ['py', 'py2'], result_dict: {'loss': 10, 'activation': 5,
            'sgd': [4, 5, '6'], 'cnn': 30, 'object_detect': 25}, exec_time: [10, 15],
            pkg_path: ['', './cnn/'], comment: ['Hello', 'world'])

        """
        if len(results) < 1:
            return None

        team_ids = set(map(lambda result: result.team_id, results))
        
        if len(team_ids) > 1:
            raise Exception('Results should have same team_ids')

        file_list = []
        pkg_path_list = []
        result_dict = {}
        comment = []
        exec_time = []

        for result in results:
            if type(result.file) == list:
                file_list += result.file
            else:
                file_list.append(result.file)

            if type(result.pkg_path) == list:
                pkg_path_list += result.pkg_path
            else:
                pkg_path_list.append(result.pkg_path)

            if type(result.comment) == list:
                comment += result.comment
            else:
                comment.append(result.comment)

            if type(result.exec_time) == list:
                exec_time += result.exec_time
            else:
                exec_time.append(result.exec_time)

            result_dict.update(result.result_dict)

        joined_result = Result(list(team_ids)[0], file_list, result_dict, 
        exec_time=exec_time, pkg_path=pkg_path_list, comment=comment)
        return joined_result


class ResultGroup:
    """
    Groups many :class:`Result` together

    A :class:`ResultGroup` clubs multiple :class:`Result` together and includes additional 
    information like ``task_name`` and ``theme_name``. 

    Parameters
    ----------
    task_name: str
    theme_name: str
    results: list, dict
        List or dictionary of results. If dictionary, key should be a team_id and 
        value should be a :class:`Result`

    Attributes
    ----------
    task_name: str
    theme_name: str
    dict_of_results: dict
        A dictionary of results where `key` is a team_id and `value` is a :class:`Result`

    Warnings
    ---------    
    Result group is an iterator. Try not to mutate it and expect it to work fabulously thereafter.
    
    Examples
    --------
    .. doctest::

        >>> result1 = Result(725, 'py', {'loss': 10, 'activation': 5, 'sgd': [4, 5, '6']}, 
        ... exec_time=10, pkg_path='', comment='Hello')
        >>> result2 = Result(109, 'py', {'loss': 7, 'activation': 15, 'sgd': [14, -5, '6']}, 
        ... exec_time=15, pkg_path='', comment='world')
        >>> ResultGroup('Task1', 'Fish Theme', [result1, result2])
        ResultGroup(task_name: Task1, theme_name: Fish Theme, dict_of_results: {725:
        Result(team_id: 725, file: py, result_dict: {'loss': 10, 'activation': 5,
        'sgd': [4, 5, '6']}, exec_time: 10, pkg_path: , comment: Hello), 109:
        Result(team_id: 109, file: py, result_dict: {'loss': 7, 'activation': 15,
        'sgd': [14, -5, '6']}, exec_time: 15, pkg_path: , comment: world)})
    """
    def __init__(self, task_name: str, theme_name: str, results):
        self.task_name = task_name
        self.theme_name = theme_name
        if type(results) == list:
            self.dict_of_results = {result.team_id if type(result.team_id) == int \
                else result.team_id: result for result in results}
        else:
            self.dict_of_results = results
        self._iter = iter(self.dict_of_results)

    def __iter__(self):
        return self
    
    def __len__(self):
        return len(self.dict_of_results)

    def __next__(self):
        try:
            self._curr_idx = next(self._iter)
            idx = self._curr_idx
            return self.dict_of_results[self._curr_idx]
        except StopIteration:
            self._iter = iter(self.dict_of_results)
            raise StopIteration

    def __eq__(self, value):
        # this method doesnt not consider private fields and functions
        # when evaluating equals
        return utils.object_equality(self, value)

    def __ne__(self, value):
        return not self.__eq__(value)

    def __repr__(self):
        return "ResultGroup(task_name: {}, theme_name: {}, dict_of_results: {})"\
            .format(self.task_name, self.theme_name, self.dict_of_results)

    def __str__(self):
        return self.__repr__()
        
    def __getitem__(self, team_id):
        try:
            if isinstance(team_id, slice):
                dict_of_results = {}
                for ii in range(*team_id.indices(team_id.stop)):
                    if self[ii] != None:
                        dict_of_results[ii] = self[ii]
                return ResultGroup(self.task_name, self.theme_name, dict_of_results)
            elif type(team_id) == str:
                if self.dict_of_results.get(team_id) != None:
                    return self.dict_of_results[team_id]
                elif self.dict_of_results.get(int(team_id)) != None:
                    return self.dict_of_results[int(team_id)]
            elif type(team_id) == int:
                if self.dict_of_results.get(team_id) != None:
                    return self.dict_of_results[team_id]
                elif self.dict_of_results.get(str(team_id)) != None:
                    return self.dict_of_results[str(team_id)]
        except KeyError as e:
            logger.exception('Exception when attempting getitem where team_id: {}'.format(team_id))
            return None
    
    # TODO: safely remove this
    # def find_by_id(self, id):
    #     # find result quickly by exploiting the fact that results are stored in sorted order
    #     for team_id, result in self.dict_of_results.items():
    #         if result.team_id == id:
    #             return result

    @staticmethod
    def from_dict(group_dict):
        """
        Creates a :class:`ResultGroup` from a :class:`dict`

        Parameters
        ----------
        group_dict: dict

        Returns
        -------
        :class:`ResultGroup`

        Examples
        --------
        .. doctest::

            >>> result_group_dict = {'task_name': 'Task1', 'theme_name': 'Fish Theme',
            ... 'dict_of_results': {725: {'team_id': 725, 'file': 'py', 'pkg_path': '',
            ... 'result_dict': {'loss': 10, 'activation': 5, 'sgd': [4, 5, '6']}, 'exec_time': 10,
            ... 'comment': 'Hello'}, 109: {'team_id': 109, 'file': 'py', 'pkg_path': '',
            ... 'result_dict': {'loss': 7, 'activation': 15, 'sgd': [14, -5, '6']}, 'exec_time': 15,
            ... 'comment': 'world'}}}
            >>> ResultGroup.from_dict(result_group_dict)
            ResultGroup(task_name: Task1, theme_name: Fish Theme, dict_of_results:
            {725: Result(team_id: 725, file: py, result_dict: {'loss': 10, 'activation': 5,
            'sgd': [4, 5, '6']}, exec_time: , pkg_path: Hello, comment: ), 109: 
            Result(team_id: 109, file: py, result_dict: {'loss': 7, 'activation': 15,
            'sgd': [14, -5, '6']}, exec_time: , pkg_path: world, comment: )})
            
        """
        dict_of_results = {}
        for team_id, result in group_dict['dict_of_results'].items():
            dict_of_results[int(team_id)] = Result.from_dict(result)
        
        return ResultGroup(group_dict['task_name'], group_dict['theme_name'], dict_of_results)
    
    def to_dict(self):
        """
        Converts from :class:`ResultGroup` to a :class:`dict`
        
        Returns
        -------
        dict

        """
        result_group = {}
        result_group['task_name'] = self.task_name
        result_group['theme_name'] = self.theme_name
        
        dict_of_results = {}
        for team_id, result in self.dict_of_results.items():
            dict_of_results[team_id] = result.to_dict()
        result_group['dict_of_results'] = dict_of_results
        return result_group

    def to_flattened_list(self, result_params_prefix='result_param'):
        flattened_results = []
        for result in self:
            flattened_results.append(result.to_flat_dict(result_params_prefix=result_params_prefix))
        return flattened_results

    @staticmethod
    def from_json(file_path):
        """
        Create a :class:`ResultGroup` from a json file

        Parameters
        ----------
        file_path: str
            Path to json file

        Returns
        -------
        :class:`ResultGroup`

        """
        # convert submissions array to json array
        if os.path.isdir(file_path):
            for file_name in os.listdir(file_path):
                if file_name.startswith('result_group_'):
                    json_file_path = os.path.join(file_path, file_name + '.json')
                    break
        else:
            json_file_path = file_path

        with open(json_file_path, 'r') as json_file:
            result_group_dict = json.load(json_file)
        
        return ResultGroup.from_dict(result_group_dict)

    def to_json(self, save_path):
        """
        Save a :class:`ResultGroup` object to json file

        Parameters
        ----------
        save_path: str
            Path to json file or directory

        Returns
        -------
        None

        """

        # convert submissions array to json array
        file_name = 'result_group_{}_{}'.format(self.theme_name, self.task_name)
        if os.path.isdir(save_path):
            json_file_path = os.path.join(save_path, file_name + '.json')
        else:
            json_file_path = save_path

        result_group_dict = self.to_dict()
        
        with open(json_file_path, 'w') as json_file:
            json.dump(result_group_dict, json_file)
    
    @staticmethod
    def result_group_file_name(self):
        """
        Returns name of result_group file according to decided naming convention 

        Returns
        -------
        str

        """
        return 'result_group_{}_{}'.format(self.theme_name, self.task_name)

    @staticmethod
    def from_csv(save_location, theme_name='', task_name=''):
        """
        Create a :class:`ResultGroup` from csv file

        .. todo::

            The feature will be built soon.

        .. deprecated:: 0.0.15
        
        Parameters
        ----------
        save_location: str
            Path to csv file or directory

        Returns
        -------
        None

        """
        # read csv into pandas dataframe
        # iterate and convert each row into a Result object
        # finally create a ResultGroup
        
        csv_path, meta_path = ResultGroup._find_result_group_files(save_location, 
        theme_name, task_name)

        dict_of_results = []

        df = pd.read_csv(csv_path, index_col=None)
        for item in df.itertuples(index=False):
            info_dict = {}
            info_dict['team_id'] = item.team_id
            info_dict['file'] = item.file
            info_dict['pkg_path'] = item.pkg_path
            result_dict = utils.subtract_dict(dict(item._asdict()), info_dict)
            if info_dict['pkg_path'] == '' or info_dict['pkg_path'] == None:
                result = Result(info_dict['team_id'], info_dict['file'], result_dict)
            else:
                result = Result(info_dict['team_id'], info_dict['file'], result_dict,
                pkg_path=info_dict['pkg_path'])
            dict_of_results.append(result)

        # print(dict_of_results)
        # read json file
        with open(meta_path, 'r') as json_file:
            result_meta = json.load(json_file)
        
        # print(result_meta)
        return ResultGroup(result_meta['task_name'], result_meta['theme_name'], dict_of_results)

    def to_csv(self, save_location, result_params_prefix='result_params'):
        """
        Save a :class:`ResultGroup` object to csv file

        Parameters
        ----------
        save_location: str
            Path to json file or directory

        Returns
        -------
        None

        """
        # comments regarding what are restrictions on theme name and task name
        file_name = 'result_group_{}_{}.csv'.format(self.theme_name, self.task_name)
        if Path(save_location).suffix != '':
            file_path = save_location
        else:
            file_path = os.path.join(save_location, file_name)
        try:
            # create csv
            list_of_dictionary = self.to_flattened_list(result_params_prefix=result_params_prefix)
            df = pd.DataFrame(list_of_dictionary)
            df.to_csv(file_path, index=False)
            # create json
            meta_dict = {'task_name': self.task_name, 'theme_name': self.theme_name}
            with open(file_path + '.json', 'w+') as json_file:
                json.dump(meta_dict, json_file)
        except Exception as e:
            logger.exception('Exception when attempting to convert {} to csv {}'.format(self, save_location))
            return False
        return True

    @staticmethod
    def _find_result_group_files(save_location, theme_name, task_name):
        if theme_name == '' or theme_name == None:
            if task_name == '' or task_name == None:
                pattern = re.compile("result_group_.*_.*\.(csv|json)$")
            else:
                pattern = re.compile("result_group_.*_{}\.(csv|json)$".format(task_name))
        elif task_name == '' and task_name == None:
            pattern = re.compile("result_group_{}_.*\.(csv|json)$".format(theme_name))
        else:
            pattern = re.compile("result_group_{}_{}\.(csv|json)$".format(theme_name, task_name))

        csv_file_name = ''
        meta_file_name = ''

        list_of_items = os.listdir(save_location)
        for item in list_of_items:
            m = pattern.search(item)
            if m != None:
                file_extension = m.group(1)
                if file_extension == 'csv':
                    complement_file_name = os.path.splitext(item)[0] + '.json'
                    if complement_file_name in list_of_items:
                        meta_file_name = complement_file_name
                        csv_file_name = m.group(0)
                elif file_extension == 'json':
                    complement_file_name = os.path.splitext(item)[0] + '.csv'
                    if complement_file_name in list_of_items:
                        meta_file_name = m.group(0)
                        csv_file_name = complement_file_name
        
        csv_path = os.path.join(save_location, csv_file_name)
        meta_path = os.path.join(save_location, meta_file_name)

        return csv_path, meta_path

    def comment_builder(self, method, *args, **kwargs):
        """
        Specify a method to make comments for each team based on their result

        Parameters
        ----------
        method: function
            Takes a :class:`Result`, args and kwargs as arguments and returns a `comment` as ``str``
        args: 
            Arguments specified by user given to the method
        kwargs: 
            Named arguments specified by user given to the method

        Returns
        -------
        None

        Examples
        --------
        .. doctest::

            >>> # create a result_group that looks like below
            ResultGroup(task_name: Task0, theme_name: Homecoming, dict_of_results: {75: 
            Result(team_id: 75, file: ['py'], result_dict: {'loss': 15, 'activation': 5,
            'sgd': [4, 5, 7]}, pkg_path: abc, comment: ), 987: Result(team_id: 987, file: py,
            result_dict: {'loss': 30, 'activation': 25, 'sgd': [14, -5, 10]}, pkg_path: , 
            comment: ), 453: Result(team_id: 453, file: py, result_dict: {'loss': 10,
            'activation': 5, 'sgd': [4, 5, '6']}, pkg_path: , comment: )})
            
            >>> def build_comment(result, gracemarks, cutoff): # the comment builder function
            ...     total = result.add(average=False).result_dict['total']
            ...     if total + gracemarks > cutoff:
            ...         return "Congrats you passed"
            ...     return "Please try again next year"

            >>> result_group.comment_builder(build_comment, 5, 35)
            >>> new_result_group = result_group.make_comments()
            >>> print(new_result_group)
            
            ResultGroup(task_name: Task0, theme_name: Homecoming, dict_of_results: {75:
            Result(team_id: 75, file: ['py'], result_dict: {'loss': 15, 'activation': 5,
            'sgd': [4, 5, 7]}, pkg_path: abc, comment: Congrats you passed), 987: Result(
            team_id: 987, file: py, result_dict: {'loss': 30, 'activation': 25, 
            'sgd': [14, -5, 10]}, pkg_path: , comment: Congrats you passed), 453: 
            Result(team_id: 453, file: py, result_dict: {'loss': 10, 'activation': 5, 
            'sgd': [4, 5, '6']}, pkg_path: , comment: Please try again next year)})
            
        """
        self._build_comment = method
        self._args = args
        self._kwargs = kwargs

    def make_comments(self):
        """
        Uses `method` specified in :attr:`comment_builder` to generate comments for each result 
        in ``dict_of_results``

        Returns
        -------
        :class:`ResultGroup`
            :class:`ResultGroup` with each :class:`Result` having comments built using method 
            specified 
            in :class:`comment_builder`

        Examples
        --------
        

        """
        dict_of_results = copy.deepcopy(self.dict_of_results)
        for team_id, result in self.dict_of_results.items():
            dict_of_results[team_id].comment = self._build_comment(result, *self._args,
            **self._kwargs)           
        return ResultGroup(self.task_name, self.theme_name, dict_of_results)
