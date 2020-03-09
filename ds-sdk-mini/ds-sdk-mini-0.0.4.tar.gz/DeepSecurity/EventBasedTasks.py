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
    def createEventBasedTask(self, payload):
        return self._connection.post(url='/eventbasedtasks', data=payload)
    def searchEventBasedTasks(self, payload):
        return self._connection.post(url='/eventbasedtasks/search', data=payload)
    def describeEventBasedTask(self, eventbasedtaskID):
        return self._connection.get(url='/eventbasedtasks/' + str(eventbasedtaskID))
    def modifyEventBasedTask(self, eventbasedtaskID, payload):
        return self._connection.post(url='/eventbasedtasks/' + str(eventbasedtaskID), data=payload)
    def deleteEventBasedTask(self, eventbasedtaskID):
        return self._connection.delete(url='/eventbasedtasks/' + str(eventbasedtaskID))
