from __future__ import print_function

from .constants import *
from .events import Events
from .company import *
from .house import *
from .board_log import *


class Board:
	def __init__(self,
	             length=BoardProps.length,
	             houses=BoardProps.houses,
	             companies=BoardProps.companies,
	             shop_range=BoardProps.shop_range,
	             company_types=types
	             ):

		# Set private vars
		self._len = length
		self._houses = houses
		self._num_companies = companies
		self._company_types = company_types
		self._shop_range = shop_range

		self.need_to_adjust_closest = False
		self.log = BoardLog()

		self._gen_board()

	def _gen_board(self):

		# Set up board
		self._board = []

		# Init with nulls
		for x in range(0, self._len):
			to_append = []                  # Column
			for y in range(0, self._len):   # Add x amount of nulls
				to_append.append(None)      # Append to column
			self._board.append(to_append)   # Append to board

		# Set up companies
		self.companies = []
		for _ in range(0, self._num_companies):         # Create x number of companies
			_type = random.choice(self._company_types)  # Pick a random type for the company
			company = Company(_type, self)              # Create the company
			self.companies.append(company)              # Append to list of companies

			# Set up stores
			num_stores = round(rand_range_int(self._shop_range) * _type.stores_multiplier)

			if num_stores == 0:     # Prevent having no stores
				num_stores += 1

			# Set up stores for the company
			for __ in range(0, int(num_stores)):     # Create x number of stores
				pos = self.get_place()          # Get a valid place
				store = Store(company, pos)     # Create the company
				self.place(store)               # Add it to the board
				company.add_store(store)        # Add to the company

		# Set up houses
		self.houses = []
		self.build_houses(self._houses)

	@property
	def length(self):
		return self._len

	@property
	def num_houses(self):
		return self._houses

	@property
	def num_companies(self):
		return self._num_companies

	def build_houses(self, houses):
		for _ in range(0, int(houses)):
			pos = self.get_place()

			closest_stores = self.calc_closest(pos)

			house = House(closest_stores, pos)
			self.place(house, pos)
			self.houses.append(house)

	def place(self, obj, pos=None):
		if not pos:
			pos = self.get_place()

		self._board[pos[0]][pos[1]] = obj

		return pos

	def get_place(self):
		while True:
			x = random.randint(0, self._len - 1)
			y = random.randint(0, self._len - 1)

			if not self._board[x][y]:
				return x, y

	def calc_closest(self, pos):
		closest_stores = []

		for company in self.companies:
			closest = None
			closest_dist = float("inf")

			for store in company.stores:
				dist_sqrd = (pos[0] - store.pos[0]) ** 2 + (pos[1] - store.pos[1]) ** 2

				if dist_sqrd < closest_dist:
					closest = store
					closest_dist = dist_sqrd

			closest_stores.append(closest)

		return closest_stores

	def sim(self):
		self.log.reset()

		for house in self.houses:
			house.sim()

		for company in self.companies:
			company.sim()

		if self.need_to_adjust_closest:
			for house in self.houses:
				pos = house.pos
				closest = self.calc_closest(pos)
				house.stores = closest

		self.do_events()

		self.need_to_adjust_closest = False
		self.log.output()

	def _do_event(self, prob, callback):
		rand = random.random()
		if prob > rand:
			callback()

	def do_events(self):
		events = []

		# House
		def house_event():
			def callback():
				rand = rand_range_float(Events.houses.amount)   # Pick percent of new houses
				num = int(len(self.houses) * rand)            # Calc num of houses
				self.build_houses(num)                          # Create the objects
				self.log.houses_build(num)                     # Add to the log
			self._do_event(Events.houses.prob, callback)
		events.append(house_event)

		for event in events:
			event()

	def company_positions(self):
		print("\n--- Company Positions ---\n")
		for x in self.companies:
			x.output()
			print()
		print()

