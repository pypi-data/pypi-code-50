import pika
import uuid
import os
import json
from rabbitmqX.patterns.client.rpc_client import RPC_Client
from rabbitmqX.journal.journal import Journal

class ClockifyService(RPC_Client):
    
    def __init__(self, type):

        RPC_Client.__init__(self,'integration.sspo.clockify')
        self.type = type

    def integrate(self, organization_id = None, key= None, application= None):
        
        data = {'organization_id': organization_id, 
                "key": key, 
                "application": application}  
        
        journal = Journal(organization_id,self.type,data,"integration")
        return json.loads(self.do(journal))