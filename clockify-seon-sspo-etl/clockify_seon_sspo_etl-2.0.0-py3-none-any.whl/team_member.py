import logging
logging.basicConfig(level=logging.INFO)

from .services.team_member_service import TeamMemberService

class TeamMember():

    def do(self, data):
        try:
            
            logging.info("TeamMember: Syncronizing") 
            team_member_service = TeamMemberService()
            team_member_service.synchronized(data)
        
        except Exception as erro:
            logging.error(erro)
            logging.error(erro.__dict__) 
    