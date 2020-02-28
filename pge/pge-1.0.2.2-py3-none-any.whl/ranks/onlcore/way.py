import networkx as nx
import numpy as np

from mcg.extreme.estimator.nonopt.intervals import IntervalsEstimate
from pge.ranks.extrem_onl import NodeExInfo


class WayEx(NodeExInfo):
    @staticmethod
    def get_ex(gr, root, frm, long=True):
        pathes = []
        di = []
        n = 0

        if long:
            for node in gr.get_ids():
                if node == root:
                    continue

                ways = list(nx.all_simple_paths(gr.get_nx_graph(), source=root, target=node))
                lns = [len(way) for way in ways]
                pathes.append(ways[np.argmax(lns)])
                di.append(np.max(lns))
                n += np.max(lns)
        else:
            pathes_ = nx.single_source_shortest_path(gr.get_nx_graph(), source=root)
            for node in gr.get_ids():
                if node == root:
                    continue

                pathes.append(pathes_[node])
                di.append(len(pathes_[node]))
                n += len(pathes_[node])

        if hasattr(frm, "__iter__") and not isinstance(frm, str):
            ex = []
            for frm_ in frm:
                xs, lv = gr.get_ln_attrs(frm_, pathes)
                exes = [IntervalsEstimate.estimate(xs, lv_, opt=False) for lv_ in lv]
                bks = [1/IntervalsEstimate.back(xs, lv_) for lv_ in lv]
                ex.append(min([1, exes[np.argmin(np.abs(np.subtract(exes, bks)))]]))
        else:
            xs, lv = gr.get_ln_attrs(frm, pathes)
            exes = [IntervalsEstimate.estimate(xs, lv_, opt=False) for lv_ in lv]
            bks = [1/IntervalsEstimate.back(xs, lv_) for lv_ in lv]
            ex = min([1, exes[np.argmin(np.abs(np.subtract(exes, bks)))]])

        return ex, np.max(di), n
