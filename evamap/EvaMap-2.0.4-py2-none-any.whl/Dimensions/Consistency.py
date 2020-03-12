from EvaMap.Dimensions.Dimension import Dimension
from EvaMap.Metrics.subClassesProperties import subClassesProperties
from EvaMap.Metrics.equivalentClassesProperties import equivalentClassesProperties
from EvaMap.Metrics.disjointWith import disjointWith
from EvaMap.Metrics.domainRange import domainRange

class Consistency(Dimension) :

    def __init__(self, nom='Consistency', list_metrics=[domainRange, subClassesProperties, equivalentClassesProperties, disjointWith]):
        super().__init__(nom, list_metrics)