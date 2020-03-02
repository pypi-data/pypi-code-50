"""
This file contains the message definitions for messages passed to the event store process via
the request multiprocessing queue
"""


class _BaseMessage:
    def __init__(self, message_type):
        self.message_type = message_type


class ShutdownMessage(_BaseMessage):
    TYPE = "SHUTDOWN"

    def __init__(self):
        super(ShutdownMessage, self).__init__(ShutdownMessage.TYPE)


class ResetMessage(_BaseMessage):
    TYPE = "RESET"

    def __init__(self):
        super(ResetMessage, self).__init__(ResetMessage.TYPE)


class GetAllEventsMessage(_BaseMessage):
    TYPE = "GET_ALL"

    def __init__(self):
        super(GetAllEventsMessage, self).__init__(GetAllEventsMessage.TYPE)


class GetFullEventLogMessage(_BaseMessage):
    TYPE = "GET_FULL"

    def __init__(self):
        super(GetFullEventLogMessage, self).__init__(GetFullEventLogMessage.TYPE)


class GetAllMatchingEventsMessage(_BaseMessage):
    TYPE = "GET_MATCHING"

    def __init__(self, expectations):
        super(GetAllMatchingEventsMessage, self).__init__(GetAllMatchingEventsMessage.TYPE)
        self.expectations = expectations


class AddEventMessage(_BaseMessage):
    TYPE = "ADD"

    def __init__(self, event_fields):
        super(AddEventMessage, self).__init__(AddEventMessage.TYPE)
        self.event_fields = event_fields


class ExpectEventMessage(_BaseMessage):
    TYPE = "EXPECT"

    def __init__(self, expectations):
        super(ExpectEventMessage, self).__init__(ExpectEventMessage.TYPE)
        self.expectations = expectations


class RemoveExpectedEventMessage(_BaseMessage):
    TYPE = "REMOVE_EXPECTED"

    def __init__(self, event):
        super(RemoveExpectedEventMessage, self).__init__(RemoveExpectedEventMessage.TYPE)
        self.event = event


class DeleteMatchingEventsMessage(_BaseMessage):
    TYPE = "DELETE_MATCHING"

    def __init__(self, expectations):
        super(DeleteMatchingEventsMessage, self).__init__(DeleteMatchingEventsMessage.TYPE)
        self.expectations = expectations
