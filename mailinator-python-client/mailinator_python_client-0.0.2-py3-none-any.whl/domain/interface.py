from typing import List

from mailinator.client import ResourceInterface
from mailinator.constants import DOMAINS_URL, DOMAIN_URL

from .domain import Domain


class DomainInterface(ResourceInterface):

	def __init__(self, domain_id: str):
		self.base_url = DOMAIN_URL.format(domain_id=domain_id)

	def execute(self, session) -> Domain:
		result = session.get(self.base_url)
		return Domain.from_json(result.text)


class DomainsInterface(ResourceInterface):

	def __init__(self):
		self.base_url = DOMAINS_URL

	def execute(self, session) -> List[Domain]:
		result = session.get(self.base_url)
		domains_dict = result.json()['domains']
		return Domain.schema().load(domains_dict, many=True)
