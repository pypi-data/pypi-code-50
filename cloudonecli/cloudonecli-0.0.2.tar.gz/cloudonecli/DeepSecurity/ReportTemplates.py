#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.

#import connect
#import config

class ReportTemplates:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection
    ##EventBasedTasks
    def listReportTemplates(self):
        return self._connection.get(url='/reporttemplates')
    def searchReportTemplates(self, payload):
        return self._connection.send(url='/reporttemplates/search', data=payload)
    def describeReportTemplates(self, reportID):
        return self._connection.get(url='/reporttemplates/' + str(reportID))

