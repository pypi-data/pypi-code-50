import os
from bs4 import BeautifulSoup
import yaml
from telegram_util import matchKey
import cached_url
from datetime import date
import re

LINK_PREFIX = 'https://t.me/s/'

def findSrc(raw):
	pivot1 = "background-image:url('"
	index = raw.find(pivot1)
	raw = raw[index + len(pivot1):]
	pivot2 = "')"
	index = raw.find(pivot2)
	return raw[:index]

def findResource(source):
	soup = BeautifulSoup(cached_url.get(LINK_PREFIX + source), 'html.parser')
	name = soup.find('meta', {'property': 'og:title'})['content']
	links = {}
	for item in soup.find_all('a', class_='tgme_widget_message_link_preview'):
		if 'telegra.ph' not in item['href']:
			continue
		title = item.find('div', class_='link_preview_title').text
		links[item['href']] = title
	pics = []
	for item in soup.find_all('a', class_='tgme_widget_message_photo_wrap'):
		text = item.parent.find('div', class_='tgme_widget_message_text')
		src = findSrc(item['style'])
		img = '<figure><img src="%s"/></figure>' % src
		pics.append((img, text or ''))
	texts = []
	for item in soup.find_all('div', class_='tgme_widget_message_wrap'):
		if 'telegra.ph' in item.text:
			continue
		if item.find('a', class_='tgme_widget_message_photo_wrap'):
			continue
		preview = item.find('a', class_='tgme_widget_message_link_preview')
		if not preview:
			continue
		preview.name = 'div'
		text = item.find('div', class_='tgme_widget_message_text')
		texts.append((text, preview))
	return name, links, pics, texts

	
