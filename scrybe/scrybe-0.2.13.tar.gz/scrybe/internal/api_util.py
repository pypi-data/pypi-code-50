from scrybe.internal.code_capture.source_code import CodeCapture
from scrybe.internal.depgraph import TrackingGraph
from scrybe.internal.depgraph.node_util import get_scrybe_dashboard_url_for_node


def get_scrybe_dashboard_url(obj):
    """
    :param obj: The object can be a tracked model, dataset or a matplotlib figure object
    :return: Tuple of url and error message. Error message is set only when error is not found
    """
    if not TrackingGraph.has_tracked_obj(obj=obj):
        return None, "Object is not tracked by Scrybe"
    obj_node = TrackingGraph.get_node_for_tracked_object(obj=obj)
    return get_scrybe_dashboard_url_for_node(obj_node=obj_node)


def peek(obj):
    url, error_msg = get_scrybe_dashboard_url(obj=obj)
    if not url:
        print(error_msg)
        return
    print(url)
    if CodeCapture.is_notebook():
        from IPython.display import IFrame
        return IFrame(src=url, width='100%', height='800px')
