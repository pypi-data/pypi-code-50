from flask import Blueprint, jsonify

from ifile.version import __version__

blueprint = Blueprint('api', __name__)
get_version = lambda: (jsonify({"version": __version__}), 200) # noqa


@blueprint.after_app_request
def after_request_func(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = \
        'OPTIONS, GET, POST, PUT, DELETE, PATCH'
    response.headers['Access-Control-Allow-Headers'] = \
        'Origin, X-Requested-With, Content-Type, Accept'
    return response


from ifile.api import routes
