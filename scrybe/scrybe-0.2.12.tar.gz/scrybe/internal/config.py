import logging
import threading
import uuid
from typing import Union

LOGGER = logging.getLogger("scrybe_logger")


class Config(object):
    class InternalConfig(object):
        def __init__(self, project_info, dashboard_server_url):
            uid = str(uuid.uuid4()).replace("-", "")
            self.project_info = project_info
            self.dashboard_server_url = dashboard_server_url
            self.run_id = uid[:6] + uid[-6:]
            self.labels = None
            self.min_data_rows_for_stats = Config._min_data_rows_for_stats
            # The next two variables are used to determine whether the dataset
            # creation line of code should be captured or not
            self.src_code_disable_count = 0
            self.is_src_code_disabled_by_user = False
            # Boolean to check whether we should capture the complete python code or not
            self.code_capture_enabled = True
            self.lock = threading.Lock()

        def get_project_id(self):
            return self.project_info.get("id", None)

        def get_dashboard_server_url(self):
            return self.dashboard_server_url

        def get_run_id(self):
            return self.run_id

        def set_label(self, label: str):
            if label is None or len(label) == 0:
                self.labels = None
                return
            if isinstance(label, str):
                self.labels = [label]
            elif isinstance(label, list):
                self.labels = label

        def set_min_data_rows_for_stats(self, min_rows: int):
            self.min_data_rows_for_stats = min_rows

        def get_labels(self):
            return self.labels

        def get_min_data_rows_for_stats(self):
            return self.min_data_rows_for_stats

        def enable_src_code_tracking(self, force_enable=False):
            if force_enable:
                self.is_src_code_disabled_by_user = False
            self.lock.acquire()
            try:
                self.src_code_disable_count -= 1
            finally:
                self.lock.release()

        def disable_src_code_tracking(self, force_disable=False):
            if force_disable:
                self.is_src_code_disabled_by_user = True
            self.lock.acquire()
            try:
                self.src_code_disable_count += 1
            finally:
                self.lock.release()

        def is_src_code_enabled(self):
            """Used to determine whether the dataset creation line of code should be captured or not"""
            # Not acquiring lock because the cost of getting a wrong value here might be
            # less than acquiring a lock every time. We can afford to be wrong a few times
            return self.src_code_disable_count == 0 and not self.is_src_code_disabled_by_user

        def is_code_capture_enabled(self):
            """Used to check whether we should capture the complete python code/file or not"""
            return self.code_capture_enabled

        def enabled_code_capture(self):
            self.code_capture_enabled = True

        def disable_code_capture(self):
            self.code_capture_enabled = False

    _internal_config = None
    _min_data_rows_for_stats = 100
    has_exited = False

    @classmethod
    def get_project_id(cls):
        if cls._internal_config is not None:
            return cls._internal_config.get_project_id()
        return None

    @classmethod
    def get_dashboard_server_url(cls):
        if cls._internal_config is not None:
            return cls._internal_config.get_dashboard_server_url()
        return None

    @classmethod
    def get_run_id(cls):
        if cls._internal_config is not None:
            return cls._internal_config.get_run_id()
        return None

    @classmethod
    def set_label(cls, label: Union[str, list, None]):
        if cls._internal_config is not None:
            cls._internal_config.set_label(label=label)
        else:
            LOGGER.error("Config has not been initialized")

    @classmethod
    def set_min_data_rows_for_stats(cls, min_rows: int):
        if cls._internal_config is not None:
            cls._internal_config.set_min_data_rows_for_stats(min_rows=min_rows)
        else:
            LOGGER.error("Config has not been initialized")

    @classmethod
    def get_labels(cls):
        if cls._internal_config is not None:
            return cls._internal_config.get_labels()
        return None

    @classmethod
    def get_min_data_rows_for_stats(cls):
        if cls._internal_config is not None:
            return cls._internal_config.get_min_data_rows_for_stats()
        return cls._min_data_rows_for_stats

    @classmethod
    def is_initialized(cls):
        return cls._internal_config is not None

    @classmethod
    def enable_src_code_tracking(cls, force_enable=False):
        if cls._internal_config is not None:
            cls._internal_config.enable_src_code_tracking(force_enable=force_enable)
        else:
            LOGGER.error("Config has not been initialized")

    @classmethod
    def disable_src_code_tracking(cls, force_disable=False):
        if cls._internal_config is not None:
            cls._internal_config.disable_src_code_tracking(force_disable)
        else:
            LOGGER.error("Config has not been initialized")

    @classmethod
    def is_src_code_enabled(cls):
        """Used to determine whether the dataset creation line of code should be captured or not"""
        if cls._internal_config is not None:
            return cls._internal_config.is_src_code_enabled()
        else:
            return False

    @classmethod
    def is_code_capture_enabled(cls):
        """Used to check whether we should capture the complete python code/file or not"""
        if cls._internal_config is not None:
            return cls._internal_config.is_code_capture_enabled()
        else:
            return False

    @classmethod
    def enabled_code_capture(cls):
        if cls._internal_config is not None:
            cls._internal_config.enabled_code_capture()

    @classmethod
    def disable_code_capture(cls):
        if cls._internal_config is not None:
            cls._internal_config.disable_code_capture()


def init_config(project_info, dashboard_server_url):
    Config._internal_config = Config.InternalConfig(project_info=project_info,
                                                    dashboard_server_url=dashboard_server_url)
