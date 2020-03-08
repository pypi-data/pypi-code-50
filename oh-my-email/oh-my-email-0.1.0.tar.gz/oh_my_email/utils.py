# coding:utf-8
"""
description: 
author: jiangyx3915
date: 2020-03-05
"""
import base64
import requests
from typing import List
from bs4 import BeautifulSoup
from oh_my_email.exception import DownloadResourceException


def _serialize_contacts(contacts: List["OhMyEmailContact"]) -> List[str]:
    return [item.render() for item in contacts]


def _serialize_contacts2str(contacts: List["OhMyEmailContact"]) -> str:
    return ','.join(_serialize_contacts(contacts=contacts))


def analyze_html_img(html):
    return [img.get('src') for img in BeautifulSoup(html, "lxml").find_all("img")]


def img2base64(img_url):
    result = requests.get(img_url)
    if result:
        return str(base64.b64encode(result.content), encoding='utf-8')
    raise DownloadResourceException(f"Download Img {img_url} error")