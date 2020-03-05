from EvaMap.Dimensions.Dimension import Dimension
from EvaMap.Metrics.A_Error import Error
from EvaMap.Metrics.localLink import localLink
from EvaMap.Metrics.externalLink import externalLink


class Availability(Dimension):

    def __init__(self, nom='Availability', list_metrics=[Error, localLink, externalLink]):
        super().__init__(nom, list_metrics)
