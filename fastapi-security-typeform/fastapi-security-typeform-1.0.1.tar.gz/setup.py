# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_security_typeform']

package_data = \
{'': ['*']}

install_requires = \
['fastapi']

setup_kwargs = {
    'name': 'fastapi-security-typeform',
    'version': '1.0.1',
    'description': '',
    'long_description': '# fastapi-security-typeform\n\nSecurity plugin for [FastAPI](https://github.com/tiangolo/fastapi) which allows you check \n[Typeform signature](https://developer.typeform.com/webhooks/secure-your-webhooks/) in your webhook endpoint. \n\n## How to setup signing flow for your typeform webhook\n\n**Current flow** is here https://developer.typeform.com/webhooks/secure-your-webhooks/ \n(it\'s little bit a lie about `working only via API`)\n\ntl;dr:\n * create a webhook via UI or API\n * generate random string (secret)\n * update a webhook via UI or API with your secret\n \n\n\n## How to use\n\nUse pip or another package management util:\n```bash\npip install fastapi-security-typeform\n```\n\nor\n\n```bash\npoetry add fastapi-security-typeform\n```\n\nor\n\n```bash\npipenv install fastapi-security-typeform\n```\n\nThen initialize it with your webhook secret and pass it to endpoint as dependency.\n\nIt will raise 403 error if signature isn\'t valid.\n\n```python\nfrom fastapi import Depends, FastAPI\n\nfrom fastapi_security_typeform import SignatureHeader\n\napp = FastAPI()\nsignature_header_security = SignatureHeader(secret=b\'{your_secret}\')\n\n@app.post("/typeform_webhook")\ndef typeform_webhook(signature = Depends(signature_header_security)):\n    ...\n    return {"success": True}\n\n```\n',
    'author': 'Dima Boger',
    'author_email': 'meetup@piterpy.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/piterpy-meetup/fastapi-security-typeform',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
