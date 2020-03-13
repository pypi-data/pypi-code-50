from mloyalty.base import Mloyalty


class Operator(Mloyalty):
    def __init__(self, username=None, password=None, base_url=None, db_backend=None):
        super().__init__(username, password, base_url, db_backend)

    def get_user_info(self):
        """
        Информация об Операторе, Партнере, Точке пользователя.
        :return: словарь данных
        """
        method_url = 'api/values/UserInfo'
        params = self.get_request_params()
        payload = {
            'Operator': params['operator_id'],
            'Partner': params['partner_id'],
            'Pos': params['pos_id'],
        }

        return self._make_request(params['token'], method_url, method='post', params=payload)

    def get_gain_operator_period(self, date_from, date_to):
        """
        Получение среднего чека и выручки Оператора по месяцам.
        :return: словарь данных
        """
        method_url = 'api/values/GainOperatorPeriod'
        params = self.get_request_params()
        payload = {
            'Operator': params['operator_id'],
            'From': date_from,
            'To': date_to,
        }

        return self._make_request(params['token'], method_url, method='post', params=payload)
