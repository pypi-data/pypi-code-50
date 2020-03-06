# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['bookify']
install_requires = \
['stapler==1.0.0b1']

entry_points = \
{'console_scripts': ['bookify = bookify:main']}

setup_kwargs = {
    'name': 'bookify',
    'version': '1.1.1',
    'description': 'Transform pdf files into books for double-sided printing',
    'long_description': "# Bookify\n> Transform pdf files into books for double-sided printing\n\n## Preparing the book: Layout\n1. Use Calibre to convert the book to .docx format\n2. Modify the resulting docx, applying the following changes:\n\t- Add title page + empty page (usually the second page is empty)\n\t- Maybe add extra pages such as index or dedication\n\t- Add page numbering (make sure to make it start only after the special pages such as index/dedication)\n\t- Make sure that every new chaper is in an odd page (this is to make it so that the first page of every chaper appears on the left)\n\t- Make the total number of pages a multiple of 4 (if it's not, empty pages will be added at the end to pad it)\n\t- It's recommended to set the size of the document to A5 and use generous margins\n3. Export the document into a pdf (we will refer to this pdf as `formatted.pdf`)\n\n**Note**: You can use [this docx](https://raw.githubusercontent.com/corollari/bookify/master/book.docx) as a template and/or example of the book layout described.\n\n## Build book\n### Install pdfjam\n```\nsudo apt-get install pdfjam # Ubuntu\nsudo dnf install texlive-pdfjam-bin # Fedora\n```\n\n### Build\n```\npip install bookify\nbookify formatted.pdf 20\n```\n**Usage**: First argument (`formatted.pdf`) is the name of the pdf and second argument (`20`) is the signature size, that is, the number of pages per booklet\n\n## Extra: Getting books from wattpad\n```\npip install FanFicFare\nfanficfare https://www.wattpad.com/story/9999999-story-title\n```\nUse URLs like:\n * https://www.wattpad.com/story/9999999-story-title\n * https://www.wattpad.com/story/9999999\n * https://www.wattpad.com/9999999-chapter-is-ok-too\n",
    'author': 'Albert',
    'author_email': 'github@albert.sh',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
