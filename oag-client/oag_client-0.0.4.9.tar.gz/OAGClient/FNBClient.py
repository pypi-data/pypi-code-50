import requests
import json
from .flight_view_helper import convert_oag_status_to_normal_form, parse_date_time

class FNBClient:
    def __init__(self, app_id, app_key):
        self.URL = "https://fnb.flightview.com/"
        self.app_id = app_id
        self.app_key = app_key

    def make_request(self, fnb_request_object):
        post_body = {
            "RequestParameters": {
                "appid": self.app_id,
                "appkey": self.app_key
            }
        }
        request_url = self.URL + fnb_request_object
        print(request_url)

        response = requests.post(url=request_url, data=json.dumps(post_body))
        content = json.loads(response.content)


        if response.status_code == 200 and content['Success']:
            return content
        else:
            return {"error": response.status_code, "content": content}

    def parse_update(self, update_dict):
        flight = {
            'FlightIdentifier': {
                'AirlineCode': update_dict['FlightIdentifier']['AirlineCode'],
                'FlightNumber': update_dict['FlightIdentifier']['FlightNumber'],
                'DepartureAirportCode': update_dict['FlightIdentifier']['DepartureAirportCode'],
                'ArrivalAirportCode': update_dict['FlightIdentifier']['ArrivalAirportCode'],
                'SchedDepartureLocal': parse_date_time(update_dict['FlightIdentifier']['SchedDepartureLocal']),
            },
            'Alert': update_dict['Alert'],
            'Flight': {
                'fv_flight_id': update_dict['FlightData']['FvFlightId'],
                'airline_iata': update_dict['FlightData']['AirlineCode'],
                'number': update_dict['FlightData']['FlightNumber'],
                'origin_airport_code': update_dict['FlightData']['SchedDepartureAirportCode'],
                'dest_airport_code': update_dict['FlightData']['SchedArrivalAirportCode'],
                'status': convert_oag_status_to_normal_form(update_dict['FlightData']['Status'].lower()),
                'origin_scheduled_dep': parse_date_time(update_dict['FlightData']['SchedDepartureLocal']),
                'dest_scheduled_arrival': parse_date_time(update_dict['FlightData']['SchedArrivalLocal']),
                'origin_scheduled_dep_utc': parse_date_time(update_dict['FlightData']['SchedDepartureUtc']),
                'dest_scheduled_arrival_utc': parse_date_time(update_dict['FlightData']['SchedArrivalUtc']),
                'estimated_departure_accuracy': update_dict['FlightData']['LatestDeparture']['Accuracy'],
                'estimated_departure_utc': parse_date_time(update_dict['FlightData']['LatestDeparture']['DateTimeUtc']),
                'estimated_departure': parse_date_time(update_dict['FlightData']['LatestDeparture']['DateTimeLocal']),
                'estimated_arrival_accuracy': update_dict['FlightData']['LatestArrival']['Accuracy'],
                'estimated_arrival_utc': parse_date_time(update_dict['FlightData']['LatestArrival']['DateTimeUtc']),
                'estimated_arrival': parse_date_time(update_dict['FlightData']['LatestArrival']['DateTimeLocal']),
                'origin_terminal': update_dict['FlightData']['DepartureTerminal'],
                'dest_terminal': update_dict['FlightData']['ArrivalTerminal'],
                'origin_gate':  update_dict['FlightData']['DepartureGate'],
                'dest_gate': update_dict['FlightData']['ArrivalGate'],
                'dest_baggage': update_dict['FlightData']['Baggage'],
                'aircraft_type': update_dict['FlightData']['AircraftType'],
                'origin_country':  update_dict['FlightData']['DepAirportCountryId'],
                'dest_country': update_dict['FlightData']['ArrAirportCountryId'],
                'tail_number': update_dict['FlightData']['TailNumber'],
            },
            "AlertIdentifier": update_dict['AlertIdentifier'],
        }

        return flight

