# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mate3']

package_data = \
{'': ['*']}

install_requires = \
['pymodbus>=2.2,<3.0']

extras_require = \
{'mate3_pg': ['psycopg2>=2.8.3,<3.0.0', 'pyyaml>=5.1.2,<6.0.0']}

entry_points = \
{'console_scripts': ['mate3 = mate3.main:main',
                     'mate3_pg = mate3.mate3_pg:main',
                     'mate3_write = mate3.mate3_write:main']}

setup_kwargs = {
    'name': 'mate3',
    'version': '0.4.0',
    'description': '',
    'long_description': '# Outback Mate 3s Python Library\n\nThis library provides complete support for all outback devices (at least in theory, \nI don\'t own all the devices so cannot test it). Writing data is also supported.\n\nThis data is accessed though the Mate3s\' Modbus interface. You must therefore \nhave a Mate3s which is connected to your local network using its ethernet port.\n\nTested on Python 3.7. May work on 3.6.\n\n## Installation\n\nThe recommended installation is as follows:\n\n```\npip install mate3\n```\n\nAfter this you should be able to run the `mate3` command.\n\n---\n\nIf you wish to edit the mate3 source (contributions are gladly received!), \nthen you can get the project directly from GitHub:\n\n```\n# Install poetry if you don\'t have it already (if you\'re unsure, you don\'t have it)\npip install poetry\n\n# Get the source\ngit clone https://github.com/adamcharnock/mate3.git\ncd mate3\n\n# Install mate3 and its dependencies. This also makes the mate3 command available.\npoetry install\n```\n\nAfter this you should be able to run the `mate3` command and edit the \nproject\'s source code.\n\n## Enabling the Modbus interface on your Mate 3\n\nTBA. System -> opticsre -> Modbus?\n\n## Using the library\n\nExample use:\n\n```python\nfrom mate3 import mate3_connection\nfrom mate3.parsers import ChargeControllerParser, ChargeControllerConfigurationParser\nfrom mate3.base_structures import Device\n\n# IP address of your Mate3s\nhost = \'192.168.0.123\'\n# The Modbus port on the Mate3s. The default (502) will be \n# fine unless you have configured your Mate3s differently\nport = 502\n\n# Connect to the Mate3s\nwith mate3_connection(host, port) as client:\n    # Get all blocks of fields from the Mate3s \n    # and print each one out.\n    all_blocks = client.all_blocks()\n    for block in all_blocks:\n        print(block)\n    \n    # Get all values for a specific device\n    values = client.get_device_blocks(Device.charge_controller)\n    print(list(values))\n\n    # Or get specific fields\n    values = client.get_values(\n        ChargeControllerParser.battery_current, \n        ChargeControllerParser.battery_voltage\n    )\n    # Prints a list of currents, one for each of your charge controllers\n    print(values[ChargeControllerParser.battery_current]) \n    # Prints a list of voltages, one for each of your charge controllers\n    print(values[ChargeControllerParser.battery_voltage])\n\n    # Writing data\n    # (BE CAREFUL! YOU COULD EASILY DAMAGE YOUR EQUIPMENT WITH THIS FEATURE!)\n    client.set_value(\n        field=ChargeControllerConfigurationParser.absorb_volts,\n        value=330,\n        port=3\n    )\n\n```\n\n## Using the command line interface (CLI)\n\n### Reading data\n\nA simple CLI is available which will read all available values from the Mate3:\n\n```\n$ mate3 -h\nusage: mate3 [-h] [--host HOST] [--port PORT]\n             [--format {text,prettyjson,json}]\n\nRead all available data from the Mate3 controller\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --host HOST, -H HOST  The host name or IP address of the Mate3\n  --port PORT, -p PORT  The port number address of the Mate3\n  --format {text,prettyjson,json}, -f {text,prettyjson,json}\n                        Output format\n```\n\nExample use:\n\n```\n$ mate3 --host 192.168.0.123\n```\n\n### Writing data\n\nYou can also set values on the mate3s using the `mate3_write` command.\n\n**WARNING:** Please make sure you read [the license](https://github.com/adamcharnock/mate3/blob/master/LICENSE) \nbefore using this feature. You could easily damage your equipment by setting \nincorrect values. Don\'t come crying to me if you destroy your batteries, \nor if this library takes it upon itself to do so.\n\nWarnings aside, here is how you use it:\n\n```\n# Show the available writable fields\n$ mate3_write -H 192.168.0.123 --list-fields\n\n# Start your backup generator! \n# (if that is what your inverter\'s auxiliary output is connected to)\n$ mate3_write -H 192.168.0.123 --set radian_inverter_configuration.aux_control=2\n\n# Turn it off again\n$ mate3_write -H 192.168.0.123 --set radian_inverter_configuration.aux_control=0\n```\n\n## Using `mate3_pg` to write data to Postgres\n\nThe `mate3_pg` command reads data from your Mate3 and writes it to a Postgres database.\n\nIn addition to a Mate3s connected to your network, you will need:\n\n* A running Postgres database\n* A definitions YAML file. ([example](https://github.com/adamcharnock/mate3/blob/master/pg_config.yaml))\n\nExample use:\n\n```\n$ mate3_pg \\\n    -H 192.168.0.123 \\ \n    --definitions /path/to/my/definitions.yaml \\\n    --database-url postgres://username:password@host:5432/database_name \\\n    --debug\n```\n\nYou will need to replace `192.168.0.123` with your Mate3s\' IP. Replace `/path/to/my/pg_config.yaml` with \na path to your definitions file (see [example](https://github.com/adamcharnock/mate3/blob/master/pg_config.yaml)).\nReplace the `username`, `password`, `host`, and `database_name` values with those for your Postgres database.\n\nFull details of the `mate3_pg` command:\n\n```\n$ mate3_pg --help\nusage: mate3_pg [-h] --host HOST [--port PORT] [--interval INTERVAL] [--database-url DATABASE_URL] --definitions DEFINITIONS [--hypertables] [--quiet] [--debug]\n\nRead all available data from the Mate3 controller\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --host HOST, -H HOST  The host name or IP address of the Mate3\n  --port PORT, -p PORT  The port number address of the Mate3\n  --interval INTERVAL, -i INTERVAL\n                        Polling interval in seconds\n  --database-url DATABASE_URL\n                        Postgres database URL\n  --definitions DEFINITIONS\n                        YAML definition file\n  --hypertables         Should we create tables as hypertables? Use only if you are using TimescaleDB\n  --quiet, -q           Hide status output. Only errors will be shown\n  --debug               Show debug logging\n```  \n\n## Various notes\n\nThe `structures.py` and `parsers.py` files are *auto generated* \nfrom the CSV files located in `registry_data/`. The CSV files are \ngenerated though text extraction from the \n[axs_app_note.pdf](http://www.outbackpower.com/downloads/documents/appnotes/axs_app_note.pdf) \nPDF provided by OutBack. This process is handled by two python files:\n\n* `csv_generator.py` – Extract the CSV data from the PDF\n* `code_generator.py` – Generate the Python code from the CSV data\n\n## Future work\n\n* Web interface?\n\n## Release process\n\n```\n# Check everything has been comitted\ngit diff\n\n# Update setup.py et al\ndephell deps convert\n\n# Up the version\npoetry version {major|minor|bug}\n\n# Review the resulting changes\ngit diff\n\n# Build\npoetry publish --build\n\n# Commit\ngit ci  -m "Version bump"\ngit push\ngit push --tags\n```\n\n## Credits\n\nThis is a heavily refactored version of \n[basrijn\'s Outback_Mate3 library](https://github.com/basrijn/Outback_Mate3).\nThank you basrijn!\n',
    'author': 'Adam Charnock',
    'author_email': 'adam@adamcharnock.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
