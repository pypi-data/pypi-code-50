from EvaMap.Metrics.metric import metric

def duplicatedRules(g_onto, liste_map, g_map, raw_data, g_link) :
    result = metric()
    result['name'] = "Duplicated rules"
    result['score'] = 1
    result['feedbacks'].append(f"{str(len(liste_map) - len(g_map))} rules are duplicated")
    if liste_map:
        result['score'] = len(g_map)/len(liste_map) # Propriété d'un graph RDF
    return result

