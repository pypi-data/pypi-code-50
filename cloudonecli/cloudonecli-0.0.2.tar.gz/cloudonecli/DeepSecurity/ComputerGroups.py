#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.

#import connect
#import config

class ComputerGroups:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection
    ##ComputerGroups
    def listComputerGroups(self):
        return self._connection.get(url='/computergroups')
    def createComputerGroup(self, payload):
        return self._connection.send(url='/computergroups', data=payload)
    def searchComputerGroup(self, payload):
        return self._connection.send(url='/computergroups/search', data=payload)
    def describeComputerGroups(self, groupID):
        return self._connection.get(url='/computergroups/' + str(groupID))
    def modifyComputerGroup(self, id, payload):
        return self._connection.send(url='/computergroups/' + str(id), data=payload)
    def deleteComputerGroup(self, id):
        return self._connection.delete(url='/computergroups/' + str(id))



