from ..service.service import Service

class Factory(object):
    
    @staticmethod
    def create(service_enum):
        instance = Service(service_enum.value)
        return instance