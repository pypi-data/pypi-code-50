#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.
#import connect
#import config

class Administrators:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection
    ##Administrators
    def listAdministrators(self):
        return self._connection.get(url='/administrators')
    def createAdministrator(self, payload):
        return self._connection.send(url='/administrators', data=payload)
    def administrator(self, adminID):
        return self._connection.get(url='/administrators/' + str(adminID))
    def modifyAdministrator(self, adminID, payload):
        return self._connection.get(url='/administrators/' + str(adminID), data=payload)
    def deleteAdministrator(self, adminID):
        return self._connection.delete(url='/administrators/' + str(adminID))
    def searchAdministrators(self, payload):
        return self._connection.send(url='/administrators/search', data=payload)
    #Roles
    def listAdministratorRoles(self):
        return self._connection.get(url='/roles')
    def createAdministratorRole(self, payload):
        return self._connection.send(url='/roles', data=payload)
    def searchAdministratorRole(self, payload):
        return self._connection.send(url='/roles/search', data=payload)
    def administratorRole(self, roleID):
        return self._connection.get(url='/roles/' + str(roleID))
    def modifyadministratorRole(self, roleID, payload):
        return self._connection.send(url='/roles/' + str(roleID), data=payload)
    def deleteAdministratorRole(self, roleID):
        return self._connection.delete(url='/roles/' + str(roleID))

