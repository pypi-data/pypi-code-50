import tweepy

from twistream.log import log

LOG = log.get_logger()


def get_api(consumer_key, consumer_secret,access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)
