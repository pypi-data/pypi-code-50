import rdflib
import requests

from EvaMap.Metrics.metric import metric

def longURI(g_onto, liste_map, g_map, raw_data, g_link) :
    result = metric()
    result['name'] = "Long URIs"
    nbPossible = 0
    points = 0
    set_URIs = set()
    for s, p, o in g_map.triples((None, None, None)):
        if isinstance(s, rdflib.term.URIRef) :
            set_URIs.add(s)
    for s in set_URIs:
        if isinstance(s, rdflib.term.URIRef) :
            nbPossible = nbPossible + 1
            if len(s) >= 80 :
                points = points + 1
                result['feedbacks'].append(f"{str(s)} is more than 79 characters")
    if nbPossible == 0:
        result['score'] = 1
    else :
        result['score'] = 1-points/nbPossible
    return result