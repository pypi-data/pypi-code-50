from voximplant_client import exceptions, helpers
from voximplant_client.entities.base import BaseVoximplantEntity


class VoximplantUsers(BaseVoximplantEntity):
    def _get_application_id(self, app) -> int:
        application_id = self.client.applications.get_id(app)
        if application_id is None:
            raise exceptions.VoximplantBadApplicationNameException('Non-existant application name given: {}'.format(app))

        return application_id

    def list(self, app: str):
        application_id = self._get_application_id(app)
        url = helpers.append_to_querytring('GetUsers', application_id=application_id)
        return self.http.get_list(url)

    def add(self, app: str, user_name: str, user_display_name: str, user_password: str):
        return self.http.post('AddUser', payload=dict(
            application_id=self._get_application_id(app),
            user_name=user_name,
            user_display_name=user_display_name,
            user_password=user_password,
        ))

    def update(self, app: str, user_name: str, **new_params):
        return self.http.post('SetUserInfo', payload=dict(
            application_id=self._get_application_id(app),
            user_name=user_name,
            **new_params,
        ))
