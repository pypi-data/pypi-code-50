from abc import ABC, abstractmethod
from .MarketDataUtils import *
from .Exceptions import *

pd.set_option('mode.chained_assignment', None)

class TickFactorsGeneratorBase(ABC):
	def __init__(self):
		self.tickLabelFrame = self.TickLabelFrame()

	@abstractmethod
	def TickLabelFrame(self):
		return pd.DataFrame()

	def FactorsFrameGenerationProcess(self, instrument, tradingDate):
		try:
			rawTickFrame = self.RawTickFrame(instrument, tradingDate)
			tickFrame = self.TickFramePreprocessing(rawTickFrame)
			factorsFrame = self.GenerateFactorsFrame(tickFrame)
			return factorsFrame
		except NoDataError as e:
			print(e)
			raise ProcessFailure("error, failed to generate factors frame for %s on %s" % (instrument, tradingDate))

	@abstractmethod
	def RawTickFrame(self, instrument, tradingDate):
		return pd.DataFrame()

	@abstractmethod
	def TickFramePreprocessing(self, rawTickFrame):
		return rawTickFrame

	@abstractmethod
	def GenerateFactorsFrame(self, dataFrame):
		return dataFrame