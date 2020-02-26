#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.

#import connect
#import config

class Certificates:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection
    ##Certificates
    def describeCertificate(self, certID):
        return self._connection.get(url='/certificates/' + str(certID))
    def deleteCertificate(self, certID):
        return self._connection.delete(url='/certificates/' + str(certID))
    def getCertificateByURL(self, url):
        return self._connection.get(url='/certificates/target?' + str(url))
    def listCertificate(self, certID):
        return self._connection.get(url='/certificates')
    def addCertificate(self, payload):
        return self._connection.send(url='/certificates', data=payload)

