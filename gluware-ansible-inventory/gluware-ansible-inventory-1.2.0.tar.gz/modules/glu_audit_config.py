#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Gluware Inc.

ANSIBLE_METADATA = {'metadata_version': '1.2.0',
                    'status': ['stableinterface'],
                    'supported_by': 'Gluware Inc'}

DOCUMENTATION = '''
    module: glu_audit_config
    short_description: Perform a audit on the current captured config on a Gluware Device
    description:
        - For the current Gluware device trigger a audit on the current captured config in Gluware Control using the glu_device_id.
    version_added: '2.8'
    author:
        - John Anderson
    options:
        glu_connection_file:
            description:
                - Reference to a yaml file with connection information to the Gluware Control system.
                - The glu_devices inventory file (*glu_devices.yml) can be used for this file.
                - The keys of 'host', 'username', 'password', or 'trust_any_host_https_certs' are 
                  read from the this file for connection information.
                - For a key not found in the connection file then the environment variable is used, if available.
                - If the glu_connection_file is not specified then the environment variables are used, if available.
                - If there is no connection information then this module will error out.
            env:
                - name: GLU_CONTROL_HOST
                - name: GLU_CONTROL_USERNAME
                - name: GLU_CONTROL_PASSWORD
                - name: GLU_CONTROL_TRUST_ANY_HOST_HTTPS_CERTS
            type: string
            required: False
        glu_device_id:
            description:
                - Id in Gluware Control for the device.
                - The glu_devices inventory plugin automatically supplies this variable.
            type: string
            required: True
        audit_title:
            description:
                - Title for the audit report in Gluware Control.
            type: string
            required: True
        audit_policy_name:
            description:
                - Name of audit policy in Gluware Control to use for running the audit on the current captured configuration for the device.
            type: string
            required: True
        run_capture_config:
            description:
                - First run a capture of the config of the device before running the audit.
            type: boolean
            required: False
'''

EXAMPLES = r'''
    #
    # Trigger a Gluware Control audit on the current captured config for the current device.
    #
    - name: Creating a audit on the current captured config for the current device
      glu_audit_config:
        glu_connection_file : "{{ inventory_file }}"
        glu_device_id: "{{ glu_device_id }}"
        audit_title: "Checking config for correct NTP Server"
        audit_policy_name: "Data Center NTP Server Audit"

    #
    # Trigger a Gluware Control capture config and a audit for the current device.
    #
    - name: Capturing the current config then running a audit on that captured config for the current device
      glu_audit_config:
        glu_connection_file : "{{ inventory_file }}"
        glu_device_id: "{{ glu_device_id }}"
        audit_title: "Checking config for password strength"
        audit_policy_name: "Data Center Password Strength Audit"
        run_capture_config: True

'''

import re
import json
import sys
import os
import pprint
import yaml

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import Request, urllib_error, ConnectionError, socket, httplib

# Python 2/3 Compatibility
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

# Python 2/3 Compatibility
try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote



