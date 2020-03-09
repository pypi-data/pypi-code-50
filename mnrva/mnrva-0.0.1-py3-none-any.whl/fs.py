import json
import csv
import os
import sys
from mnrva.utils import console


class FileSystem(object):

	def __init__(self):
		self.base_url = os.path.abspath(os.path.split(sys.argv[0])[0]) + '/'

	def readJSON(self, filename):
		try:
			json_data = open(self.base_url + filename).read()
			return json.loads(json_data)
		except:
			console.error('-- Error -- Read file json')
			return None

	def readCSV(self, filename):
		try:
			csv_data = open(self.base_url + filename)
			return csv.reader(csv_data)
		except:
			console.error('-- Error -- Read file csv')
			return None

	def getSchema(self, filename):
		fileSchema = self.base_url + 'schemas/' + filename + '.sql'
		if os.path.exists(fileSchema):
			return fileSchema
		else:
			console.error('-- Error -- Schema Not found')
			return None

	def makeDir(self, directory):
		path_dir = self.base_url + directory
		if not os.path.exists(path_dir):
			os.mkdir(path_dir)

	def makeFile(self, filename):
		filename = self.base_url + filename
		if not os.path.exists(filename):
			open(filename, 'w').close()

	def writeFile(self, filename, text=''):
		filename = self.base_url + filename
		if os.path.exists(filename):
			f = open(filename, 'w')
			f.write(text)
			f.close()


if __name__ == '__main__':
	print('*** Welcome to Minerva 4R. Social Data Mining S.A. 2019 ***')
