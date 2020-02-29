from cautil.utils.authorization import AuthorizationUtilInterface
from cautil import ConfigDataException
import json
import time
import jwt
from cryptography.fernet import Fernet
import datetime

class DB(AuthorizationUtilInterface):

	def __init__(self, config):
		self.config = config
		self.__validate_configuration(self.config)
	

	def get_configuration(self, **kwargs):
		return self.config


	def login(self, userdetails):
		
		key = self.config['key'].encode("utf-8")
		cipher = Fernet(key)
		credential_byte = json.dumps(userdetails).encode('utf-8')
		cred_enc = cipher.encrypt(credential_byte)	
		encode_enc={
			'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
			'token':cred_enc.decode("utf-8")
		}
		
		token = jwt.encode(encode_enc, self.config['DBtoAccessKey'])
		id_token=token.decode("utf-8")
		return {"statusCode": 200, "body": {"access_token":encode_enc['token'], 'id_token':id_token}}

	def validate_token(self, token):
		try:
			jwt_decoded_details = jwt.decode(token, self.config['DBtoAccessKey'])
			decoded_cipher=jwt_decoded_details['token'].encode("utf-8")
			key = self.config['key'].encode("utf-8")
			cipher = Fernet(key)
			decrypted_values= cipher.decrypt(decoded_cipher).decode('utf-8')
			decrypted_values = json.loads(decrypted_values)
			
			return {"statusCode": 200, "body": {"message": 'Token is valid', 'claims': decrypted_values}}
		except:
			return {"statusCode": 500, "body": {"message": 'Token is invalid'}}


	def create_user(self, username, password, user_details={}, **kwargs):
		return {"statusCode": 500, "body": {"msg": 'not implemented'}}

	def delete_user(self, user_id, **kwargs):

		return {"statusCode": 500, "body": {"msg": 'not implemented'}}

	def refresh_access(self, **kwargs):
		encode_enc={
			'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
			'token':kwargs['userdetails']['access_token']
		}
		token = jwt.encode(encode_enc, self.config['DBtoAccessKey'])
		id_token=token.decode("utf-8")
		return {"statusCode": 200, "body": {"id_token":id_token, 'username':kwargs['userdetails']['username']}}

		

	def __validate_configuration(self, config):
		config_req_param_list = ["DBtoAccessKey"]

		for param in config_req_param_list:
			if(param not in self.config):
				raise ConfigDataException(
					'Config param `{}` is missing'.format(param))
		return True
