
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