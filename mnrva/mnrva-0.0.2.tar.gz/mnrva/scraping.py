import json
import urllib3
import certifi
from urllib.parse import quote
from mnrva.utils import console
import urllib.request


class Scraping(object):
	def __init__(self, method='GET', secure=True):

		if secure:
			self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
		else:
			self.http = urllib3.PoolManager()

		self.method = method
		self.agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

	def getHTML(self, url, data=None):
		result = {'error': False, 'data': None}

		url_safe = quote(url, ':/?=')
		try:
			if self.method == 'POST':
				response = self.http.request_encode_body(self.method, url_safe, fields=data, headers=self.agent)
			else:
				response = self.http.request_encode_url(self.method, url_safe, fields=data, headers=self.agent)

			if response.status == 200:
				try:
					result['data'] = response.data.decode()
				except:
					result['data'] = response.data
			else:
				console.error('Error de Url ' + url + ' ' + str(response.status))
				result['data'] = 'Error de Url {0} {1}'.format(url, response.status)
				result['error'] = True

		except BaseException as e:
			console.error('Url no disponible ' + url)
			result['data'] = e
			result['error'] = True

		return result

	def getURL(self, url, data={}, header={}, withHeaders=False):
		try:
			if self.method == 'POST':
				response = self.http.request_encode_body(self.method, url, fields=data, headers=header)
			else:
				response = self.http.request_encode_url(self.method, url, fields=data, headers=header)

			if response.status == 200 or response.status == 400:
				try:
					dataDecoded = json.loads(response.data.decode())
					if withHeaders:
						return {'response': dataDecoded, 'headers': response.headers}
					else:
						return dataDecoded
				except:
					console.error('Format invalid, only JSON')
					return False
			else:
				console.error('Error de Url ' + url + ' ' + str(response.status))
				return False
		except:
			console.error('Url no disponible ' + url)
			return False

	def getFile(self, url):
		response = self.http.request_encode_url(self.method, url)
		if response.status == 200:
			try:
				return response.data
			except:
				return False

	def getFileAudio(self, url):
		with urllib.request.urlopen(url) as audio_file:
			content = audio_file.read()
			return content

	def sendJSON(self, url, json_file):
		response = self.http.request_encode_url('POST', url, headers={'Content-Type': 'application/json'}, body=json.dumps(json_file))
		datadecoded = json.loads(response.data.decode())
		return datadecoded


if __name__ == '__main__':
	print('*** Welcome to Minerva 4R. Social Data Mining S.A. 2019 ***')