import rdflib
import requests

from EvaMap.Metrics.metric import metric


def Error(g_onto, liste_map, g_map, raw_data, g_link) :
    result = metric()
    result['name'] = "Availability error"
    points = 0
    set_URIs = set()
    for s, p, o in g_map.triples((None, None, None)):
        if isinstance(s, rdflib.term.URIRef):
            set_URIs.add(_process_URI(s))
        if isinstance(p, rdflib.term.URIRef) and p != rdflib.term.URIRef('a'):
            set_URIs.add(_process_URI(p))
        if isinstance(o, rdflib.term.URIRef):
            set_URIs.add(_process_URI(o))
    nbPossible = len(set_URIs)
    for elt in set_URIs :
        a = requests.get(elt)
        try:
            a.raise_for_status()
        except:
            result['feedbacks'].append(f"It seems that {str(elt)} is not available: returns HTTP code {a.status_code}")
            points = points + 1
    if nbPossible == 0:
        result['score'] = 1
    else:
        result['score'] = 1-points/nbPossible
    return result


def _process_URI(uri):
    uri = str(uri)
    uri_without_ref = uri.split('$(')[0]
    if uri_without_ref != uri:
        uri_without_ref = uri_without_ref.rsplit('/', 1)[0] + '/'
    return uri_without_ref
