import os.path
import subprocess

class Twetch: 

	def __init__(self, content=None, media=None, reply_tx=None, like_tx=None, published_url=None):
		self.content = content
		self.media = media
		self.reply_tx = reply_tx
		self.like_tx = like_tx
		self.published_url = published_url

	def publish(self):
		"""
		Publish a Twetch. The type of Twetch (media post, reply, branch, etc.)
		is based on the attributes you set when instantiating your Twetch
		object.

		Successful Twetches set the 'published_url' attribute to the URL of
		your Twetch.

		The 'content' attribute is required. All others are optional.
		"""
		if not self.content:
			raise TypeError("Attribute 'content' cannot be 'NoneType'")

		if self.media:
			try:
				media_file = os.path.abspath(str(self.media))
			except:
				raise OSError("Unable to derive absolute path of media file.")

		try:
			if self.reply_tx and self.media:
				process = subprocess.run(
					['twetch', 'post', '--content', str(self.content), '--file', media_file, '--reply', str(self.reply_tx)],
					stdout=subprocess.PIPE,
					stderr=subprocess.PIPE
					)
			elif self.reply_tx:
				process = subprocess.run(
					['twetch', 'post', '--content', str(self.content), '--reply', str(self.reply_tx)],
					stdout=subprocess.PIPE,
					stderr=subprocess.PIPE
					)
			elif self.media:
				process = subprocess.run(
					['twetch', 'post', '--content', str(self.content), '--file', media_file],
					stdout=subprocess.PIPE,
					stderr=subprocess.PIPE
					)
			else:
				process = subprocess.run(
					['twetch', 'post', '--content', str(self.content)],
					stdout=subprocess.PIPE,
					stderr=subprocess.PIPE
					)
			
			stdout_str = process.stdout.decode('utf-8')
			stderr_str = process.stderr.decode('utf-8')
		except:
			raise OSError("Twetch CLI subprocess run failed.")

		if "No Funds" in stdout_str:
			raise Exception("No funds in signing wallet. Add BSV and try again.")
		elif len(process.stderr.decode('utf-8')) > 0:
			return process.stderr.decode('utf-8')
		elif "published!" in stdout_str:
			stdout_list = stdout_str.split("published!")
			url = stdout_list[1].strip()
			self.published_url = url
		else:
			raise Exception("Error publishing content to Twetch.")

	def like_twetch(self):
		"""
		Like a Twetch. 

		The 'like_tx' attribute is required. This should be a string
		of the Twetch post TXID you're liking.
		"""
		if not self.like_tx:
			raise TypeError("Attribute 'like_tx' cannot be 'NoneType'")

		try:
			process = subprocess.run(['twetch', 'like', '-t', str(self.like_tx)],
				stdout=subprocess.PIPE,
				stderr=subprocess.PIPE)
			
			stdout_str = process.stdout.decode('utf-8')
			stderr_str = process.stderr.decode('utf-8')
		except:
			raise OSError("Twetch CLI subprocess run failed.")

		if "No Funds" in stdout_str:
			raise Exception("No funds in signing wallet. Add BSV and try again.")
		elif len(process.stderr.decode('utf-8')) > 0:
			return process.stderr.decode('utf-8')
		elif "liked!" in stdout_str:
			stdout_list = stdout_str.split("liked!")
			url = stdout_list[1].strip()
			self.published_url = url
		else:
			raise Exception("Error liking Twetch {}.".format(self.like_tx))

	def get_address(self):
		"""
		Fetches the active signing address from your Twetch SDK install and returns it as a string.
		"""
		try:
			process = subprocess.run(['twetch', 'address'], 
				stdout=subprocess.PIPE,
				stderr=subprocess.PIPE)
			response = process.stdout.decode('utf-8')
			stdout_list = response.split("address:")
			address = stdout_list[1].strip()

			if len(process.stderr.decode('utf-8')) > 0:
				return process.stderr.decode('utf-8')
			else:
				return address
		except:
			raise Exception("Failed to derive address.")

	def get_balance(self):
		"""
		Fetches the balance of the wallet from your Twetch SDK install and returns it as a float.

		Unit: BSV
		"""
		try:
			process = subprocess.run(['twetch', 'balance'], 
				stdout=subprocess.PIPE, 
				stderr=subprocess.PIPE)
			response = process.stdout.decode('utf-8')
			stdout_list = response.split("balance:")
			balance = float(stdout_list[1].strip().strip(" BSV"))

			if len(process.stderr.decode('utf-8')) > 0:
				return process.stderr.decode('utf-8')
			else:
				return balance
		except:
			raise Exception("Failed to derive balance.")

	@property 
	def serialize(self):
		return {
		"content": self.content,
		"media": self.media,
		"reply_tx": self.reply_tx,
		"like_tx": self.like_tx,
		"published_url": self.published_url
		}

	def __repr__(self):
		return "Twetch('{}', '{}', '{}', '{}', '{}')".format(self.content, 
			self.media, 
			self.reply_tx, 
			self.like_tx, 
			self.txid)






