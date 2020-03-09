"""
File contains main class for the PyAuthAdapter
"""
import os
import yaml
import json
import requests
import logging
from json.decoder import JSONDecodeError
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError, HTTPError


# Configure logger
logging.basicConfig(level=logging.DEBUG)


class Auth:
    """
    Contains methods to connect to YoungOnes Auth.
    """

    config: dict
    active_env: str
    credentials: dict
    adapter: HTTPAdapter

    def __init__(
        self,
        env: str,
        username: str,
        password: str,
        grant_override: str = "",
        auto_login: bool = True,
    ) -> None:
        # Loading config
        self.config = yaml.safe_load(open("config.yaml", "r"))
        self.config = self.config["settings"]

        # Loading credentials & env
        self.active_env = env
        self.credentials = self.config["credentials"]
        self.credentials["username"] = username
        self.credentials["password"] = password

        # Setting up requests adapter
        self.adapter = HTTPAdapter(
            max_retries=self.config["http"]["max_retries"]
        )

        # Override grant_type if enabled
        if grant_override != "":
            self.credentials['scopes']['grant_type'] = grant_override

        # Auto-login if enabled
        if auto_login is True:
            self.login()

    def register(self) -> dict:
        """
        Registers a new user with YoungOnes Auth
        """

        # Preparing request URL
        env: str = self.config["environs"][self.active_env]
        action: str = self.config["actions"]["register"]
        base: str = self.config["url"]
        url: str = f"{base}{env}{action}"

        headers: dict = {"X-Requested-With": "XMLHttpRequest"}
        data: dict = {
            "email": self.credentials["username"],
            "password": self.credentials["password"],
        }

        try:  # To register with youngones auth
            logging.info(
                "Attempting to register as %s" % self.credentials["username"]
            )
            with requests.session() as session:
                session.mount(url, self.adapter)
                response = session.post(url=url, headers=headers, data=data)

        except (HTTPError, ConnectionError):
            details: str = "Error: connection failed when registering"
            logging.exception(msg=details)
            return {
                "statusCode": 503,
                "body": {
                    "message": "Service Unavailable",
                    "details": f"{details}",
                },
            }
        else:
            logging.info("Register request completed...")

        try:  # To parse return data
            return_data = json.loads(response.text)
        except JSONDecodeError:
            details: str = "Error: could not parse json for login"
            logging.exception(msg=details)
            return {
                "statusCode": 500,
                "body": {"message": "Server Error", "details": f"{details}"},
            }
        else:
            logging.info("Register request successfully parsed...")
            logging.info("Register complete.")
            return return_data

    def login(self) -> dict:
        """
        Logs the user in on YoungOnes Auth
        """

        # Preparing request URL
        env: str = self.config["environs"][self.active_env]
        action: str = self.config["actions"]["login"]
        base: str = self.config["url"]
        url: str = f"{base}{env}{action}"

        headers: dict = {"X-Requested-With": "XMLHttpRequest"}
        data: dict = {
            "grant_type": self.config["scopes"]["grant_type"],
            "client_id": self.config["credentials"]["client_id"],
            "client_secret": self.config["credentials"]["client_secret"],
            "username": self.config["credentials"]["username"],
            "password": self.config["credentials"]["password"],
        }

        try:  # To login to youngones auth
            logging.info(
                "Attempting to login as %s" % self.credentials["username"]
            )
            with requests.session() as session:
                session.mount(url, self.adapter)
                response = session.post(url=url, headers=headers, data=data)
        except (HTTPError, ConnectionError):
            details: str = "Error: connection failed when logging in"
            logging.exception(msg=details)
            return {
                "statusCode": 503,
                "body": {
                    "message": "Service Unavailable",
                    "details": f"{details}",
                },
            }
        else:
            logging.info("Login request completed...")

        try:  # To parse return data
            return_data: dict = json.loads(response.text)
            os.environ["access_token"] = return_data["access_token"]
            os.environ["refresh_token"] = return_data["refresh_token"]
        except JSONDecodeError:
            details: str = "Error: could not parse json for login"
            logging.exception(msg=details)
            return {
                "statusCode": 500,
                "body": {"message": "Server Error", "details": f"{details}"},
            }
        except KeyError:
            details: str = "Error: no tokens in login return_data"
            logging.exception(msg=details)
            return {
                "statusCode": 500,
                "body": {"message": "Server Error", "details": f"{details}"},
            }
        else:
            logging.info("Login request successfully parsed...")
            logging.info("Login complete.")
            return return_data

    def who_am_i(self) -> dict:
        """
        Returns information about the currently logged in user
        """

        # Preparing request URL
        env: str = self.config["environs"][self.active_env]
        action: str = self.config["actions"]["who_am_i"]
        base: str = self.config["url"]
        url: str = f"{base}{env}{action}"

        access_token: str
        try:  # To retrieve access_token from env
            access_token = os.getenv("access_token")
        except KeyError:
            details: str = "Who-am-i could not retrieve access_token"
            logging.exception(msg=details)
            return {
                "statusCode": 400,
                "body": {"message": "Bad Request", "details": details},
            }

        headers: dict = {
            "X-Requested-With": "XMLHttpRequest",
            "Authorization": f"Bearer {access_token}",
        }

        try:  # To retrieve user session info
            logging.info("Attempting to get current user session")
            with requests.session() as session:
                session.mount(url, self.adapter)
                response = session.get(url=url, headers=headers)
        except (HTTPError, ConnectionError):
            details: str = "Error: connection failed when getting whoami"
            logging.exception(msg=details)
            return {
                "statusCode": 503,
                "body": {
                    "message": "Service Unavailable",
                    "details": f"{details}",
                },
            }
        else:
            logging.info("Who-am-i request completed...")

        try:  # To parse return data
            return_data = json.loads(response.text)
        except JSONDecodeError:
            details: str = "Error: could not parse json for login"
            logging.exception(msg=details)
            return {
                "statusCode": 500,
                "body": {"message": "Server Error", "details": f"{details}"},
            }
        else:
            logging.info("Who-am-i request successfully parsed...")
            logging.info("Who-am-i complete.")
            return return_data

    def logout(self) -> dict:
        # Preparing request URL
        env: str = self.config["environs"][self.active_env]
        action: str = self.config["actions"]["logout"]
        base: str = self.config["url"]
        url: str = f"{base}{env}{action}"

        access_token: str
        try:  # To retrieve access_token from env
            access_token = os.getenv("access_token")
        except KeyError:
            details: str = "Logout could not retrieve access_token"
            logging.exception(msg=details)
            return {
                "statusCode": 400,
                "body": {"message": "Bad Request", "details": details},
            }

        headers: dict = {
            "X-Requested-With": "XMLHttpRequest",
            "Authorization": f"Bearer {access_token}",
        }

        try:  # To register with youngones auth
            with requests.session() as session:
                session.mount(url, self.adapter)
                response = session.post(url=url, headers=headers)
        except (HTTPError, ConnectionError):
            details: str = "Error: connection failed when logging out"
            logging.exception(msg=details)
            return {
                "statusCode": 503,
                "body": {
                    "message": "Service Unavailable",
                    "details": f"{details}",
                },
            }
        else:
            logging.info("Logout request completed...")

        try:  # To parse return data
            return_data = json.loads(response.text)
        except JSONDecodeError:
            details: str = "Error: could not parse json for logout"
            logging.exception(msg=details)
            return {
                "statusCode": 500,
                "body": {"message": "Server Error", "details": f"{details}"},
            }
        else:
            logging.info("Logout request succesfully parsed.")
            logging.info("Logout complete.")
            return return_data
