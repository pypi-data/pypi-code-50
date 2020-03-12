# -*- coding: utf-8 -*-
"""
 This script initializes the plugin, making it known to QGIS.
"""


def classFactory(iface):
    """ Load Viper class from file viper.
    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """

    from mesma.mesma_plugin import MesmaPlugin
    return MesmaPlugin(iface)
