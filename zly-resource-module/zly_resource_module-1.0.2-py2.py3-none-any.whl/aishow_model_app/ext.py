# -*- coding: utf-8 -*-
from flask_caching import Cache
from flask_moment import Moment
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_pagedown import PageDown

db=SQLAlchemy()
migrate=Migrate()
moment = Moment()
session=Session()
# bootstarp = Bootstrap()
cache=Cache(config={'CACHE_TYPE':'simple'})
# pagedown = PageDown()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def init_ext(app):
    CORS(app, supports_credentials=True)
    db.init_app(app=app)
    session.init_app(app)
    moment.init_app(app)
    migrate.init_app(app, db)
    # bootstarp.init_app(app)
    cache.init_app(app)
    login_manager.init_app(app)
    # pagedown.init_app(app)
