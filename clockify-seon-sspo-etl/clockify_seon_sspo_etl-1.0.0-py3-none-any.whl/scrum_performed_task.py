from .services import factories
import logging
logging.basicConfig(level=logging.INFO)
class ScrumPerformedTask():

    is_instance_of = "spo.intended.activity.x"
    
    def do(self, data):
        try:
            logging.info("Performed Task")
            task_service = factories.TaskServiceFactory()
            task_service.synchronized(data)

        except Exception as erro:
            logging.error(erro)
            logging.error(erro.__dict__) 