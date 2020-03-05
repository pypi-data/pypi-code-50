from EvaMap.Dimensions.Dimension import Dimension
from EvaMap.Metrics.humanReadable import humanReadableURIs
from EvaMap.Metrics.humanDesc import humanDesc
from EvaMap.Metrics.longTerm import longTerm


class Clarity(Dimension) :

    def __init__(self, nom='Clarity', list_metrics=[humanReadableURIs, humanDesc]):
        super().__init__(nom, list_metrics)