from .abstract_service import AbstractService
from fuzzywuzzy import process, fuzz

import logging
from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories
logging.basicConfig(level=logging.INFO)


class TaskService(AbstractService):

    def __config(self):
        
        self.application_project =  application_factories.ScrumAtomicProjectFactory()
        self.application_sprint = application_factories.SprintFactory()
        self.application_sprint_backlog = application_factories.SprintBacklogFactory()
        self.application_team_member = application_factories.TeamMemberFactory()
            
        self.application_scrum_intented_development_task = application_factories.ScrumIntentedDevelopmentTaskFactory()
        self.application_scrum_performed_development_task = application_factories.ScrumPerformedDevelopmentTaskFactory()            
            
    
    def synchronized(self, data):
        try:
                
            self.configuration(data)
            self.__config()
            
            scrum_projects = self.application_project.get_all(self.organization_id)

            workspaces = self.clockify.get_all_workspaces()
            
            clockify_projects_name = []
            clockify_projects_dict = {}
            
            logging.info("Synchronized Task: workspaces")
            for workspace in workspaces:
                projects_clockify = self.clockify.get_all_projects(workspace['id'])
                
                for project in projects_clockify:
                
                    clockify_projects_name.append (project['name'])
                    data = {"project": project, "workspace": workspace['id']}
                    clockify_projects_dict[project['name']] = data 
            
            logging.info("Synchronized Task: Project")
            for scrum_project in scrum_projects:
                logging.info("Synchronized Task: Project is Root: "+str(scrum_project.root))
                if scrum_project.root == False:
                    project = process.extractOne(scrum_project.name,
                                                clockify_projects_name, 
                                                scorer=fuzz.partial_ratio, 
                                                score_cutoff=80)
                    
                    if project is not None:
                        
                        name = project[0]
                        project = clockify_projects_dict[name]
                        logging.info("Synchronized Task: Project: "+str(name))
                        project_id = project["project"]['id']
                        workspace_id = project["workspace"]
                        
                        sprint = self.application_sprint.retrive_limbo(scrum_project.uuid)
                        logging.info("Synchronized Task: Project: "+str(name)+" sprint : "+sprint.name)
                        sprint_backlog = self.application_sprint_backlog.retrive_by_name_and_project_name(sprint.name,scrum_project.name)
                        
                        tasks = self.clockify.get_task_active(workspace_id, project_id)
                        
                        for task in tasks:
                            if task is not None:
                                self.__create_task_seon(task, scrum_project, sprint_backlog, sprint)

            logging.info("Synchronized Task: End")
        except Exception as erro:
            logging.error (erro)
            logging.error (erro.__dict__)

    def __create_task_seon(self, task, scrum_project, sprint_backlog, sprint):
        try:
            
            logging.info("Synchronized Task: Project: " + scrum_project.name+ " : "+task['name'])
            scrum_intented_development_task = model_factories.ScrumIntentedDevelopmentTaskFactory(
                                name = task['name'],
                                description = '',
                                sprint_backlogs = [sprint_backlog],
                                sprints = [sprint]
            )
                            
            team_member = None

            if task['assigneeId'] is not None:
                logging.info("Synchronized Task: Searching Team Member: " + scrum_project.name+ " : "+task['name'])
                team_member = self.application_team_member.retrive_by_external_id_and_project_name(task['assigneeId'],scrum_project.name)
                            
                if team_member is not None:
                    
                    logging.info("Synchronized Task: Searching Team Member: " + scrum_project.name+ " : "+task['name']+" : "+team_member.name)
                    scrum_intented_development_task.assigned_by = [team_member]
                    
                    logging.info("Synchronized Task: Create Scrum Intented Development Task")        
                    self.application_scrum_intented_development_task.create(scrum_intented_development_task)
                            
                    scrum_performed_development_task = model_factories.ScrumPerformedDevelopmentTaskFactory(
                                name = task['name'],
                                description = '',
                                sprint_backlogs = [sprint_backlog],
                                sprints = [sprint],
                                caused_by = scrum_intented_development_task.id
                            )
                    
                    logging.info("Synchronized Task: Create Scrum Performed Development Task")
                    self.application_scrum_performed_development_task.create(scrum_performed_development_task)
                    
                    if scrum_intented_development_task is not None:
                        logging.info("Synchronized Task: Create Application Reference of Scrum Itented ")
                        self.create_application_reference(scrum_intented_development_task.name,
                                                                scrum_intented_development_task.description,
                                                                task['id'],
                                                                "task",
                                                                scrum_intented_development_task.uuid,
                                                                scrum_intented_development_task.type)
                    if scrum_performed_development_task is not None:
                        logging.info("Synchronized Task: Create Application Reference of Scrum Performed: "+scrum_performed_development_task.name)
                        self.create_application_reference(scrum_performed_development_task.name,
                                                                scrum_performed_development_task.description,
                                                                task['id'],
                                                                "task",
                                                                scrum_performed_development_task.uuid,
                                                                scrum_performed_development_task.type)
        except Exception as erro:
            logging.error (erro)
            logging.error (erro.__dict__)
            