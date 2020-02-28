
class SpreadD:
    def run(self, graph, checkers, tmp_name="msg"):
        for node in graph.get_ids():
            graph.set_attr(node, tmp_name, [node])


