#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.

#import connect
#import config

class APIUsageMetrics:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection
    ##APIUsageMetrics
    def listAPIUsageMetrics(self):
        return self._connection.get(url='/apiusagemetrics')
    def searchAPIUsageMetrics(self, payload):
        return self._connection.send(url='/apiusagemetrics', data=payload)

