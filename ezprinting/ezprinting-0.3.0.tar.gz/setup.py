# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ezprinting']

package_data = \
{'': ['*']}

install_requires = \
['pycups>=1.9.74']

setup_kwargs = {
    'name': 'ezprinting',
    'version': '0.3.0',
    'description': 'Python package to easily print to a printer configured on either a CUPS server or Google Cloud Print.',
    'long_description': '# ezprinting\n\n## IMPORTANT NOTE!\nAs of version 0.3, support for GCP has been removed (Google announced that Google Cloud Print \nservice will be discontinued at the end of 2020).\n\n\n## Description\n\nPython package to easily submit print jobs to a printer configured on a CUPS server.\n\n\n## Installation ##\npip install ezprinting\nor\npoetry add ezpriting\n\npyCups is a dependency which needs libcups2-dev (this is the name on Ubuntu/Debian) \nto be installed (sudo apt install libcups2-dev).\n\n## Quick Start Guide ##\n\n**Note:** success=True/False in the examples below indicate whether or not the print job was successfully submitted to CUPS, not that it was successfully printed.\n\n### 1. Option one:\n```\nfrom ezprinting import PrintJob\n\n\nwith open(\'dummy.pdf\', \'rb\') as f:\n    content = f.read()\n\n# Use host="cups.domain.tld:631", username="lpadmin", password="123456" to specify\n# a remote cups server with authentication.\n# By default "localhost:631" is assumed with blank user/passwd\npjob = PrintJob.new_cups(printer_name=\'cups-printer-name\', content=content)\nsuccess = pjob.print()\n\n\n\n\n```\nIf **content** is PDF, there is no need to specify content_type. Auto detection of content-type is not available yet, \nif you skip content_type than "application/pdf" is assumed.\n\n\n### 2. Option two:\n```\nfrom ezprinting import PrintServer, Printer, PrintJob\nimport json\n\nwith open(\'dummy.pdf\', \'rb\') as f:\n    content = f.read()\n\n# If we want CUPS on localhost...\nprint_server = PrintServer.cups()\n# If we want remote CUPS server...\nprint_server = PrintServer.cups(host="cups.domain.tld:631", username="lpadmin", password="123456")\n\nconnection_ok, message = print_server.test_connection()\nprint("Testing connection: {} - {}".format(connection_ok, message))\n\n# Let\'s check what printers we have available\nif connection_ok:\n    printers = print_server.get_printers()\n    print(json.dumps(printers, sort_keys=True, indent=4))\n    printer = Printer(print_server, \'printer name (CUPS) or printer ID (GCP)\')\n    printer_exists = printer.check_printer_exists() \n    print("Does the printer exist on that print server? {}".format(printer_exists))\n    if printer_exists:\n        pjob = PrintJob(printer=printer, content=content)\n        success = pjob.print()\n        print(\'Print job submitted with success? {}\'.format(success))\n        if success:\n            print(\'Print job id: {}\'.format(pjob.job_id))\n```\n\n## Testing\n\nYou can easily test the functionality of this package by making use of the built in test code.\n\nTo test CUPS functionality you must have a valid *tests/private_data/cups.json*.\n\nTo define the documents you want to test print and the printers where those documents should be test printed you must\nhave the files:\n\n* tests/private_data/printers.json\n* tests/data/print_tests.json\n\nCommented sample json files are provided (do not forget to delete the comments, JSON does not support comments).\n\n## State of this package\nThe code in this repository is being used in production and mostly works. However, it is very new and does not handle \nwell exceptional cases. A large piece that is still missing is functionality on the PrintJob class to track the \nlifecycle of a print job and being able to figure out what went wrong when something goes wrong (e.g. paper jam, out of\n paper, out of ink, etc). Your help is welcome to fill in the gaps. And please, do file bug reports.\n\n## Main TO-DOs\n* [ ] Develop functionality on the PrintJob class to track the state of a print job and identify causes of failure (e.g. jam, out of paper, out of ink, etc)  \n* [ ] Enable printing directly to IPP printers;\n* [ ] Add-on: mqtt monitor to send print jobs received on mqtt topics, with full QoS implementation; \n\n**Feel free to help fill-in the gaps!**\n\n\n## Other notes\n* pycups <=1.9.73 has a bug that prevents CUPS from working. You will see a filter failed or some kind of "document corrupted" message;\n\n',
    'author': 'Marcelo Bello',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mbello/ezprinting',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
