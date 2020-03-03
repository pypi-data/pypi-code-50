import requests


class TorpedoClient:
    def __init__(self, torpedo_url=None, client_id=None, client_name=None):
        self.torpedo_url = torpedo_url
        self.cliend_id = client_id
        self.client_name = client_name

    def send_email(self, email, subject=None, template_name=None, data=None):
        response = requests.post(
                f'{self.torpedo_url}/send-email',
                json={
                    'to_email': email,
                    'subject': subject,
                    'template_name': template_name,
                    'data': data,
                    'client': self.client_name,
                }
            )
        response.raise_for_status()
        return response
