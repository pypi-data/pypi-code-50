import re


class TextTools():
    """ """

    def clean_text(self, text):
        """Clean text with only characters and numbers."""
        text = re.sub(r'[^\w]', '', text).lower()
        return text

    def get_subdomain(self, host):
        return host.replace('www.', '').split('.')[0]
