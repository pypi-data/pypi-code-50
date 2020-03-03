import json
from datetime import datetime
from py42.sdk.file_event_query.file_event_query import FileEventQuery
from py42.sdk.file_event_query.event_query import InsertionTimestamp

from c42eventextractor.compat import str
from c42eventextractor.common import convert_datetime_to_timestamp, IncompatibleFilterError

_DEFAULT_LOOK_BACK_DAYS = 60
_MAX_PAGE_SIZE = 10000
_TIMESTAMP_PRECISION = 0.001
INSERTION_TIMESTAMP_FIELD_NAME = u"insertionTimestamp"
EXPOSURE_TYPE_FIELD_NAME = u"exposure"


class FileEventExtractor(object):
    _previous_event_count = _MAX_PAGE_SIZE

    def __init__(self, sdk, handlers):
        self._sdk = sdk
        self._handlers = handlers

    @property
    def previous_event_count(self):
        return self._previous_event_count

    def extract(self, *args):
        # type: (iter, iter) -> None
        """Queries for recent security exposure events.
           Passes the raw response from the py42 call to `handlers.handle_response`.
           The default implementation of `handlers.handle_response` prints `response.text` to the console.
           Provide your own implementation for `handlers.handle_response` to do something else.
           Makes subsequent calls to py42 and `handlers.handle_response`
                if the total event count is greater than 10,000.

        Args:
            *args: Additional file event query filter groups. Note: Throws an exception if receives an
                InsertionTimestamp filter.
        """
        filter_groups = list(args)
        FileEventExtractor._verify_compatibility_of_filter_groups(filter_groups)
        self._extract_all(filter_groups)

    def extract_advanced(self, query):
        try:
            response = self._sdk.security.search_file_events(query)
            if response.text:
                response_dict = json.loads(response.text)
                self._record_checkpoints(response_dict)
                self._handlers.handle_response(response)
            return response
        except Exception as ex:
            self._handlers.handle_error(ex)

    def _extract_all(self, filter_groups):
        if self.previous_event_count < _MAX_PAGE_SIZE:
            return

        query = self._create_file_event_query(filter_groups)
        if self.extract_advanced(query):
            self._extract_all(filter_groups)

    def _create_file_event_query(self, filter_groups):
        filter_groups = self._create_filter_groups(filter_groups)
        query = FileEventQuery(*filter_groups)
        query.sort_direction = u"desc"
        query.sort_key = INSERTION_TIMESTAMP_FIELD_NAME
        query.page_size = _MAX_PAGE_SIZE
        return query

    def _create_filter_groups(self, filter_groups):
        insertion_filter = self._create_insertion_timestamp_filter()
        if insertion_filter:
            filter_groups.append(insertion_filter)
        return filter_groups

    @staticmethod
    def _verify_compatibility_of_filter_groups(filter_groups):
        for group in filter_groups:
            if not group:
                continue
            filters = json.loads(str(group)).get(u"filters")
            if not filters:
                continue
            for event_filter in filters:
                if event_filter.get(u"term") == INSERTION_TIMESTAMP_FIELD_NAME:
                    raise IncompatibleFilterError()

    def _create_insertion_timestamp_filter(self):
        current_position = self._handlers.get_cursor_position()
        if current_position:
            return InsertionTimestamp.on_or_after(current_position + _TIMESTAMP_PRECISION)

    def _record_checkpoints(self, response_dict):
        self._record_count(response_dict)
        self._record_insertion_timestamp(response_dict)

    def _record_count(self, response_dict):
        total_count_key = u"totalCount"
        count = response_dict[total_count_key] or 0
        self._previous_event_count = count

    def _record_insertion_timestamp(self, response_dict):
        insertion_time = self._get_insertion_timestamp_from_dict(response_dict)
        if insertion_time is not None:
            self._handlers.record_cursor_position(insertion_time)

    def _get_insertion_timestamp_from_dict(self, response_dict):
        events = self._get_events_from_dict(response_dict)
        if events and INSERTION_TIMESTAMP_FIELD_NAME in events[0]:
            return self._get_insertion_timestamp_from_event(events[0])

    @staticmethod
    def _get_events_from_dict(response_dict):
        file_events_key = u"fileEvents"
        if file_events_key in response_dict:
            return response_dict[file_events_key]

    @staticmethod
    def _get_insertion_timestamp_from_event(event):
        insertion_time_str = event[INSERTION_TIMESTAMP_FIELD_NAME]
        insertion_time = datetime.strptime(insertion_time_str, u"%Y-%m-%dT%H:%M:%S.%fZ")
        insertion_timestamp = convert_datetime_to_timestamp(insertion_time)
        return insertion_timestamp
