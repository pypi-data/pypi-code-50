#!/usr/bin/env python3

import requests
import json

def make_payload(method, params):
    """
    Makes the JSON-RPC payload
    :param method: Name of the RPC method to invoke
    :param params: Parameters of the method
    :return: Full payload
    """
    payload = {"method": method}
    if len(params) > 0:
        payload["params"] = params
    return payload


class ConclaveClient():
    def __init__(self, host, port):
        self.ep = "http://{}:{}/".format(host, port)


    def node_info(self):
        """
        Gets some information on the remote node
        :return: Information on the node
        """
        return self._send("NodeInfo")


    def _send(self, method, params={}):
        """
        Sends a request to the Concalve RPC server
        :param method: Name of the RPC method to invoke
        :param params: Parameters of the method
        :return: JSONified response
        """
        post_data = json.dumps(make_payload(method, params))
        return requests.post(self.ep, data=post_data).json()
