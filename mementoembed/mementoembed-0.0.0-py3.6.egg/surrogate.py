from bs4 import BeautifulSoup

class Surrogate:
    """
        Surrogate generates and stores all information about surrogates
        related to content, uri, and response_headers.
    """

    def __init__(self, uri, content, response_headers):

        self.uri = uri
        self.content = content
        self.response_headers = response_headers

        self.soup = BeautifulSoup(self.content, "html5lib")

        self.text_snippet_string = None
        self.striking_image_uri = None
        self.title_string = None

    @property
    def text_snippet(self):
        if self.text_snippet_string == None:

            self.text_snippet_string = self._getMetadataDescription()

            if self.text_snippet_string == None:

                self.text_snippet_string = self._getMetadataOGDescription()

                if self.text_snippet_string == None:

                    self.text_snippet_string = self._getMetadataTwitterDescription()

        return self.text_snippet_string

    @property
    def striking_image(self):
        
        if self.striking_image_uri == None:

            self.striking_image_uri = self._getMetadataOGImage()

            if self.striking_image_uri == None:

                self.striking_image_uri = self._getMetadataTwitterImage()

        return self.striking_image_uri

    @property
    def title(self):

        if self.title_string == None:
            self.title_string = self.soup.title.string

        return self.title_string

    def _getMetadataDescription(self):

        description = None

        for metatag in self.soup.find_all("meta"):
            if metatag.get("name") == "description":
                description = metatag.get("content")

        return description

    def _getMetadataOGDescription(self):

        description = None

        for metatag in self.soup.find_all("meta"):
            if metatag.get("property") == "og:description":
                description = metatag.get("content")

        return description

    def _getMetadataTwitterDescription(self):

        description = None

        for metatag in self.soup.find_all("meta"):
            if metatag.get("name") == "twitter:description":
                description = metatag.get("content")

        return description
        
    def _getMetadataOGImage(self):

        imageurl = None

        for metatag in self.soup.find_all("meta"):
            if metatag.get("property") == "og:image":
                imageurl = metatag.get("content")

        return imageurl

    def _getMetadataTwitterImage(self):

        imageurl = None

        for metatag in self.soup.find_all("meta"):
            if metatag.get("name") == "twitter:image:src":
                imageurl = metatag.get("content")

        return imageurl
        

