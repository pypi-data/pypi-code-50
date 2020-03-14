# -*- coding: utf-8 -*-
import sys

from flask import Flask
from aishow_model_app.apis import init_api
from aishow_model_app.ext import init_ext
from config import configs


sys.path.append(sys.modules['__main__'])

def create_app(env):
    app = Flask(__name__)
    app.config.from_object(configs[env])
    configs[env].init_app(app)
    init_ext(app)
    init_api(app)

    # app.wsgi_app = UserMiddleware(app.wsgi_app)

    return app


