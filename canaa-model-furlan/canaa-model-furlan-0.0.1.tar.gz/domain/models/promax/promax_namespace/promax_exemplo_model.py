# CREATED BY CANAA-BASE-MODEL-CREATOR IN 2020-03-08 23:11:48.597334 : guionardo
from canaa_base import BaseModel
from datetime import date, datetime
from domain.models.promax.promax_namespace.descricao_model import DescricaoModel


class PromaxExemploModel(BaseModel):

	def __init__(self, arg: dict):
		super().__init__(arg)


		# model_id
		self.codigo_modelo: int = \
			self.get_value('codigo_modelo',field_type=int)

		# person_name
		self.nome_pessoa: str = \
			self.get_value('nome_pessoa',field_type=str)

		# birth_date
		self.data_nascimento: date = \
			self.get_value('data_nascimento',field_type=date)

		# active
		self.ativo: bool = \
			self.get_value('ativo',field_type=bool)

		# register
		self.cadastro: datetime = \
			self.get_value('cadastro',field_type=datetime)

		# rate
		self.taxa: float = \
			self.get_value('taxa',field_type=float)

		# description
		self.descricao: DescricaoModel = \
			DescricaoModel(
				self.get_value('descricao',field_type=dict)).to_dict()