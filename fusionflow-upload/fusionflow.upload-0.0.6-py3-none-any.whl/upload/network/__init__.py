"""table template for api table
"""

from ..table import Table
import requests
from functools import partial
from typing import Callable, Text, Any, TypeVar, Mapping

ValueType = TypeVar("ValueType", Callable, Text)

HEADERS = {
    "user_agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
}

class ApiTable(Table):
    """connect to a remote api server
    and fetch data from there
    
    :param params: parameters appended to uri's , 
    :type Table: Mapping[ValueType, ValueType] if value
    is str, use directly otherwise if values is 
    callback, return value will use, if value is object, object.__str__() will use
    :param parser: parser function used with init, if use subclass format, implement parse_data method
    """

    def __init__(self, uri, *, headers: Mapping[ValueType, ValueType]=None, params:Mapping[ValueType, ValueType]=None, 
                cookies:Mapping[ValueType, ValueType]=None, **kwargs):
        super().__init__(**kwargs)

        self.uri = uri
        self.headers = headers
        self.params = params
        self.cookies = cookies

        
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

        self.auth = None
        if "username" in kwargs and "password" in kwargs:
            self.auth = kwargs["username"], kwargs["password"]

        self.method = kwargs.get("method", "GET").upper()

        self.parser = kwargs.get("parser", None)


    def _format_values(self, value):
        if callable(value):
            return str(value())
        return str(value)

    
    def extract(self, **kwargs):
        if self.headers is not None:
            headers = {self._format_values(k): self._format_values(v) for k, v in self.headers.items()}
            self.session.headers.update(headers)
        
        if self.cookies is not None:
            cookies = {self._format_values(k): self._format_values(v) for k, v in self.cookies.items()}
            self.session.cookies.update(cookies)
        
        params = {}
        if self.params is not None:
            params = {self._format_values(k) : self._format_values(v) for k, v in self.params.items()}
    
        if self.auth:
            self.session.auth = self.auth
        print(self.method, self.uri, self.auth, self.params)
        data = self.session.request(self.method, self.uri, auth=self.auth, params=params)

        # use callback function or 
        if self.parser:
            return self.parser(data.json())
        return self.parse_data(data.json())

    
    def parse_data(self, data):
        """parse return data from api
        
        :param data: raw data
        :type data: json
        """
        raise NotImplementedError
        
        

        