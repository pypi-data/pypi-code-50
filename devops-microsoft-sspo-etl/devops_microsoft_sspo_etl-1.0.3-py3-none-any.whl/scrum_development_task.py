from .base_entity import BaseEntity
from devops_microsoft_mapping_sspo import factories as mapping_factories 
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

class ScrumDevelopmentTask(BaseEntity):

    def do(self,data):
        try:
            logging.info("Task")
            self.config(data)
            
            # Buscando os projetos do TFS
            work_itens = self.tfs.get_work_item_query_by_wiql_task()

            logging.info("Buscando Task")
            for work_item in work_itens:
                element = self.tfs.get_work_item(work_item.id, None,None, "All")
                
                if element.fields['System.WorkItemType'] == "Task":   
                    state = str(self.check_value(element,'System.State'))
                    
                    if state == "New" or state =="To Do":
                        self.__create_intended_task(element)
                    else:
                        self.__create_performed_task(element)
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)    

    def __create_intended_task(self, element):
        try:
            scrum_intented_development_task = mapping_factories.ScrumIntentedDevelopmentTaskFactory()
            instance_scrum_intented_development_task = scrum_intented_development_task.create(element)
        
            self.create_application_reference(
                    element.id, 
                    element.url,
                    self.WORK_ITEM, 
                    instance_scrum_intented_development_task.uuid, 
                    instance_scrum_intented_development_task.type)

        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)  
    
    def __create_performed_task(self,element):
        try:
            
            scrum_intented_development_task = mapping_factories.ScrumIntentedDevelopmentTaskFactory()
            instance_scrum_intented_development_task = scrum_intented_development_task.create(element)

            scrum_intented_development_task = mapping_factories.ScrumPerformedDevelopmentTaskFactory()
            instance_scrum_performed_development_task = scrum_intented_development_task.create(element,instance_scrum_intented_development_task)

            self.create_application_reference(
                    element.id, 
                    element.url,
                    self.WORK_ITEM, 
                    instance_scrum_intented_development_task.uuid, 
                    instance_scrum_intented_development_task.type)
            
            self.create_application_reference(
                    element.id, 
                    element.url,
                    self.WORK_ITEM, 
                    instance_scrum_performed_development_task.uuid, 
                    instance_scrum_performed_development_task.type)

        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)  
    
