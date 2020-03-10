
def SetRecommendedRenderSettings(view):
    """
    Set view settings to enable smooth interaction with the rendering widget.
    Disables interactor-based render calls and forces server-side rendering.

    Parameters
    ----------
    view: ParaView proxy view
    """
    # Disable interactor-based render calls.
    view.EnableRenderOnInteraction = 0
    # Force server-side rendering.
    view.RemoteRenderThreshold = 0


def ResetCamera(view, widget):
    """
    Reset camera center of rotation of the view and update the widget.
    
    Parameters
    ----------
    view: ParaView proxy view
    widget: RemoteRenderer widget
    """
    from paraview import simple
    simple.ResetCamera()
    view.CenterOfRotation = simple.GetActiveCamera().GetFocalPoint()
    # Update the rendering widget on the javascript side to display the changes
    widget.update_render()


def find_next_free_port(start_port):
    """
    Finds next free port starting from a given port using the psutil module.
    For port numbers smaller than 1, starts search with the first registered port (1024),
    returns None, if no free port can be found between start_port and the biggest port number (65535)
    """
    import psutil

    max_port = 65535

    if start_port < 1:
        port = 1024
    else:
        port = start_port

    while port <= max_port:
        isFree = True
        for conn in psutil.net_connections():
            if conn.status == 'LISTEN' and conn.laddr.port == port:
                port += 1
                isFree = False
                break
        if isFree:
            return port
    return None