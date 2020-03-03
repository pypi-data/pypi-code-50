import napari


def view(raw_data, surf_stack, surf_projection):
    with napari.gui_qt():
        v = napari.Viewer(title="Surfcut")
        v.add_image(raw_data, name="Raw data")
        v.add_image(surf_stack, name="Surf stack")
        v.add_image(surf_projection, name="Surf projection")
