from .DatabaseManager import FactorsDatabaseManager

class TrainingUtils(object):
	def __init__(self, config):
		self.factorsLib = config['FactorsLibrary']
		self.factorsDB = FactorsDatabaseManager(config['FactorsLibrary'], config['User'])
