import json
import os
import requests
import sys

import dcyd.utils.constants as constants


def main(project_id=None):
    """Calls the account service to get credentials."""

    # main() needs to take no args, so that it functions as an entry point.
    if project_id is None:
        project_id = str(sys.argv[1])

    # Call the account service.
    r = requests.post(
        os.path.join(constants.DCYD_APP_BASE_URL, constants.CONFIG_ROUTE),
        json={'project_id': str(project_id)}
    )

    # Save the config data.
    with open(constants.CONFIG_FILE, 'w') as f:
        json.dump(r.json(), f)

    print("Project `{}` successfully configured.".format(project_id))
    print("Protect the configuration file `{}`.".format(constants.CONFIG_FILE))

if __name__ == '__main__':
    main()
