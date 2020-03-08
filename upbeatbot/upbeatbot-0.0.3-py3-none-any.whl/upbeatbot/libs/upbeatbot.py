import logging
import random
import string

import bs4
import requests
from requests import HTTPError

from upbeatbot import settings
from upbeatbot.libs.api_mock import RequestsMock


class UpBeatBot(object):
    """Source of uplifting media"""

    # List of animals we support in our system
    # Value is a fallback picture to use in case of issues connecting to cutestpaw.com
    animals = {
        'bunnies': 'http://www.cutestpaw.com/wp-content/uploads/2016/02/Baby-bunnies.jpg',
        'bunny': 'http://www.cutestpaw.com/wp-content/uploads/2016/02/The-teeniest-bunny..jpeg',
        'cat': 'http://www.cutestpaw.com/wp-content/uploads/2016/02/Cats-rule-and-dogs-drool.jpeg',
        'cats': 'http://www.cutestpaw.com/wp-content/uploads/2015/10/Amazing-colored-baby-cats-and-mama-cat.jpg',
        'chinchilla': 'http://www.cutestpaw.com/wp-content/uploads/2014/05/Chinchilla-dust-storm.jpg',
        'chinchillas': 'http://www.cutestpaw.com/wp-content/uploads/2014/09/Baby-chinchillas.jpg',
        'chipmunk': 'http://www.cutestpaw.com/wp-content/uploads/2016/02/Chipmunk-cheeks.jpg',
        'chipmunks': 'http://www.cutestpaw.com/wp-content/uploads/2015/01/chipmunks.jpg',
        'dog': 'http://www.cutestpaw.com/wp-content/uploads/2016/02/Waooo-so-happy.jpg',
        'dogs': 'http://www.cutestpaw.com/wp-content/uploads/2015/06/rgrrrrr.jpg',
        'kitten': 'http://www.cutestpaw.com/wp-content/uploads/2016/02/The-big-leap..jpg',
        'kittens': 'http://www.cutestpaw.com/wp-content/uploads/2016/02/Double-trouble..jpg',
        'otter': 'http://www.cutestpaw.com/wp-content/uploads/2015/02/A-sea-otter.jpg',
        'otters': 'http://www.cutestpaw.com/wp-content/uploads/2012/01/Show-some-love-for-baby-otters.jpg',
        'pug': 'http://www.cutestpaw.com/wp-content/uploads/2015/10/This-pug-who-wants-you-to-get-out-of-this-car.jpg',
        'pugs': 'http://www.cutestpaw.com/wp-content/uploads/2013/02/Baby-pugs.jpg',
        'squirrel': 'http://www.cutestpaw.com/wp-content/uploads/2015/03/squirrel.jpg',
        'squirrels': 'http://www.cutestpaw.com/wp-content/uploads/2015/08/The-squirrel-savior..jpg',
    }

    def __init__(self, debug=settings.DEBUG):
        if debug:
            self.request = RequestsMock()
        else:
            self.request = requests

    def get_cute_animal_picture(self, message=None):
        """
        Return a link to a cute picture of an animal. If a message is provided, will try to parse the message for an
        animal we have registered and try to find a picture of the animal. If the message does not contain an animal
        we have registered, or is not provided, will search for a random animal from our choices.
        :param message: (str) Optional message to parse to determine what animal to search for
        :return: (str) Link to an image of a cute animal
        """
        animal = None

        if message:
            animal = self._get_animal_from_message(message)

        if animal is None:
            animal = random.choice(list(self.animals.keys()))

        animal_url = 'http://www.cutestpaw.com/?s={0}'.format(animal)
        preview_resp = self.request.get(animal_url)

        try:
            preview_resp.raise_for_status()
        except HTTPError:
            logging.warning(' Unable to fetch URL: {}'.format(animal_url), exc_info=True)
            return self.animals[animal]

        preview_soup = bs4.BeautifulSoup(preview_resp.text, 'html.parser')

        # Get random picture from preview page
        photos = preview_soup.select('#photos a')
        choice = random.choice(photos)

        picture_resp = self.request.get(choice['href'])

        try:
            picture_resp.raise_for_status()
        except HTTPError:
            logging.warning(' Unable to fetch URL: {}'.format(choice['href']), exc_info=True)
            return self.animals[animal]

        picture_soup = bs4.BeautifulSoup(picture_resp.text, 'html.parser')

        # Parse picture page for image
        img = picture_soup.select('#single-cute-wrap img')
        link = img[0]['src']

        return link

    def _get_animal_from_message(self, message):
        """
        Given a message (tweet, comment, post, etc.) parse the string to find if the message contains an animal in
        our choices list. If we can't find an animal from our choices in the text, return None
        :param message: (str) Text to search for an animal we have registered
        :return: (mixed) Animal to search for if found in message, None if no animal was found
        """
        animal = None

        for char in string.punctuation:
            message = message.replace(char, '')

        for word in message.split(' '):
            if word in self.animals.keys():
                animal = word
                break

        return animal
