import random

from .person import *
from .func import *
from .constants import *
from .id import rand_id


class House:
	def __init__(self, closest_stores, pos, *args, **kwargs):
		self.id = rand_id("store")

		self._stores = closest_stores
		self._pos = pos

		self._num_people = rand_range_int(HouseProps.people) if kwargs.get("num_people") is None else kwargs.get("num_people")

		self._people = [Person() for _ in range(0, self._num_people)]

	def sim(self):
		""" Calculates how many people eat during the simulation and distributes the sales """

		# Get the sales (this is a list of trues/falses)
		sales = [x.sim() for x in self._people]

		# Loop through the potential sales
		for sale in sales:
			# If there was a sale
			if sale:
				store = random.choice(self._stores)  # Choose a random company's store
				store.sale()                        # And assign them a sale


	@property
	def pos(self):
		""" The x,y position of the house on the board. Tuple[float, float] """
		return self._pos

	@property
	def people(self):
		""" List of Person objects that are children tpo this instance """
		return self._people

	@property
	def stores(self):
		""" List of Store objects that are the closest to the house """
		return self._stores

	@stores.setter
	def stores(self, value):
		self._stores = value
