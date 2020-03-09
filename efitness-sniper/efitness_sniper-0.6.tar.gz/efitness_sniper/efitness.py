import datetime
import json
import logging

import bs4
import requests


class LoginDataIncomplete(Exception):
    pass


class ClubEndpointEmpty(Exception):
    pass


class NotLoggedIn(Exception):
    pass


class Client:
    def __init__(self, club_subdomain: str, user: str, password: str) -> None:
        """Constructor of eFitness sniper

        Arguments:
            club_subdomain {str} -- Club subdomain (for ex. modelarnia-bb-cms if url is https://modelarnia-bb-cms.efitness.com.pl)
            login {str} --  user login
            password {str} -- user password
        """
        # Setup logger
        self.log = logging.getLogger(__name__)
        self.log.info("Creating new instance of efitness.Client with provided details")
        if club_subdomain:
            self.club_endpoint = f"https://{club_subdomain}.efitness.com.pl"
            self.club_subdomain = club_subdomain
        else:
            raise ClubEndpointEmpty("Please provide club subdomain")
        self.log.info(f"Using {self.club_endpoint} as a current eFitness endpoint.")
        # If password and user is not empty
        if user and password:
            self.user = user
            self.password = password
            self.logged_in = False  # Initially we are not logged in.
        else:
            raise LoginDataIncomplete("Please provide user and password!")
        # Setup requests session.
        self.session = requests.Session()
        self.log.info("Requests session created.")
        # Place to store current reservations cache
        self.reservations = {}

    def _post(self, location: str, data: dict = {}) -> bs4.BeautifulSoup:
        """Execute POST method to one of eFitness selected url
        
        Arguments:
            location {string} -- eFitness selected URL
        
        Keyword Arguments:
            data {dict} -- POST data that should be used in request (default: {{}})
        
        Returns:
            bs4.BeautifulSoup -- BeautifulSoup class with HTML data
        """
        self.log.debug(
            f"POST request to: {self.club_endpoint}{location} with data {data}"
        )
        response_data = bs4.BeautifulSoup(
            self.session.post(f"{self.club_endpoint}{location}", data=data,).text,
            "html.parser",
        )
        return response_data

    def _get(self, location: str) -> bs4.BeautifulSoup:
        """Execute GET method to one of eFitness selected url
        
        Arguments:
            location {string} -- eFitness selected URL
                
        Returns:
            bs4.BeautifulSoup -- BeautifulSoup class with HTML data
        """
        self.log.debug(f"GET request to: {self.club_endpoint}{location}")
        response_data = bs4.BeautifulSoup(
            self.session.get(f"{self.club_endpoint}{location}").text, "html.parser",
        )
        return response_data

    def login(self) -> bool:
        """Try login to eFitness platform

        Returns:
            dict -- Returns user data if login is successful
        """
        login_data = self._post(
            location="/Login/SystemLogin",
            data={"Login": self.user, "Password": self.password},
        )
        if login_data.find(class_="menucontainer"):
            login_name = " ".join(
                login_data.find(class_="menucontainer")
                .find(class_="modulebox")
                .find(class_="title")
                .string.split()[1:3]
            )
            self.log.info(f"Logged in as {login_name}")
            self.logged_in = True
            return True
        else:
            self.log.info(f"Provided login seems to be incorrect")
            return False

    def _update_reservations(self, html: bs4.BeautifulSoup) -> None:
        """Updates reservations cache
        
        Arguments:
            html {bs4.BeautifulSoup} -- HTML BeautifulSoup data to be parsed
        """
        for reservation in html.find_all("li"):
            # Get reservation time
            reservation_time = datetime.datetime.strptime(
                reservation.find("div").find("strong").text, "%d-%m-%Y - %H:%M"
            )
            # Get description
            description = (
                reservation.find("div")
                .text.strip()
                .split("\n")[0]
                .split(" - ")[-1]
                .strip()
            )
            if not reservation.find("a"):
                self.log.info(f"Skipping {description} - cancellation time runned out, cannot get SID")
                continue
            # Get meta:sid as this is training id in calendar
            meta_sid = int(reservation.find("a")["meta:sid"])
            reservation_data = {"time": reservation_time, "description": description}
            self.log.info(
                f"Reservation cache item {meta_sid} update with data: {reservation_data}"
            )
            self.reservations[meta_sid] = reservation_data

    def get_timetable_items(self, day: datetime.date) -> dict:
        """Get timetables for given days
        
        Arguments:
            day {datetime.date} -- Provide date which should be listed
        
        Returns:
            dict -- items that are available this day
        """
        # Init empty events dict
        events = {}
        if not self.logged_in:
            raise NotLoggedIn("Please invoke login first")
        # Get timetable data for selected day
        timetable = self._get(
            f"/kalendarz-zajec?day={day.strftime('%d-%m-%Y')}&view=DayByHour"
        )
        # This is good place to cache currently booked reservations
        self._update_reservations(timetable.find(id="calendar_registered_meetings"))
        # Go thru each entry, skip table header
        for item in timetable.find(class_="calendar_table calendar_table_day").find_all(
            "tr"
        )[1:]:
            # Get event hour
            event_time = datetime.datetime.combine(
                day,
                datetime.datetime.strptime(
                    item.find(class_="hour").text.strip(), "%H:%M"
                ).time(),
            )
            # Get event meta_sid
            event_id = int(item.find(class_="event")["meta:id"])
            # Get event description
            event_description = item.find(class_="event_name").text.strip()
            data = {"description": event_description, "time": event_time}
            self.log.info(f"Parsed event {event_id}: {data}")
            events[event_id] = data
        return events

    def book_events(self, matching_events: dict) -> None:
        """Books events provided in matching_events dict
        
        Arguments:
            matching_events {dict} -- Dict with events that should be booked
        """
        for event_sid, event_data in matching_events.items():
            # Get booking data
            booking_data = self._get(f"/schedule/showoverlay?schiid={event_sid}")
            # Get meta:mid needed for booking
            meta_member_id = int(
                booking_data.find(class_="button calendar-register-for-class")[
                    "meta:mid"
                ]
            )
            self.log.info(
                f"Found meta:mid for event ({event_data}) is {meta_member_id} - booking event."
            )
            # Running actual booking
            reservation_status = json.loads(
                str(
                    self._post(
                        "/Schedule/RegisterForClass",
                        data={"id": event_sid, "memberID": meta_member_id},
                    )
                )
            )
            self.log.info(
                f"Reservation {meta_member_id}/{event_id} POSTed. Booked: {reservation_status['Success']}"
            )

    def check_and_book(self, booking_rules: dict) -> dict:
        """Try to book workout for each provided rule
        
        Arguments:
            booking_rules {dict} -- booking rules dictionary
        
        Returns:
            dict -- new reservations added on this execution
        """
        # Empty timetable dict
        timetable = {}
        # Calculate how much days from today needs to be scraped - minimum 3
        max_look_ahead_days = 3
        for rule in booking_rules:
            if rule["look_ahead_days"] > max_look_ahead_days:
                max_look_ahead_days = rule["look_ahead_days"]
        # Generate timetable entries for given days
        for day in range(max_look_ahead_days):
            # We don't want to snip dates that should be already booked (or ones that are cancelled)
            if day >= 2:
                timetable.update(
                    self.get_timetable_items(
                        datetime.date.today() + datetime.timedelta(days=day)
                    )
                )
        matching_events = {}
        # Find rule matching events
        for rule in booking_rules:
            for event_sid, event_data in timetable.items():
                # Check if name from rule partially matches event name
                if rule["match"] in event_data["description"]:
                    # Check day of week
                    if event_data["time"].weekday() == rule["day_of_week"]:
                        # Check timeframe
                        start_time = datetime.datetime.strptime(
                            rule["after_hour"], "%H:%M"
                        ).time()
                        end_time = datetime.datetime.strptime(
                            rule["before_hour"], "%H:%M"
                        ).time()
                        if start_time < event_data["time"].time() < end_time:
                            # And finally remove items, that are already booked
                            if not event_sid in self.reservations:
                                self.log.info(
                                    f"Event {event_sid} ({event_data}) cached for reservation"
                                )
                                matching_events[event_sid] = event_data
                            else:
                                self.log.info(
                                    f"Event {event_sid} ({event_data}) already booked - skipping."
                                )
        # Book events calculated above
        self.book_events(matching_events)
        # Return matched events as dict
        return matching_events
