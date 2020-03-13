from __future__ import print_function
import random

from .func import *
from .id import rand_id


class Store:
	def __init__(self, company, pos):
		self.id = rand_id("store")

		self.parent = company
		self.pos = pos
		self.sale_price = company.sale_price

		self.store_cost = (random.randint(90, 110)/100.0) * company.store_cost_avg

		self.active = True

		self._sales = 0.0
		self._costs = 0.0

	def sale(self):
		self._sales += self.sale_price * self.parent.type.sales_multiplier

	def reset(self):
		self._sales = 0.0

	def sim(self):
		self._costs += self.store_cost
		if self.total < self.parent.type.store_close_limit:
			self.active = False
			self.parent.remove_store(self)

	@property
	def total(self):
		return round_pence(self._sales - self._costs)

	@property
	def sales(self):
		return round_pence(self._sales)

	@property
	def costs(self):
		return round_pence(self._costs)

	def output(self):
		pass