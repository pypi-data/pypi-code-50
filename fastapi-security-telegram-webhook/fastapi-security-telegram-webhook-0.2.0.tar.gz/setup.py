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
    'version': '0.2.0',
    'description': '',
    'long_description': '# fastapi-security-telegram-webhook\n\nPlugin for [FastAPI](https://github.com/tiangolo/fastapi) which allows you to secure your Telegram Bot API webhook\n endpoint with IP restriction and an optional secret token.\n\nTelegram provides two ways of getting updates: long polling and webhook. When you use webhook you just register\nendpoint address and telegram sends JSON to this address. If the bad guy finds out the address of your webhook, then\nhe can send fake "telegram updates" to your bot.\n\nTelegram doesn\'t provide any security features like signing or authentication mechanisms, so securing webhook is a task\nfor a bot developer.\n\nThence, for securing your webhook you have only two option:\n - Allow requests only from Telegram subnets. \n [Telegram assures](https://core.telegram.org/bots/webhooks#the-short-version) that they won\'t change.\n - Use secret value in endpoint address, e.g. `/telegram-webhook/468e95826f224a60a4e9355ab76e0875`. It will\n  complicate the brute force attack and you can easily change it if the value was compromised.\n\nThis little plugin allows you to use both ways to secure.\n\n## How to use\n\nUse pip or another package management util:\n```bash\npip install fastapi-security-telegram-webhook\n```\n\nor\n\n```bash\npoetry add fastapi-security-telegram-webhook\n```\n\nor\n\n```bash\npipenv install fastapi-security-telegram-webhook\n```\n\nPackage contains two Security objects: \n - `OnlyTelegramNetwork` allows request only from telegram subnets\n - `OnlyTelegramNetworkWithSecret` additionally checks secret in path\n \nExample with `OnlyTelegramNetworkWithSecret`. Pay attention to `{secret}` in path operation, it\'s required\n\n```python\nfrom fastapi import FastAPI, Body, Depends\nfrom fastapi_security_telegram_webhook import OnlyTelegramNetworkWithSecret\n\napp = FastAPI()\nwebhook_security = OnlyTelegramNetworkWithSecret(real_secret="your-secret-from-config-or-env")\n\n# {secret} in path and OnlyTelegramNetworkWithSecret as dependency:\n@app.post(\'/webhook/{secret}\', dependencies=[Depends(webhook_security)])\ndef process_telegram_update(update_raw = Body(...)):\n   ...\n\n```\n\n## Use behind proxy\n\nThe plugin uses `starlette.Request.client.host` for extracting IP address of the request, so if your web-app is\nbehind proxy you should pass the real IP to the app.\n\nFor `uvicorn` you can use `--proxy-headers` as it describes in \n[documentation](https://www.uvicorn.org/deployment/#running-behind-nginx).  ',
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
