from abc import ABC, abstractmethod
from requests import Session


class ResourceInterface(ABC):

	@abstractmethod
	def execute(self, session: Session):
		pass


class MailinatorClient(object):

	@staticmethod
	def _assert_status_hook(response, *args, **kwargs):
		response.raise_for_status()

	def __init__(self, api_token: str):
		s = Session()
		s.headers.update({
			'Authorization': api_token,
			'Content-Type': 'application/json',
		})
		s.hooks['response'] = [MailinatorClient._assert_status_hook]
		self.session = s

	def request(self, resource: ResourceInterface):
		return resource.execute(self.session)
