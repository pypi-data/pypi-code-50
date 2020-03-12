import os
import pymysql
import pymysql.cursors
import datetime
from mnrva.utils import console


class MySQL(object):
	def __init__(self, debug=False):
		try:
			self.db = pymysql.connect(  host=os.environ['DB_HOST'],
				                        port=int(os.environ['DB_PORT']),
				                        user=os.environ['DB_USER'],
				                        passwd=os.environ['DB_PASSWORD'],
				                        db=os.environ['DB_NAME'],
				                        charset='utf8',
		                                connect_timeout=5)
			self.cur = self.db.cursor(pymysql.cursors.DictCursor)
			self.debug = debug
		except pymysql.Error as e:
			self.printError(e)

	def __del__(self):
		try:
			self.db.close()
		except:
			pass

	def close(self):
		self.db.close()

	def printError(self, e):
		console.error('MySQL Error [%d]: %s' % (e.args[0], e.args[1]))

	def isInt(self, s):
		if type(s) is not int:
			if s.find('_') > -1:
				return False
			try:
				int(s)
				return True
			except ValueError:
				return False
		else:
			return True

	def sendQuery(self, query):
		if self.debug:
			console.warn('MySQL debug:' + query)

		try:
			self.cur.execute(query)
			self.db.commit()

			first_letter = query[:1].upper()
			if first_letter == 'S':
				return self.cur.fetchall()
			elif first_letter == 'I':
				return self.lastID()
			elif first_letter == 'U':
				return self.cur.rowcount
			else:
				return True

		except pymysql.Error as e:
			self.db.rollback()
			if self.debug:
				self.printError(e)
			return False

	def lastID(self):
		return self.cur.lastrowid

	def insert(self, table, data):
		fields = []
		values = []

		for key, val in data.items():
			if val is None:
				continue

			fields.append('`' + key + '`')

			if isinstance(val, datetime.date):
				val = val.strftime('%Y-%m-%dT%H:%M:%S%z')

			if self.isInt(val):
				values.append(str(val))
			else:
				if val.find('GeomFromText') >= 0:
					values.append(val)
				else:
					values.append(self.db.escape(val))

		query = 'INSERT INTO {0} ({1}) VALUES ({2});'.format(table, (','.join(fields)), (','.join(values)))
		return self.sendQuery(query)

	def insertMulti(self, table, fields, data):
		multi = []

		for val in data:
			values = []
			for value in val:
				if self.isInt(value):
					values.append(str(value))
				else:
					values.append(self.db.escape(value))

			multi.append('(' + (','.join(values)) + ')')

		query = 'INSERT INTO {0} ({1}) VALUES {2};'.format(table, (','.join(fields)), (','.join(multi)))
		return self.sendQuery(query)

	def select(self, table, data, extra='', projection='*', operator='='):
		fields = []

		for key, val in data.items():
			if self.isInt(val):
				fields.append(key + operator + str(val))
			else:
				fields.append(key + operator + self.db.escape(val))
		query = 'SELECT {0} FROM {1} WHERE {2} {3};'.format(projection, table, (' AND '.join(fields)), extra)
		return self.sendQuery(query)

	def selectOne(self, table, data, projection='*'):
		result = self.select(table, data, 'LIMIT 0,1', projection)

		if result:
			return result[0]
		else:
			return False

	def selectAll(self, table, extra='', projection='*'):
		query = 'SELECT {0} FROM {1} {2};'.format(projection, table, extra)
		return self.sendQuery(query)

	def update(self, table, data, where):
		fields = []
		f_where = []

		for key, val in data.items():
			if self.isInt(val):
				fields.append(key + '=' + str(val))
			else:
				fields.append(key + '=' + self.db.escape(val))

		for key, val in where.items():
			if self.isInt(val):
				f_where.append(key + '=' + str(val))
			else:
				f_where.append(key + '=' + self.db.escape(val))

		query = 'UPDATE {0} SET {1} WHERE {2};'.format(table, (', '.join(fields)), (' AND '.join(f_where)))
		return self.sendQuery(query)

	def database(self, database):
		self.db.select_db(database)


if __name__ == '__main__':
	print('*** Welcome to Minerva 4R. Social Data Mining S.A. 2020 ***')