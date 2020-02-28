#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.

#import connect
#import config

class EventBasedTasks:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection
    ##EventBasedTasks
    def listEventBasedTasks(self):
        return self._connection.get(url='/eventbasedtasks')
    def createEventBasedTasks(self, payload):
        return self._connection.send(url='/eventbasedtasks', data=payload)
    def searchEventBasedTasks(self, payload):
        return self._connection.send(url='/eventbasedtasks/search', data=payload)
    def describeEventBasedTasks(self, eventbasedtaskID):
        return self._connection.get(url='/eventbasedtasks/' + str(eventbasedtaskID))
    def modifyEventBasedTasks(self, eventbasedtaskID, payload):
        return self._connection.send(url='/eventbasedtasks/' + str(eventbasedtaskID), data=payload)
    def deleteEventBasedTasks(self, eventbasedtaskID):
        return self._connection.delete(url='/eventbasedtasks/' + str(eventbasedtaskID))
