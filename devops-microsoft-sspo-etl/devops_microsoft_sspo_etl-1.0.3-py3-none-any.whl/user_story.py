from .base_entity import BaseEntity
import logging
from devops_microsoft_mapping_sspo import factories 
from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories
logging.basicConfig(level=logging.INFO)
import re  

class UserStory(BaseEntity):

    def do(self,data):
        try:
            self.mapping_atomic_user = factories.AtomicUserStoryFactory()
            self.mapping_epic = factories.EpicFactory()
            self.config(data)

            self.application_application_reference = application_factories.ApplicationReferenceFactory()

            logging.info("User Story")
            logging.info("User Story: Retrive information from TFS")
            work_itens = self.tfs.get_work_item_query_by_wiql_epic_user_story_product_backlog_item()

            for work_item in work_itens:

                element = self.tfs.get_work_item(work_item.id, None,None, "All")

                if element.fields['System.WorkItemType'] == "User Story" or element.fields['System.WorkItemType'] =="Product Backlog Item":
                    logging.info("User Story: Create User Story")
                    atomic_user_story = self.mapping_atomic_user.create(element)   
                    logging.info("User Story: User Story: Reference")
                    application_reference = model_factories.ApplicationReferenceFactory(
                                                                name = atomic_user_story.name,
                                                                description = atomic_user_story.description,
                                                                application = self.application.id,
                                                                external_id = element.id,
                                                                external_url = element.url,
                                                                external_type_entity = self.WORK_ITEM,
                                                                internal_uuid = atomic_user_story.uuid,
                                                                entity_name = atomic_user_story.__tablename__
                                                            )

                    self.application_application_reference.create(application_reference)
               
                elif element.fields['System.WorkItemType'] == "Epic":
                    logging.info("User Story: Epic")
                    epic = self.mapping_epic.create(element)
                    logging.info("User Story: EPIC: Reference")
                    application_reference = model_factories.ApplicationReferenceFactory(
                                                                name = epic.name,
                                                                description = epic.description,
                                                                application = self.application.id,
                                                                external_id = element.id,
                                                                external_url =element.url,
                                                                external_type_entity = self.WORK_ITEM,
                                                                internal_uuid = epic.uuid,
                                                                entity_name = epic.__tablename__
                                                            )

                    self.application_application_reference.create(application_reference)
                    
                    
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)              
    
    