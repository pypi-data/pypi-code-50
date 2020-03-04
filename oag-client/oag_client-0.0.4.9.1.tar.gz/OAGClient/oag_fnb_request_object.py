REGISTER = 'register'
UNREGISTER = 'unregister'
ARRIVAL = 'arrival'
DEPARTURE = 'departure'

def create_fnb_request_string(*, action=None, endpoint=None, airport=None, aircraft_id=None, carrier=None, flight_number=None, year=None, month=None, day=None, time=None):
        action = "" if not action in ['register', 'unregister'] else "{}/".format(action)
        endpoint = "" if not endpoint in ['arrival', 'departure'] else "{}/".format(endpoint)
        airport = "" if airport == "" else "{}/".format(airport)
        aircraft_id = "" if not aircraft_id else "ACID/{}/".format(aircraft_id)
        carrier = "" if carrier == "" else "{}/".format(carrier)
        flight_number = "" if flight_number == "" else "{}/".format(flight_number)
        year = "" if year == "" else "{}/".format(year)
        month = "" if month == "" else "{}/".format(month)
        date = "" if day == "" else "{}/".format(day)
        time = "" if time == "" else "{}/".format(time)

        return "{}{}{}{}{}{}{}{}{}{}".format(action, endpoint, airport, aircraft_id, carrier, flight_number, year, month, date, time)