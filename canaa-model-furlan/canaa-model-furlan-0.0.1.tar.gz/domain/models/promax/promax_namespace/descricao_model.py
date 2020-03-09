# CREATED BY CANAA-BASE-MODEL-CREATOR IN 2020-03-08 23:11:48.599312 : guionardo
from canaa_base import BaseModel


class DescricaoModel(BaseModel):

	def __init__(self, arg: dict):
		super().__init__(arg)


		# key
		self.chave: int = \
			self.get_value('chave',field_type=int)

		# value
		self.valor: str = \
			self.get_value('valor',field_type=str)