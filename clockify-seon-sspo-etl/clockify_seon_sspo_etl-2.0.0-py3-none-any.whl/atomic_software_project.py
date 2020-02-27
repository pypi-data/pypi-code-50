from .services import factories as factory_service

import logging
logging.basicConfig(level=logging.INFO)

class AtomicSoftwareProject():

    def do(self, data):
        try:
            logging.info("Atomic Software Project: Integration") 
            logging.info("Atomic Software Project: Syncronizing") 

            workspace_service = factory_service.WorkspaceServiceFactory()
            workspace_service.synchronized(data, "scrum_atomic_project")

            logging.info("Atomic Software Project: creating workspace") 
            #to do
            #verificar quais projetos são root = True e não foram criados ainda

            project_service = factory_service.ProjectServiceFactory()
            logging.info("Atomic Software Project: Syncronizing") 
            project_service.synchronized(data)

            logging.info("Atomic Software Project: creating project") 
            #verificar quais projetos são root = False e não foram criados no clockify 
            #to do

        except Exception as erro:
            logging.error(erro)
            logging.error(erro.__dict__) 