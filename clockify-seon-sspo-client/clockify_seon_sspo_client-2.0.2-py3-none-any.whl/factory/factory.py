from ..service.clockify_service import ClockifyService
class Factory(object):
    
    @staticmethod
    def create(service_enum):
        instance = ClockifyService(service_enum.value)
        return instance