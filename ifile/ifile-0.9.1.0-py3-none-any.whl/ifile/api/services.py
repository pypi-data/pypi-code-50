import logging

from flask import request, jsonify
from flask.views import MethodView

from ifile import services

logger = logging.getLogger(__name__)


class Services(MethodView):
    def post(self):
        payload = request.json

        # rpc\ftp\beats
        services_name = payload["services"]

        for service_name in services_name:
            services.register(service_name)

        services.start_all()

        return jsonify({
            "services": services_name
        })

    def get(self):
        pass

    def delete(self):
        pass
