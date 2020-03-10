# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_security_telegram_webhook']

package_data = \
{'': ['*']}

install_requires = \
['fastapi']

setup_kwargs = {
    'name': 'fastapi-security-telegram-webhook',
    'version': '0.1.0',
    'description': '',
    'long_description': '# fastapi-security-telegram-webhook\n\nPlugin for [FastAPI](https://github.com/tiangolo/fastapi) which allows you secure your Telegram Bot API webhook endpoint\n with IP restriction and optional secret token.\n \n\n\n## How to use\n\nUse pip or another package management util:\n```bash\npip install fastapi-security-telegram-webhook\n```\n\nor\n\n```bash\npoetry add fastapi-security-telegram-webhook\n```\n\nor\n\n```bash\npipenv install fastapi-security-telegram-webhook\n```\n\nPackage contains two Security objects: \n - `OnlyTelegramNetwork` allows request only from telegram subnets\n - `OnlyTelegramNetworkWithSecret` additionally check secret in path\n \nExample with `OnlyTelegramNetworkWithSecret`. Pay attention to `{secret}` in path operation, it\'s required\n\n```python\nfrom fastapi import FastAPI, Body, Depends\nfrom fastapi_security_telegram_webhook import OnlyTelegramNetworkWithSecret\n\napp = FastAPI()\nwebhook_security = OnlyTelegramNetworkWithSecret(real_secret="your-secret-from-config-or-env")\n\n# {secret} in path and OnlyTelegramNetworkWithSecret as dependency:\n@app.post(\'/webhook/{secret}\', dependencies=[Depends(webhook_security)])\ndef process_telegram_update(update_raw = Body(...)):\n   ...\n\n```\n',
    'author': 'Dima Boger',
    'author_email': 'kotvberloge@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/piterpy-meetup/fastapi-security-telegram-webhook',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
