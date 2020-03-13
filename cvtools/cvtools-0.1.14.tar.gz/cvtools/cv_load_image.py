import requests
import cv2
import numpy as np

try:
    from urllib.parse import urlparse, parse_qs
except ImportError:
    from urlparse import urlparse, parse_qs


# To speed up downloading
cv_session = requests.Session()
cv_session.trust_env = False


def cv_load_image(in_, type_='path'):
    '''
    Return
        image: opencv format np.array. (C x H x W) in BGR np.uint8
    '''
    if type_ == 'url' or in_.startswith('http'):
        do_crop = False
        if "192.168" in in_:
            url = urlparse(in_)
            query = parse_qs(url.query)
            x = int(query.get("x", [-1])[0])
            y = int(query.get("y", [-1])[0])
            width = int(query.get("width", [0])[0])
            height = int(query.get("height", [0])[0])
            if x > -1:
                in_ = "http://{}{}".format(url.netloc, url.path.replace(".jpg", "").replace(".png", ""))
                do_crop = True
        img_nparr = np.frombuffer(cv_session.get(in_).content, np.uint8)
        img = cv2.imdecode(img_nparr, cv2.IMREAD_COLOR)
        if do_crop:
            img = img[y: y+height, x: x+width]
    else:
        img = cv2.imread(in_, cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION)
        # img = cv2.imread(in_)
    return img

if __name__ == "__main__":
    import sys
    import time
    st = time.time()
    img = cv_load_image(sys.argv[1])
    print(img.shape, time.time() - st)
