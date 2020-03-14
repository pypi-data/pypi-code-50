import requests
import traceback
from lxml import etree


def get_title(url):
    headers = {
        'user-agent': 'Mozilla/5.0+(Windows+NT+6.2;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/45.0.2454.101+Safari/537.36'}
    title = None
    try:
        res = requests.get(url, headers=headers, timeout=5)
        res.encoding = 'utf-8'
        response = etree.HTML(res.text)
        title = response.xpath('//title/text()')
        if len(title) != 0:
            title = title[0]
        else:
            title = None
    except:
        traceback.print_exc()
    finally:
        return title

if __name__ == '__main__':
    title = get_title(url='https://www.baidu.com')
    print(title)
