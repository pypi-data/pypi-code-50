from scrybe.internal.config import Config


def get_scrybe_dashboard_url_for_node(obj_node):
    dashboard_server_url = Config.get_dashboard_server_url()
    if not dashboard_server_url:
        return None, "Can't find Scrybe server address. Please initialize Scrybe before calling this API"

    project_id = Config.get_project_id()
    if not project_id:
        return None, "Can't find project id for the given project"

    base_url = "%s/projects/%s" % (dashboard_server_url, str(project_id))
    url = None
    from scrybe.internal.depgraph.nodes import BaseTrackingNode, ArtifactType
    if obj_node.node_type == BaseTrackingNode.Type.MODEL:
        url = "%s/models/%s" % (base_url, obj_node.client_id)
    elif obj_node.node_type == BaseTrackingNode.Type.DATA:
        url = "%s/datasets/%s" % (base_url, obj_node.client_id)
    elif obj_node.node_type == BaseTrackingNode.Type.DATASET_ARTIFACT and obj_node.object_type == ArtifactType.PLOT_IMAGE:
        url = "%s/tabs/plots/%s" % (base_url, obj_node.client_id)

    if not url:
        return None, "Dashboard url is only available for tracked model, dataset and matplotlib figure objects"
    url = url + "?client_id=true"
    return url, None
