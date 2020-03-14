from configparser import ConfigParser 
import logging
import socket
import hashlib
from logging.handlers import SysLogHandler
from base64 import (b64encode,b64decode)
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

class ContextFilter(logging.Filter):
	hostname = socket.gethostname()

	def filter(self, record):
		record.hostname = ContextFilter.hostname
		return True

def insecurelog(app_name, message, integrity_check, logger, syslog):
	format = '%(asctime)s %(hostname)s ' \
			+ app_name \
			+ ' : %(message)s' \
			+ ' : %(integrity_check)s '
	formatter = logging.Formatter(format, datefmt='%b %d %H:%M:%S')
	syslog.setFormatter(formatter)
	logger.error(message,extra={'integrity_check': integrity_check})
	return

def securelog(app_name, message, signer, logger,syslog):
	# Calculating A
	message_hash = hashlib.sha512()
	message_hash.update(message)
	# Calculating B
	digest = SHA256.new()
	digest.update(message_hash.digest())
	digest.update(message)
	digest.update(message_hash.digest())
	sig = signer.sign(digest)
	# Calculating C
	sign_hash = hashlib.sha512()
	sign_hash.update(sig)
	# Assigning Values
	A = message_hash.hexdigest()
	B = b64encode(sig)
	C = sign_hash.hexdigest()
	# Building String
	integrity_check = A + " | " + B + " | " + C
	insecurelog(app_name, message, integrity_check, logger, syslog)

	return A, B, C

def read_signing_key(config_file):
	# instantiate 
	config = ConfigParser() 
	# parse existing file 
	config.read(config_file)
	# read values from shared config 
	private_key_file 	= config.get('logging', 'signing_key')
	private_key = False
	with open (private_key_file, "r") as myfile:
		private_key = RSA.importKey(myfile.read())
	
	# Load private key and sign message
	signer = PKCS1_v1_5.new(private_key)
	return signer

def syslog_config(config_file):
	# instantiate 
	config = ConfigParser() 
	# parse existing file 
	config.read(config_file)
	# read values from shared config 
	syslog_address 	= config.get('logging', 'syslog_address') 
	syslog_port 	= config.getint('logging', 'syslog_port') 
	syslog = SysLogHandler(address=(syslog_address, syslog_port))
	syslog.addFilter(ContextFilter())
	return syslog
 
def logger_config(syslog):
	logger = logging.getLogger()
	logger.addHandler(syslog)
	logger.setLevel(logging.INFO)
	return logger

def main():
	config_file = "./log.ini"
	syslog = syslog_config(config_file)
	logger = logger_config(syslog)
	signer = read_signing_key(config_file)

	appname = "test"
	message = "This is a message"
	securelog(appname, message, signer, logger, syslog)
	exit()

if __name__== "__main__":
  main()
