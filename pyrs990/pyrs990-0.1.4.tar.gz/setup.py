# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyrs990']

package_data = \
{'': ['*']}

install_requires = \
['defusedxml>=0.6.0,<0.7.0', 'requests>=2.23.0,<3.0.0']

entry_points = \
{'console_scripts': ['pyrs990 = pyrs990.entry_point:entry_point']}

setup_kwargs = {
    'name': 'pyrs990',
    'version': '0.1.4',
    'description': 'A tool for fetching and filtering IRS 990 data.',
    'long_description': '![PyRS990 Header](https://github.com/code-for-montana/pyrs990/raw/master/pyrs990_header.png)\n\nIt\'s a pun. Get it?\n\nA Python application and library that can grab all sorts of IRS Form 990\ndata on non-profit organizations and put it into a format that can be\nconsumed easily by other applications.\n\n## Up and Running\n\nThe instructions below should allow you to get the software working\nfor your purpose (user or developer). If you run into trouble please,\nplease let us know so that we can update the instructions (or fix the\nbug you ran into).\n\n### User\n\nFor now you need to clone the repo to use it. Eventually we\'ll package it.\n\n  1. Make sure you have Python 3.8 available\n  1. Install [Poetry](https://python-poetry.org/) if you don\'t already have it\n  1. Clone the whole repo, `cd` into the `pyrs990` directory\n  1. Install dependencies - `poetry install`\n  1. Run it, some very simple examples are below:\n      1. `poetry run python -m pyrs990 --zip 59801 --use-disk-cache`\n      1. ...more examples coming soon\n  1. Run the commands again, notice the cache speedup\n  1. The cache is set to `./.pyrs990-cache/`\n\n### Developer\n\nThis project uses [Poetry](https://python-poetry.org/) because it\'s pretty slick\nand does a lot of stuff automatically and the developers are not usually Python\npeople, so that\'s great!\n\n  1. Make sure you have Python 3.8 available\n  1. Install [Poetry](https://python-poetry.org/) if you don\'t already have it\n  1. Clone the whole repo, `cd` into the `pyrs990` directory\n  1. Install dependencies - `poetry install`\n  1. If you need to add dependencies:\n      1. `poetry add coolpkg`\n  1. Make a pull request!\n\n## About the Data\n\nRight now we pull data that originated with the IRS (hence the silly name)\nbut we get it from a couple sources and information about what is actually\navailable is a little spread out as well.\n\n### Structure\n\nThere are two indices used to narrow down the list of filing documents\nthat must be downloaded a satisfy a given query. The first is an\nannual index (we refer to it as "Annual" or "Annual Index" in the\ncode). This index contains all filings processed by the IRS for a\ngiven calendar year.\n\nNote that this does not necessarily have anything\nto do with the filing year. An organization might, for example, file\nits 2016 990 in either 2017 or 2018 (or even later). There is a field,\ndescribed below, called `tax_period` that reflects the filing period.\nIn the future, we intend to further abstract this so that it is\neasier to use.\n\nThe annual index also contains a field called `object_id` that tells\nus where to find the XML document that corresponds to that row in\nthe index. PyRS990 abstracts this away, but it is still good to be\naware of it.\n\nThe second index is the "Exempt Organizations Business Master File"\ndistributed by the IRS. We refer to it as the "BMF Index". This\nindex provides the physical address of each organization, along\nwith some other helpful information. This allows the data to be\nqueried by state, zip code, and so on, which greatly reduces the\nnumber of filing documents that must be downloaded for many queries.\n\nIndices may be used to query filing documents from the command\nline using various options. Note that there are options for both\nindices and for the filing documents themselves. If possible, it\nis a good idea to try to use as many index fields as you can to\nreduce the number of files you have to download.\n\nSee the example queries for more information.\n\n### Sources\n\nThe [IRS BMF index files](https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf)\nare hosted by the IRS directly and are available by state and region.\n\n[Descriptions of the variables](https://www.irs.gov/pub/irs-soi/eo_info.pdf)\ncontained in the files and the process used to build them are\nalso available (it is also linked from the page above).\n\nThe annual index files come from an\n[AWS S3 bucket](https://registry.opendata.aws/irs990/)\nmanaged by the IRS. The contents of the bucket are described there.\n\nThere is also [a readme](https://docs.opendata.aws/irs-990/readme.html)\nthat demonstrates how to download the files here (it is also linked\nfrom the page above):\n\nThe filing documents themselves also come from this same\n[AWS S3 bucket](https://registry.opendata.aws/irs990/)\nin XML format. For the extremely XML-savvy, you can checked out the\n[schema documentation](https://www.irs.gov/e-file-providers/current-valid-xml-schemas-and-business-rules-for-exempt-organizations-modernized-e-file)\non the IRS website. PyRS990 abstracts this away, however,\nso there\'s no real need to understand it if you only want to access the\ndata in a convenient format.\n\nFinally, while not strictly a data source, the\n[IRSx documentation](http://www.irsx.info/) created\nby ProPublica contains descriptions of many of the filing fields in a\nsimple, readable format. For developers, PyRS990 has been designed to\nwork with the exact XPath selectors listed in the IRSx documentation, so\nif you want to add a field to the `Filing` object, this is the place to\nlook first.\n',
    'author': 'George Lesica',
    'author_email': 'george@lesica.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/code-for-montana/pyrs990',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
