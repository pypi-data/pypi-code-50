from rdflib.graph import Graph
import json

from EvaMap.Dimensions.Availability import Availability
from EvaMap.Dimensions.Clarity import Clarity
from EvaMap.Dimensions.Conciseness import Conciseness
from EvaMap.Dimensions.Connectability import Connectability
from EvaMap.Dimensions.Consistency import Consistency
from EvaMap.Dimensions.Coverability import Coverability
from EvaMap.utils import yarrrml_parser as YARRRML


class EvaMap:

    g_link = Graph()
    g_map = Graph()
    g_onto = Graph()
    liste_map = []
    dimensions_list = [(Availability(), 1), (Clarity(), 1), (Conciseness(), 1), (Connectability(), 1), (Consistency(), 1), (Coverability(), 1)]
    score_tot = []
    final_list = []
    raw_data = {}
    final_score = 0

    def __init__(self, rdf_ontology, yarrrml_mapping, json_data):
        if not self.read_json(json_data): return
        if not self.read_rdf(rdf_ontology): return
        self.g_link, self.liste_map = YARRRML.parse_to_rdf_mapping(yarrrml_mapping)
        self.g_map = self.g_link

    def read_json(self, json_data):
        try:
            self.raw_data = json.loads(json_data)
            self.raw_data = self.raw_data.get('records')
            if not self.raw_data:
                print(f'JSON data Syntax Error: records key not found. get JSON from the ODS API')
                return False
        except json.decoder.JSONDecodeError as exception:
            print(f'JSON data Syntax Error: {exception}')
            return False
        return True

    def read_rdf(self, rdf):
        for syntax in 'xml/rdf', 'ttl', 'nt':
            try:
                self.g_onto.parse(data=rdf, format=syntax)
                break
            except Exception:
                pass
        if len(self.g_onto) <= 0: return False
        for s, p, o in self.g_onto.triples((None, None, None)):
            self.g_link.add((s, p, o))
        return True

    def set_weight(self, dict):
        i = 0
        for poids in self.liste:
            self.weight[i] = poids

    def evaluate_mapping(self):
        self.final_score = 0
        tot_weight = 0
        for dimension in self.dimensions_list:
            dimension_score = dimension[0].calc_score(self.g_onto, self.liste_map, self.g_map, self.raw_data, self.g_link)
            self.score_tot.append(dimension_score)
            self.final_list.append(dimension[0].dim_to_string())
            self.final_score += (dimension[1] * dimension_score)
            tot_weight += dimension[1]
        self.final_score = self.final_score / tot_weight

    def get_total_score(self):
        return self.final_score

    def get_complet_result(self):
        return self.final_list
