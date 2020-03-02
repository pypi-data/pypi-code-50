"""
A collection of helper functions for interacting with the test event store
"""
from typing import List, Dict, Any, Callable, Optional
import copy
import time
import logging
from multiprocessing import connection
import requests

from .test_event import TestEvent
from .expectation import Expectation
from .errors import TesLibError, EventNotFoundError, UnexpectedEventFoundError
from .library_settings import _TesLibInstance
from .messages import (
    GetAllEventsMessage,
    GetFullEventLogMessage,
    GetAllMatchingEventsMessage,
    RemoveExpectedEventMessage,
    ExpectEventMessage,
    DeleteMatchingEventsMessage,
)
from .constants import EVENT_SOURCE_KEY, EVENT_TYPE_KEY, EVENT_ID_KEY, EVENT_STATE_KEY
from .constants import DEFAULT_IP, DEFAULT_PORT, NO_MATCHING_EVENT_FOUND

logger = logging.getLogger("tes_lib")


def wait_for_response(context: str, recv_connection: connection.Connection, timeout=0.5) -> Any:

    if recv_connection.poll(timeout=timeout):
        result = recv_connection.recv()
    else:
        logger.warning(f"No message received from event store, context: {context}")
        raise TesLibError(f"No response from event store, context: {context}")
    return result


def get_all_events(timeout: int = 1) -> List[Dict]:
    """Get all events currently in the event store

    :param timeout: The amount of time to give the event store to return all the events
    :return: A list of events
    """
    tes_lib = _TesLibInstance.get_instance()

    tes_lib.queue.put(GetAllEventsMessage())

    result = wait_for_response("get_all_events", tes_lib.parent_conn, timeout=timeout)

    return result


def _event_matches_expectations(event: Dict, expectations: List[Expectation]) -> bool:
    for expectation in expectations:
        if expectation.event_field_name not in event:
            return False

        event_value = event[expectation.event_field_name]
        if not expectation.comparison_function(event_value, expectation.comparison_value):
            return False

    return True


def _log_event_store(
    events: List[Dict],
    order_by: str,
    order_by_default: Any,
    fields_to_log: Optional[List[str]],
    fields_to_exclude: Optional[List[str]],
    filters: Optional[List[Expectation]],
    required_fields: List[str],
):
    if fields_to_log and fields_to_exclude:
        logger.error(
            "fields_to_log and fields_to_exlcude have been provided."
            " fields_to_exclude will be ignored"
        )

    # Filter events
    if filters:
        filtered_events = []

        for event in events:
            if _event_matches_expectations(event, filters):
                filtered_events.append(event)

        events = filtered_events

    # Order events
    if order_by != EVENT_ID_KEY:
        events = sorted(events, key=lambda x: (x.get(order_by, order_by_default), x[EVENT_ID_KEY]))
    else:
        events = sorted(events, key=lambda x: x[EVENT_ID_KEY])

    # Filter event fields
    if fields_to_log:
        for event in events:
            # Each event can have different fields so we have to do this every time
            keys_to_remove = [key for key in event.keys() if key not in fields_to_log]

            for field in required_fields:
                if field in keys_to_remove:
                    keys_to_remove.remove(field)

            for key in keys_to_remove:
                del event[key]

    elif fields_to_exclude:

        for field in required_fields:
            if field in fields_to_exclude:
                fields_to_exclude.remove(field)

        for event in events:
            for key in fields_to_exclude:
                if key in event.keys():
                    del event[key]

    logger.info("***** Logging Event Store *****")

    for event in events:
        event_id = event[EVENT_ID_KEY]
        del event[EVENT_ID_KEY]
        logger.info(f"event_id: {event_id}, {dict(sorted(event.items()))}")

    logger.info("***** End Of Event Store *****")


def log_full_event_store(
    order_by: str = EVENT_ID_KEY,
    order_by_default: Any = None,
    fields_to_log: List[str] = None,
    fields_to_exclude: List[str] = None,
    filters: List[Expectation] = None,
):
    """See log_event_store for param details

    This function is the same as log_event_store except that it will also contain events that
    have been deleted or removed from the store due to being expected.
    """
    tes_lib = _TesLibInstance.get_instance()

    tes_lib.queue.put(GetFullEventLogMessage())

    events = wait_for_response("log_full_event_store", tes_lib.parent_conn, timeout=5)

    _log_event_store(
        events,
        order_by,
        order_by_default,
        fields_to_log,
        fields_to_exclude,
        filters,
        [EVENT_ID_KEY, EVENT_STATE_KEY],
    )


def log_event_store(
    order_by: str = EVENT_ID_KEY,
    order_by_default: Any = None,
    fields_to_log: List[str] = None,
    fields_to_exclude: List[str] = None,
    filters: List[Expectation] = None,
):
    """Log the current contents of the event store

    :param order_by: The field events should be ordered by
    :param order_by_default: The value to use when ordering for events that don't have the order_by
                             field
    :param fields_to_log: Event fields to log, all others will be excluded - incompatible with
                          fields_to_exclude. If not provided all fields will be logged. The
                          event_id field will be included even if not specified in the fields_to_log
    :param fields_to_exclude: Fields to exclude, all others will be logged - incompatible with
                              fields_to_log. If not provided all fields will be logged. The
                              event_id field cannot be excluded.
    :param filters: Only log the events that meet the given expectations. If not provided all
                    events will be logged
    :return: None
    """
    events = get_all_events()

    _log_event_store(
        events,
        order_by,
        order_by_default,
        fields_to_log,
        fields_to_exclude,
        filters,
        [EVENT_ID_KEY],
    )


