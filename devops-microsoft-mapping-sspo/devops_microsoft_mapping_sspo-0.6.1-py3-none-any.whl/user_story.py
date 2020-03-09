from .base_entity import BaseEntity
from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories
import logging
logging.basicConfig(level=logging.INFO)
import re  
class UserStory(BaseEntity):

    def __init__(self):
        super().__init__()
        self.user_story = None
        self.user_story_application = None
        self.element = None
        self.application_application_reference = application_factories.ApplicationReferenceFactory()
        
    def set_name_description(self):
        self.user_story.name = self.element.fields['System.Title']
        self.user_story.description = str(self.check_value(self.element,'System.Description'))
    
    def retrive_dates(self):

        created_data = self.check_value(self.element,'System.CreatedDate')
        activated_date = self.check_value(self.element,'Microsoft.VSTS.Common.ActivatedDate')
        resolved_date = self.check_value(self.element,'Microsoft.VSTS.Common.ResolvedDate')
        closed_date = self.check_value(self.element,'Microsoft.VSTS.Common.ClosedDate')

        if created_data is not None and created_data is not 'None':
            self.user_story.created_date = self.validate_date_format(str(created_data)) 
                            
        if activated_date is not None and activated_date is not 'None':
            self.user_story.activated_date = self.validate_date_format(str(activated_date))
                    
        if resolved_date is not None and resolved_date is not 'None':
            self.user_story.resolved_date = self.validate_date_format(str(resolved_date)) 
                    
        if closed_date is not None and closed_date is not 'None':
            self.user_story.closed_date = self.validate_date_format(str(closed_date))

    def retrive_project_name(self):
        
        project_name = self.check_value(self.element,"System.AreaLevel2") 
        if project_name is None:
            project_name = self.check_value(self.element,"System.AreaLevel1") 
        return project_name
    
    def retrive_product_backlog(self, project_name):
        product_backlog = self.application_product_backlog.retrive_by_project_name(project_name)
        return product_backlog    
    
    def create(self):
        try:
            logging.info("User Story")

            logging.info("User Story: add name and description")
            self.set_name_description()
            
            logging.info("User Story: add dates")
            #recuperando as datas    
            self.retrive_dates()

            story_points = self.check_value(self.element,'Microsoft.VSTS.Scheduling.StoryPoints')
            logging.info('User Story: Story Point: '+str(story_points))

            if story_points is not None: 
                self.user_story.story_points  = story_points

            logging.info("User Story: project name")
            #Adicionando o EPIC o backlog
            project_name = self.retrive_project_name()
            
            logging.info("User Story: retrive Product Backlog: "+project_name)
            product_backlog = self.retrive_product_backlog(project_name)

            # Product Backlog 
            logging.info("User Story: add Product Backlog :"+str(product_backlog.id))
            
            self.user_story.product_backlog = product_backlog.id

            logging.info("User Story: Retrive Team Members")
            self.retrive_team_members()

            logging.info("User Story: create Seon Element")
            self.user_story_application.create(self.user_story)
            
            logging.info("User Story: Create reference")
            
            #application reference
            application_reference = model_factories.ApplicationReferenceFactory(
                                                    name = self.user_story.name,
                                                    description = self.user_story.description,
                                                    application = self.application.id,
                                                    external_id = self.element.id,
                                                    external_url = self.element.url,
                                                    external_type_entity = self.WORK_ITEM,
                                                    internal_uuid = self.user_story.uuid,
                                                    entity_name = self.user_story.__tablename__
                                                )

            self.application_application_reference.create(application_reference)
                                        
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)