from .base_entity import BaseEntity
from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories
from datetime import datetime

import logging
logging.basicConfig(level=logging.INFO)
import re  
class UserStory(BaseEntity):

    def __init__(self):
        super().__init__()
        self.user_story = None
        self.user_story_application = None
        self.element = None
        self.application_product_backlog = application_factories.ProductBacklogFactory()
        self.application_person = application_factories.PersonFactory()

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
    
    def validate_date_format(self, date):

        try:
            return datetime.strptime(str(date), '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError:
            return datetime.strptime(str(date), '%Y-%m-%dT%H:%M:%SZ')

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
                                        
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)

    def retrive_team_members(self):
        try:
            created_by = self.check_value(self.element,'System.CreatedBy')
            activated_by = self.check_value(self.element,'Microsoft.VSTS.Common.ActivatedBy') 
            closed_by = self.check_value(self.element,'Microsoft.VSTS.Common.ClosedBy') 
            assigned_by = self.check_value(self.element,'System.AssignedTo')

            project_name = self.retrive_project_name()

            if created_by is not None and created_by is not 'None':
                team_member = self.retrive_team_member_seon(created_by,project_name)
                self.user_story.created_by = team_member.id
                            
            if activated_by is not None and activated_by is not 'None':
                team_member = self.retrive_team_member_seon(activated_by,project_name)
                self.user_story.activated_by = team_member.id
            
            if closed_by is not None and closed_by is not 'None':
                team_member = self.retrive_team_member_seon(closed_by,project_name)
                self.user_story.closed_by = team_member.id
            
            if assigned_by is not None and assigned_by is not 'None':
                logging.info("Assigned: "+assigned_by['id'])
                team_member = self.retrive_team_member_seon(assigned_by,project_name)
                if team_member is not None:
                    self.user_story.assigned_by = [team_member]
        
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)              
