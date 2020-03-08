import logging
from .scrum_development_task import ScrumDevelopmentTask
from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories
logging.basicConfig(level=logging.INFO)
from datetime import datetime

class ScrumPerformedDevelopmentTask(ScrumDevelopmentTask):

    def create (self, element, scrum_intented_development_task):
        try:
            self.element = element
            self.scrum_development_task = model_factories.ScrumPerformedDevelopmentTaskFactory()
            self.scrum_development_application = application_factories.ScrumPerformedDevelopmentTaskFactory()

            logging.info('Performed Task:Performed Task assigned with Intented')
            self.scrum_development_task.caused_by = scrum_intented_development_task.id
            
            logging.info('Performed Task: Calling scrum development task function')            
            super().create()
            
            logging.info('Performed Task:Persiting performed task')
            self.scrum_development_application.create(self.scrum_development_task)

            return self.scrum_development_task
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)   

