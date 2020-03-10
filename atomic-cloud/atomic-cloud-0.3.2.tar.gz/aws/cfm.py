import os
import sys
import time
import itertools

import boto3
from botocore.exceptions import ClientError
from jinja2 import Environment, Template, FileSystemLoader

from po.pretty_object import PrettyObject

###############################################################################
# CloudFormation
###############################################################################

# Stack Status Values
CREATE_COMPLETE = 'CREATE_COMPLETE'
CREATE_IN_PROGRESS = 'CREATE_IN_PROGRESS'
CREATE_FAILED = 'CREATE_FAILED'
ROLLBACK_IN_PROGRESS = 'ROLLBACK_IN_PROGRESS'
ROLLBACK_FAILED = 'ROLLBACK_FAILED'
ROLLBACK_COMPLETE = 'ROLLBACK_COMPLETE'
DELETE_IN_PROGRESS = 'DELETE_IN_PROGRESS'
DELETE_FAILED = 'DELETE_FAILED'
DELETE_COMPLETE = 'DELETE_COMPLETE'
UPDATE_IN_PROGRESS = 'UPDATE_IN_PROGRESS'
UPDATE_COMPLETE_CLEANUP_IN_PROGRESS = 'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'
UPDATE_COMPLETE = 'UPDATE_COMPLETE'
UPDATE_ROLLBACK_IN_PROGRESS = 'UPDATE_ROLLBACK_IN_PROGRESS'
UPDATE_ROLLBACK_FAILED = 'UPDATE_ROLLBACK_FAILED'
UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS = 'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS'
UPDATE_ROLLBACK_COMPLETE = 'UPDATE_ROLLBACK_COMPLETE'
REVIEW_IN_PROGRESS = 'REVIEW_IN_PROGRESS'

# Capability Values
CAPABILITY_IAM = 'CAPABILITY_IAM'
CAPABILITY_NAMED_IAM = 'CAPABILITY_NAMED_IAM'
CAPABILITY_AUTO_EXPAND = 'CAPABILITY_AUTO_EXPAND'

cfn = boto3.client('cloudformation')
po = PrettyObject()

_deletion_stack = []

def add_to_deletion_stack(stack_name: str):
    global _deletion_stack
    dstring = f"cfm.delete_stack(stack_name = '{stack_name}')\n"
    _deletion_stack.append(dstring)

def write_deletion_stack(fname: str):
    """
    Writes a python file that, when run, deletes the resources created since the last time this was executed (or the last call of clear_deletion_stack()).
    You'll want to run this whenever you create a set of dependent stacks that should be removed as a single unit.

    :param fname: The path to the deletion script you're creating. The file should be named something like 'xyz.py' - the output is a python script.
    """
    global _deletion_stack
    out = "from aws import cfm\nprint('deleting stacks:')\n"
    while len(_deletion_stack) > 0:
      out += _deletion_stack.pop()
    file = None
    try:
      file = open(fname, 'wt')
      file.seek(0)
      file.write(out)
      file.truncate()
      print(f"wrote stack deletion file '{fname}'")
      clear_deletion_stack()
    finally:
      if file is not None:
        file.close()

def clear_deletion_stack():
    """
    Clears the deletion stack. Use when you don't want to include previously created resources in the next deletion script you generate with write_deletion_stack().
    Note: This happens automatically whenever you call write_deletion_stack(), so there's no need to call it immediately following a write.
    """
    global _deletion_stack
    _deletion_stack = []

def list_stacks(stack_status_filter=None):
    """
    Gets a list of all stacks.
    
    :param stack_status_filter: The list of stack status types to include (if not present, all types are included)
    :return: a list of all stack summaries or None if the filter was bad
    """
    if stack_status_filter is str:
        stack_status_filter = [stack_status_filter]  # handles single filter as string
    stacks_remain = True
    all_stacks = []
    token = None
    try:
        while stacks_remain:
            if token and stack_status_filter:
                stacks = cfn.list_stacks(StackStatusFilter=stack_status_filter, NextToken=token)
            elif stack_status_filter:
                stacks = cfn.list_stacks(StackStatusFilter=stack_status_filter)
            elif token:
                stacks = cfn.list_stacks(NextToken=token)
            else:
                stacks = cfn.list_stacks()
            all_stacks.extend(stacks['StackSummaries'])
            if 'NextToken' in stacks:
                token = stacks['NextToken']
            stacks_remain = 'NextToken' in stacks
    except ClientError:
        return None
    return all_stacks


def describe_stacks(stack_name=None):
    """
    Describes all stacks (or one with a given name)
    
    :param stack_name: The name or ID of the stack you'd like to describe. Must be an ID for deleted stacks
    :return: a list of all stack summaries (or, if a stack_name was specified and not found, None)
    """
    stacks_remain = True
    all_stacks = []
    token = None
    try:
        while stacks_remain:
            if token and stack_name:
                stacks = cfn.describe_stacks(StackName=stack_name, NextToken=token)
            elif stack_name:
                stacks = cfn.describe_stacks(StackName=stack_name)
            elif token:
                stacks = cfn.describe_stacks(NextToken=token)
            else:
                stacks = cfn.describe_stacks()
            all_stacks.extend(stacks['Stacks'])
            if 'NextToken' in stacks:
                token = stacks['NextToken']
            stacks_remain = 'NextToken' in stacks
    except ClientError:  # if the stack_name provided isn't found
        return None
    return all_stacks


