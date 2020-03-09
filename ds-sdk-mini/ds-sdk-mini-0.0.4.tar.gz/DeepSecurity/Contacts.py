#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.

#import connect
#import config

class Contacts:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection
    ##Contacts
    def listContacts(self):
        return self._connection.get(url='/contacts')
    def createContacts(self, payload):
        return self._connection.post(url='/contacts', data=payload)
    def describeContact(self, contactID):
        return self._connection.get(url='/contacts/' + str(contactID))
    def modifyContact(self, contactID, payload):
        return self._connection.post(url='/contacts/' + str(contactID), data=payload)
    def deleteContacts(self, contactID):
        return self._connection.delete(url='/contacts/' + str(contactID))
    def dsearchContacts(self, contactID):
        return self._connection.get(url='/contacts/search' + str(contactID))


