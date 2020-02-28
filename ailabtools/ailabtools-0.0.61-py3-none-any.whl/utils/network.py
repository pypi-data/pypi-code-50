from PIL import Image
import io
import numpy as np
import urllib.request as urllib_request
from io import BytesIO
import time

def download_img_file(url, retry=0, retry_gap=0.1, proxy=None):
    if proxy == None:
        proxies={}
    else:
        proxies = {'http': proxy, 'https': proxy}
    try:
        proxy_handler = urllib_request.ProxyHandler(proxies)
        opener = urllib_request.build_opener(proxy_handler)
        img = Image.open(BytesIO(opener.open(url).read())).convert('RGB')
        return img
    except Exception as e:
        if retry > 0:
            time.sleep(retry_gap)   
            return download_img_file(url, retry=retry-1, proxy=proxy)
        else:
            return None