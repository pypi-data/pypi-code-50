GRAPH = (("file_name",),{'type':str,'help':"use graph file GRAPH",'metavar':'GRAPH'})
CONFIG = [
    ("nx",{'help':"count total length of edges in NX graph",'args':[GRAPH]}),
    ("gt",{'help':"count total length of edges in GT graph",'args':[GRAPH]}),
    ("npz",{'help':"count total length of edges in NPZ graph",'args':[GRAPH]})
]

def compute_length_gt(g):
    es = g.get_edges([g.ep.weight,g.ep.air])
    total_length = 0
    for e in es:
        if not e[3]:
            total_length += e[2]/1000.
    return total_length

def length_nx(file_name):
    from limic.util import start, end, status, load_pickled
    from limic.convert import transform_nx_gt
    start("Loading graph from",file_name)
    g = load_pickled(file_name)
    end()
    start("Transforming graph to rescaled GT format")
    h = transform_nx_gt(g,rescale=True)
    end()
    start("Computing length using rescaled GT")
    length = compute_length_gt(h)
    end('')
    status(length)

def length_gt(file_name):
    from limic.util import start, end, status, load_gt
    from limic.convert import transform_gt_npz, transform_npz_nx, transform_nx_gt
    start("Loading graph from",file_name)
    g = load_gt(file_name)
    end()
    start("Checking whether GT graph is rescaled")
    if g.gp.rescaled:
        status("YES")
        start("Computing length using GT")
        length = compute_length_gt(g)
        end('')
        status(length)
    else:
        status("NO (forcing reconversion)")
        start("Transforming graph to NPZ format")
        h = transform_gt_npz(g,penalize=20)
        end()
        start("Transforming graph to NX format")
        i = transform_npz_nx(h)
        end()
        start("Transforming graph to rescaled GT format")
        j = transform_nx_gt(i,rescale=True)
        end()
        start("Computing length using rescaled GT")
        length = compute_length_gt(j)
        end('')
        status(length)

def length_npz(file_name):
    from limic.util import start, end, status, load_npz
    from limic.convert import transform_npz_nx, transform_nx_gt
    start("Loading graph from",file_name)
    g = load_npz(file_name)
    end()
    start("Transforming graph to NX format")
    h = transform_npz_nx(g)
    end()
    start("Transforming graph to rescaled GT format")
    i = transform_nx_gt(h,rescale=True)
    end()
    start("Computing length using rescaled GT")
    length = compute_length_gt(i)
    end('')
    status(length)
