import os
import re
import requests


class LineNotify:

    API_URL = 'https://notify-api.line.me/api/notify'
    token = None

    def __init__(self, token):
        self.token = token

    def send(self, message, image_path=None, sticker=None):

        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }

        data = {'message': message}

        # send image
        files = None
        if image_path is not None:
            if re.search('^http', image_path):

                data['imageThumbnail'] = image_path
                data['imageFullsize'] = image_path

            elif os.path.isfile(image_path):

                files = {'imageFile': open(image_path, 'rb')}

        # send sticker
        if sticker is not None:
            # TODO: check key
            data['stickerPackageId'] = sticker['stickerPackageId']
            data['stickerId'] = sticker['stickerId']

        r = requests.post(self.API_URL, data=data,
                          headers=headers, files=files)

        if r.status_code != 200:
            return False

        resp = r.json()
        if 'status' not in resp.keys() or resp['status'] != 200:
            return False

        return True


def send(token, message, image_path=None, sticker=None):
    ln = LineNotify(token)
    return ln.send(message, image_path, sticker)
