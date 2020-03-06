"""Contains models used throughout the codebase
"""
import typing as t
from typing_extensions import TypedDict
from datetime import datetime, date
from enum import Enum

ETag = t.NewType("ETag", object)


class EventCreator(TypedDict, total=False):
    id: str
    email: str
    displayName: str
    self: bool


class EventOrganizer(TypedDict, total=False):
    id: str
    email: str
    displayName: str
    self: bool


class EventTime(TypedDict, total=False):
    date: str
    dateTime: str
    timeZone: str


class EventAttendee(TypedDict, total=False):
    id: str
    email: str
    displayName: str
    organizer: bool
    self: bool
    resource: bool
    optional: bool
    responseStatus: str
    comment: str
    additionalGuests: int


class EventResource(TypedDict, total=False):
    kind: str
    etag: ETag
    id: str
    status: str
    htmlLink: str
    created: str
    updated: str
    summary: str
    description: str
    location: str
    colorId: str
    creator: EventCreator
    organizer: EventOrganizer
    start: EventTime
    end: EventTime
    endTimeUnspecified: bool
    recurrence: t.Any
    recurringEventId: str
    originalStartTime: EventTime
    transparency: str
    visibility: str
    iCalUID: str
    sequence: str
    attendees: t.List[EventAttendee]
    attendeesOmitted: bool
    extendedProperties: t.Any
    hangoutLink: str
    conferenceData: t.Any
    entryPoints: t.Any
    conferenceSolution: t.Any
    conferenceId: str
    signature: str
    notes: str
    gagdet: t.Any
    reminders: t.Any
    source: t.Any
    attachments: t.Any


class CalendarResource(TypedDict, total=False):
    """Representation of a calendar used in the Calendar's endpoint.

    See https://developers.google.com/calendar/v3/reference/calendars
    """

    kind: str
    id: str
    summary: str
    description: str
    location: str
    timeZone: str
    etag: ETag
    conferenceProperties: t.Any


class ListCalendarDefaultReminders(TypedDict, total=False):
    method: str
    minutes: int


class ListCalendar(TypedDict, total=False):
    kind: str
    etag: ETag
    id: str
    summary: str
    description: str
    location: str
    timeZone: str
    summaryOverride: str
    colorId: str
    backgroundColor: str
    foregroundColor: str
    hidden: bool
    selected: bool
    accessRole: str
    defaultReminders: t.List[ListCalendarDefaultReminders]
    notificationSettings: t.Any
    primary: bool
    deleted: bool
    conferenceProperties: t.Any


class ListCalendarResponse(TypedDict, total=False):
    kind: str
    etag: ETag
    nextPageToken: str
    nextSyncToken: str
    items: t.List[ListCalendar]


class FreeBusyBusyObject(TypedDict, total=False):
    start: str
    end: str


class FreeBusyErrorObject(TypedDict, total=False):
    domain: str
    reason: str


class FreeBusyCalendarValue(TypedDict, total=False):
    errors: t.List[FreeBusyErrorObject]
    busy: t.List[FreeBusyBusyObject]


class FreeBusyResponse(TypedDict, total=False):
    kind: str
    timeMin: str
    timeMax: str
    calendars: t.Dict[str, FreeBusyCalendarValue]


class ParserContext(Enum):
    NONE = 0  # only at the start of the file
    UNK = 1  # unstructured just a string
    TASK = 2  # the default parser context md todolist


class TaskStatus(Enum):
    """The status of a task.

    The comments encode the character used to identify the task in the
    todo field. For example, '- [x]' would be done and '- [c]' would
    be canceled.
    """

    CANCELED = 0  # c
    IN_PROGRESS = 1  # -
    UNSCHEDULED = 2  # ' '
    DONE = 3  # x
    IDEA = 4  # ?
    BLOCKED = 5  # b


class Task(object):
    def __init__(self):
        super().__init__()
        self.status: TaskStatus
        # projects tagged on the task with +project
        self.projects: t.List[str] = []
        # people tagged on the task with +people
        self.people: t.List[str] = []
        # the id of the task (used for syncing with calendar)
        self.id: str
        # the context date of the task i.e. // year-mm-dd
        self.date: datetime.date
        # the task description
        self.description: str
        # the time estimate of the task in minutes
        self.estimate: int
        # the line number of the task in the todo file
        self.line_number: int
        # the children of the task AKA indented sub tasks
        self.children: t.List["Task"] = []
        # day the task is due
        self.due_date: t.Optional[date] = None
        # day the task is scheduled
        self.scheduled_date: t.Optional[date] = None

    def __str__(self):
        return f"{self.description}"
