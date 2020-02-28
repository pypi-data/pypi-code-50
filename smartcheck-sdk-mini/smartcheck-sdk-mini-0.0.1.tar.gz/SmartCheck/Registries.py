#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.
#import connect
#import config

class Registries:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection
    def listRegistries(self, limit=25, expand="all", query=None):
        url = "/registries"
        params={'limit': limit, 'expand':expand}
        if query:
            params['query'] = query
        rtv = self._connection.get(url=url, params=params)
        items = rtv['registries']
        while "next" in rtv:
            params['cursor'] = rtv['next']
            rtv = self._connection.get(url=url, params=params)
            items.extend(rtv['registries'])
        return items
    def createRegistrie(self, payload):
        return self._connection.post(url='/registries', data=payload)
    def describeRegistrie(self, id):
        return self._connection.get(url='/registries/' + str(id))
    def modifyRegistrie(self, id, data):
        return self._connection.post(url='/registries/' + str(id), payload=data)
    def deleteRegistrie(self, id):
        return self._connection.delete(url='/registries/' + str(id))
    def listRegistrieImages(self, id):
        return self._connection.get(url='/registries/' + str(id) + "/images")
    def describeRegistrieImage(self, id, imageID):
        return self._connection.get(url='/registries/' + str(id) + "/images/" + str(imageID))
    def describeRegistriesDashboard(self):
        return self._connection.get(url='/registries/dashboard')
