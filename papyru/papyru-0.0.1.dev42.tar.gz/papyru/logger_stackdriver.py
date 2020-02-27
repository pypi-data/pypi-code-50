import atexit
from os import environ
from queue import Queue
from sys import stderr
from threading import Thread

import google.cloud.logging_v2 as gce_logging
from google.logging.type.log_severity_pb2 import LogSeverity
from google.protobuf.struct_pb2 import Struct

import papyru.logger_types as T
from papyru.logger_stdout import format_summary


def make_stackdriver_sink():
    project_id = environ.get('PAPYRU_PROJECT_ID', None)
    cluster_name = environ.get('PAPYRU_CLUSTER_NAME', None)
    namespace_id = environ.get('PAPYRU_NAMESPACE_ID', None)
    container_name = environ.get('PAPYRU_CONTAINER_NAME', None)
    pod_id = environ.get('PAPYRU_POD_ID', None)

    if not all(map(lambda e: e is not None,
                   [project_id,
                    cluster_name,
                    namespace_id,
                    container_name,
                    pod_id])):
        return None

    if 'GOOGLE_APPLICATION_CREDENTIALS' not in environ:
        print('WARNING missing credentials for stackdriver logging')
        return None

    try:
        return StackdriverSink(project_id,
                               cluster_name,
                               namespace_id,
                               container_name,
                               pod_id)
    except Exception as exc:
        print('WARNING could not initialize Stackdriver logging')
        print(exc)
        return None


class StackdriverSink:
    SHUTDOWN_GRACE_TIMEOUT = 5.0  # seconds

    def _make_logging_client():
        return gce_logging.LoggingServiceV2Client()

    def __init__(self,
                 project_id,
                 cluster_name,
                 namespace_id,
                 container_name,
                 pod_id):

        self.client = StackdriverSink._make_logging_client()
        self.log_name = 'projects/%s/logs/%s' % (project_id, container_name)
        self.resource = {
            'type': 'container',
            'labels': {
                'cluster_name': cluster_name,
                'namespace_id': namespace_id,
                'container_name': container_name,
                'pod_id': pod_id,
            }
        }

        self.queue = Queue()
        self.worker = Thread(target=self._log_loop, daemon=True)

        atexit.register(self._teardown)

        self.worker.start()

    def commit(self, item):
        self.queue.put(item)

    def _teardown(self):
        self.queue.put(None)
        self.worker.join(timeout=StackdriverSink.SHUTDOWN_GRACE_TIMEOUT)

    def _log_loop(self):
        while True:
            item = self.queue.get()

            if item is None:
                break

            self._send_log_entry(item)
            self.queue.task_done()

    def _assess_severity(item):
        MESSAGE_SEVERITY_MAP = {
            T.Message.SUCCESS: LogSeverity.INFO,
            T.Message.INFO: LogSeverity.INFO,
            T.Message.WARNING: LogSeverity.WARNING,
            T.Message.FAILURE: LogSeverity.ERROR,
            T.Message.CRITICAL: LogSeverity.CRITICAL,
        }

        if isinstance(item, T.Message):
            return MESSAGE_SEVERITY_MAP[item.severity]
        elif isinstance(item, T.Trace):
            return LogSeverity.ERROR
        elif isinstance(item, T.Sequence):
            if item.resolution == T.Message.SUCCESS:
                return next(
                    iter(sorted(map(StackdriverSink._assess_severity,
                                    item.items),
                                reverse=True)),
                    LogSeverity.DEFAULT)
            else:
                return LogSeverity.ERROR
        else:
            raise NotImplementedError()

    def _send_log_entry(self, item):
        try:
            self.client.write_log_entries([
                gce_logging.types.LogEntry(
                    log_name=self.log_name,
                    resource=self.resource,
                    json_payload=_encode_protobuf(item),
                    severity=StackdriverSink._assess_severity(item))
            ], dry_run=False)
        except Exception as exc:
            print('Sending logs to Stackdriver failed: %s' % exc,
                  file=stderr)


def _encode_protobuf(item):
    if isinstance(item, T.Message):
        s = Struct()
        s.update({'message': item.message})
        return s
    elif isinstance(item, T.Sequence):
        s = Struct()
        s.update({'message': format_summary(item),
                  'description': item.description,
                  'resolution': item.resolution,
                  'items': list(map(_encode_protobuf, item.items))})
        return s
    elif isinstance(item, T.Trace):
        s = Struct()
        s.update({
            'message': format_summary(item),
            'summary': _encode_protobuf(item.summary),
            'frames': list(map(_encode_protobuf, item.frames)),
        })
        return s
    elif isinstance(item, T.Trace.Summary):
        s = Struct()
        s.update({
            'description': item.description,
            'exception': str(item.exception),
        })
        return s
    elif isinstance(item, T.Trace.Frame):
        s = Struct()
        s.update({
            'filename': item.filename,
            'linenumber': item.linenumber,
            'line': item.line
        })
        return s
    else:
        raise NotImplementedError()
