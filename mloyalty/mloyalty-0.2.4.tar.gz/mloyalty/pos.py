from mloyalty.base import Mloyalty


class POS(Mloyalty):
    def __init__(self, username=None, password=None, base_url=None, db_backend=None):
        super().__init__(username, password, base_url, db_backend)

    def get_poses(self):
        """
        Получение информации о точках Партнера.
        :return: словарь данных
        """
        method_url = 'api/site/GetPoses'
        params = self.get_request_params()
        payload = {
            'Operator': params['operator_id'],
            'PartnerID': params['partner_id'],
        }

        return self._make_request(params['token'], method_url, method='post', params=payload)
