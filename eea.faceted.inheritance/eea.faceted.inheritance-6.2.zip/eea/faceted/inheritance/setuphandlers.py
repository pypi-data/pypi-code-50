""" Various setup
"""
from logging import getLogger
from zope.annotation.interfaces import IAnnotations
from zope.interface import noLongerProvides
from Products.CMFCore.utils import getToolByName
from eea.faceted.inheritance.config import ANNO_ANCESTOR
from eea.faceted.inheritance.interfaces import IFacetedHeritor
logger = getLogger("eea.faceted.inheritance.post_uninstall")


def setupVarious(context):
    """ Various setup
    """
    if context.readDataFile('eea.faceted.inheritance.txt') is None:
        return


def uninstall_faceted(context):
    """ Custom script to remove interface traces on uninstall """
    remove_annotations(context)
    remove_default_views(context)
    remove_assigned_interfaces(context)


def remove_assigned_interfaces(context):
    remove_interface(context, IFacetedHeritor)


def remove_interface(context, iface):
    """ Remove interface assignment from objects"""
    portal_catalog = getToolByName(context, "portal_catalog")
    brains = portal_catalog(object_provides=iface.__identifier__)
    logger.info(
        "Removing {0} interface from {1} objects".format(
            iface.__identifier__, len(brains)
        )
    )
    for brain in brains:
        item = brain.getObject()
        noLongerProvides(item, iface)


def remove_annotations(context):
    """Remove criteria configuration from annotations"""
    portal_catalog = getToolByName(context, "portal_catalog")
    brains = portal_catalog(object_provides=IFacetedHeritor.__identifier__)
    for brain in brains:
        item = brain.getObject()
        annotations = IAnnotations(item)
        if ANNO_ANCESTOR in annotations:
            del annotations[ANNO_ANCESTOR]
            logger.info("Removed criteria configuration from {0}".format(brain.getPath()))


def remove_default_views(context):
    portal_catalog = getToolByName(context, "portal_catalog")
    brains = portal_catalog(object_provides=IFacetedHeritor.__identifier__)
    for brain in brains:
        item = brain.getObject()
        if (
            item.hasProperty("layout")
            and item.getProperty("layout") == "facetednavigation_view"
        ):
            item.manage_delProperties(["layout"])
            logger.info(
                "Removed facetednavigation_view layout from {0}".format(brain.getPath())
            )
