from cautil.utils.authorization import AuthorizationUtilInterface
from cautil import ConfigDataException

import boto3
import hmac
import hashlib
import base64
import urllib
import json
import time
from jose import jwk, jwt


class Cognito(AuthorizationUtilInterface):

	def __init__(self, config):
		self.client = None
		self.config = config
		self.config = self.get_configuration()
		self.__validate_configuration(self.config)

	def get_configuration(self, **kwargs):
		arn_split_value = str(self.config['cognitoUserPoolArn']).split(':')
		self.config['cognitoUserPoolId'] = str(
			(arn_split_value[5].split('/'))[1])
		self.config['cognitoRegionName'] = str(arn_split_value[3])
		cognito_client = self.__get_boto3_client()
		response = cognito_client.list_user_pool_clients(
			UserPoolId=self.config['cognitoUserPoolId'])
		self.config['cognitoClientId'] = response['UserPoolClients'][0]['ClientId']
		response = cognito_client.describe_user_pool_client(
			UserPoolId=self.config['cognitoUserPoolId'], ClientId=self.config['cognitoClientId'])
		self.config['cognitoClientSecret'] = response['UserPoolClient']['ClientSecret']
		return self.config

	def validate_token(self, token, **kwargs):
		try:
			keys_url = 'https://cognito-idp.{}.amazonaws.com/{}/.well-known/jwks.json'.format(
				self.config['cognitoRegionName'], self.config['cognitoUserPoolId'])
			response = urllib.request.urlopen(keys_url)
			keys = json.loads(response.read().decode('utf-8'))['keys']
			token = str(token)
			headers = jwt.get_unverified_headers(token)
			kid = headers['kid']
			key_index = -1
			for i in range(len(keys)):
				if kid == keys[i]['kid']:
					key_index = i
					break
			if key_index == -1:
				return {"statusCode": 500, "body": {"msg": 'Token is invalid'}}
			public_key = jwk.construct(keys[key_index])
			try:
				message, encoded_signature = str(token).rsplit('.', 1)
			except:
				return {"statusCode": 500, "body": {"msg": 'Token is invalid'}}
			rem = len(encoded_signature) % 4
			if rem > 0:
				encoded_signature += '=' * (4 - rem)
			decoded_signature = base64.urlsafe_b64decode(
				str.encode(encoded_signature))
			if not public_key.verify(str.encode(message), decoded_signature):
				return {"statusCode": 500, "body": {"msg": 'Token is invalid'}}
			try:
				claims = jwt.get_unverified_claims(token)
			except:
				return {"statusCode": 500, "body": {"msg": 'Token is invalid'}}
			if time.time() > claims['exp']:
				return {"statusCode": 500, "body": {"msg": 'Token is invalid'}}
			if claims['aud'] != self.config['cognitoClientId']:
				return {"statusCode": 500, "body": {"msg": 'Token is invalid'}}
			validate_response = {}
			validate_response['claimsUserName'] = claims['cognito:username']
			validate_response['claimsGroups'] = claims['cognito:groups']
			return {"statusCode": 200, "body": {"msg": 'Token is valid', 'claims': validate_response}}
		except Exception as e:
			return {"statusCode": 500, "body": {"msg": str(e)}}

	def login(self, username, password, token=None, **kwargs):
		try:
			login_response = {}
			cognito_client = self.__get_boto3_client()
			resp = cognito_client.admin_initiate_auth(
				UserPoolId=self.config['cognitoUserPoolId'],
				ClientId=self.config['cognitoClientId'],
				AuthFlow='ADMIN_NO_SRP_AUTH',
				AuthParameters={
					'USERNAME': username,
					'SECRET_HASH': self.__get_secret_hash(username),
					'PASSWORD': password
				},
				ClientMetadata={
					'username': username,
					'password': password
				})
			login_response['IdToken'] = resp['AuthenticationResult']['IdToken']
			login_response['AccessToken'] = resp['AuthenticationResult']['AccessToken']
			login_response['RefreshToken'] = resp['AuthenticationResult']['RefreshToken']
			return {"statusCode": 200, "body": {"msg": 'Logged in successfully', 'claims': login_response}}
		except Exception as e:
			return {"statusCode": 500, "body": {"msg": str(e)}}

	def create_user(self, username, password, user_details={}, **kwargs):
		try:
			client = self.__get_boto3_client()
			resp = client.sign_up(
				ClientId=self.config['cognitoClientId'],
				SecretHash=self.__get_secret_hash(username),
				Username=username,
				Password=password,
				UserAttributes=[{'Name': 'email', 'Value': user_details['email']},
								{'Name': 'address', 'Value': user_details['address']}]
			)
			if 'user_group' in user_details and user_details['user_group'] is not None:
				response_add_user_group = client.admin_add_user_to_group(
					UserPoolId=self.config['cognitoUserPoolId'], Username=username, GroupName=user_details['user_group'])
			response_confirm = client.admin_confirm_sign_up(
				UserPoolId=self.config['cognitoUserPoolId'],
				Username=username
			)
			return {"statusCode": 200, "body": {"msg": 'User created successfully'}}
		except client.exceptions.UsernameExistsException as e:
			return {"statusCode": 400, "body": {"msg": 'User already exists'}}
		except Exception as e:
			return {"statusCode": 500, "body": {"msg": str(e)}}

	def delete_user(self, user_id, **kwargs):
		try:
			cognito_client = self.__get_boto3_client()
			response_remove_user_group = cognito_client.admin_delete_user(
				UserPoolId=self.config['cognitoUserPoolId'], Username=user_id)
			return {"statusCode": 200, "body": {"msg": 'User deleted successfully'}}
		except Exception as e:
			return {"statusCode": 500, "body": {"msg": str(e)}}

	def refresh_access(self, refresh_token, **kwargs):
		try:
			event = kwargs
			cognito_client = self.__get_boto3_client()
			response = cognito_client.initiate_auth(ClientId=self.config['cognitoClientId'],
													AuthFlow='REFRESH_TOKEN_AUTH',
													AuthParameters={
				'REFRESH_TOKEN': refresh_token,
				'SECRET_HASH': self.__get_secret_hash(event['username'])})
			refresh_response = {}
			refresh_response['IdToken'] = response['AuthenticationResult']['IdToken']
			refresh_response['AccessToken'] = response['AuthenticationResult']['AccessToken']
			refresh_response['RefreshToken'] = refresh_token
			return {"statusCode": 200, "body": {"msg": 'Refreshed access successfully', 'claims': refresh_response}}
		except Exception as e:
			return {"statusCode": 500, "body": {"msg": str(e)}}

	def __get_boto3_client(self):
		if self.client is None:
			self.client = boto3.client('cognito-idp', region_name=self.config['cognitoRegionName'], aws_access_key_id=self.config['cognitoAccessKey'],
									   aws_secret_access_key=self.config['cognitoSecretKey'])
		return self.client

	def __get_secret_hash(self, username):
		msg = username + self.config['cognitoClientId']
		dig = hmac.new(str(self.config['cognitoClientSecret']).encode('utf-8'),
					   msg=str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
		d2 = base64.b64encode(dig).decode()
		return d2

	def __validate_configuration(self, config):
		config_req_param_list = [
			"cognitoAccessKey",
			"cognitoSecretKey",
			"cognitoUserPoolArn",
			"cognitoUserPoolId",
			"cognitoRegionName",
			"cognitoClientId",
			"cognitoClientSecret"
		]
		for param in config_req_param_list:
			if(param not in self.config):
				raise ConfigDataException(
					'Config param `{}` is missing'.format(param))
		return True
