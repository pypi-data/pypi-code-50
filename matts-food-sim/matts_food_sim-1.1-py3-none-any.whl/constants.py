from .company_type import *

types = [
	CompanyType(
		name='Fast Food',
		store_costs=(150.0, 200.0),
		sale_price=(4.0, 6.0),
		stores_multiplier=2.5,
		cost_per_meal=(0.1, 0.3),
		sales_multiplier=3.5,
		store_close_limit=-1000.0,
		store_open_limit=5000.0
	),
	CompanyType(
		name='Family',
		store_costs=(100.0, 200.0),
		sale_price=(6.0, 8.0),
		stores_multiplier=1,
		cost_per_meal=(0.4, 0.5),
		sales_multiplier=1,
		store_close_limit=-1000.0,
		store_open_limit=5000.0
	),
	CompanyType(
		name='Named-Chef',
		store_costs=(100.0, 200.0),
		sale_price=(10.0, 12.0),
		stores_multiplier=0.5,
		cost_per_meal=(0.4, 0.5),
		sales_multiplier=0.5,
		store_close_limit=-1000.0,
		store_open_limit=5000.0
	),
]


class BoardProps:
	length = 200
	houses = 2000
	companies = 7
	shop_range = (2, 5)
	company_types = types


class PersonProps:
	probability = 0.4


class HouseProps:
	people = (1, 5)


Prefix = {
	"person": 'p-',
	"house": 'h-',
	"store": 's-',
	"company": 'c-',
}