def expect_event(
    expectations: List[Expectation],
    timeout: float = 5,
    poll_interval: float = 0.1,
    on_failure: Callable = log_event_store,
) -> Dict:
    """Expect an event - finds the first event that matches all the given expectations in the
    event store. This event is then removed from the event store and returned.

    :param expectations: The list of expectations the event must meet
    :param timeout: The amount of time to wait for the event
    :param poll_interval: The time between polling for the event
    :param on_failure: The function to call when we fail to find the expected event
    :return: The found event
    :raises EventNotFoundError: The expected event was not found
    """
    returned_event: Any = NO_MATCHING_EVENT_FOUND

    end_time = time.time() + timeout
    tes_lib = _TesLibInstance.get_instance()

    while returned_event is NO_MATCHING_EVENT_FOUND and time.time() < end_time:
        tes_lib.queue.put(ExpectEventMessage(expectations))

        returned_event = wait_for_response("expect_event", tes_lib.parent_conn)

        if returned_event is NO_MATCHING_EVENT_FOUND:
            time.sleep(poll_interval)

    # Remove the event now that we have found it
    if returned_event != NO_MATCHING_EVENT_FOUND:
        tes_lib.queue.put(RemoveExpectedEventMessage(returned_event))

    if returned_event == NO_MATCHING_EVENT_FOUND:
        on_failure()
        raise EventNotFoundError(
            f"Failed to find an event matching the following expectations: {expectations}"
        )

    return returned_event


def dont_expect_event(expectations: List[Expectation], timeout: float, poll_interval: float = 0.1):
    """Don't expect any events in the event store matching the given expectations

    :param expectations: The list of expectations to match against
    :param timeout: The amount of time to wait without seeing the event
    :param poll_interval: The time between polling for the event
    :return: None
    :raises UnexpectedEventFoundError: An unexpected event was found that matches the given
            expectations
    """
    returned_event = NO_MATCHING_EVENT_FOUND

    end_time = time.time() + timeout
    tes_lib = _TesLibInstance.get_instance()

    while returned_event is NO_MATCHING_EVENT_FOUND and time.time() < end_time:
        tes_lib.queue.put(ExpectEventMessage(expectations))

        returned_event = wait_for_response("expect_event", tes_lib.parent_conn)

        if returned_event is NO_MATCHING_EVENT_FOUND:
            time.sleep(poll_interval)

    if returned_event != NO_MATCHING_EVENT_FOUND:
        raise UnexpectedEventFoundError(
            f"An unexpected event {returned_event} was found"
            f" matching the following expectations {expectations}"
        )


def get_all_matching_events(expectations: List[Expectation], timeout: float = 1) -> List[Dict]:
    """Get all events from the store that match the given expectations

    :param expectations: The list of expectations the event must meet
    :param timeout: The amount of time to wait for the event
    :param poll_interval: The time between polling for the event
    :return: A list of the events found
    """
    tes_lib = _TesLibInstance.get_instance()
    tes_lib.queue.put(GetAllMatchingEventsMessage(expectations))

    events = wait_for_response("get_all_matching_events", tes_lib.parent_conn, timeout=timeout)

    return events


def delete_all_matching_events(expectations: List[Expectation], timeout: float = 1) -> int:
    """Delete all events from the store that match the given expectations

    :param expectations: The list of expectations the event must meet
    :param timeout: The amount of time to wait for the event
    :param poll_interval: The time between polling for the event
    :return: The number of events deleted
    """
    tes_lib = _TesLibInstance.get_instance()
    tes_lib.queue.put(DeleteMatchingEventsMessage(expectations))

    num_events_removed = wait_for_response(
        "delete_all_matching_events", tes_lib.parent_conn, timeout=timeout
    )

    return int(num_events_removed)


def add_raw_event(
    event_source: str,
    event_type: Any,
    additional_event_params: Dict,
    ip_address: str = DEFAULT_IP,
    port: int = DEFAULT_PORT,
):
    """Add an event to the event store by fields rather than via a TestEvent

    This is a helper function which will make a POST request to the add event webserver

    :param event_source: The name of the event source
    :param event_type: The event type
    :param additional_event_params: A json compatible dictionary of field_name to field_value
                                    Note a copy of this dictionary will be taken
    :param ip_address: The ip address of the add event webserver
    :param port: The port of the add event webserver
    :return: None
    :raises TesLibError: An error occurred adding the event to the event store
    """
    url = "http://{}:{}/add".format(ip_address, port)

    event_params = copy.deepcopy(additional_event_params)
    event_params[EVENT_SOURCE_KEY] = event_source
    event_params[EVENT_TYPE_KEY] = event_type

    response = requests.post(url=url, json=event_params)
    if response.status_code != requests.codes.ok:
        raise TesLibError(f"Failed to add event to the store: {response.text}")


def add_event(test_event: TestEvent, ip_address: str = DEFAULT_IP, port: int = DEFAULT_PORT):
    """Add an event to the event store

    This is a helper function which will make a POST request to the add event webserver

    :param test_event: A TestEvent instance
    :param ip_address: The ip address of the add event webserver
    :param port: The port of the add event webserver
    :return: None
    :raises TesLibError: An error occurred adding the event to the event store
    """
    url = "http://{}:{}/add".format(ip_address, port)

    event_params = vars(test_event)

    response = requests.post(url=url, json=event_params)
    if response.status_code != requests.codes.ok:
        raise TesLibError(f"Failed to add event to the store: {response.text}")
