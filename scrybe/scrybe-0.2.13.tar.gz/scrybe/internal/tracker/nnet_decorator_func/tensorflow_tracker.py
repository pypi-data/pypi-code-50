import logging

LOGGER = logging.getLogger(__name__)
LOG_METRICS = True
LOG_HISTOGRAMS = True


def extract_from_add_summary(file_writer, summary, global_step):
    from tensorflow.core.framework import summary_pb2

    extracted_values = {"metrics": {}, "histo": []}

    if isinstance(summary, bytes):
        summ = summary_pb2.Summary()
        summ.ParseFromString(summary)
        summary = summ

    for value in summary.value:
        field = value.WhichOneof("value")

        if field == "simple_value":
            extracted_values["metrics"][value.tag] = value.simple_value
        elif field == "histo":
            extracted_values["histo"].append(value.histo)

    return extracted_values, global_step


# def convert_histograms(histo):
#     """
#     Convert tensorboard summary histogram format into a histogram.
#     """
#     histogram = Histogram()
#     values = histo.bucket_limit
#     counts = histo.bucket
#     histogram.add(values, counts)
#     return histogram


def add_summary_logger(value, orig_func, *args, **kwargs):
    """
    Note: auto_metric_logging controls summary metrics and histograms
    Note: assumes "simple_value" is a metric
    """
    try:
        LOGGER.debug(
            "Extracting metrics/histograms from add_summary()", exc_info=True
        )
        # if (
        #     experiment.auto_metric_logging
        #     and not experiment.disabled_monkey_patching
        #     and (LOG_METRICS or LOG_HISTOGRAMS)
        # ):
        #     LOGGER.debug("TENSORBOARD LOGGER CALLED")
        #     values, step = extract_from_add_summary(*args, **kwargs)
        #     if values["metrics"] and LOG_METRICS:
        #         experiment.log_metrics(values["metrics"], step=step)
            # if values["histo"] and LOG_HISTOGRAMS:
            #     for histo in values["histo"]:
            #         experiment.log_histogram_3d(convert_histograms(histo), step=step)

    except Exception:
        LOGGER.error(
            "Failed to extract metrics/histograms from add_summary()", exc_info=True
        )


def summary_scalar_logger(value, orig_func, *args, **kwargs):
    """
    Note: Assumes summary.scalars are metrics.
    """
    try:
        LOGGER.debug(
            "Extracting metrics from tensorflow.summary.scalar()", exc_info=True
        )
        # if (
        #     experiment.auto_metric_logging
        #     and not experiment.disabled_monkey_patching
        #     and LOG_METRICS
        # ):
        #     name, data, step = get_args(*args, **kwargs)
        #     experiment.log_metric(name, data, step=step)
    except Exception:
        LOGGER.error(
            "Failed to extract metrics from tensorflow.summary.scalar()", exc_info=True
        )


def summary_histogram_3d_logger(value, orig_func, *args, **kwargs):
    try:
        LOGGER.debug(
            "Extracting histogram 3D from tensorflow.summary.histogram()",
            exc_info=True,
        )
        # if (
        #     experiment.auto_metric_logging
        #     and not experiment.disabled_monkey_patching
        #     and LOG_HISTOGRAMS
        # ):
        #     # FIXME:
        #     name, data, step = get_args(*args, **kwargs)
        #     experiment.log_histogram_3d(name, data, step=step)
        #     pass
    except Exception:
        LOGGER.error(
            "Failed to extract histogram 3D from tensorflow.summary.histogram()",
            exc_info=True,
        )


def get_args(name, data, step=None, **kwargs):
    """
    Wrapper to parse args
    """
    return (name, data, step)


def patch(module_finder):
    # tensorflow 1.11.0 - 1.14.0 in non-compatible mode:
    module_finder.register_after(
        "tensorflow.python.summary.writer.writer",
        "FileWriter.add_summary",
        add_summary_logger,
    )
    # tensorflow 2:
    module_finder.register_after(
        "tensorboard.plugins.scalar.summary_v2", "scalar", summary_scalar_logger
    )
    module_finder.register_after(
        "tensorboard.plugins.scalar.summary_v2",
        "histogram",
        summary_histogram_3d_logger,
    )
