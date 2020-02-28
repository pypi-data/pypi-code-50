from flask import jsonify
from flask.views import MethodView

from werkzeug import exceptions as exc

from ifile.manage import client as client_api


class Client(MethodView):
    def get(self, id):
        clients = client_api.Clients()
        client = clients.get_client_by_id(id)

        if client is None:
            raise exc.NotFound(f"the client {id} not found")

        return jsonify(client.to_json())


class Clients(MethodView):
    def get(self):
        clients = client_api.Clients()

        return jsonify(clients.to_json())
