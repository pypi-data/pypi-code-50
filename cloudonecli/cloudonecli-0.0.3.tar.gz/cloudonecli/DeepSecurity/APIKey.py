#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.

#import connect
#import config

class APIKeys:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection
    ##APIKeys
    def describeCurrentAPIKey(self):
        return self._connection.get(url='/apikeys/current')
    def modifyCurrentAPIKey(self, payload):
        return self._connection.get(url='/apikeys/current', data=payload)
    def currentAPIKeySecretKey(self, payload):
        return self._connection.get(url='/apikeys/current/secretkey', data=payload)
    def describeAPIKey(self, apikeyID):
        return self._connection.get(url='/apikeys/' + str(apikeyID))
    def modifyAPIKey(self, apikeyID, payload):
        return self._connection.get(url='/apikeys/' + str(apikeyID), data=payload)
    def deleteAPIKey(self, apikeyID):
        return self._connection.delete(url='/apikeys/' + str(apikeyID))
    def generateSecretAPIKey(self, apikeyID, payload):
        return self._connection.send(url='/apikeys/' + str(apikeyID) +'/secretkey', data=payload)
    def listAPIKeys(self):
        return self._connection.get(url='/apikeys')
    def createAPIKey(self, payload):
        return self._connection.get(url='/apikeys', data=payload)
    def searchPIKeys(self, payload):
        return self._connection.get(url='/apikeys/search', data=payload)


