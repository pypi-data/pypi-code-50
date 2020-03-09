import logging
from .base_entity import BaseEntity
from devops_microsoft_mapping_sspo import factories 
logging.basicConfig(level=logging.INFO)
from datetime import datetime

class ScrumDevelopmentTask(BaseEntity):

    def do(self,data):

        try:
            logging.info("Scrum Development Task:Start")
            logging.info("Scrum Development Task:Retrive Information about Task")
            self.config(data)
            
            content = data["content"]
            id = content['id']
            event_type = content['eventType']
            
            work_item = self.tfs.get_work_item(str(id),None,None, "All")

            if event_type == "workitem.created":
                self.__create(work_item)
            elif event_type == "workitem.updated":
                self.__update(work_item)
            else: 
                self.__delete(work_item)

            logging.info("Scrum Development Task:End")
            
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)  

    def __create(self, work_item):
        logging.info("Scrum Development Task: Creating")

        scrum_intented_development_task = factories.ScrumIntentedDevelopmentTaskFactory()
        scrum_intented_development_task_instance = scrum_intented_development_task.create(work_item)
        
        self.create_application_reference(
            work_item.id, 
            work_item.url, 
            "WorkItem",
            scrum_intented_development_task_instance.uuid, 
            scrum_intented_development_task_instance.__tablename__)

        logging.info("Scrum Development Task: Created")
    
    def __update(self, work_item):
        logging.info("Scrum Development Task: Update")
    
    def __delete(self, work_item):
        logging.info("Scrum Development Task: Delete")

   