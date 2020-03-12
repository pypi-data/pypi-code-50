# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['aws_lambda']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.10.7,<2',
 'botocore>=1.13.7,<2',
 'docutils>=0.14,<0.16',
 'six>=1.12.0,<2']

setup_kwargs = {
    'name': 'python-lambda-4dn',
    'version': '2.0.0b1',
    'description': 'A forked version of python-lambda for 4DN-DCIC use in packaging and deploying lambda functions.',
    'long_description': '=================\npython-lambda-4dn\n=================\n\n(python-λ forked for 4DN-DCIC projects)\n---------------------------------------\n\n\n.. image:: https://img.shields.io/pypi/v/python-lambda-4dn.svg\n  :alt: Pypi\n  :target: https://pypi.python.org/pypi/python-lambda-4dn/\n\n.. image:: https://travis-ci.org/4dn-dcic/python-lambda.svg?branch=master\n  :alt: Build Status\n  :target: https://travis-ci.org/4dn-dcic/python-lambda\n\n.. image:: https://coveralls.io/repos/github/4dn-dcic/python-lambda/badge.svg?branch=master\n  :alt: Coverage\n  :target: https://coveralls.io/github/4dn-dcic/python-lambda?branch=master\n\nThis is a toolset for developing and deploying *serverless* Python code in AWS Lambda.\n\n.. Important::\n\n This is a FORK of Nick Ficano\'s `Python-lambda <https://pypi.python.org/pypi/python-lambda>`_\n package. It will NOT be updated regularly and is frozen for the needs of projects at the\n `4D Nucleome Data Coordination and Integration Center (4DN-DCIC)\n <https://github.com/4dn-dcic>`_.\n\nDescription\n===========\n\nAWS Lambda is a service that allows you to write Python, Java, or Node.js code that\ngets executed in response to events like http requests or files uploaded to S3.\n\nWorking with Lambda is relatively easy, but the process of bundling and deploying your code\nis not as simple as it could be.\n\nThe *Python-Lambda* library takes away the guess work of developing your Python-Lambda\nservices by providing you a toolset to streamline the annoying parts.\n\nImportant Legal Notice\n======================\n\nThe original `Python-lambda <https://pypi.python.org/pypi/python-lambda>`_ is licensed under\nan ISCL license. `The version of that license active at time of the fork is here\n<https://github.com/nficano/python-lambda/blob/01f1b8c3651de4e772618851b2117277ca95b1b4/LICENSE>`_.\nGithub\'s summary of that license describes it as:\n\n A permissive license lets people do anything with your code with proper attribution\n and without warranty. The ISC license is functionally equivalent to the BSD 2-Clause\n and MIT licenses, removing some language that is no longer necessary.\n\nSince our derivative work is covered under the MIT license, and on a theory\nthat the underlying license is equivalent to the MIT license,\nwe shorthand our licensing requirements as just "MIT" because that\'s more consistent\nwith how we describe licensing for other 4DN-DCIC software.\nHowever, for the properly formal legal detail,\nplease refer to our actual `LICENSE <LICENSE>`_.\n\nSystem Requirements\n===================\n\n* Python 3.6\n* Pip (Any should work)\n* Virtualenv (>=15.0.0)\n\nSetting Up a Virtual Environment (OPTIONAL)\n===========================================\n\nThis is optional.\nIf you do not create a virtual environment, Poetry will make one for you.\nBut there are still good reasons you might want to make your own, so here\nare three ways to do it:\n\n* If you have virtualenvwrapper that knows to use Python 3.6::\n\n   mkvirtualenv myenv\n\n* If you have virtualenv but not virtualenvwrapper, and you have python3.6 in your ``PATH``::\n\n   virtualenv myenv -p python3.6\n\n* If you are using ``pyenv`` to control what environment you use::\n\n   pyenv exec python -m venv myenv\n\n\nInstalling Poetry in a Virtual Environment\n==========================================\n\nOnce you have created a virtual environment, or have decided to just let Poetry handle that,\ninstall with poetry::\n\n   poetry install\n\n\nGetting Started\n===============\n\nUsing this library is intended to be as straightforward as possible.\nCode for a very simple lambda used in the tests is reproduced below.\n\n.. code:: python\n\n  config = {\n      \'function_name\': \'my_test_function\',\n      \'function_module\': \'service\',\n      \'function_handler\': \'handler\',\n      \'handler\': \'service.handler\',\n      \'region\': \'us-east-1\',\n      \'runtime\': \'python3.6\',\n      \'role\': \'helloworld\',\n      \'description\': \'Test lambda\'\n  }\n\n  def handler(event, context):\n      return \'Hello! My input event is %s\' % event\n\nThis code illustrates the two things required to create a lambda. The first is ``config``,\nwhich specifies metadata for AWS. One important thing to note in here is the ``role`` field.\nThis must be a IAM role with Lambda permissions - the one in this example is ours.\nThe second is the ``handler`` function. This is the actual code that is executed.\n\nGiven this code in ``example_function.py`` you would deploy this function like so:\n\n.. code:: python\n\n  from aws_lambda import deploy_function\n  import example_function\n  deploy_function(example_function,\n                  function_name_suffix=\'<suffix>\',\n                  package_objects=[\'list\', \'of\', \'local\', \'modules\'],\n                  requirements_fpath=\'path/to/requirements\',\n                  extra_config={\'optional_arguments_for\': \'boto3\'})\n\nAnd that\'s it! You\'ve deployed a simple lambda function. You can navigate to the AWS\nconsole to create a test event to trigger it or you can invoke it directly using Boto3.\n\nAdvanced Usage\n==============\n\nMany of the options specified in the above code block when it came to actually\ndeploying the function are not used. These become more useful as you want to make more\ncomplicated lambda functions. The ideal way to incorporate dependencies into lambda functions\nis by providing a ``requirements.txt`` file. We rely on ``pip`` to install these packages\nand have found it to be very reliable. While it is also possible to specify local modules\nas well through ``package_objects``, doing so is not recommended because those modules\nmust be specified at the top level of the repository in order to work out of the box.\nThere is a comment on this topic in ``example_function_package.py``\nwith code on how to handle it.\n\nTests\n========\n\nTests can be found in the ``test_aws_lambda.py``. Using the tests as a guide to develop\nyour lambdas is probably a good idea. You can also see how to invoke the lambdas directly\nfrom Python (and interpret the response).  You can invoke all of this by just doing::\n\n    pytest\n\nThe usual ``pytest`` arguments are permited. For example, to invoke an individual test,\nmention its name. To see verbose output, use ``-v``; or use ``-vv`` for extra-verbose output,\nas in::\n\n    pytest -vv -k test_deploy_lambda_with_package_and_requirements\n\n',
    'author': '4DN-DCIC Team',
    'author_email': 'support@4dnucleome.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/4dn-dcic/python-lambda',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<3.7',
}


setup(**setup_kwargs)
