"""
Evaluate module provides :class:`Evaluate` to execute a :class:`~gradefast.test.GFTest`
on a :class:`~gradefast.submission.SubmissionGroup`
"""
import os
import csv
import sys
import time
import glob
import logging
import datetime
import traceback
from pathlib import Path
import multiprocessing as mp

from gradefast.utils import Extracter
from gradefast import logconfig
from gradefast.aggregate import Aggregate
from gradefast.result import Result, ResultGroup
from gradefast.test import GFCliTest, GFTest, GFCommandTest, TestType
from gradefast.submission import Submission, SubmissionGroup

logger = logconfig.configure_and_get_logger(__name__)

# TODO: Can I reference a file inside unzipped zips if TestType.FILE is selected
# If so how to do that?
# file_item_to_test is unzipped, does it unzip the zipped if its not unzipped already?? 
class Evaluate:
    """
    Allows evaluating a :class:`~gradefast.test.GFTest` on a 
    :class:`gradefast.submission.SubmissionGroup`.

    Parameters
    ----------
    test: :class:`~gradefast.test.GFTest`

    result_path: str, optional
        Path to persist the :class:`~gradefast.result.ResultGroup` as json file.
        Default is './'

    clean: bool, optional
        Cleans or resets state of the test working directory after running test on
        each :class:`~gradefast.submission.Submisison`

    timeout: int, optional
        Maximum time to run the test for. Default is 10 seconds

    .. todo:

        Clean option is yet to be implemented

    Attributes
    ----------
    test: :class:`~gradefast.test.GFTest`

    result_path: str

    clean: bool

    timeout: int

    Examples
    --------
    .. doctest::
        
        >>> evaluate = Evaluate(test, result_path='./generated/', timeout=15)
        <gradefast.evaluate.Evaluate object at 0x7ff50d76af60>
        >>> result_group, exceptions = evaluate(submission_group)
        
    """
    def __init__(self, test, result_path='./', clean=True, timeout=10):
        # Submissions contain multiple test entry points for example main.py, result.txt, result.png 
        # Multiple tests per Submission takes care of evaluating these multiple files
        # Result from each of these tests may or may not be aggregated
        # Alternatively, there can be a single test evaluating all of these files 
        # evaluate tests on each submission
        # self.submissions = submissions
        if not isinstance(test, GFTest):
            raise TypeError('Test should be instance of gradefast.test.GFTest')
        self.test = test
        self.result_path = result_path
        # len of tests should be same as marking_scheme
        self.clean = clean
        self.timeout = timeout

    # TODO: Support multiple packages to be imported
    def pkg_setup(self, submission, test):
        """
        Mount package given in :class:`~gradefast.test.GFTest` when evaluating a
        particular :class:`~gradefast.submission.Submission`

        Parameters
        ----------
        submission: :class:`~gradefast.submission.Submission`
        test: :class:`~gradefast.test.GFTest`

        Returns
        -------
        None
        """
        full_pkg_path = self.make_pkg_full_path(submission, test)
        logger.debug(full_pkg_path)
        
        matches = glob.glob(full_pkg_path)
        if len(matches) > 0:
            full_pkg_path = matches[0]
        else:
            raise FileNotFoundError('Package not found')
        logger.debug(full_pkg_path)
        sys.path.append(full_pkg_path)
        return True


    def run_test(self, file_path, submission, test, conn):
        """
        Runs a :class:`~gradefast.test.GFTest` on a particular
        :class:`~gradefast.submission.Submission`

        Parameters
        ----------
        file_path: str

        submission: :class:`~gradefast.submission.Submission`

        test: :class:`~gradefast.test.GFTest`

        conn: :class:`~multiprocessing.connection.Connection`
            A child connection object to send data back to parent

        Returns
        -------
        None

        """
        # set stdout to another file for logging
        sys.stdout = open('output_gf_test_{}.log'.format(test.file_item_to_test), 'a')

        result_dict = {}
        comment = ''
        exception_tr = []
        try:
            if test.test_type == TestType.PYTHON:
                self.pkg_setup(submission, test)
                result_dict, comment, exception_tr = test(submission)
            elif test.test_type == TestType.FILE:
                result_dict, comment, exception_tr = test(file_path, submission)
            conn.send([result_dict, comment, exception_tr])
            conn.close()
        except Exception as e:
            exception = getattr(e, 'message', repr(e))
            logger.error('THIS IS AN EXCEPTION THAT GETS PASSED {}. This shouldnt be empty'.format(exception))
            # TODO: logger.exception
            logger.exception('Attempted running test: test_type - {}, '.format(test.test_type)    \
                + 'file_item_to_test: {}, pkg_path: {} where '.format(test.file_item_to_test, test.pkg_path)    \
                + 'submission was {}'.format(submission))
            conn.send([{}, '', [exception]])
            conn.close()

    # TODO(manjrekarom): Handle unzipping of zips
    def make_pkg_full_path(self, submission, test):
        """
        Returns full path of the package from the information contained in
        :class:`~gradefast.submission.Submission` and :class:`~gradefast.test.GFTest`

        Parameters
        ----------
        submission: :class:`~gradefast.submission.Submission`
        
        test: :class:`~gradefast.test.GFTest`

        Returns
        -------
        str
            Full path of the package
        """
        file_item_to_test = test.file_item_to_test
        try:
            file_dict = submission.items[file_item_to_test]
        except KeyError as e:
            logger.exception('Exception when attempting item access on submission {} '.format(submission)    \
                + 'and item {}'.format(file_item_to_test))
            raise Exception("Specified file item {} doesn't exist for submission with team id {}"\
                .format(file_item_to_test, submission.team_id))

        file_extension = Path(file_dict['path']).suffix

        # means it is a package
        if file_extension == '':
            directory_path = file_dict['path']
            return os.path.abspath(os.path.join(directory_path, test.pkg_path))
        elif file_extension.lower() == '.zip':
            zip_path = file_dict['path']
            # check if corresponding unzipped folder exists
            file_item_to_test_unzipped = file_item_to_test + '_unzipped'
            if submission.items.get(file_item_to_test_unzipped) == None:
                # path to
                extracted_directory_path = Extracter.get_default_unzip_path(zip_path)
                # extract the zip file
                Extracter.extract_file(zip_path, extracted_directory_path)
            return os.path.abspath(os.path.join(extracted_directory_path, test.pkg_path))
        # what is it's a single python file outside of any package?
        else:
            return str(Path(file_dict['path']).resolve().parent)

    def _evaluate(self, submission, test):
        """
        Executes :class:`~gradefast.test.GFTest` according to the
        :class:`~gradefast.test.TestType` provided, on the given 
        :class:`~gradefast.submission.Submission`
        
        Parameters
        ----------
        submission: :class:`~gradefast.submission.Submission`
        test: :class:`~gradefast.test.GFTest`
        
        Returns
        -------
        result_dict: dict
        comment: str
        exceptions_tr: list
        
        """
        try:
            result_dict = {}
            comment = ''
            exception_tr = []
            
            # BEFORE TEST
            before_output = [command.run(submission) for command in test.before]

            if isinstance(test, GFCliTest):
                result_dict, comment, exception_tr = test(submission)
            if isinstance(test, GFCommandTest):
                result_dict, comment, exception_tr = test(submission)
            elif isinstance(test, GFTest):
                ctx = mp.get_context()
                par_conn, child_conn = ctx.Pipe()
                if test.test_type == TestType.FILE:
                    if submission.items.get(test.file_item_to_test) != None:
                        file_path = submission.items[test.file_item_to_test]['path']
                    else:
                        file_path = None
                    p = ctx.Process(target=self.run_test, args=(file_path, submission, test, child_conn,))
                elif test.test_type == TestType.PYTHON:
                    # TODO: package_path may be a list of packages
                    p = ctx.Process(target=self.run_test, args=(None, submission, test, child_conn,))
                p.start()
                if par_conn.poll(timeout=self.timeout):
                    result_dict, comment, exception_tr = par_conn.recv()
                p.join(timeout = self.timeout)
                p.terminate()
            # AFTER TEST
            after_output = [command.run(submission) for command in test.after]
        except Exception as e:
            # log all exceptions
            # print(traceback.format_exc())
            err_tr = getattr(e, 'message', repr(e))
            logger.exception("Error when attempting to evaluate submission {} with ".format(submission)
            + "test {}. The error was: {}".format(test, err_tr))
            return {}, '', [err_tr]

        return result_dict, comment, exception_tr

    # TODO: return result_group
    def __call__(self, submissions):
        # evaluate
        # on each submission in submissions run each test in tests
        task_name = ''
        theme_name = ''

        if isinstance(submissions, SubmissionGroup):
            task_name = submissions.task_name
            theme_name = submissions.theme_name

        result_group = ResultGroup(task_name, theme_name, {})
        exceptions = []

        for idx, submission in enumerate(submissions):
            # print(submission.file_list)
            # evaluate
            # if marks are not given, do no transformation of result
            
            start_time = time.time()

            result_dict, comment, exception = self._evaluate(submission, self.test)
            
            end_time = time.time()
            exec_time = end_time - start_time

            print('Evaluated submission of team: {} with result {}'.format(submission.team_id, result_dict))
            logger.debug('Evaluated submission of team: {} {}'.format(submission.team_id, result_dict))
            
            # TODO: can replace this method with Result.from_submission_test
            result = Result(submission.team_id, self.test.file_item_to_test, result_dict, 
            exec_time=exec_time, pkg_path=self.test.pkg_path, comment=comment, error=exception)
            
            result_group = Aggregate.combine(ResultGroup(task_name, theme_name, 
            {result.team_id: result}), result_group)
            
            result_group.to_json(self.result_path)
            exceptions.append(exception)

        return result_group, exceptions
