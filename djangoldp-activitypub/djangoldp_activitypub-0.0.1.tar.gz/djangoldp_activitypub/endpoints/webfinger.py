import re
from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import Resolver404

from djangoldp.endpoints.webfinger import WebFinger
from djangoldp.models import Model

ACCT_RE = re.compile(
    r'(?:acct:)?(?P<userinfo>[\w.!#$%&\'*+-/=?^_`{|}~]+)@(?P<host>[\w.:-]+)')


class Acct(object):
    def __init__(self, acct):
        m = ACCT_RE.match(acct)
        if not m:
            raise ValueError('invalid acct format')
        (userinfo, host) = m.groups()
        self.userinfo = userinfo
        self.host = host


class APWebFinger(WebFinger):

    def response(self, response_dict, rel, acct):
        if rel is None or "self" in rel:
            user = get_user_model().objects.filter(email="{}@{}".format(acct.userinfo, acct.host)).first()
            if user is not None:
                self.add_user_infos(response_dict, user)
            elif acct.host == urlparse(settings.SITE_URL).hostname:
                user = get_user_model().objects.filter(username=acct.userinfo).first()
                if user is not None:
                    self.add_user_infos(response_dict, user)
                else:
                    container = acct.userinfo
                    try:
                        model = Model.resolve_container(container)
                        href = self.uri(model.get_container_path())
                        self.add_webfinger_infos(href, response_dict)
                    except Resolver404:
                        pass

        return response_dict

    def add_webfinger_infos(self, href, response_dict):
        response_dict['aliases'].append(href)
        response_dict['links'].append({
            'rel': "self",
            'type': "application/activity+json",
            'href': href
        })

    def add_user_infos(self, response_dict, user):
        href = self.uri(Model.resource_id(user))
        self.add_webfinger_infos(href, response_dict)
