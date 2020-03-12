import os
import sys
from feyn import QLattice

def test_update():
    good=0
    simple=0
    runs = 30
    steps = 4
    for _ in range(runs):
        lt = QLattice(reset=True)

        r1 = lt.add_register("Age", "cont")
        r2 = lt.add_register("Smoker", "cont")
        r3 = lt.add_register("insurable", "cont")

        r4 = lt.add_register("a", "cont")
        r5 = lt.add_register("b", "cont")
        r6 = lt.add_register("c", "cont")
        r7 = lt.add_register("d", "cont")

        qgraph = lt.get_qgraph([r1, r2, r4, r5, r6, r7], r3, steps=steps)

        the_graph = None
        for g in qgraph.graphs:
            if g.size>5 and g.edge_count>8:
                the_graph = g
                break

        
        if the_graph:
            lt.update(the_graph)
            new_qgraph = lt.get_qgraph([r1, r2, r4, r5, r6, r7], r3, steps=steps)

            if the_graph in new_qgraph.graphs:
                good+=1
                print("+", end="")
            else:
                print("-", end="")
        else:
            print("s", end="")
            simple +=1
        sys.stdout.flush()

    print("\nGood %i, Simple: %i, Bad: %i"%(good, simple, runs-good-simple))

test_update()
