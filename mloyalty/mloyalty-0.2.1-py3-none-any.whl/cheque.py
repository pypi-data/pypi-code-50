from mloyalty.base import Mloyalty


class Cheque(Mloyalty):
    def __init__(self, username=None, password=None, base_url=None, db_backend=None):
        super().__init__(username, password, base_url, db_backend)

    def get_cheques(self, loyalty_client_id, page, size):
        """
        Получение списка чеков с детализацией до позиций.
        :param loyalty_client_id: идентификатор участника
        :param page: страница
        :param size: размер страницы
        :return: словарь данных
        """
        method_url = 'api/client/GetCheques'
        params = self.get_request_params()
        payload = {
            'Operator': params['operator_id'],
            'Client': loyalty_client_id,
            'Page': page * size - size + 1,
            'PageSize': size,
        }

        return self._make_request(params['token'], method_url, method='post', params=payload)

    def get_cheque_detail(self, cheque_id):
        """
        Получение детелизации чека по заданному ID чека
        :param cheque_id: ID чека
        :return: словарь данных
        """
        method_url = 'api/client/GetChequeDetail'
        params = self.get_request_params()
        payload = {
            'ChequeID': cheque_id,
        }

        return self._make_request(params['token'], method_url, method='post', params=payload)
