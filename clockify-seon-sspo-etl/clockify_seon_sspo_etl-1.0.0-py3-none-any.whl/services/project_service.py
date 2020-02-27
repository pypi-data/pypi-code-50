from .abstract_service import AbstractService
from fuzzywuzzy import process, fuzz

from pprint import pprint
from sspo_db.application import factories as application_factories
import logging
logging.basicConfig(level=logging.INFO)

class ProjectService(AbstractService):

    def synchronized(self,data):
        try:
            logging.info("Synchronized Project")
            
            self.configuration(data)
            workspaces = self.clockify.get_all_workspaces()
            
            clockify_projects_name = []
            clockify_projects_dict = {}
            
            logging.info("Synchronized Project: workspaces")
            for workspace in workspaces:
                projects_clockify = self.clockify.get_all_projects(workspace['id'])
                for project in projects_clockify:
                    
                    clockify_projects_name.append (project['name'])
                    data = {"project": project, "workspace": workspace['id']}
                    clockify_projects_dict[project['name']] = data 
            
            application_project =  application_factories.ScrumAtomicProjectFactory()
            
            scrum_projects = application_project.get_all(self.organization_id)
            
            for scrum_project in scrum_projects:

                if scrum_project.root == False:
                    project = process.extractOne(scrum_project.name,
                                                clockify_projects_name, 
                                                scorer=fuzz.partial_ratio, 
                                                score_cutoff=80)
                    
                    if project is not None:
                        
                        name = project[0]
                        project = clockify_projects_dict[name]
                        id_clockify = project["project"]['id']
                        logging.info("Synchronizing Project: "+scrum_project.name)
                        self.create_application_reference(scrum_project.name, 
                                                            scrum_project.description,
                                                            id_clockify,
                                                            "project",
                                                            scrum_project.uuid,
                                                            scrum_project.type)
                    
        except Exception as erro:
            logging.error (erro)
            logging.error (erro.__dict__)


    '''
    def __synchronized_project_with_workspace(self,data, type, workspace_id):
        try:
            logging.info("Synchronized Project with workspace:")
            
            organization_id = data["organization"]["id"]
            logging.info("Synchronized Project workspace: organization ID "+organization_id)
            
            self.configuration(data,organization_id)
            
            clockify_projects_name = []
            clockify_projects_dict = {}
            
            logging.info("Synchronized Project workspace: workspaces")
            projects_clockify = self.clockify.get_all_projects(workspace_id)
            
            for project in projects_clockify:
                clockify_projects_name.append (project['name'])
                clockify_projects_dict[project['name']] = project 
            
            name = data["name"]
            logging.info("Synchronized Project workspace get project name:  "+name)
            logging.info("Synchronized Project workspace get project size:" +str())
            
            if len(clockify_projects_name) == 0:
                logging.info("Synchronized Project workspace no projects")
                return None

            project = process.extractOne(name,clockify_projects_name,
                        scorer=fuzz.partial_ratio, score_cutoff=80)
            
            if project is not None:
                logging.info("FOUND"+name)
                logging.info("Synchronized Project workspace Found: name "+name)
                id_clockify = clockify_projects_dict[project[0]]['id']
                logging.info("Synchronized Project workspace: Enviando para SEON")
                url = "http://localhost:8060/api/process/"+type+"/synchronized/"
                self.send_to_seon(type,"project",id_clockify,url)
                logging.info("Synchronized Project workspace: Enviado para SEON")
                return id_clockify
            else:
                logging.info("Synchronized Project workspace Found: name "+name)
                logging.info("NOT FOUND"+name)
            
            return None
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  
            return None
        except Exception as erro:
            pprint (erro.__dict__)
    
    def create_project_with_workspace(self, data, type, workspace_id):    
        project_id = self.__synchronized_project_with_workspace(data,type, workspace_id)
        if project_id is None:
            self.__create_project_with_workspace(data,type,workspace_id)

    def __create_project_with_workspace(self, data, type, workspace_id):
        try:
            
            logging.info("Create Project with workspace") 
            organization_id = data["organization"]["id"]
            logging.info("Create Project with workspace: Organization ID: "+ organization_id)
            self.configuration(data,organization_id)
            
            name = data["name"]
            logging.info("Create Project with workspace: name: "+ name)
            logging.info("Create Project with workspace com ID: "+str(workspace_id))
            response = self.clockify.create_new_project(workspace_id,name)
            logging.info("Create Project with workspace:")
            
            if response.status_code == 201:
                logging.info("Create Project with workspace: 201")
                response = response.json()
                clockify_id = response["id"]
                url = "http://localhost:8060/api/process/"+type+"/synchronized/"
                self.send_to_seon(type,"project",clockify_id,url)
                
                logging.info("Create Project with workspace: enviado para o SEON")
                return clockify_id
            else:
                logging.info("Create Project with workspace: erro")  
                logging.info(response = response.json()) 
                return None
            
        except Exception as erro:
            logging.error (erro)
            logging.error (erro.__dict__)
    
    def __create_project(self, data, type):
        try:
            logging.info("Create Project") 
            organization_id = data["organization"]["id"]
            
            logging.info("Create Project: Organization ID: "+ organization_id)    
            self.configuration(data,organization_id)
            
            name = data["name"]
            application_references = data["complex_project"]["application_reference"]
            application_reference_selected = self.find_application_reference(application_references,"workspace")
            workspace_id = application_reference_selected["external_id"]
            logging.info("Create Project: Workspace ID: "+ workspace_id)    

            response = self.clockify.create_new_project(workspace_id,name)
            
            
        except Exception as erro:
            logging.error (erro)
            logging.error (erro.__dict__)
    '''
    
    