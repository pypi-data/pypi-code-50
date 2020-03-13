

class CompanyType:
	def __init__(self,
		name,
		store_costs,
		sale_price,
		cost_per_meal,
		stores_multiplier,
		sales_multiplier,
		store_close_limit,
		store_open_limit,
	):

		self.name = name
		self.store_costs = store_costs
		self.sale_price = sale_price
		self.cost_per_meal_percent = cost_per_meal
		self.stores_multiplier = stores_multiplier
		self.sales_multiplier = sales_multiplier
		self.store_close_limit = store_close_limit
		self.store_open_limit = store_open_limit
