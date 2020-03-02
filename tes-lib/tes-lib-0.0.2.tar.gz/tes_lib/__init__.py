"""
tes-lib

A library to enable asynchronous event based testing of complex systems.
"""

from .library_settings import initialise, cleanup, reset_event_store
from .expectation import Expectation
from .event_helpers import (
    expect_event,
    add_event,
    add_raw_event,
    get_all_events,
    delete_all_matching_events,
    get_all_matching_events,
    log_event_store,
    log_full_event_store,
    dont_expect_event,
)
from .errors import TesLibError, EventNotFoundError, UnexpectedEventFoundError
from .test_event import TestEvent

__all__ = [
    "initialise",
    "cleanup",
    "reset_event_store",
    "Expectation",
    "add_event",
    "add_raw_event",
    "delete_all_matching_events",
    "dont_expect_event",
    "expect_event",
    "get_all_events",
    "get_all_matching_events",
    "log_event_store",
    "log_full_event_store",
    "EventNotFoundError",
    "TesLibError",
    "UnexpectedEventFoundError",
    "TestEvent",
]