def get_stack_status(stack_name: str):
    """
    Extracts just the StackStatus field.  This is useful for
    waiting on the stack for a status change.

    :param stack_name: Stack to query.
    :return: string value of status or None if the stack wasn't found
    """
    stacks = describe_stacks(stack_name=stack_name)
    if stacks:
        return stacks[0]['StackStatus']
    return None  # changed from a string status


def get_stack(stack_name: str):
    """
    Gets the stack information.

    :param stack_name: Stack to query.
    :return: `cloudformation.Stack <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#stack>`_
    """
    stacks = describe_stacks(stack_name)
    if stacks:
        return stacks[0]
    return None


def stack_exists(stack_name: str):
    """
    Returns true if StackStatus == CREATE_COMPLETE
    :param stack_name: Name of stack
    :return: True if StackStatus is CREATE_COMPLETE
    """
    # stacks = list_stacks(stack_status_filter = ['CREATE_COMPLETE', 'CREATE_IN_PROGRESS'])
    if describe_stacks(stack_name=stack_name):
        return True
    return False


def wait_for_stack(stack_name: str, pend_status: str):
    """
    Waits for the specified pend_status to clear.   This function
    will provide a spinner while waiting for the status to change.

    :param stack_name: Name of stack to observe.
    :param pend_status: Status we will wait on until it changes.  For
    example, if the pend_status == CREATE_IN_PROGRESS, we'll wait until
    it changes to something else like CREATE_COMPLETED.

    :return:
    """
    spinner = itertools.cycle('-\\|/')

    status = pend_status
    print(status)
    while status == pend_status:
        sys.stdout.write(spinner.__next__())  # write the next character
        sys.stdout.flush()  # flush stdout buffer (actual character display)
        sys.stdout.write('\b')
        time.sleep(1)
        status = get_stack_status(stack_name)

    print(status)
    return status


def create_stack(fn: str, params={}, capabilities=[], stack_name: str = None, debug = False):
    """
    Creates a cloud formation stack.  The template file is preprocesssed with Jinja using
    the passed in parameters.

    :param fn: File name of cloud formation template
    :param params: Parameters required by the template
    :param capabilities: Used to add IAM capabilities if we are doing
    something that is powerful such as creating roles.
    :param stack_name: Used to specify a non-standard stack name
    :param debug: If set to True, outputs the template after Jinja template rendering.  Default is False.
    :return: `cloudformation.Stack <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#stack>`_
    """
    file = None

    try:
        # create stack name
        (path, filename) = os.path.split(fn)
        if stack_name is None:
            stack_name = params['EnvType'] + '-' + filename.split('.')[0]

        # if stack already exists, skip and return true
        if stack_exists(stack_name):
            print(f"{stack_name} already exists - skipping stack creation.")
            return True

        print(f"Creating {stack_name}...")

        # Render Template
        env = Environment(loader=FileSystemLoader(path))
        template = env.get_template(filename)

        template_body = template.render(params)

        if debug:
            print(template_body)

        # get params list
        template_validated = cfn.validate_template(TemplateBody=template_body)

        # create parameters
        if template_validated.get('Parameters') is not None:
            cfn_params = [
                {'ParameterKey': kvp['ParameterKey'], 'ParameterValue': params[kvp['ParameterKey']]}
                for kvp in template_validated['Parameters']
            ]

        # create stack
        metadata = cfn.create_stack(StackName=stack_name,
                                   TemplateBody=template_body,
                                   Parameters=cfn_params,
                                   Capabilities=capabilities,
                                   OnFailure="DO_NOTHING")

        # wait for the stack
        status = wait_for_stack(stack_name, CREATE_IN_PROGRESS)
        summary = get_stack(stack_name)
        po.print(summary)

        if status != CREATE_COMPLETE: 
            raise Exception(f'Stack creation failed: {stack_name}')

        add_to_deletion_stack(stack_name)
        return summary

    except IOError as e:
        print(f"Can't open stack {e}") 

    finally: 
        if file is not None:
            file.close()


def get_export_value(stack_name: str, export_name: str):
    """
    Gets a value that the given stack has exported

    :param stack_name: the name of the stack that exports the value
    :param export_name: the exported name (unique)
    :return: the exported value as a string
    """
    if not stack_exists(stack_name):
      return None
    outs = get_stack(stack_name)['Outputs']
    if not outs:
      return None
    for out in outs:
      if out['ExportName'] == export_name:
        return out['OutputValue']


def delete_stack(stack_name: str):
    """
    Deletes the specified stack.

    :param stack_name: Name of stack to remove
    :return: Last known status.
    """
    print(f'Deleting {stack_name}...')
    cfn.delete_stack(StackName=stack_name)
    status = wait_for_stack(stack_name, DELETE_IN_PROGRESS)

    return status
