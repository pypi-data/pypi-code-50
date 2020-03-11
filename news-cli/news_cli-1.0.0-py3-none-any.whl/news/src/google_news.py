"""
Get google news

"""
import requests
from common.get_api import get_api


def __process_response(data):
    """
    process the response received from API

    :param data response from api
    :return:
    """

    res = []
    articles = data.get("articles")

    for i in range(len(articles)):
        node = articles[i]
        title = node.get("title")
        description = node.get("description")
        url = node.get("url")
        published_at = node.get("publishedAt")
        res.append((title, description, url, published_at))

    return res


def __find_sources(api_details, area):
    """

    :param api_details:
    :param area:
    :return:
    """
    if area.lower() in api_details.get("area"):
        return ",".join(api_details.get("area").get(area.lower()).get("sources"))
    else:
        return ",".join(api_details.get("sources"))


def __get_api_details(source, area=None):
    """
    Get api details

    :return:
    """
    api_details = get_api(source)
    if area is None:
        payload = {"sources": ",".join(api_details.get("sources")), "apiKey": api_details.get("api_key")}
    else:
        sources = __find_sources(api_details, area)
        payload = {"sources": sources, "apiKey": api_details.get("api_key")}

    url = api_details["url"]
    return payload, url


def get_headlines(area=None) -> list:
    """
    Get current headlines

    :param area
    :return:
    """
    path = "top-headlines/"
    payload, url = __get_api_details("newsapi", area)
    response = requests.get(url+path, params=payload)
    if response.status_code == 200:
        return __process_response(response.json())
    else:
        return []


def get_keyword_news(keyword) -> list:
    """
    Get current headlines

    :return:
    """
    path = "everything/"
    payload, url = __get_api_details("newsapi")
    payload["q"] = keyword
    payload["sortBy"] = "popularity"
    response = requests.get(url+path, params=payload)
    if response.status_code == 200:
        return __process_response(response.json())
    else:
        return []