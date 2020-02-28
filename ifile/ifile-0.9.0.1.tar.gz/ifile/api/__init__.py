from flask import Blueprint, jsonify

from ifile.version import __version__

blueprint = Blueprint('api', __name__)
get_version = lambda: (jsonify({"version": __version__}), 200) # noqa

from ifile.api import routes
