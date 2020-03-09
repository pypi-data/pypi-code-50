#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.
#import connect
#import config

class AwsConnectors:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection
    ##connectors
    def listConnectors(self):
        return self._connection.get(url='/awsconnectors')
    def createConnector(self, payload):
        return self._connection.post(url='/awsconnectors', data=payload)
    def describeConnector(self, connectorID):
        return self._connection.get(url='/awsconnectors/' + str(connectorID))
    def modifyConnector(self, connectorID, payload):
        return self._connection.post(url='/awsconnectors/' + str(connectorID), data=payload)
    def deleteConnector(self, connectorID):
        return self._connection.delete(url='/awsconnectors/' + str(connectorID))
    def searchConnector(self, payload):
        return self._connection.send(url='/awsconnectors/search', data=payload)
