from .abstract_service import AbstractService
from fuzzywuzzy import process, fuzz
from sspo_db.application import factories as application_factories

import logging
logging.basicConfig(level=logging.INFO)

class TeamMemberService(AbstractService):

    def synchronized(self, data):

        try:
            logging.info("Synchronized Team Member") 
            
            self.configuration(data)
            workspaces = self.clockify.get_all_workspaces()
            
            clockify_users = []
            clockify_users_dict = {}

            for workspace in workspaces:
                users = self.clockify.get_all_workspace_users(workspace['id'])
                
                for user in users:
                    clockify_users.append (user['email'])
                    clockify_users_dict[user['email']] = user
            
            person_application = application_factories.PersonFactory()
            people = person_application.get_all(self.organization_id)
            
            for person in people:
                if person.email is not None:
                    user = process.extractOne(person.email,clockify_users, scorer=fuzz.partial_ratio,score_cutoff=80)
                    if user is not None:
                    
                        email = user[0]
                        clockify_team_member = clockify_users_dict[email]
                        id_clockify = clockify_team_member['id']
                        logging.info("Synchronizing Project: "+person.name)

                        self.create_application_reference(person.name, 
                                                            person.description,
                                                            id_clockify,
                                                            "member",
                                                            person.uuid,
                                                            person.__tablename__)
            
        except Exception as erro:
            logging.error (erro)
            logging.error (erro.__dict__)
    