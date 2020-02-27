import requests
from datetime import datetime
from django.conf import settings

AUTHORIZATION = settings.LINE_NOTIFY_TOKEN
LINE_NOTIFY_API = settings.LINE_NOTIFY_API

class LINENotify:

    @staticmethod
    def notify_hook(subtitle, data=None, **kwargs):
        if data and type(data) == dict:
            message_temp = make_message_from_dict(data=data)
        elif kwargs and not data:
            message_temp =  make_message_from_dict(data=kwargs)
        else:
            raise ValueError("Datatype of value must be dictionary type or you can use **kwargs")

        message_temp = "".join([str(m) for m in message_temp])
        message = f"{subtitle}\n\n{message_temp}"

        try:
            request = requests.post(LINE_NOTIFY_API, data={'message': message}, headers={'Authorization': AUTHORIZATION},)
        except:
            return request
        return request

def make_message_from_dict(data):
    message = []
    for key, val in data.items():
        message.append(f"{key} : {val}\n")
    return message

def generate_notify_data(obj, key_type="id", header=None):
    data = {}
    _type = None
    try:
        if key_type == "id":
            data["Order ID"] = obj.id
            _type = obj.id
        elif key_type == "slug":
            _type = obj.slug
            data["Order ID"] = obj.slug
        data["name"] = obj.first_name
        data["email"] = obj.email
        data["created_at"] = datetime.now()
        if header:
            data["url"] = f"{header}/{_type}"
    except:
        raise
    return data