import json
from Lib.wrapper import IntraLib
from Lib.args import Args


class Campus(IntraLib):
    """
    This class handles all campus users that can be retrieved through the
    42 API.
    """
    def __init__(self):
        """
        Rules possibilities.
        """
        self.rules = ['id', 'login', 'url']
        super().__init__()

    def get_campus_users(self, cursus_id, **options):
        args = Args()
        #print (cursus_id)
        options["rules"] = self.rules
        if args.hydrate_values(options) is False:
            raise ValueError("Options couldn't be extracted.")
        # if cursus_id == "kh":
        #     users = self.api_get("/v2/campus/16/users", args, "GET")
        # elif cursus_id == "bg":
        users = self.api_get("/v2/campus/" + str(cursus_id) + "/users", args, "GET")
        # else:
        #     raise ValueError("Values must be either kh or bg.")
        if options.get("pretty", False):
            return json.dumps(users, indent=4, sort_keys=True)
        return users