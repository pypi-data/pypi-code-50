import json
import os
import requests
import sys

import dcyd.utils.constants as constants


def main(project_id=None):
    """Calls the config service to get credentials."""

    # main() needs to take no args, so that it functions as an entry point.
    if project_id is None:
        project_id = sys.argv[1]

    # Call the config service.
    r = requests.post(
        os.path.join(constants.DCYD_API_URL, constants.CONFIG_ROUTE),
        json={'project_id': project_id}
    )

    # Save the config data. Need to add prefix `mpm_` to distinguish it from the
    # GCP project_id. Totally internal.
    config = r.json()
    config.update({'mpm_project_id': project_id})

    with open(constants.CONFIG_FILE, 'w') as f:
        json.dump(config, f)

    print("Project `{}` successfully configured.".format(project_id))
    print("Protect the configuration file `{}`.".format(constants.CONFIG_FILE))
