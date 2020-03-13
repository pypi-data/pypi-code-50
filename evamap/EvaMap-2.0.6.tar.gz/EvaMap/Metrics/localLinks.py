from EvaMap.Metrics.metric import metric
from rdflib import URIRef


def localLinks(g_onto, liste_map, g_map, raw_data, g_link):
    result = metric()
    result['name'] = "Use of one global mapping"
    result['score'] = 1
    ressources = set()
    for s, _, _ in g_map.triples((None, None, None)) :
        if isinstance(s, URIRef):
            ressources.add(s)
    isolated_ressources = 0
    for ressource in ressources:
        nb_link = 0
        for ressource, _, obj in g_map.triples((ressource, None, None)) :
            if isinstance(obj, URIRef) and obj in ressources:
                nb_link +=1
                break
        for subj, _, ressource in g_map.triples((None, None, ressource)) :
            if isinstance(subj, URIRef) and subj in ressources:
                nb_link +=1
                break
        if nb_link == 0:
            result['feedbacks'].append(f"resource {str(ressource)} is not linked to another resource")
            isolated_ressources += 1
    nb_ressources = len(ressources)
    if nb_ressources > 1:
        result['score'] = (nb_ressources - isolated_ressources) / nb_ressources
    return result
