"""Private constants used with tes-lib"""
import logging

EVENT_SOURCE_KEY = "event_source"
EVENT_TYPE_KEY = "event_type"
EVENT_ID_KEY = "event_id"
EVENT_STATE_KEY = "event_state"

NO_MATCHING_EVENT_FOUND = "No Matching Event Found"

DEFAULT_IP = "127.0.0.1"
DEFAULT_PORT = 8080
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
