
class Job(object):
    """ """

    def __init__(self, description, url, company=''):
        self.description = description
        self.url = url
        self.company = company

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (
                self.description == other.description and
                self.url == other.url and
                self.company == other.company)

        return False

    def __str__(self):
        return "{0} {1} {2}".format(self.description, self.url, self.company)

    def __repr__(self):
        return "description={0} url={1} company={2}".format(
            self.description, self.url, self.company)
