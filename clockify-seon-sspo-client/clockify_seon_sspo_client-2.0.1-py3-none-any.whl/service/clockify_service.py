import pika
import uuid
import os
import json
from pprint import pprint
from rabbitmqX.patterns.client.work_queue_task_client import Work_Queue_Task_Client
from rabbitmqX.journal.journal import Journal

class ClockifyService(Work_Queue_Task_Client):
    
    def __init__(self, type):

        Work_Queue_Task_Client.__init__(self,'integration.sspo.clockify')
        
        self.type = type

    def integrate(self, organization_id = None, key= None, application= None):
        
        data = {'organization_id': organization_id, 
                "key": key, 
                "application": application}         
        journal = Journal(organization_id,self.type,data,"integration_with")

        self.send(journal)