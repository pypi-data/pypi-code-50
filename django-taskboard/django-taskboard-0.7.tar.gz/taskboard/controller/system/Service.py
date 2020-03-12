import psutil


class Service:
    @staticmethod
    def all():
        return [{'name': service.name()} for service in psutil.win_service_iter()]
