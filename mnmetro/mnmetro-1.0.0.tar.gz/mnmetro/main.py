import json
import sys

import requests

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

base_url = "http://svc.metrotransit.org/NexTrip/"

direction_value = {
    1: "Southbound",
    2: "Eastbound",
    3: "Westbound",
    4: "Northbound"
}


class GetProviders(object):
    """
    From the API docs: Returns a list of area Transit providers. Providers are identified in the list of Routes allowing routes to be selected for a single provider.
    """

    def __init__(self):
        self.name = "Providers"

    def all_providers(self):
        try:
            data = requests.get(url=f"{base_url}{self.name}", headers=headers).json()
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        providers = {}

        for provider in data:
            providers[int(provider['Value'])] = provider['Text']

        return providers

    
    def provider_for(self, id=None, name=None):
        if all(value is None for value in {name, id}):
            raise ValueError("Expected either 'name' or 'id' for provider.")
        elif all(value is not None for value in {name, id}):
            raise ValueError("Expected either 'name' or 'id' for provider, not both.")

        providers = self.all_providers()

        if id is not None:
            if id in providers.keys():
                return providers[id]         
            else:
                raise ValueError(f"There is no provider named {name} in the providers available.")
        else:
            if name in providers.values():
                for key, value in providers.items():
                    if value == name:
                        return key
            else:
                raise ValueError(f"There is no provider id {id} in the providers available.")


class GetRoutes(object):
    """
    From the API docs: Returns a list of Transit routes that are in service on the current day.
    """

    def __init__(self):
        self.name = "Routes"

    def all_routes(self):
        try:
            r = requests.get(url=f"{base_url}{self.name}", headers=headers).json()
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        data = []

        # Force the ID's for provider and route to be ints not str
        for route in r:
            data.append({
                "Description":route["Description"],
                "ProviderID":int(route["ProviderID"]),
                "Route":int(route["Route"])
            })


        return data

    def route_ids(self):
        try:
            data = self.all_routes()
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        route_ids = []

        for route in data:
            route_ids.append(route["Route"])

        route_ids.sort()

        return route_ids

    def route_for(self, route_id):
        if not hasattr(route_id, "__pow__"):
            raise TypeError(f"{type(route_id)} is an unsupported operand. Should be an int.")

        try:
            data = self.all_routes()
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        for item in data:
            if item["Route"] == route_id:
                return item
        return f"The provided route_id: {route_id} does not appear in the Routes."


class GetDirections(object):
    def __init__(self):
        self.name = "Directions"
    
    def direction_for(self, route_id):
        if not hasattr(route_id, "__pow__"):
            raise TypeError(f"{type(route_id)} is an unsupported operand. Should be an int.")

        data = requests.get(url=f"{base_url}{self.name}/{route_id}", headers=headers).json()

        if len(data) != 0:
            directions = {
                data[0]["Text"]:int(data[0]["Value"]),
                data[1]["Text"]:int(data[1]["Value"])
            }
        else:
            raise ValueError(f"{route_id} is not a valid Route ID.")
        
        return directions


class GetStops(object):
    def __init__(self):
        self.name = "Stops"

    def full_stops_for(self, route_id):
        if not hasattr(route_id, "__pow__"):
            raise TypeError(f"{type(route_id)} is an unsupported operand. Should be an int.")

        data = GetDirections().direction_for(route_id)

        total_stops = {}

        for item in data.values():
            data = requests.get(url=f"{base_url}{self.name}/{route_id}/{item}", headers=headers).json()

            if len(data) != 0:
                stops_dict = {}
                
                for stops in data:
                    stops_dict[stops["Text"]] = stops["Value"]
        
                temp_value = stops_dict
            else:
                raise Exception(f"Looks to be an incorrect direction({self.direction}) or route_id({self.route_id})")

            total_stops[direction_value[item]] = temp_value

        return total_stops

    def stops_for(self, route_id, direction):
        data = requests.get(url=f"{base_url}{self.name}/{route_id}/{direction}", headers=headers).json()

        if len(data) != 0:
            stops_dict = {}
            
            for stops in data:
                stops_dict[stops["Text"]] = stops["Value"]
    
            return stops_dict
        else:
            raise Exception(f"Looks to be an incorrect direction({self.direction}) or route_id({self.route_id})")


class GetDepartures(object):
    """
    From the API docs: This operation is used to return a list of departures scheduled for any given bus stop. A StopID is an integer value identifying any one of the many thousands of bus stops in the metro. Stop information can be derived from the GTFS schedule data updated weekly for public use. https://gisdata.mn.gov/dataset/us-mn-state-metc-trans-transit-schedule-google-fd
    """

    def __init__(self):
        pass

    def departure_for(self, stop_id):
        self.stop_id = stop_id

        data = requests.get(url=f"{base_url}{self.stop_id}", headers=headers).json()

        if len(data) == 0:
            raise Exception(f"Looks to be an incorrect direction({self.direction}) or route_id({self.route_id})")
        else:
            return data


class GetTimepointDepartures(object):
    def __init__(self):
        pass

    def times_for(self, route_id, direction, node_id):
        self.route_id = route_id
        self.direction = direction
        self.node_id = node_id

        data = requests.get(url=f"{base_url}{self.route_id}/{self.direction}/{self.node_id}", headers=headers).json()

        if len(data) == 0:
            raise Exception(f"Looks to be an incorrect direction({self.direction}) or route_id({self.route_id}) and or node_id({self.node_id})")
        else:
            return data


class GetVehicleLocations(object):
    """
    From the API docs: This operation returns a list of vehicles currently in service that have recently (within 5 minutes) reported their locations. A route paramter is used to return results for the given route. Use "0" for the route parameter to return a list of all vehicles in service.
    """

    def __init__(self):
        self.name = "VehicleLocations"
        self.route_id = 0

    def all_vehicles(self):
        return requests.get(url=f"{base_url}{self.name}/{self.route_id}", headers=headers).json()

    def location_for(self, route_id):
        self.route_id = route_id
        return requests.get(url=f"{base_url}{self.name}/{self.route_id}", headers=headers).json()
