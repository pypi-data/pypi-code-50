from directory_api_client.base import AbstractAPIClient

url_corruption_perceptions_index = 'dataservices/corruption-perceptions-index/{country_code}/'
url_easeofdoingbusiness = 'dataservices/easeofdoingbusiness/{country_code}/'


class DataServicesAPIClient(AbstractAPIClient):

    def get_corruption_perceptions_index(self, country_code):
        return self.get(
            url=url_corruption_perceptions_index.format(country_code=country_code),
            use_fallback_cache=True
        )

    def get_easeofdoingbusiness(self, country_code):
        return self.get(
            url=url_easeofdoingbusiness.format(country_code=country_code),
            use_fallback_cache=True,
        )
