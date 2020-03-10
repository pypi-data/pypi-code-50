from ..service.tfs_service import TFSService

class Factory(object):
    
    @staticmethod
    def create(service_enum):
        instance = TFSService(service_enum.value)
        return instance