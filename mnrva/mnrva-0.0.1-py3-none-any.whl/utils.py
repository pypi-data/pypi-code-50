import json
import re
import multiprocessing


def use(package, lib=''):
	if lib == '':
		lib = package.title()
	package = __import__('mnrva.' + package, fromlist=lib)
	method = getattr(package, lib)
	return method

def removeEmoji(text):
	try:
		emojis = re.compile(u'[\U00010000-\U0010ffff]')
	except re.error:
		emojis = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')

	return emojis.sub(u'', text)

def runWorkers(workers, method):
	processes = [multiprocessing.Process(target=method, args=(w,)) for w in workers]
	[process.start() for process in processes]
	[process.join() for process in processes]


class console(object):
	@staticmethod
	def log(text):
		print("\033[0;32;40m {0}\033[0;37;40m".format(text))

	@staticmethod
	def warn(text):
		print("\033[0;33;40m {0}\033[0;37;40m".format(text))

	@staticmethod
	def info(text):
		print("\033[0;36;40m {0}\033[0;37;40m".format(text))

	@staticmethod
	def error(text):
		print("\033[0;31;40m {0}\033[0;37;40m".format(text))

	@staticmethod
	def dir(dict):
		print(json.dumps(dict, indent=1))

	@staticmethod
	def about():
		print("\033[0;32;40m Tools Minerva IV\033[0;37;40m")


if __name__ == '__main__':
	print('*** Welcome to Minerva 4R. Social Data Mining S.A. 2019 ***')


