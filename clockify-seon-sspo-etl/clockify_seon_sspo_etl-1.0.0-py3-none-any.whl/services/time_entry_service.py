from .abstract_service import AbstractService
from datetime import datetime
import logging
from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories
logging.basicConfig(level=logging.INFO)


class TimeEntryService(AbstractService):

    def __config (self):
        self.application_project =  application_factories.ScrumAtomicProjectFactory()
        self.application_project =  application_factories.ScrumAtomicProjectFactory()
        self.application_sprint = application_factories.SprintFactory()
        self.application_sprint_backlog = application_factories.SprintBacklogFactory()
        self.application_team_member = application_factories.TeamMemberFactory()
                
        self.application_scrum_intented_development_task = application_factories.ScrumIntentedDevelopmentTaskFactory()
        self.application_scrum_performed_development_task = application_factories.ScrumPerformedDevelopmentTaskFactory()            
        
        self.application_intented_stakeholder_participation = application_factories.IntentedStakeholderParticipationFactory()
        self.application_performed_stakeholder_participation = application_factories.PerformedStakeholderParticipationFactory()
        self.application_performed_fragment_participation = application_factories.PerformedFragmentParticipationFactory()
    
    def synchronized(self, data):
        try:
            logging.info("Synchronized Time Entry: Start")
            self.__config()
            self.configuration(data)
            workspaces = self.clockify.get_all_workspaces()
            scrum_projects = self.application_project.get_all(self.organization_id)

            for workspace in workspaces:
                users = self.clockify.get_all_workspace_users(workspace['id'])
                logging.info("Synchronized Time Entry: Retriving users")
            
                for user in users:

                    logging.info("Synchronized Time Entry: Retriving time entry from: "+user['name'])
                    logging.info("Synchronized Time Entry: Retriving time entry from Workspace: "+workspace['id']+ " : "+user['id'])
                    time_entries = self.clockify.get_all_time_entry_user(workspace['id'], user['id'])
                    logging.info("Synchronized Time Entry: Time Entry Recovered")
                    for time_entry in time_entries:
                        scrum_project = self.application_project.retrive_by_external_uuid(time_entry['projectId'])
                        if scrum_project is not None and scrum_project in scrum_projects:
                            if time_entry['taskId'] is not None:
                                self.__update_task(scrum_project, time_entry)
                            else:
                                self.__create_task(scrum_project, time_entry)


            logging.info("Synchronized Time Entry: End")
        except Exception as erro:
            logging.error (erro)
            logging.error (erro.__dict__)

    def __update_task (self, scrum_project, time_entry):
        try:
            logging.info("Synchronized Task: Project:" + scrum_project.name+ " : "+time_entry['description'])
        
            task_id = time_entry["taskId"]
            
            scrum_intented_development_task = self.application_scrum_intented_development_task.retrive_by_external_uuid(task_id)
            scrum_performed_development_task= self.application_scrum_performed_development_task.retrive_by_external_uuid(task_id)

            self.__create_stakeholder_participation(scrum_project,scrum_intented_development_task,scrum_performed_development_task,time_entry)
            
            
        except Exception as erro:
            logging.error (erro)
            logging.error (erro.__dict__)
        
        
    def __create_task(self, scrum_project, time_entry):
        try:
            
            logging.info("Synchronized Create Task: Project:" + scrum_project.name+ " : "+time_entry['description'])
            
            sprint = self.application_sprint.retrive_limbo(scrum_project.uuid)
            sprint_backlog = self.application_sprint_backlog.retrive_by_name_and_project_name(sprint.name,scrum_project.name)
            
            scrum_intented_development_task = model_factories.ScrumIntentedDevelopmentTaskFactory(
                name = time_entry['description'],
                description = time_entry['description'],
                sprint_backlogs = [sprint_backlog],
                sprints = [sprint]
            )
            team_member = None
            
            if time_entry['userId'] is not None:
                team_member = self.application_team_member.retrive_by_external_id_and_project_name(time_entry['userId'],scrum_project.name)
                            
            if team_member is not None:
                scrum_intented_development_task.assigned_by = [team_member]
            else: 
                logging.error("Synchronized Create Task: Project: Team Member is None")
            
            logging.info("Synchronized Create Task: Create Task in Project:" + scrum_project.name+ " : "+time_entry['description'])                
            self.application_scrum_intented_development_task.create(scrum_intented_development_task)
            
            # Criando o performed development task
            scrum_performed_development_task = model_factories.ScrumPerformedDevelopmentTaskFactory(
                                caused_by = scrum_intented_development_task.id
            )
            self.application_scrum_performed_development_task.create(scrum_performed_development_task)          
             
            self.__create_stakeholder_participation(scrum_project, scrum_intented_development_task,scrum_performed_development_task,time_entry)
            
        except Exception as erro:
            logging.error (erro)
            logging.error (erro.__dict__)

    
    def __create_stakeholder_participation(self, scrum_project, scrum_intented_development_task, scrum_performed_development_task, time_entry):
        try:
            
            team_member = None
            
            if time_entry['userId'] is not None:
                team_member = self.application_team_member.retrive_by_external_id_and_project_name(time_entry['userId'],scrum_project.name)
            
            intented_stakeholder_participation = model_factories.IntentedStakeholderParticipationFactory(
                team_member = team_member.id ,
                intented_activity = scrum_intented_development_task.id
            )
            
            
            logging.info("Synchronized Create Task: Intented Stakeholder Participation")                
            self.application_intented_stakeholder_participation.create(intented_stakeholder_participation)
            
            logging.info("Synchronized Create Task: Performed Stakeholder Participation")                
            performed_stakeholder_participation = model_factories.PerformedStakeholderParticipationFactory(
                performed_activity = scrum_performed_development_task.id,
                caused_by = intented_stakeholder_participation.id
            )
            
            self.application_performed_stakeholder_participation.create(performed_stakeholder_participation)
            
            date_format = "%Y-%m-%dT%H:%M:%fZ" 

            start_date = str(time_entry['timeInterval']['start'])
            start_date = datetime.strptime(start_date, date_format)

            end_date = str(time_entry['timeInterval']['end'])
            end_date = datetime.strptime(end_date, date_format)
            
            logging.info("Synchronized Create Task: Performed Fragment Participation - StartDate: "+str(start_date)+" EndDate: "+str(end_date))
            performed_fragment_participation = model_factories.PerformedFragmentParticipationFactory(
                performedStakeholderParticipation = performed_stakeholder_participation.id,
                description = time_entry['description'],
                startDate = start_date,
                endDate = end_date

            )
            logging.info("Synchronized Create Task: Performed Fragment Participation")  
            self.application_performed_fragment_participation.create(performed_fragment_participation)

            self.create_application_reference(None, None, time_entry['id'],"time_entry",performed_fragment_participation.uuid, performed_fragment_participation.__tablename__)

        except Exception as erro:
            logging.error (erro)
            logging.error (erro.__dict__)
    
    
