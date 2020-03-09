from slackclient import SlackClient


class Slack(object):

	def __init__(self):
		token = ""
		self.sc = SlackClient(token)

	def send(self, user, channel, message):
		self.sc.api_call(
			"chat.postMessage",
			channel=channel,
			text=message,
			username=user
		)


if __name__ == '__main__':
	print('*** Welcome to Minerva 4R. Social Data Mining S.A. 2019 ***')
