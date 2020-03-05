from ada.base import BaseADA


class TestCase(BaseADA):
    url = "test-case/"

    def create(self, name, status, duration, execution_id, **kwargs):
        data = {
            'name': name,
            'status': status,
            'duration': duration,
            'execution': execution_id,
        }
        data.update(kwargs)
        return super(TestCase, self).create(data)
