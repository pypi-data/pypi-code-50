import facebook


class Facebook(object):
    """"""

    def __init__(self):
        self._facebook = None

    def connect(self, token):
        """Connect to Facebook using passed in Graph API token"""

        self._facebook = facebook.GraphAPI(token)

    def get_page_posts(self, page_id):
        """Get latest 100 posts from Facebook page feed"""
        page = self._facebook.get_object("{}/posts?limit=100".format(page_id))
        return page['data']

    def try_post(self, page_id, post_message):
        """Post message to Facebook feed."""
        try:
            self._facebook.put_object(page_id, "feed", message=post_message)
            return True, post_message
        except Exception as e:
            return False, str(e)
