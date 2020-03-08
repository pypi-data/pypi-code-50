from .scrum_project import ScrumProject
from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories
import logging
logging.basicConfig(level=logging.INFO)

class ScrumComplexProject(ScrumProject):

    def create(self, element, organization_id):
        try:
            logging.info("Scrum Atomic Project: Start")
            self.element = element
            self.organization = organization_id
            self.scrum_development_task = model_factories.ScrumComplexProjectFactory
            self.scrum_development_application = application_factories.ScrumComplexProjectFactory()
            
            super().create()
            logging.info("Scrum Atomic Project: End")
            return self.scrum_project
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)