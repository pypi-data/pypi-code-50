from .error import NotEnoughParamsError, TrellogyError, ReadOnlyError
import requests


class Component:
    def __init__(self, **kwargs):
        self._attr = kwargs['_attributes']
        self.bool_to_str = {True: 'true', False: 'false'}

        # Verify key, token, id and set these attributes:
        if 'key' not in kwargs.keys():
            raise NotEnoughParamsError('key')
        if 'token' not in kwargs.keys():
            raise NotEnoughParamsError('token')
        if 'id' not in kwargs.keys():
            raise NotEnoughParamsError('id')
        self._key = kwargs['key']
        self._token = kwargs['token']
        self._id = kwargs['id']

        # Add empty attributes starting with '-':
        for attribute in kwargs['_attributes']:
            setattr(self, '_' + attribute, None)

        # Set attributes that are given:
        for key in kwargs:
            setattr(self, '_' + key, kwargs[key])

    def req(self, method, path, **kwargs):
        base = 'https://api.trello.com/1'

        methods = {'POST': requests.post, 'GET': requests.get,
                   'PUT': requests.put, 'DELETE': requests.delete}
        if method.upper() not in methods.keys():
            raise TrellogyError('Invalid method `{}`.'.format(method))

        # Create query string:
        query = ['key={}'.format(self._key), 'token={}'.format(self._token)]
        for key in kwargs:
            query.append('{}={}'.format(key, kwargs[key]))
        query = "?"+"&".join(query)

        # Send request and validate it, and return JSON:
        response = methods[method](base+path+query)
        if response.status_code != 200:
            raise TrellogyError(response.text)
        return response.json()

    def __getattr__(self, name):
        # Redirect underscored attributes to non-underscored attributes:

        if name in self._attr:
            return getattr(self, '_'+name)
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        # Bypass self._attr
        if name == '_attr':
            return super().__setattr__(name, value)

        # Raise error when attributes are overrided by user explictly:
        if name in self._attr:
            raise ReadOnlyError(name)

        # Otherwise, set attribute to the class:
        super().__setattr__(name, value)
