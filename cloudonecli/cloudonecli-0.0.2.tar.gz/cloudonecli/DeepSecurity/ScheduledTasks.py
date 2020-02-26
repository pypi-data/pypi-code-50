#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.

#import connect
#import config

class ScheduledTasks:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection
    ##ScheduledTasks
    def listScheduledTasks(self):
        return self._connection.get(url='/scheduledtasks')
    def createScheduledTasks(self, payload):
        return self._connection.send(url='/scheduledtasks', data=payload)
    def searchScheduledTasks(self, payload):
        return self._connection.send(url='/scheduledtasks/search', data=payload)
    def describeScheduledTasks(self, scheduledtaskID):
        return self._connection.get(url='/scheduledtasks/' + str(scheduledtaskID))
    def modifyScheduledTasks(self, scheduledtaskID, payload):
        return self._connection.send(url='/scheduledtasks/' + str(scheduledtaskID), data=payload)
    def deleteScheduledTasks(self, scheduledtaskID):
        return self._connection.delete(url='/scheduledtasks/' + str(scheduledtaskID))
