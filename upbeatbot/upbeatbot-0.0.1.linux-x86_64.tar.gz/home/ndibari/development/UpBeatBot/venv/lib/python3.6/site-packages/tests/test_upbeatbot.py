import logging
import unittest
from unittest import mock

from requests import HTTPError

from upbeatbot.libs.upbeatbot import UpBeatBot


logging.disable(logging.CRITICAL)


class TestUpbeatBot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.upbeat_bot = UpBeatBot()

    @mock.patch('bs4.BeautifulSoup')
    @mock.patch('requests.get')
    def test_get_cute_animal_picture_happy_path(self, mock_request, mock_soup):
        expected_picture = 'https://cutestpaw.com/cat/happy-pic.jpg'

        mock_preview_soup = mock.Mock()
        mock_preview_soup.select.return_value = [{'href' : 'https://example.com'}]

        mock_picture_soup = mock.Mock()
        mock_picture_soup.select.return_value = [{'src': expected_picture}]

        mock_soup.side_effect = [mock_preview_soup, mock_picture_soup]

        mock_preview_response = mock.Mock()
        mock_image_response = mock.Mock()
        mock_request.side_effect = [mock_preview_response, mock_image_response]

        picture = self.upbeat_bot.get_cute_animal_picture()

        self.assertEqual(picture, expected_picture)

    @mock.patch('requests.get')
    def test_get_cute_animal_picture_fails_fetching_preview(self, mock_request):
        mock_response = mock.Mock()
        mock_response.raise_for_status.side_effect = HTTPError
        mock_request.return_value = mock_response

        picture = self.upbeat_bot.get_cute_animal_picture('cat')

        self.assertEqual(picture, self.upbeat_bot.animals['cat'])

    @mock.patch('bs4.BeautifulSoup')
    @mock.patch('requests.get')
    def test_get_cute_animal_picture_fails_fetching_image(self, mock_request, mock_soup):
        mock_preview_soup = mock.Mock()
        mock_preview_soup.select.return_value = [{'href' : 'https://example.com'}]
        mock_soup.return_value = mock_preview_soup

        mock_preview_response = mock.Mock()
        mock_image_response = mock.Mock()
        mock_image_response.raise_for_status.side_effect = HTTPError
        mock_request.side_effect = [mock_preview_response, mock_image_response]

        picture = self.upbeat_bot.get_cute_animal_picture('cat')

        self.assertEqual(picture, self.upbeat_bot.animals['cat'])

    def test_get_animal_from_message_chosen_animal_returned(self):
        tweet = 'Hey @upbeatbot send me a dog!'
        animal = self.upbeat_bot._get_animal_from_message(tweet)

        self.assertEqual(animal, 'dog')

    def test__get_animal_from_message_returns_None_if_no_animal_found(self):
        tweet = 'Hey @upbeatbot send me a pic!'
        animal = self.upbeat_bot._get_animal_from_message(tweet)

        self.assertIsNone(animal)
