"""
.. include:: ../recipes/test.rst
    :start-line: 5
    :end-line: 13

See the :ref:`tutorial <test-recipe>` for better understanding
"""
import os
import re
import ast
import json
import logging
import subprocess

from abc import ABC, ABCMeta, abstractmethod
from enum import Enum

from gradefast import logconfig
from gradefast.exceptions import *
from gradefast.utils import combine_list_elements
from gradefast.result import Result
from gradefast.command import Command

logger = logconfig.configure_and_get_logger(__name__)

class TestType(Enum):
    """
    An enum to indicate type of the test.

    Options are FILE, PKG and SCRIPT

    .. todo::

        SCRIPT is yet to be added
    """
    FILE=1
    PYTHON=2
    SCRIPT=3

def find_pattern_in_output(name, out):
    if name == 'result_dict':
        pattern = re.compile("<result-dict>(\{.*\})</result-dict>")
    elif name == 'comment':
        pattern = re.compile("<comment>(.*)</comment>")
    elif name == 'exception':
        pattern = re.compile("<exception>(.*)</exception>")
    else:
        return None
    m = pattern.search(out)
    if m == None:
        return None
    # parantheses can be used to group text inside pattern; group 0 is whole match
    try:
        logger.debug('Attempting json loads on {}'.format(m.group(1)))
        if m.group(1) == '':
            return ''
        result = json.loads(m.group(1))
        return result
    except json.decoder.JSONDecodeError:
        # log here
        raise ParseError("{} should be encoded as a json string".format(name))


def parse_output(output):
    if type(output) != str:
        raise Exception("Output from console should be string")
    result_dict = find_pattern_in_output('result_dict', output) or {}
    comment = find_pattern_in_output('comment', output)
    exception = find_pattern_in_output('exception', output)
    return result_dict, comment, exception
  
class GFCliTest:
    def __init__(self, test_script_location, file_item_to_test, parameters=[], 
    test_type=TestType.FILE, plagiarism_check=False):
        # A test consists of a test_script file written by theme developers 
        # and a test entry point usually present in student submissions
        
        # The test script will be written in python. The test script will have 
        # a call to dependencies like :
        # 1. 

        # The Entry Points can be a:
        # 1. directory
        # 2. program file like .c or .py
        # 3. result.txt or result.png file
        
        self.test_script_location = test_script_location
        if not os.path.exists(test_script_location):
            raise FileNotFoundError("Test script not found")

        self.test_type = test_type
        if self.test_type == TestType.FILE:
            self.file_item_to_test = file_item_to_test

        self.parameters = parameters
        if len(self.parameters) == 0:
            raise InvalidParameterException("Provide atleast 1 parameter")

        for param in parameters:
            if type(param) != str:
                raise InvalidParameterException("Parameters should contain list of strings only")

    def __call__(self, submission):
        if self.test_type == TestType.FILE:
            working_dir = os.path.dirname(self.test_script_location)
            proc = subprocess.Popen([
                "python", self.test_script_location,
                "-f", submission.file_paths[self.file_item_to_test],
                "--team-id", str(submission.team_id)], 
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=working_dir)
            stdout, stderr = proc.communicate()
            result = json.loads(stdout)
            
            if type(result) != dict:
                raise TypeError("Result should be a list")
            # result = Result(result)
            return result, stderr


class GFTest(ABC):
    """
    Represents a test that outputs a result, comment and exceptions encountered
    while evaluating the test

    Each class written by developer intended to be a test extends :class:`~GFTest`
    and implements the :attr:`~GFTest.__call__()` method. :attr:`~GFTest.__call__()`
    receives parameters according to the TestType.

    Parameters
    ----------
    test_type: :class:`TestType`
        Specifies the type of test. This option influences what parameters are passed to
        :attr:`~GFTest.__call__()` and extra configurations before evaluation.

    file_item_to_test: str
        File on which the test is evaluated. ``e.g. 'zip', 'txt', 'png2', 'unzipped3'``

    pkg_path: str, optional
        Path to the package if the test_type is `TestType.PYTHON`

    plagiarism_check: bool, optional
        To enable plagiarism checking on :attr:`~file_item_to_test`. Default is ``False``d

    .. todo::

        Plagiarism check to be implemented

    Attributes
    ----------
    test_type: :class:`TestType`

    file_item_to_test: str

    pkg_path: str
    
    plagiarishm_check: bool

    """
    def __init__(self, test_type, file_item_to_test, pkg_path='', plagiarism_check=False, 
    before=[], after=[]):
        self.test_type = test_type
        self.file_item_to_test = file_item_to_test
        self.pkg_path = pkg_path
        if not isinstance(self.test_type, TestType):
            raise TypeError("test_type should be of type gradefast.test.TestType")
        self.test_type = test_type
        self.plagiarism_check = plagiarism_check
        self.before = before
        self.after = after

    def __repr__(self):
        return "GFTest(test_type: {}, file_item_to_test: {}, pkg_path: {}, plagiarism_check: {})"\
            .format(self.test_type, self.file_item_to_test, self.pkg_path, self.plagiarism_check)

    def __str__(self):
        return self.__repr__()

    @abstractmethod
    def __call__(self, *args):
        """
        Implements logic of test

        When :class:`GFTest` is subclassed, this method should be implemented.
        It receives parameters according to the selected test type.

        Following are the types and parameters the __call__() method receives: 
        
        TestType.FILE
            file_path, submission
        TestType.PYTHON
            submission

        """
        raise NotImplementedError()

class GFCommandTest(GFTest):
    def __init__(self, command, plagiarism_check=False, before=[], after=[]):
        super().__init__(TestType.SCRIPT, '', pkg_path='', plagiarism_check=plagiarism_check, 
        before=before, after=after)
        if not isinstance(command, Command):
            raise TypeError("command should be an instance of gradefast.command.Command")
        self.command = command

    def __call__(self, submission):
        logger.debug('Attempting command test on {}'.format(submission))
        proc, out, err = self.command.run(submission)
        logger.debug('Result of command execution {}'.format(out))
        result_dict, comment, exception = parse_output(out)
        return result_dict, comment, combine_list_elements(exception, err)
        
    # def run(self, submission):
    #     for command in self.before:
    #         command.run(submission)

    #     self.__call__(submission)

    #     for command in self.after:
    #         command.run(submission)
