# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['depdf', 'depdf.components']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.8.2,<5.0.0', 'pdfplumber>=0.5.16,<0.6.0']

setup_kwargs = {
    'name': 'depdf',
    'version': '0.1.1',
    'description': 'PDF table & paragraph extractor',
    'long_description': '# DePDF\n\nAn ultimate pdf file disintegration tool. DePDF is designed to extract tables and paragraphs into structured markup language [eg. html] from embedding pdf pages. You can also use it to convert page/pdf to html.\n\nBuilt on top of [`pdfplumber`](https://github.com/jsvine/pdfplumber)\n\n# Table of Contents\n[toc]\n\n\n# Installation\n`pip install depdf`\n\n# Example\n```python\nfrom depdf import DePDF\nfrom depdf import DePage\n\n# general\nwith DePDF.load(\'test/test_general.pdf\') as pdf\n    pdf_html = pdf.to_html\n    print(pdf_html)\n\n# with dedicated configurations\nc = Config(\n    debug_flag=True,\n    verbose_flag=True,\n    add_line_flag=True\n)\npdf = DePDF.load(\'test/test_general.pdf\', config=c)\npage_index = 23  # start from zero\npage = pdf_file.pages[page_index]\npage_soup = page.soup\nprint(page_soup.text)\n```\n\n\n# APIs\n| **functions** | usage |\n|:---:|---|\n| `extract_page_paragraphs` | extract paragraphs from specific page |\n| `extract_page_tables` | extract tables from specific page |\n| `convert_pdf_to_html` | convert the entire pdf to html | \n| `convert_page_to_html` | convert specific page to html | \n\n\n# In-Depth\n\n## In-page elements\n* Paragraph\n    + Text\n    + Span\n* Table\n    + Cell\n* Image\n\n## Common properties\n| **property & method** | explanation |\n|:---:|---|\n| `html` | converted html string |\n| `soup` | converted beautiful soup |\n| `bbox` | bounding box region | \n| `save_html` | write html tag to local file| \n\n## DePDf HTML structure\n```html\n<div class="{pdf_class}">\n    %for <!--page-{pid}-->\n        <div id="page-{}" class="{}">\n            %for {html_elements} endfor%\n        </div>\n    endfor%\n</div>\n```\n\n## DePage HTML element structure\n\n### Paragraph\n```html\n<p>\n    {paragraph-content}\n    <span> {span-content} </span>\n    ... \n</p>\n```\n\n### Table\n```html\n<table>\n    <tr>\n        <td> {cell_0_0} </td>\n        <td> {cell_0_1} </td>\n        ...\n    </tr>\n    <tr colspan=2>\n        <td> {cell_1_0} </td>\n        ...\n    </tr>\n    ...\n</table>\n```\n\n### Image\n```\n<img src="temp_depdf/$prefix.png"></img>\n```\n# Appendix\n\n## DePage element denotations\n> Useful element properties within page\n\n![page element](annotations.jpg)\n\n## todo\n\n* [ ] add support for multiple-column pdf page\n* [ ] better table structure recognition\n* [x] recognize embedded objects inside page elements',
    'author': 'Meltonization',
    'author_email': 'mengzy1989@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/meldonization',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
