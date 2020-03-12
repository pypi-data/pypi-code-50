from functools import reduce
from .TrainingUtils import *
from ..Exceptions import *

class MultiInstrumentTickTrainingUtils(TickTrainingUtils):
	def __init__(self, userConfig, modelConfig):
		TickTrainingUtils.__init__(self, userConfig)
		self.factorsInfo = dict()
		for instConfig in modelConfig['Instruments']:
			conf = dict()
			#因子库因子
			if 'LibFactors' in instConfig:
				conf['FactorLibInfo'] = {lib['LibName']:{'Fields':[f['Name'] for f in lib['Factors']]} for lib in instConfig['LibFactors']}
			#本地因子集
			if 'LocalFactors' in instConfig:
				conf['LocalSetInfo'] = {lSet['SetName']:{'RootDir':lSet['RootDir'],'Fields':[f['Name'] for f in lSet['Factors']]} for lSet in instConfig['LocalFactors']}
			self.factorsInfo[instConfig['Name']] = conf

	def CompleteFactorsFrame(self, tradingDate):
		try:
			instRawFrames = [self.InstrumentFactorsFrame(instrument, tradingDate) for instrument in self.factorsInfo.keys()]
			if len(instRawFrames) == 0:
				raise NoDataError('error, no instrument config for model, please check model config file')
			elif len(instRawFrames) == 1:
				consFrame = instRawFrames[0]
			else:
				consFrame = reduce(lambda left,right: pd.merge(left, right, on=TickTrainingUtils.alignField), instRawFrames)
			return consFrame
		except Exception as e:
			print(e)
			raise NoDataError('error, failed to get consolidated raw factors frame on %s' % tradingDate)

	def InstrumentFactorsFrame(self, instrument, tradingDate):
		try:
			frames = list()
			dFields = list()
			if 'FactorLibInfo' in self.factorsInfo[instrument]:
				for libName in self.factorsInfo[instrument]['FactorLibInfo'].keys():
					dFields.extend(self.factorsInfo[instrument]['FactorLibInfo'][libName]['Fields'])
					frames.append(self.GetLibFactorsData(libName, instrument, tradingDate, self.factorsInfo[instrument]['FactorLibInfo'][libName]['Fields']))
			if 'LocalSetInfo' in self.factorsInfo[instrument]:
				for setName in self.factorsInfo[instrument]['LocalSetInfo'].keys():
					dFields.extend(self.factorsInfo[instrument]['LocalSetInfo'][setName]['Fields'])
					frames.append(self.GetLocalFactorsData(setName, self.factorsInfo[instrument]['LocalSetInfo'][setName]['RootDir'], instrument, tradingDate, self.factorsInfo[instrument]['LocalSetInfo'][setName]['Fields']))
			renamingDict = {f:'%s_%s' % (instrument, f) for f in dFields}
			if len(frames) == 0:
				raise NoDataError('error, no data field specified for %s, please check model config file' % instrument)
			elif len(frames) == 1:
				consFrame = frames[0]
			else:
				consFrame = reduce(lambda left,right: pd.merge(left, right, on=TickTrainingUtils.alignField), frames)
			consFrame.rename(columns=renamingDict, inplace=True)
			return consFrame
		except Exception as e:
			print(e)
			raise NoDataError('error, failed to get raw factors frame for %s on %s' % (instrument, tradingDate))
