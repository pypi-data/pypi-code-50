from datetime import datetime as dt
import logging
import sys
from time import sleep

import requests
import twitter

from upbeatbot import settings
from upbeatbot.libs.api_mock import TwitterAPIMock
from upbeatbot.libs.upbeatbot import UpBeatBot

logging.basicConfig(filename=settings.LOG_FILE, level=logging.INFO)


# Debug config
DEBUG = '--debug' in sys.argv or settings.DEBUG


def connect_api():
    return twitter.Api(
        settings.CONSUMER_KEY,
        settings.CONSUMER_SECRET,
        settings.ACCESS_TOKEN,
        settings.ACCESS_TOKEN_SECRET
    )


def main():
    tweet_text = 'Hey @{0}, hope this brightens your day!'
    pass_number = 0
    upbeat_bot = UpBeatBot(debug=DEBUG)

    while True:
        time = dt.now().strftime('%b %d, %Y @ %H:%M:%S')
        pass_info = ' --Pass: {0} | {1}--'.format(pass_number, time)
        logging.info(pass_info)

        try:
            if DEBUG:
                conx = TwitterAPIMock()
            else:
                conx = connect_api()

            logging.info(' Connected to API OK')
            mentions = conx.GetMentions()

            if mentions:
                logging.info(' Got {0} mentions'.format(len(mentions)))

                for mention in mentions:
                    user = mention.user.screen_name

                    if not mention.favorited:
                        logging.info(' Gonna tweet @{0}'.format(user))
                        logging.info(' User tweet: {}'.format(mention.text))

                        text = tweet_text.format(user)
                        img = upbeat_bot.get_cute_animal_picture(mention.text)

                        # Don't actually tweet the test account
                        if user != 'upbeatbottest':
                            conx.PostUpdate(text, img)
                            logging.info(' Tweeted @{0} OK'.format(user))

                        conx.CreateFavorite(status=mention)

                    else:
                        logging.info(' Already tweeted @{0}'.format(user))

            else:
                logging.info(' Got no mentions')

        except requests.exceptions.ConnectionError as conn_error:
            error_type = type(conn_error)
            url = conn_error.request.url

            logging.exception(
                ' Caught exception {type} trying to reach url: {url} \n'
                ' Full traceback:'.format(
                    type=error_type,
                    url=url
                )
            )

        except Exception:
            logging.exception(
                ' Unhandled exception at pass: {pass_number} \n'
                ' Full traceback:'.format(
                    pass_number=pass_number
                )
            )

        logging.info(' Going to sleep for {}s..'.format(settings.SLEEP_TIMEOUT))
        sleep(settings.SLEEP_TIMEOUT)
        logging.info(' Waking up!')
        logging.info(' -----------------')
        pass_number += 1


if __name__ == '__main__':
    main()
