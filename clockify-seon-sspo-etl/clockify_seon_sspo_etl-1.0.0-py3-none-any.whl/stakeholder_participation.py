from .services.time_entry_service import TimeEntryService
import logging
logging.basicConfig(level=logging.INFO)

class StakeholderParticipation():

    def do(self, data):
        try:
            
            time_entry_service = TimeEntryService()
            time_entry_service.synchronized(data)

        except Exception as erro:
            logging.error(erro)
            logging.error(erro.__dict__) 
    