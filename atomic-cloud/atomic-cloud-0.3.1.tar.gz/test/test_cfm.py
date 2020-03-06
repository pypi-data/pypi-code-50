from unittest import TestCase

from aws.cfm import *
import os


def abs_path(file: str):
    """
    Sets an absolute path relative to the **k9** package directory.

    Example::
        result = abs_path('myfile)

    Result::
        /Users/simon/git/k9/k9/myfile


    This is used primarily for building unit tests within the K9 package
    and is not expected to be useful to K9 library users.

    :param file: File or directory to attach absolute path with
    :return: absolute path to specified file or directory
    """
    basedir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(basedir, file)


class TestCloudFormation(TestCase):

    def describe_stacks_fail(self):
        self.assertIsNone(describe_stacks('bogus-garbage-1234')[0])

    def test_get_stack_status_fail(self):
        status = get_stack_status('bogus-garbage-1234')
        self.assertIsNone(status)

    def test_get_stack_fail(self):
        stack = get_stack('bogus-garbage-1234')
        self.assertIsNone(stack)

    def test_stack_exists_fail(self):
        self.assertFalse(stack_exists('bogus-garbage-1234'))

    def test_describe_stacks_name(self):
        try:
            create_stack(abs_path('test/unit-basic-stack.yaml'), stack_name='unit-describe-name')
            stacks = describe_stacks(stack_name='unit-describe-name')
            self.assertIsNotNone(stacks[0])
            self.assertEqual(stacks[0]['StackName'], 'unit-describe-name')
        finally:
            delete_stack('unit-describe-name')

    def test_list_stacks_bad_filter(self):
        try:
            n = list_stacks(stack_status_filter=['asdf_garbo'])
            self.assertIsNone(n)
        except Exception as e:
            print(e)
            self.fail('Hit an exception with bad filter')

    def test_list_stacks_good_filter(self):
        try:
            stack = create_stack(abs_path('test/unit-basic-stack.yaml'), stack_name='unit-list-good-filter')
            stack_list = list_stacks(stack_status_filter=['CREATE_COMPLETE'])
            found = False
            for s in stack_list:
                if s['StackName'] == 'unit-list-good-filter':
                    found = True
                    break
            self.assertTrue(found)
        finally:
            delete_stack('unit-list-good-filter')

    def test_list_stacks_no_filter(self):
        try:
            stack = create_stack(abs_path('test/unit-basic-stack.yaml'), stack_name='unit-list-no-filter')
            stack_list = list_stacks()
            found = False
            for s in stack_list:
                if s['StackName'] == 'unit-list-no-filter':
                    found = True
                    break
            self.assertTrue(found)
        except Exception as e:
            print(e)
            self.fail('Probably hit a throttling exception. This does not mean the fn is broken.')
        finally:
            delete_stack('unit-list-no-filter')

    def test_get_stack_status_success(self):
        try:
            stack = create_stack(abs_path('test/unit-basic-stack.yaml'), stack_name='unit-status-success')
            status = get_stack_status(stack_name='unit-status-success')
            self.assertEqual(status, 'CREATE_COMPLETE')
        finally:
            delete_stack('unit-status-success')

    def test_get_stack_success(self):
        try:
            stack = create_stack(abs_path('test/unit-basic-stack.yaml'), stack_name='unit-get-stack-success')
            found = get_stack('unit-get-stack-success')
            self.assertIsNotNone(found)
            self.assertEqual(found['StackName'], 'unit-get-stack-success')
        finally:
            delete_stack('unit-get-stack-success')

    def test_stack_exists_success(self):
        try:
            create_stack(abs_path('test/unit-basic-stack.yaml'), stack_name='unit-stack-exists-success')
            self.assertTrue(stack_exists('unit-stack-exists-success'))
        finally:
            delete_stack('unit-stack-exists-success')

    def test_deletion_stack(self):
        f = None
        try:
            clear_deletion_stack()
            add_to_deletion_stack('stack-1')
            add_to_deletion_stack('stack-2')
            add_to_deletion_stack('stack-3')
            write_deletion_stack('test-teardown.py')
            f = open('test-teardown.py')
            printed = f.read()
            expected = "from aws import cfm\nprint('deleting stacks:')\ncfm.delete_stack(stack_name = 'stack-3')\ncfm.delete_stack(stack_name = 'stack-2')\ncfm.delete_stack(stack_name = 'stack-1')\n"
            self.assertEqual(printed, expected)
        finally:
            if f:
                f.close()
            if os.path.exists('test-teardown.py'):
                os.remove('test-teardown.py')
            clear_deletion_stack()