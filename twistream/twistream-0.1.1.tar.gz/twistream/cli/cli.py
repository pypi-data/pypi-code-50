import os

import click
import tweepy
import yaml

from twistream.backends import BACKENDS
from twistream.log import log
from twistream.twitter import client, listeners

LOG = log.get_logger()

CONFIG_DIR = os.path.join(os.environ['HOME'], '.twistream')


@click.group(help='Automate data collection from Twitter streaming API')
def twistream():
    pass


@twistream.command(help='Connect to the real-time Twitter Streaming API and start collecting tweets')
@click.argument('config_file')
@click.option('--log-level', type=click.Choice(['INFO', 'DEBUG', 'ERROR']), default='INFO')
@click.option('--tracks', required=True, type=click.STRING, help='Comma separated list of words to follow')
@click.option('--exclude-retweets', is_flag=True, help='Do not include retweets in the collection process')
@click.option('--exclude-quotes', is_flag=True, help='Do not include quoted tweets in the collection process')
def collect(config_file, log_level, tracks, exclude_retweets, exclude_quotes):
    log.set_level(log_level)

    with open(config_file, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    backend = config.get('backend')
    backend_params = config.get('backend_params')

    tracks = [t for t in tracks.split(',')]

    LOG.info(f"Listening for tweets with the following tracks: {', '.join(tracks)}")
    LOG.info(f'Using {backend} backend')

    # Initialize stream listener and start listening
    storage_backend = BACKENDS[backend].get('object')(backend_params)
    listener = listeners.TracksListener(storage_backend,
                                        exclude_retweets=exclude_retweets,
                                        exclude_quotes=exclude_quotes)
    auth = client.get_api(config.get('twitter').get('consumer_key'),
                          config.get('twitter').get('consumer_secret'),
                          config.get('twitter').get('access_token'),
                          config.get('twitter').get('access_token_secret')).auth
    stream = tweepy.Stream(auth=auth, listener=listener)
    stream.filter(track=tracks, is_async=True)


@twistream.command(help='Create a configuration file to run your data collections')
def init():
    click.echo('Before you start your data collection, you need to create a configuration for twistream to ' +
               'be able to connect to twitter API and store your tweets somewhere. First thing you need to do is ' +
               'create a twitter application and get the credentials. Refer to the README file if you don\'t ' +
               'know how to do this.')

    click.echo('\n\nCreating configuration directory...')
    if not os.path.exists(CONFIG_DIR):
        os.mkdir(CONFIG_DIR)

    click.echo('\n\nFirst things first, your application credentials \n')

    consumer_key = input('Application consumer_key: ')
    consumer_secret = input('Application consumer_secret: ')
    access_token = input('Application access_token: ')
    access_token_secret = input('Application access_token_secret: ')

    click.echo('\nGreat, which backend do you want to use for storing your tweets?\n')

    backend = ''
    while backend not in BACKENDS.keys():
        backend = input(f'Choose from: {["|".join(BACKENDS.keys())]}: ')

    params_list = BACKENDS[backend].get('params')
    params = dict()

    for param in params_list:
        params[param] = input(f'Enter a value for {param}: ')

    config_file = input('\nLast step! Name your configuration file [default config.yaml]: ')
    config_file = config_file if config_file != '' else 'config.yaml'

    config = {
        'twitter': {
            'consumer_key': consumer_key,
            'consumer_secret': consumer_secret,
            'access_token': access_token,
            'access_token_secret': access_token_secret
        },
        'backend': backend,
        'backend_params': params
    }
    with open(config_file, 'w') as f:
        yaml.dump(config, f)

    click.echo(f'Done! Your configuration {config_file} has been created')
