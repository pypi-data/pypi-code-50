from __future__ import print_function
from builtins import str
import requests
import json
import argparse


def main():
    """
    This function retrieves all sensors from the host, and generates or updates all bins for them.
    The user needs to have master permissions in the geostreams service to be able to generate the bins.\

    Arguments:
        host - the url for the geostreams service. Example: http://seagrant-dev.ncsa.illinois.edu:9002/geostreams
        username - user with master permission in geostream service
        password - password for user in geostream service
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="host url",
                        default="http://localhost:9000/")
    # Sample URL to go around nginx
    # - nginx times out the request because it takes longer than 5 seconds
    # - "http://seagrant-dev.ncsa.illinois.edu:9002/geostreams")
    parser.add_argument('-u', '--user', help="Geostreams username")
    parser.add_argument('-p', '--password', help="Geostreams password")

    args = parser.parse_args()
    host = args.host
    username = args.user
    password = args.password

    user = {'identifier': username, 'password': password}
    r = requests.post(host + '/api/authenticate',
        data=json.dumps(user), headers={'Content-Type':'application/json'})

    if r.status_code == 200:
        r.headers["Content-Encoding"] = "application/json"

        sensors = requests.get(host + "/api/sensors")
        sensors_json = json.loads(sensors.text)
        parsed_sensors = sensors_json["sensors"]

        for sensor in parsed_sensors:
            sensor_id = sensor["id"]
            endpoint = host + '/api/cache?sensor_id=' + str(sensor_id)
            s = requests.post(endpoint, headers=r.headers)
            print("Cache created for sensor with id: " + str(sensor_id))


if __name__ == "__main__":
    main()
