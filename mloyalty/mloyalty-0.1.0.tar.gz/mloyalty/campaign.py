from mloyalty.base import Mloyalty


class Campaign(Mloyalty):
    def __init__(self, username=None, password=None, base_url=None):
        super().__init__(username, password, base_url)

    def get_campaigns(self):
        """
        Получение информации об акциях Оператора ПЛ.
        :return: словарь данных
        """
        method_url = 'api/site/GetCampaigns'
        params = self.get_request_params()
        payload = {
            'Operator': params['operator_id'],
        }

        return self._make_request(params['token'], method_url, method='post', params=payload)

    def get_campaign(self, campaign_id):
        """
        Получение информации о акции по её идентификатору.
        :param campaign_id: идентификатор акции
        :return: словарь данных
        """
        method_url = 'api/site/GetCampaign'
        params = self.get_request_params()
        payload = {
            'CampaignID': campaign_id,
        }

        return self._make_request(params['token'], method_url, method='post', params=payload)
