from .services import factories
import logging
logging.basicConfig(level=logging.INFO)

class ComplexSoftwareProject():
    is_instance_of = "spo.software_project.complex"
    
    def do(self, data):
        try:
            logging.info("Complex Software Project: Syncronizing") 

            workspace_service = factories.WorkspaceServiceFactory()
            workspace_service.synchronized(data, "scrum_complex_project")
            
            logging.info("Complex Software Project: creating") 
            #criando o workspace

        except Exception as erro:
            logging.error(erro)
            logging.error(erro.__dict__) 