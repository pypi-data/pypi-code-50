# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['laziest', 'laziest.conf']

package_data = \
{'': ['*']}

install_requires = \
['black>=18.3-alpha.0,<19.0',
 'clifier>=0.0.3,<0.0.4',
 'codegraph>=0.0.4,<0.0.5']

entry_points = \
{'console_scripts': ['lazy = laziest.conf.cli:init_cli']}

setup_kwargs = {
    'name': 'laziest',
    'version': '0.0.dev4',
    'description': '',
    'long_description': 'Laziest\n=======\n\nGenerator of test_*.py files for your Python code.\nPackage that trying generate unit tests for you.\n\nIn step of testing idea :)\n\nFrom code like this:\n\n.. code-block:: python\n\n    def one_condition_custom_exception_and_return_binary_op_and_key(arg1, arg2, arg3):\n        if arg1 == \'1\':\n            raise CustomException(\'we hate 1\')\n        elif arg2[3] > 2:\n            print(f\'{arg2[3]} more when 2\')\n        var = 1\n        alias = var\n        return arg1 * arg2[3] + arg3[\'number\'], var * arg1 * alias - 2\n\n\nLaziest create such test:\n\n.. code-block:: python\n\n    def test_one_condition_custom_exception_and_return_binary_op_and_key(capsys):\n\n        assert one_condition_custom_exception_and_return_binary_op_and_key(\n            arg1=-720, arg2=[1.14, 5.79, 0.67, -984], arg3={"number": 1}\n        ) == (708481, -722)\n\n        with pytest.raises(CustomException):\n            #  error message: we hate 1\n            one_condition_custom_exception_and_return_binary_op_and_key(\n                arg1="1", arg2=[1.14, 5.79, 0.67, 2.05], arg3={"number": 1}\n            )\n        one_condition_custom_exception_and_return_binary_op_and_key(\n            arg1=166, arg2=[1.14, 5.79, 0.67, 935], arg3={"number": 1}\n        )\n        captured = capsys.readouterr()\n        assert captured.out == "935 more when 2\\n"\n\n\n\nIntroducing\n-----------\n`>>> Some slides with idea <<<\n<https://docs.google.com/presentation/d/e/2PACX-1vSXnDvg4BbdOzuw9ryCuYUqbKtgtKYSNw2JfCc56_rwqH3Vqq2wDbsB_OWC6wuSmnQVpXSRtqgUP8gu/pub?start=false&loop=false&delayms=5000&slide=id.g7df2d22da0_0_0>`_\n\n\nHi!\n\nIf you was hope to see information of production-ready solution - sorry, no.\n\nThis is just a try to create POC of idea to generate unit tests based on AST.\n\nIn source code you can see a mess with very strange constractions and a lot of \'TODO\'s\nthis is only because pack in very active development phase and I forget idea to plan it first and then develop,\nbecause all my \'plans\' crashed after adding support of 4-5 AST nodes and their combinations\n\nYou can think about this project like a something \'study\':\nI invistigate metaprogramming and AST in idea generate unittests from source code :)\n\nAnd you can join me in this investigation if you interesting in this too!\nSo if you want to know how far this idea can go - join me in this interesting and fun road (check section Contributing)\n\n\nLittle bit of history\n---------------------\n\nThis is a 3rd version of package implementation, before using a mix of work with AST and tokenisation (current state)\nI tried different ways:\n\n1. inspect and other tools with live objects\n2. only syntax and tokens + regexes\n\nand the current state with AST.\n\nI also checked packages that already exist, but they produce different result (but maybe you will be interesting\nmore in them, when in this project in-work, so I attach links, if you don\'t know yet this packages - check them):\n\n\n\nInstallation:\n*************\n\n    pip install laziest\n\n\nUsage:\n*************\n\n.. code-block:: bash\n\n    lazy /path/to/python/code/files\n\n\nFor example:\n\n.. code-block:: bash\n\n    lazy /home/yourUser/laziest/tests/code_sample/done/conditions.py\n\n\nIt will generate test file in directory:\n\n.. code-block:: bash\n\n    /home/yourUser/laziest/tests/test_conditions.py\n\n\nRun tests with \'pytest\' to check that they are valid:\n\n.. code-block:: bash\n\n    pytest /home/yourUser/laziest/tests/functional/test_primitive_code.py\n\n\nFlag -d\n*******\n\nIf you want to generate empty tests in case if code not supported by generator yet, you can use flag \'-d\'.\nOutput will be - generated modules for all functions, but without asserts, in body of function you will see a\ncomment with error and \'pass\'.\n\nFor example, you have a code with logic, that not supported yet by generator, for example:\n\n.. code-block:: python\n\n    def string_format_named_three_args(arg1, arg2, arg3):\n        return \'{first} this is {name} ! {last}\'.format(name=arg1, first=arg2, last=arg3)\n\n\nIf you run lazy with flag \'-d\' - you will have success test generation and in test module you will see for this function test:\n\n.. code-block:: python\n\n    def test_string_format_named_three_args():\n\n        # string indices must be integers\n\n        # Traceback (most recent call last):\n        #  File "/Users/jvolkova/laziest/laziest/functions.py", line 163, in test_creation\n        #    func_definition, func_name, func_data, class_, class_method_type)\n        # TypeError: string indices must be integers\n        #\n        pass\n\nTests\n*****\n\nYou can run laziest tests with tox and check output.\n\n\n\nContributing\n************\n\nPull requests are welcome.\n\nWhat and how you can contribute?\n\n1. Ideas, comment to logic, some architecture and solutions plans - this is very welcome, because I works alone in\nthis thing and I can be very subjective and make wrong solutions.\n\n2. Cases in laziest/tests/code_sample/todo.\n\nHow create case:\n\n\nA. Use like a sample:\nlaziest/tests/code_sample/done/primitive_code.py\n\nB. You need to add operations from simplest (if they was not covered in different cases) to most complicated.\nSo, if you want add into code cases this function:\n\n.. code-block:: python\n\n    def function_with_vars_operations(new_name, use_data, validate_len=True):\n        if validate_len and len(new_name) > 15:\n                raise Exception("Impossible to set so long name. Lenght of the name must be < 15 symbols)\n        user_data[\'name\'] = new_name\n        return user_data\n\nC. You must to be sure, that already supported (or covered by cases):\n\n1. Functions with arguments\n2. if statements\n3. if statements with 2 or more conditions, because here we see \'validate_len\' - first condition and \'len(new_name) > 15\' - second condition\n4. you need check that conditions like \'if something\' are supported and covered or create cases for that separate. Why does it matter? Because, \'if validate_len\' under the hood mean \'validate_len != 0, validate_len != [], validate_len != () or any other empty container\'\n5. correct work with default values for \'validate_len=True\' - so need 2 assert, test with default value and without\n6. and etc.\n\nD. Try to split your result on blocks, if you don\'t see in code samples something that already ready.\nYou also can just run generator on separated functions to see does generator cover test case correct or not.\n\nFor current example \'separated\' functions can be at least (because 1 and 2 already supported):\n1.\n\n.. code-block:: python\n\n    def function_with_multiple_if_conditions(new_name, use_data, validate_len):\n        if validate_len != 0 and len(new_name) > 15:\n                raise Exception("Impossible to set so long name. Lenght of the name must be < 15 symbols)\n        return user_data\n\n\n2. now same but with default value\n\n.. code-block:: python\n\n    def function_with_default_value(new_name, use_data, validate_len=True):\n        if validate_len != False:\n                raise Exception("Impossible to set so long name. Lenght of the name must be < 15 symbols)\n        return user_data\n\n\n3. now same but without \'!=\'\n\n.. code-block:: python\n\n    def function_with_if_exist(new_name, use_data, validate_len=True):\n        if validate_len:\n                raise Exception("Impossible to set so long name. Lenght of the name must be < 15 symbols)\n        return user_data\n\nYou can change places of 2 and 3 - this is not matter.\n\n4. and at the end\n\n.. code-block:: python\n\n    def function_with_vars_operations(new_name, use_data, validate_len=True):\n        if validate_len and len(new_name) > 15:\n                raise Exception("Impossible to set so long name. Lenght of the name must be < 15 symbols)\n        user_data[\'name\'] = new_name\n        return user_data\n\n3. If you added some features in code, please make sure to update tests as appropriate:\n\nThis is mean you add in laziest/tests/code_sample/done construction that successful covered by generator and tests that was generated also passed.\n\n\nLicense\n*******\n\nThis project is licensed under the Apache License - see the `LICENSE`_ file for details\n\n.. _`LICENSE`: LICENSE\n',
    'author': 'xnuinside',
    'author_email': 'xnuinside@gmail.com',
    'url': 'https://github.com/xnuinside/laziest',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
