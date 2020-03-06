#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2020, Sviatoslav Sydorenko
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Say hello."""
from __future__ import absolute_import, print_function, unicode_literals
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = """
---
module: python.dist.boo
short_description: greeter
description:
- Says hello
version_added: "2.10"

options:
  name:
    description: >
      person to greet
    required: true
    default: "world"

requirements: []
author:
- "Sviatoslav Sydorenko (@webknjaz)"
notes:  []
"""


EXAMPLES = """
- python.dist.boo:
    name: you

- python.dist.boo:  # world
"""


import six

from ansible.module_utils.basic import AnsibleModule


class BooModuleError(RuntimeError):
    def __init__(self, msg, error_args={}, *args, **kwargs):
        super(BooModuleError, self).__init__(msg, *args, **kwargs)

        self.error_args = error_args
        self.error_args['msg'] = self.error_args.get('msg', msg)


class BooAnsibleModule(AnsibleModule):
    """Boo."""

    @classmethod
    def execute(cls):
        """Process Ansible module invocation."""
        cls().run()

    def __init__(self):
        """Initialize Ansible module spec."""
        super(BooAnsibleModule, self).__init__(
            argument_spec=dict(
                name=dict(default='world'),
            ),
            required_one_of=[['name']],
            supports_check_mode=False,
        )

    @property
    def name(self):
        """Retrieve name param."""
        return self.params['name']

    def run(self):
        """Execute action chosen."""
        try:
            greeting = self.hello()
        except BooModuleError as mod_err:
            self.fail_json(**mod_err.error_args)
        else:
            self.exit_json(
                msg='Greeting {name} completed.'.
                format(name=self.name.title()),
                greeting=greeting,
            )

    def hello(self):
        """Greet somebody."""
        if not self.name:
            raise BooModuleError(
                'Greeting `{name}` was unsuccessful'.
                format(name=self.name),
                error_args={
                    'msg': '`name` arg should not be empty',
                },
            )

        return 'Hello, {name}!'.format(name=self.name)


if __name__ == '__main__':
    BooAnsibleModule.execute()