def run_module():

    # Module parameters
    module_args = dict(
        glu_device_id=dict(type='str', required=True),
        glu_connection_file=dict(type='str', required=False),
        audit_title=dict(type='str', required=True),
        audit_policy_name=dict(type='str', required=True),
        run_capture_config=dict(type='bool', required=False)
    )

    # Initialize the AnsibleModule to use in communication from and to the
    # code (playbook, etc) interacting with this module.
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    glu_connection_file = module.params.get('glu_connection_file')

    # Figure out the Gluware Control connection information.
    api_dict = {
        'host' : os.environ.get('GLU_CONTROL_HOST'),
        'username' : os.environ.get('GLU_CONTROL_USERNAME'),
        'password' : os.environ.get('GLU_CONTROL_PASSWORD'),
        'trust_any_host_https_certs' : os.environ.get('GLU_CONTROL_TRUST_ANY_HOST_HTTPS_CERTS'),
    }

    if (glu_connection_file) :
        # Try to read the inventory file for the connection information.
        file_err = ""
        if (os.path.exists(glu_connection_file)):
            try:
                with open(glu_connection_file, "r") as file:
                    file_dict = yaml.load(file, Loader=yaml.FullLoader)

                    # Merge the file values to the api_dict.
                    # This allows the environment vars to be overriden by the file values, if the environment values exist.
                    api_dict.update(file_dict)
            except IOError as io_err:
                file_err = "File error: "+io_err
                #Do nothing..

    # Test to see if the api_dict has all the required properties.
    if (not api_dict.get('host')):
        module.fail_json(msg="Missing 'host' or GLU_CONTROL_HOST to make Gluware API call.", changed=False)
    if (not api_dict.get('username')):
        module.fail_json(msg="Missing 'username' or GLU_CONTROL_USERNAME to make Gluware API call.", changed=False)
    if (not api_dict.get('password')):
        module.fail_json(msg="Missing 'password' or GLU_CONTROL_PASSWORD to make Gluware API call.", changed=False)
         
    # All the required values exist, so use the information in the file for the connection information.
    api_host = api_dict.get('host')

    # Make sure there is a http or https preference for the api_host
    if not re.match('(?:http|https)://', api_host):
        api_host = 'https://{host}'.format(host=api_host)

    # Make sure the Content-Type is set correctly.. otherwise it defaults to application/x-www-form-urlencoded which
    # causes a 400 from Gluware Control
    http_headers = {
        'Content-Type' : 'application/json'
    }

    # Create the request_handler to make the calls with.
    request_handler = Request(url_username=api_dict['username'], 
                            url_password=api_dict['password'], 
                            validate_certs=not(api_dict.get('trust_any_host_https_certs', False)), 
                            force_basic_auth=True,
                            headers=http_headers)

    # Default result JSON object
    result = dict(
        changed=False
    )

    # First get the id for the passed audit policy name.
    audit_policy_name = module.params.get('audit_policy_name')

    # This api call is for Gluware Control.
    api_url_1 = urljoin(api_host, '/api/audit/policies?name='+quote(audit_policy_name))

    # Make the actual api call.
    response = None
    try:
        response = request_handler.get(api_url_1)
    except (ConnectionError, httplib.HTTPException, socket.error, urllib_error.URLError) as e2:
        error_msg = 'Gluware Control call failed for getting audit policy: {msg}'.format(msg=e2)
        module.fail_json(msg=error_msg, changed=False)

    # Read in the JSON response to a object.
    arrayResponse = []
    try: 
        readResponse = response.read()
        arrayResponse = json.loads(readResponse)
    except (ValueError, TypeError) as e:
        error_msg = 'Gluware Control call getting audit policy response failed to be parsed as JSON: {msg}'.format(msg=e)
        module.fail_json(msg=error_msg, changed=False)

    if (len(arrayResponse) == 0):
        error_msg = 'No audit policy was found for the name: "{msg}"'.format(msg=audit_policy_name)
        module.fail_json(msg=error_msg, changed=False)

    if (len(arrayResponse) != 1):
        error_msg = 'More than one audit policy was found for the name: "{msg}"'.format(msg=audit_policy_name)
        module.fail_json(msg=error_msg, changed=False)

    audit_obj = arrayResponse[0]

    audit_policy_id = audit_obj.get('id')

    if (not audit_policy_id):
        error_msg = 'No audit policy id was found for the name: "{msg}"'.format(msg=audit_policy_name)
        module.fail_json(msg=error_msg, changed=False)

    
    # Make the api call to execute the audit.
    audit_title = module.params.get('audit_title')
    glu_device_id = module.params.get('glu_device_id')
    run_capture_config = module.params.get('run_capture_config')

    # This api call is for Gluware Control.
    api_url_1 = urljoin(api_host, '/api/audit/execute')
    
    # Create the body of the request.
    api_data = {
        "name" : audit_title,
        "deviceIds" : [glu_device_id],
        "policyId" : audit_policy_id
    }
    if (run_capture_config):
        api_data['capture'] = True
        api_data['snapshotName'] = audit_title

    http_body = json.dumps(api_data)

    # Make the actual api call.
    try:
        response = request_handler.post(api_url_1, data=http_body)
    except (ConnectionError, httplib.HTTPException, socket.error, urllib_error.URLError) as e2:
        error_msg = 'Gluware Control call failed for executing the audit: {msg}'.format(msg=e2)
        module.fail_json(msg=error_msg, changed=False)

    module.exit_json(**result)


def main():
    run_module()

if __name__ == '__main__':
    main()

