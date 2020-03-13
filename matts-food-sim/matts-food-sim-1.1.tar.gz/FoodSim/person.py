import random

from .constants import *
from .id import rand_id


class Person:
	def __init__(self, *args, **kwargs):
		self.id = rand_id("store")

		self._prob = PersonProps.probability if kwargs.get("prob") is None else kwargs.get("prob")

		# Check the value is valid
		if not 0.0 <= self._prob <= 1.0:
			raise ValueError("Probability must be between 0.0 and 1.0")


	def sim(self):
		# See if they will eat at a store
		return self._prob > random.random()
