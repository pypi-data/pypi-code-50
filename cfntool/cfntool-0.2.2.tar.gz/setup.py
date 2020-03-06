# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cfntool']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.12.15,<2.0.0',
 'ccalogging>=0.3.3,<0.4.0',
 'chaim>=0.8.0,<0.9.0',
 'getopt2>=0.0.3,<0.0.4']

entry_points = \
{'console_scripts': ['cfn = cfntool.installtemplate:main']}

setup_kwargs = {
    'name': 'cfntool',
    'version': '0.2.2',
    'description': 'Tool to Install and Delete Cloudformation stacks easily.',
    'long_description': "cfntool\n=======\n\nA tool to Create and Delete Cloudformation stacks easily.\nUses credentials from your `~/.aws/credentials` file via boto3\n\nInstall\n-------\n\n::\n\n  $ python3 -m pip install cfntool --user\n\n\nUsage\n-----\n\n::\n\n  cfn [-options]\n\n  options:\n      -h This help\n      -m parameter list string:\n            'something=somevalue,somethingelse=someothervalue'\n      -P profile to use to install the stack (not required if 'all' is chosen)\n\n  required options:\n      -a account name\n      -n name of stack\n      -p product tag\n      -t full path to Cloudformation template to use\n\n  All actions are mutually exclusive\n  you must provide one action\n\n  Actions:\n      -A install/update all accounts\n      -D delete named stack\n      -I install/update the named stack\n      -S status of named stack\n\n  if you provide more than one action, the last one on the\n  command line 'wins'.\n\nExamples\n--------\n\nCreate a stack from a yaml template::\n\n  $ cfn -I -p mytool -P myaccountalias -m myaccount -n myStackName \\\n      -t ~/src/mystack.yaml -m 'LambdaVersion=0.0.2,Owner=SRE'\n\n  06/03/2020 08:40:05 [INFO ]  profile: myaccountalias, account id 1234567890, account name myaccount\n  06/03/2020 08:40:06 [ERROR]  stack: myStackName does not exist\n  06/03/2020 08:40:06 [WARNI]  stack myStackName does not exist (anymore)\n  06/03/2020 08:40:06 [INFO ]  creating stack myStackName\n  06/03/2020 08:41:47 [INFO ]  Stack myStackName is CREATE_COMPLETE\n\n\nStatus of named stack::\n\n  $ cfn -S -P myaccountalias -n myStackName\n\n  06/03/2020 08:42:14 [INFO ]  stack myStackName is status: CREATE_COMPLETE\n\nDelete a stack::\n\n  $ cfn -D -P myaccountalias -n myStackName\n\n  06/03/2020 08:44:39 [INFO ]  Stack myStackName is CREATE_COMPLETE\n  06/03/2020 08:44:39 [WARNI]  deleting stack: myStackName\n  06/03/2020 08:46:20 [ERROR]  stack: myStackName does not exist\n  06/03/2020 08:46:20 [WARNI]  stack myStackName does not exist (anymore)\n  06/03/2020 08:46:20 [INFO ]  stack myStackName is status: None\n",
    'author': 'Chris Allison',
    'author_email': 'chris.charles.allison@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ccdale/cfntool',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
