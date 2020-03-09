import json
from Lib.wrapper import IntraLib
from Lib.args import Args


class Student(IntraLib):
    """
    This class handles all student details that can be retrieved through the
    42 API.
    """
    def __init__(self):
        """
        Rules possibilities.
        """
        self.rules = ['id', 'email', 'displayname', 'image_url',
                    'correction_point', 'pool_month', 'login']
        super().__init__()

    def student_data(self, login, pretty=False):
        args = Args()
        response = self.api_get_single("/v2/users/" + str(login), "GET")
        details = response.content
        if pretty:
            return json.dumps(details, indent=4, sort_keys=True)
        return details