from .base_entity import BaseEntity
import logging
logging.basicConfig(level=logging.INFO)

class ScrumProject(BaseEntity):

    def __init__(self):
        super().__init__()
        self.scrum_project = None
        self.scrum_project_application = None
        self.element = None
        
    def create(self):
        try:
            
            self.scrum_project.name = self.element.name
            self.scrum_project.description = self.element.description
            self.scrum_project.organization = self.organization
                
            self.scrum_project_application.create(self.scrum_project)
                
            self.create_application_reference(
                    self.element.id, 
                    self.element.url,
                    self.PROJECT_TFS, 
                    self.scrum_project.uuid, 
                    self.scrum_project.type)
            
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__) 

