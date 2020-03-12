from EvaMap.Dimensions.Dimension import Dimension
from EvaMap.Metrics.longURI import longURI
from EvaMap.Metrics.duplicatedRules import duplicatedRules

class Conciseness(Dimension) :

    def __init__(self, nom='Conciseness', list_metrics=[longURI, duplicatedRules]):
        super().__init__(nom, list_metrics)