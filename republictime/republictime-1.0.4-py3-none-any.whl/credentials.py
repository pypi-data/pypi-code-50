# Credential class here.
class Credentials(object):

    def __init__(self, apikey, url):
        self.apikey = apikey
        self.url = url

    def get_apikey(self):
        return self.apikey

    def get_url(self):
        return self.url

    def get_headers(self):
        return dict(authorization='Bearer ' + self.apikey)
