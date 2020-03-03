import threading

from scrybe.internal.config import Config

thread_local = threading.local()
PLOT_IN_PROGRESS_KEY = "plotting_in_progress"
METRIC_IN_PROGRESS = "metric_in_progress"
PATCHING_DISABLED = "patching_disabled"
STATS_PATCHING_DISABLED = "stats_patching_disabled"


def is_metric_in_progress():
    return getattr(thread_local, METRIC_IN_PROGRESS, None)


def set_metric_in_progress():
    setattr(thread_local, METRIC_IN_PROGRESS, True)


def unset_metric_in_progress():
    setattr(thread_local, METRIC_IN_PROGRESS, None)


def is_plotting_in_progress():
    return getattr(thread_local, PLOT_IN_PROGRESS_KEY, None)


def set_plotting_in_progress():
    setattr(thread_local, PLOT_IN_PROGRESS_KEY, True)


def unset_plotting_in_progress():
    setattr(thread_local, PLOT_IN_PROGRESS_KEY, None)


class ThreadLocalVarHandler(object):
    class PatchingHandler(object):
        def __init__(self, var_name, handle_src_code=False):
            self.var_name = var_name
            self.handle_src_code = handle_src_code

        def disable_patching(self):
            if self.handle_src_code:
                Config.disable_src_code_tracking()
            current_state = getattr(thread_local, self.var_name, None)
            if current_state is None:
                current_state = 0
            setattr(thread_local, self.var_name, current_state + 1)

        def is_patching_disabled(self):
            current_state = getattr(thread_local, self.var_name, None)
            if current_state is None or current_state == 0:
                return False
            return True

        def enable_patching(self):
            if self.handle_src_code:
                Config.enable_src_code_tracking()
            current_state = getattr(thread_local, self.var_name, None)
            if current_state is None:
                return
            current_state -= 1
            if current_state == 0:
                current_state = None
            setattr(thread_local, self.var_name, current_state)

    stats = PatchingHandler(STATS_PATCHING_DISABLED)
    all_func = PatchingHandler(PATCHING_DISABLED, handle_src_code=True)
