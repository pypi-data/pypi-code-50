from datetime import datetime

from ifile.db.sqlalchemy import api as db_api


class Client(object):
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip
        self.role = "client"

        host = self._add()
        self.id = host.id
        self.is_register = host.is_register
        self.last_alive_time = host.last_alive_time

    def _add(self):
        params = {
            "name": self.hostname,
            "ip": self.ip,
            "role": self.role
        }

        host = db_api.get_host(**params)
        if host is None:
            host = db_api.add_host(**params)
        return host

    def register(self):
        host = db_api.update_host(self.id, is_register=True)
        self.is_register = host.is_register

    def unregister(self):
        host = db_api.update_host(self.id, is_register=False)
        self.is_register = host.is_register

    def activate(self):
        host = db_api.update_host(
            self.id,
            is_register=True,
            last_alive_time=datetime.now()
        )
        self.is_register = host.is_register

    def to_json(self):
        return {
            "id": self.id,
            "name": self.hostname,
            "ip": self.ip,
            "is_register": self.is_register,
            "last_alive_time": self.last_alive_time
        }


class Clients(object):
    def __init__(self):
        self.clients = {}
        self.register
        self._refresh()

    def _refresh(self):
        clients = db_api.get_hosts(role="client")
        for c in clients:
            client = Client(c.name, c.ip)
            self.clients[(client.hostname, client.ip)] = client

    def activate_client(self, hostname, ip):
        client = self.clients.get((hostname, ip), None)
        if client is None:
            client = self.add_client(hostname, ip)

        client.activate()

    def add_client(self, hostname, ip):
        client = Client(hostname, ip)
        self.clients[(hostname, ip)] = client

        if not client.is_register:
            self.register(hostname, ip)

        return client

    def get_client(self, hostname, ip):
        client = self.clients.get((hostname, ip), None)
        return client

    def get_client_by_id(self, id):
        for (_, _), client in self.clients.items():
            if client.id == id:
                return client
        return None

    def register(self, hostname, ip):
        client = self.get_client(hostname, ip)
        client.register()

    def unregister(self, hostname, ip):
        client = self.get_client(hostname, ip)
        client.unregister()

    def to_json(self):
        clients = []
        for (_, _), client in self.clients.items():
            clients.append(client.to_json())

        return clients
