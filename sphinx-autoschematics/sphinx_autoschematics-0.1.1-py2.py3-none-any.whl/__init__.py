import pkg_resources

from autoschematics.automodel import SchematicsModelDocumenter, SchematicsTypeDocumenter


def setup(app):
    """Setup is our entrypoint to being a sphinx extension"""
    app.add_autodocumenter(SchematicsModelDocumenter)
    app.add_autodocumenter(SchematicsTypeDocumenter)

    return {
        "version": pkg_resources.get_distribution("sphinx-autoschematics").version,
        "parallel_read_safe": True,
    }
