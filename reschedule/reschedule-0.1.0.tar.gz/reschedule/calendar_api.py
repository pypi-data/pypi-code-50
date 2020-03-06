"""Methods for using the google calendar api."""
import os
import pickle
import typing as t
from datetime import datetime, timedelta

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from .config import (
    SCOPES,
    task_calendar_name,
)
from .models import (
    CalendarResource,
    EventResource,
    FreeBusyResponse,
    ListCalendar,
    ListCalendarResponse,
)
from .time_helpers import (
    beginning_of_day_utc,
    datetime_to_index,
    end_of_day_utc,
    now_utc,
    parse_rfc_33339,
    total_indices_per_day,
    work_start_utc,
    work_end_utc,
)


def local_file_path(filename):
    return os.path.abspath(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)
    )


def get_google_api_credentials():
    """Get credentials for accessing the google api."""
    credentials = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(local_file_path("token.pickle")):
        with open(local_file_path("token.pickle"), "rb") as token:
            credentials = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                local_file_path("credentials.json"), SCOPES,
            )
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(local_file_path("token.pickle"), "wb") as token:
            pickle.dump(credentials, token)
    return credentials


class CalendarAPI(object):
    def __init__(self):
        super().__init__()
        # service used to access google calendar api
        self.service = build("calendar", "v3", credentials=get_google_api_credentials())
        self._task_cal = None
        self._list_cals = None

    def get_task_calendar(self) -> ListCalendar:
        if self._task_cal is not None:
            return self._task_cal
        # get all existing calendars
        existing_calendars = self.get_calendar_list_calendars()
        # if one already exists return it
        for existing_task_cal in filter(
            lambda c: c["summary"] == task_calendar_name, existing_calendars
        ):
            self._task_cal = existing_task_cal
            return existing_task_cal
        else:
            # otherwise create a new calendar
            calendar: CalendarResource = {
                "summary": task_calendar_name,  # title of the calendar
                "description": "Events generated from my todo.md file",  # calendar description
                "timeZone": "America/New_York",
            }
            created_calendar: CalendarResource = self.service.calendars().insert(
                body=calendar
            ).execute()
            # insert the new calendar in the calendar list
            calendar_list_entry = ListCalendar(id=created_calendar["id"], selected=True)
            created_calendar_list_entry = (
                self.service.calendarList().insert(body=calendar_list_entry).execute()
            )
            self._task_cal = created_calendar_list_entry
            # reset list cals since we added to the calendar list
            self._list_cals = None
            return created_calendar_list_entry

    def get_calendar_list_calendars(self) -> t.List[ListCalendar]:
        """Get all the calendars from the user's calendar list."""
        if self._list_cals is not None:
            return self._list_cals
        all_calendars: t.List[ListCalendar] = []
        page_token = None
        while True:
            calendar_list: ListCalendarResponse = self.service.calendarList().list(
                pageToken=page_token, showHidden=True
            ).execute()
            for calendar_list_entry in calendar_list["items"]:
                all_calendars.append(calendar_list_entry)
            page_token = calendar_list.get("nextPageToken")
            if not page_token:
                break
        self._list_cals = all_calendars
        return all_calendars

    def get_events_from_task_calendar(self) -> t.List[EventResource]:
        all_events: t.List[EventResource] = []
        page_token = None
        while True:
            events = (
                self.service.events()
                .list(
                    calendarId=self.get_task_calendar()["id"],
                    pageToken=page_token,
                    timeZone="UTC",
                    showDeleted=True,
                )
                .execute()
            )
            for event in events["items"]:
                all_events.append(event)
            page_token = events.get("nextPageToken")
            if not page_token:
                break
        return all_events

    def get_visible_calendar_list_calendars(self):
        """Get only those calendars displayed on the user's calendar list."""
        all_calendars = self.get_calendar_list_calendars()
        return [c for c in all_calendars if not c.get("hidden", False)]

    # chunk size in minutes
    def get_busy_array_for_day(self, day_offset: int) -> t.List[bool]:
        # query gcal for free busy results
        timeMin = beginning_of_day_utc(day_offset).isoformat()
        timeMax = end_of_day_utc(day_offset).isoformat()
        free_busy_result: FreeBusyResponse = (
            self.service.freebusy()
            .query(
                body={
                    "timeMin": timeMin,
                    "timeMax": timeMax,
                    "items": [
                        # query all calendars except the task cal
                        {"id": c["id"]}
                        for c in self.get_visible_calendar_list_calendars()
                        if c["summary"] != task_calendar_name
                    ],
                }
            )
            .execute()
        )

        # add free busy results to intervals
        intervals = []
        for c in free_busy_result["calendars"].values():
            for sb in c["busy"]:
                start = parse_rfc_33339(sb["start"])
                end = parse_rfc_33339(sb["end"]) - timedelta(minutes=1)
                intervals.append([start, end])
        # busy from beginning of day to work start time
        intervals.append(
            [
                beginning_of_day_utc(day_offset),
                work_start_utc(day_offset) - timedelta(minutes=1),
            ]
        )
        # busy from work end time to end of day
        intervals.append([work_end_utc(day_offset), end_of_day_utc(day_offset)])

        # busy from beginning of day until now
        if beginning_of_day_utc(day_offset) < now_utc():
            intervals.append([beginning_of_day_utc(day_offset), now_utc()])

        # create an array
        busy = [False] * total_indices_per_day()
        for start, end in intervals:
            # mark times between start and end as busy
            index_start = datetime_to_index(start, day_offset)
            index_end = datetime_to_index(end, day_offset)
            for i in range(index_start, index_end + 1):
                busy[i] = True

        return busy

    def delete_event_from_task_calendar(self, event_id: str):
        self.service.events().delete(
            calendarId=self.get_task_calendar()["id"], eventId=event_id
        ).execute()

    def schedule_task(
        self,
        description: str,
        event_id: str,
        start: datetime,
        end: datetime,
        patch: bool,
    ):
        event_body = {
            "summary": description,
            "start": {"dateTime": start.isoformat()},
            "end": {"dateTime": end.isoformat()},
            "id": event_id,
            "status": "confirmed",
        }
        if patch:
            self.service.events().patch(
                calendarId=self.get_task_calendar()["id"],
                eventId=event_id,
                body=event_body,
            ).execute()
        else:
            self.service.events().patch(
                calendarId=self.get_task_calendar()["id"],
                eventId=event_id,
                body=event_body,
            ).execute()
