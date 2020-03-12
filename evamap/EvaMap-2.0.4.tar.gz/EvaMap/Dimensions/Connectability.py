from EvaMap.Dimensions.Dimension import Dimension
from EvaMap.Metrics.sameAs import sameAs
from EvaMap.Metrics.externalURIs import externalURIs
from EvaMap.Metrics.externalLink import externalLink
from EvaMap.Metrics.localLinks import localLinks


class Connectability(Dimension) :

    def __init__(self, nom='Connectability', list_metrics=[sameAs, externalURIs, localLinks, externalLink]):
        super().__init__(nom, list_metrics)
