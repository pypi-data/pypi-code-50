import os
import numpy as np
import pandas as pd
from dateutil.parser import parse
from .DatabaseManager import FactorsDatabaseManager
from .Exceptions import *

class TrainingUtils(object):
	def __init__(self, userInfo):
		self.dbManager = FactorsDatabaseManager(userInfo)

class TickTrainingUtils(object):
	alignField = 'TickLabel'

	def __init__(self, userInfo):
		TrainingUtils.__init__(self, userInfo)

	def GetLibFactorsData(self, libName, instrument, tradingDate, dataFields):
		try:
			tradingDate = str(parse(tradingDate).date()).replace('-', '')
			tableName = [tb for tb in self.dbManager.FactorTables(libName) if tb.endswith('Factors_%s_%s' % (instrument, tradingDate))]
			assert len(tableName) == 1, 'error, no factors data table for %s on %s in %s' % (instrument, tradingDate, libName)
			availFields = self.dbManager.GetTableColumns(libName, tableName[0])
			sql = "SELECT %s" % self.alignField
			cols = [TickTrainingUtils.alignField]
			for f in dataFields:
				sql += ', %s' % f
				cols.append(f)
				if not f in availFields:
					raise NoDataError('error, field %s not in factors table for %s on %s' % (f, instrumentId, tradingDate))
			sql += ' FROM %s' % tableName[0]
			return pd.DataFrame(self.dbManager.GetQueryResult(libName, sql), columns = cols)
		except Exception as e:
			print(e)
			raise NoDataError('error, failed to get factors frame from library %s for %s on %s' % (libName ,instrument, tradingDate))

	def GetLocalFactorsData(self, setName, rootDir, instrument, tradingDate, dataFields):
		try:
			tradingDate = str(parse(tradingDate).date()).replace('-', '')
			fileName = '%s/%s/%s.csv' % (rootDir, tradingDate, instrument)
			if not os.path.exists(fileName):
				raise NoDataError('error, factor set %s does not contain data file for %s on %s' % (setName, instrument, tradingDate))
			df = pd.read_csv('%s/%s/%s.csv' % (rootDir, tradingDate, instrument))
			for f in dataFields:
				if not f in df.columns:
					raise NoDataError('error, field %s not in factors table for %s on %s' % (f, instrument, tradingDate))
			return df[[TickTrainingUtils.alignField]+dataFields]
		except NoDataError as e:
			print(e)
			raise NoDataError('error, failed to get factors frame from local set for %s on %s' % (setName, instrument, tradingDate))