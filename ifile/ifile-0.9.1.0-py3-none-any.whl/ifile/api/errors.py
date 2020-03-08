import logging

from flask import jsonify
from werkzeug import exceptions as exc

from ifile.api import blueprint as bp

logger = logging.getLogger(__name__)


@bp.errorhandler(Exception)
def internal_server(e):
    logger.exception(str(e))
    return jsonify({
        "message": str(e)
    })


@bp.errorhandler(exc.NotFound)
def notfound(e):
    logger.exception(str(e))
    return jsonify({
        "message": str(e)
    })
