"""A wrapper for the Stater-API"""

import requests
import json

version = "0.0.0"

server_name: str = None
server_password: str = None

_url = "http://helix2.ddns.net/stater/"


def check_config():
    if server_name != None:
        if type(server_name) != str:
            raise TypeError("stater.server_name not of type str.")
    else:
        raise ValueError("server_name not specified.")
    if server_password != None:
        if type(server_password) != str:
            raise TypeError("stater.server_password not of type str.")
    else:
        raise ValueError("stater.server_password not specified.")


def get_server(name: str = None, id: int = None):
    if name != None:
        data = {"name": name}
    elif id != None:
        data = {"id": id}
    else:
        raise TypeError(
            "No arguments provided. Unsure which server to get.")
    r = requests.post(_url + "api/getserver",
                      json.dumps(data))
    try:
        server = json.loads(r.text)
    except json.JSONDecodeError:
        server = r.text
    return server


def register_server(name: str, password: str, description: str = None, repo_url: str = None, main_status: int = None, components: dict = None):
    """register a new server.

    This will automatically update the package config so you are up and running with the newest credentials."""
    data = {"name": name, "password": password}
    if description != None and type(description) == str:
        data["description"] = description
    if repo_url != None and type(repo_url) == str:
        data["repoURL"] = repo_url
    if main_status != None and type(main_status) == int:
        data["mainStatus"] = main_status
    if components != None and type(components) == dict:
        data["components"] = json.dumps(components)

    r = requests.post(_url + "api/registerserver", json.dumps(data))
    if r.status_code == 200:
        global server_name
        global server_password
        server_name = name
        server_password = password
        return True
    else:
        return (False, r.status_code, r.text)


def delete_server(name_or_id=None, password: str = None):
    """Delete server specified by `name_or_id` with `password`. Alternatively, the configuration of the package will be used."""
    if name_or_id == None and password == None:
        check_config()
        payload = {"name": server_name, "password": server_password}

    elif (name_or_id != None) != (password != None):
        raise TypeError(
            "name_or_id xor password specified. Expected both or neither.")
    else:
        payload = {"password": password}
        if type(name_or_id) == str:
            payload["name"] = name_or_id
        elif type(name_or_id) == int:
            payload["id"] = name_or_id
        else:
            raise TypeError("name_or_id of wrong type (expected str or int)")
    r = requests.post(_url + "api/deleteserver", json.dumps(payload))
    if r.status_code == 200:
        return True
    else:
        return (False, r.status_code, r.text)


def change_server(name: str = None, description: str = None, repo_url: str = None, main_status: int = None, components: dict = None, password: str = None):
    """Change server according to arguments (using package config).

    This will automatically change the config so it has the right credentials."""
    check_config()
    global server_name
    global server_password
    payload = {"name": server_name, "password": server_password}
    if name != None:
        if type(name) != str:
            raise TypeError("name expected to be of type str.")
        payload["newName"] = name
    if description != None:
        if type(description) != str:
            raise TypeError("description expected to be of type str.")
        payload["description"] = description
    if repo_url != None:
        if type(repo_url) != str:
            raise TypeError("repo_url expected to be of type str.")
        payload["repoURL"] = repo_url
    if main_status != None:
        if type(main_status) != int:
            raise TypeError("main_status expected to be of type int.")
        payload["mainStatus"] = main_status
    if components != None:
        if type(components) != dict:
            raise TypeError("components expected to be of type dict.")
        payload["components"] = json.dumps(components)
    if password != None:
        if type(password) != str:
            raise TypeError("password expected to be of type str.")
        payload["newPassword"] = password
    r = requests.post(_url + "api/changeserver", json.dumps(payload))
    if r.status_code == 200:
        if name != None:
            server_name = name
        if password != None:
            server_password = password
        return True
    else:
        return (False, r.status_code, r.text)


def update_component(component: str, status: int):
    check_config()
    if type(component) != str:
        raise TypeError(
            "component needs to be of type str (hint: it's the name!)")
    if type(status) != int:
        raise TypeError(
            "status need to be of type int. See docs for possible values.")
    payload = {"name": server_name, "password": server_password,
               "component": component, "status": status}
    r = requests.post(_url + "api/updatecomponent", json.dumps(payload))
    if r.status_code == 200:
        return True
    else:
        return (False, r.status_code, r.text)
