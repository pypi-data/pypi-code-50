from .abstract_service import AbstractService
from fuzzywuzzy import process, fuzz
from sspo_db.application import factories as application_factories
import logging
from pprint import pprint 
logging.basicConfig(level=logging.INFO)

class WorkspaceService(AbstractService):

    def __create(self, scrum_projects):
        try:
            for scrum_project in scrum_projects:
                if scrum_project.root == True:
                    project = self.clockify.create_new_workspace(scrum_project.name)
                    self.create_application_reference(None, None,project['id'],"workspace", scrum_project.uuid, scrum_project.type)
        
        except Exception as erro:
            logging.error(erro)
            logging.error(erro.__dict__) 

    def create (self, data, type):
        try:
            logging.info("Create Workspace") 
            self.configuration(data)
            
            logging.info("Create Workspace: organization ID: "+self.organization_id) 
            #criando workspace com projetos que não foram sincronizados
            #buscar complex project root == TRue
            #buscar atomic project root = true
            application_scrum_complex_project = application_factories.ScrumComplexProjectFactory()
            application_scrum_atomic_project = application_factories.ScrumAtomicProjectFactory()

            scrum_complex_projects = application_scrum_complex_project.x()
            scrum_atomic_projects = application_scrum_atomic_project.x()
            
            self.__create(scrum_complex_projects)
            self.__create(scrum_atomic_projects)

            
        except Exception as erro:
            logging.error(erro)
            logging.error(erro.__dict__) 

    def synchronized(self, data, type):
        try:
            logging.info("Synchronized Workspace") 
            self.configuration(data)
            
            logging.info("Synchronized Workspace: organization ID: "+self.organization_id) 
            logging.info("Synchronized Workspace: Recover Workspace:") 
            
            workspaces = self.clockify.get_all_workspaces()
            
            clockify_workspaces_name = []
            clockify_workspaces_dict = {}
                
            logging.info("Synchronized Workspace:: Analisando os Workspace:")
            for workspace in workspaces:
                clockify_workspaces_name.append (workspace['name'])
                clockify_workspaces_dict[workspace['name']] = workspace
            
            application_project = None
            logging.info("Synchronized Workspace:: Buscando os projetos no banco")
            if type == "scrum_complex_project":
                application_project = application_factories.ScrumComplexProjectFactory()
            else:
                application_project =  application_factories.ScrumAtomicProjectFactory()
            
            scrum_projects = application_project.get_all(self.organization_id)
            
            for scrum_project in scrum_projects:
                if scrum_project.root == True:
                    workspace = process.extractOne(scrum_project.name,
                                                clockify_workspaces_name, 
                                                scorer=fuzz.partial_ratio, 
                                                score_cutoff=98)
                    
                    if workspace is not None:
                        name = workspace[0]
                        id_clockify = clockify_workspaces_dict[name]['id']
                        self.create_application_reference(scrum_project.name, 
                                                            scrum_project.description,
                                                            id_clockify,
                                                            "workspace",
                                                            scrum_project.uuid,
                                                            scrum_project.type)
                        
            
        except Exception as erro:
            logging.error(erro)
            logging.error(erro.__dict__) 
