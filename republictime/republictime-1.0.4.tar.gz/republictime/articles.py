import requests
from republictime.credentials import Credentials


class Article(Credentials):

    def __init__(self, data=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if data.lower() == "djangopost":
            self.data = "post/"
        else:
            self.data = "article/"
        self.endpoint = self.data + "api/article/"
        self.list = "all/"
        self.url = self.url + self.endpoint + self.list
        try:
            self.request = requests.get(self.url, headers=self.get_headers())
        except requests.exceptions.RequestException as e:
            print(e)
        else:
            self.response = self.request.json()
        self.articles = []

    def get_article(self, promoted=None, trending=None):
        if self.request.status_code == 200:
            if promoted and trending:
                self.articles.clear()
                for article in self.response:
                    if article['is_promote'] and article['is_trend']:
                        self.articles.append(article)
                return self.articles
            elif promoted and trending is None:
                self.articles.clear()
                for article in self.response:
                    if article['is_promote']:
                        self.articles.append(article)
                return self.articles
            elif promoted is False and trending is None:
                self.articles.clear()
                for article in self.response:
                    if article['is_promote'] is False:
                        self.articles.append(article)
                return self.articles
            elif trending and promoted is None:
                self.articles.clear()
                for article in self.response:
                    if article['is_trend']:
                        self.articles.append(article)
                return self.articles
            self.articles.clear()
            return self.response
        else:
            return self.response
