

class BoardLog:
	def __init__(self):
		self._log = []

	def reset(self):
		self._log = []

	def store_remove(self, company):
		msg = "The {} restaurant \"{}\" has closed a store due to losses".format(company.type.name, company.id)
		self._log.append(msg)

	def houses_build(self, amount):
		msg = "{} houses have been built in the town".format(amount)
		self._log.append(msg)

	def close(self, company):
		msg = "The {} restaurant \"{}\" has closed".format(company.type.name, company.id)
		self._log.append(msg)

	def output(self):
		for msg in self._log:
			print(msg)
