from clockify.clockify import Clockify
import logging
logging.basicConfig(level=logging.INFO)

from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories

class AbstractService():

    def __init__(self):

        self.application = None
        self.secret = None
        self.element_id = None
        self.clockify = None
        
        self.application_application_reference = application_factories.ApplicationReferenceFactory()
        self.application_service = application_factories.ApplicationFactory()
        self.application_organization = application_factories.OrganizationFactory()

    def __create_clockify(self, secret):
        self.clockify =  Clockify(secret)  
    
    def configuration(self, data):
        self.organization_id = data["organization_id"]
        self.secret = data["key"]
        self.application_id = data["application"]

        self.organization = self.application_organization.get_by_uuid(self.organization_id)
        self.application = self.application_service.get_by_uuid(self.application_id)
        
        self.__create_clockify(self.secret)

    def create_application_reference(self,name,description,external_id,external_type_entity, internal_uuid, entity_name ):
        try:
            application_reference = model_factories.ApplicationReferenceFactory(
                                                        name = name,
                                                        description = description,
                                                        application = self.application.id,
                                                        external_id = external_id,
                                                        external_type_entity = external_type_entity,
                                                        internal_uuid = internal_uuid,
                                                        entity_name = entity_name
                                                    )
            logging.info("Create Application Reference")
            self.application_application_reference.create(application_reference)
        except Exception as erro:
            logging.error (erro)
            logging.error (erro.__dict__)
