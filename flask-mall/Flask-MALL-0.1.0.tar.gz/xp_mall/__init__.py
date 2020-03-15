# -*- coding: utf-8 -*-

import logging
import os
import re
from logging.handlers import  RotatingFileHandler

import click
from flask import Flask, render_template, request, send_from_directory
from flask_login import current_user, login_manager
from flask_sqlalchemy import get_debug_queries
from flask_wtf.csrf import CSRFError


from xp_mall.admin import admin_module
from xp_mall.member import member_module
from xp_mall.mall import mall_module
from xp_mall.extensions import bootstrap, db, login_manager, csrf, ckeditor, moment, toolbar, migrate
from xp_mall.extensions import cache, whooshee, dropzone
from xp_mall.settings import config
from xp_mall.customization_filter import *
from xp_mall.models.category import GoodsCategory

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('xp_mall')
    app.config['secret_key'] = os.getenv("SECRET_KEY")
    app.config.from_object(config[config_name])
    @app.route('/uploads/<path:filename>')
    def get_image(filename):
        return send_from_directory(app.config['XPMALL_UPLOAD_PATH'], filename)

    register_logging(app)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_shell_context(app)
    register_template_context(app)
    register_request_handlers(app)
    # login_manager.anonymous_user = Guest
    return app


def register_logging(app):
    class RequestFormatter(logging.Formatter):

        def format(self, record):
            record.url = request.url
            record.remote_addr = request.remote_addr
            return super(RequestFormatter, self).format(record)

    request_formatter = RequestFormatter(
        '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
        '%(levelname)s in %(module)s: %(message)s'
    )
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = RotatingFileHandler(os.path.join(basedir, 'logs/python-xp.log'),
                                       maxBytes=10 * 1024 * 1024, backupCount=10)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    app.logger.addHandler(file_handler)
    if not app.debug:
        app.logger.addHandler(file_handler)


def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    ckeditor.init_app(app)
    moment.init_app(app)
    toolbar.init_app(app)
    migrate.init_app(app, db)
    # print(cache.init_app)
    cache.init_app(app)
    whooshee.init_app(app)
    dropzone.init_app(app)


def register_blueprints(app):
    # app.register_blueprint(article_bp)
    app.register_blueprint(admin_module, url_prefix='/admin')
    app.register_blueprint(member_module, url_prefix='/member')
    app.register_blueprint(mall_module, url_prefix='/')



def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)


def register_template_context(app):
    @app.context_processor
    def make_template_context():
        pass
        # admin = Admin.query.first()
        # # categories = Category.query.order_by(Category.name).all()
        # # links = Link.query.order_by(Link.name).all()
        # if current_user.is_authenticated:
        #     unread_comments = GoodsComment.query.filter_by(reviewed=False).count()
        # else:
        #     unread_comments = None
        # return {}
        # return dict(
        #     admin=admin, #categories=categories,
        #     links=links, unread_comments=unread_comments)


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    @click.option('--username', prompt=True, help='The username used to login.')
    @click.option('--password', prompt=True, hide_input=True,
                  confirmation_prompt=True, help='The password used to login.')
    def init(username, password):
        admin = Admin.query.first()
        if admin is not None:
            click.echo('The administrator already exists, updating...')
            admin.username = username
            admin.set_password(password)
        else:
            click.echo('Creating the temporary administrator account...')
            admin = Admin(
                username=username,
                blog_title='Bluelog',
                blog_sub_title="No, I'm the real thing.",
                name='Admin',
                about='Anything about you.'
            )
            admin.set_password(password)
            db.session.add(admin)

        category = GoodsCategory.query.first()
        if category is None:
            click.echo('Creating the default category...')
            category = GoodsCategory(name='Python简明手册', parent_id=0, order_id=0)
            db.session.add(category)

        db.session.commit()
        click.echo('Done.')



    @app.cli.command()
    def initrole():
        click.echo("Initializing the roles and permissions")
        Role.init_role()
        click.echo("Done.")


def register_request_handlers(app):
    @app.after_request
    def query_profiler(response):
        for q in get_debug_queries():
            if q.duration >= app.config['XPCMS_SLOW_QUERY_THRESHOLD']:
                app.logger.warning(
                    'Slow query: Duration: %fs\n Context: %s\nQuery: %s\n '
                    % (q.duration, q.context, q.statement)
                )
        return response



if __name__=="__main__":
    create_app("development")