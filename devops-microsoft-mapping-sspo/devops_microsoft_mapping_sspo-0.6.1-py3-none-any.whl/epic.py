from .user_story import UserStory
from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories
import logging
logging.basicConfig(level=logging.INFO)
import re  

class Epic(UserStory):

    def create(self, element, organization):
        try:
            logging.info("User Story: Create Atomic User Story")
            self.element = element
            self.user_story = model_factories.EpicFactory()
            self.user_story_application = application_factories.EpicFactory()
            
            super().create()
            
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)