#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.

#import connect
#import config

class gcpconnector:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection

    def createGCPConnectorAction(self, id, payload):
        return self._connection.send(url='/gcpconnectors/' + str(id) + '/actions', data=payload)
    def describeGCPConnectorAction(self, id, actionID):
        return self._connection.get(url='/gcpconnectors/' + str(id) + '/actions/' + str(actionID))
    def listCPConnector(self):
        return self._connection.get(url='/gcpconnectors')
    def createGCPConnector(self, payload):
        return self._connection.send(url='/gcpconnectors', data=payload)
    def searchGCPConnector(self, payload):
        return self._connection.send(url='/gcpconnectors/search', data=payload)
    def describeGCPConnector(self, id):
        return self._connection.get(url='/gcpconnectors/' + str(id))
    def modifyGCPConnector(self, id, payload):
        return self._connection.send(url='/gcpconnectors/' + str(id), data=payload)
    def deleteGCPConnector(self, id):
        return self._connection.delete(url='/gcpconnectors/' + str(id))





