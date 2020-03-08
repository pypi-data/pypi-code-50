IN = (("file_name_in",),{'type':str,'help':"graph file to convert",'metavar':'GRAPH'})
OUT = (("file_name_out",),{'type':str,'help':"graph file to save to",'metavar':'GRAPH'})
INC = (("file_name_in",),{'type':str,'help':"cache file to convert",'metavar':'CACHE'})
OUTC = (("file_name_out",),{'type':str,'help':"cache file to save to",'metavar':'CACHE'})
INDIRECT = (("-i","--indirect"),{'action':'store_true','dest':'indirect','default':False,'help':"transform indirectly via GT"})
RESCALE = (("-r","--rescale"),{'action':'store_true','default':False,'dest':'rescale','help':"rescale to int32"})
PENALIZE = (("-p","--penalize"),{'type':int,'default':20,'dest':'penalize','help':"penalize air time by factor PENALTY",'metavar':'PENALTY'})
CONFIG = [
    ("nx",{'help':"convert NX graph",'args':[
        ("gt",{'help':"convert to GT graph",'args':[
            RESCALE,IN,OUT
        ]}),
        ("npz",{'help':"convert to NPZ graph",'args':[
            INDIRECT,RESCALE,PENALIZE,IN,OUT
        ]}),
    ]}),
    ("gt",{'help':"convert GT graph",'args':[
        ("nx",{'help':"convert to NX graph",'args':[
            PENALIZE,IN,OUT
        ]}),
        ("npz",{'help':"convert to NPZ graph",'args':[
            PENALIZE,IN,OUT
        ]})
    ]}),
    ("npz",{'help':"convert NPZ graph",'args':[
        ("nx",{'help':"convert to NX graph",'args':[
            IN,OUT
        ]}),
        ("gt",{'help':"convert to GT graph",'args':[
            RESCALE,IN,OUT
        ]})
    ]}),
    ("cache",{'help':"convert pickled cache",'args':[
        ("dbm",{'help':"convert to DBM cache",'args':[
            INC,OUTC
        ]})
    ]}),
    ("dbm",{'help':"convert DBM cache",'args':[
        ("cache",{'help':"convert to pickled cache",'args':[
            INC,OUTC
        ]})
    ]})
]

def transform_nx_gt(g,rescale=False):
    from graph_tool import Graph
    from limic.util import haversine_distance
    h = Graph(directed=False)
    h.vp.id = h.new_vertex_property("int64_t")
    if rescale:
        h.vp.lat = h.new_vertex_property("int32_t")
        h.vp.long = h.new_vertex_property("int32_t")
        h.ep.weight = h.new_edge_property("int32_t")
        h.ep.air = h.new_edge_property("bool")
    else:
        h.vp.lat = h.new_vertex_property("double")
        h.vp.long = h.new_vertex_property("double")
        h.ep.weight = h.new_edge_property("float")
    h.gp.rescaled = h.new_graph_property("bool")
    h.gp.rescaled = rescale
    pos2vertex = {}
    intersection_id = 0
    for n in g.nodes():
        v = h.add_vertex()
        pos2vertex[n[1],n[2]] = v
        if n[0] < 0:
            intersection_id -= 1
            h.vp.id[v] = intersection_id
        else:
            h.vp.id[v] = n[0]
        h.vp.lat[v] = int(n[1]*10000000) if rescale else n[1]
        h.vp.long[v] = int(n[2]*10000000) if rescale else n[2]
    for n,m,w in g.edges.data("weight"):
        e = h.add_edge(pos2vertex[n[1],n[2]],pos2vertex[m[1],m[2]])
        if rescale:
            w2 = haversine_distance(longx=n[2],latx=n[1],longy=m[2],laty=m[1])
            h.ep.air[e] = w2 < 0.9*w
            if h.ep.air[e]:
                w = w2
        h.ep.weight[e] = int(w*1000) if rescale else w
    return h

def convert_nx_gt(file_name_in,file_name_out,rescale=False):
    from limic.util import start, end, file_size, load_pickled, save_gt
    start("Loading graph from",file_name_in)
    g = load_pickled(file_name_in)
    end('')
    file_size(file_name_in)
    start("Initialzing id mapping and neighbours map")
    h = transform_nx_gt(g,rescale)
    end()
    start("Saving to",file_name_out)
    save_gt(file_name_out,h)
    end('')
    file_size(file_name_out)

def transform_nx_npz(g):
    from numpy import array, int64, int32, float64, float32
    vs = g.nodes()
    es = g.edges.data("weight")
    ids = [None]*len(vs)
    lat = [None]*len(vs)
    long = [None]*len(vs)
    id2edges = []
    edges_weight = []
    edges_neighbor = []
    v2index = {}
    index = 0
    ns = []
    for v in vs:
        v2index[v] = index
        ids[index] = v[0]
        lat[index] = v[1]
        long[index] = v[2]
        index += 1
        ns.append([])
    for e in es:
        w = e[2]
        f = v2index[e[0]]
        t = v2index[e[1]]
        ns[f].append((t,w))
        ns[t].append((f,w))
    counter = 0
    for n in ns:
        id2edges.append(counter)
        edges_weight.extend(map(lambda x:x[1],n))
        edges_neighbor.extend(map(lambda x:x[0],n))
        counter += len(n)
    id2edges.append(counter)
    h = {}
    h['ids'] = array(ids,dtype=int64)
    h['lat'] = array(lat,dtype=float64)
    h['long'] = array(long,dtype=float64)
    h['id2edges'] = array(id2edges,dtype=int32)
    h['edges_weight'] = array(edges_weight,dtype=float32)
    h['edges_neighbor'] = array(edges_neighbor,dtype=int32)
    return h

def convert_nx_npz(file_name_in,file_name_out,indirect=False,rescale=False,penalize=20):
    from limic.util import start, end, file_size, load_pickled, save_npz
    start("Loading graph from",file_name_in)
    g = load_pickled(file_name_in)
    end('')
    file_size(file_name_in)
    if indirect:
        start("Transforming to GT format")
        i = transform_nx_gt(g,rescale)
        end()
        start("Transforming to NPZ format")
        h = transform_gt_npz(i,penalize)
        end()
    else:
        start("Transforming to NPZ format")
        h = transform_nx_npz(g)
        end()
    start("Saving to",file_name_out)
    save_npz(file_name_out,h)
    end('')
    file_size(file_name_out)            

def convert_gt_nx(file_name_in,file_name_out,penalize=20):
    from limic.util import start, end, file_size, load_gt, save_pickled
    start("Loading graph from",file_name_in)
    g = load_gt(file_name_in)
    end('')
    file_size(file_name_in)
    start("Transforming to NPZ format")
    i = transform_gt_npz(g,penalize)
    end()
    start("Transforming to NX format")
    h = transform_npz_nx(i)
    end()
    start("Saving to",file_name_out)
    save_pickled(file_name_out,h)
    end('')
    file_size(file_name_out)            

def transform_gt_npz(g,penalize=20):
    from numpy import array, int64, int32, float64, float32
    vs = g.get_vertices([g.vp.id,g.vp.lat,g.vp.long])
    rescale = g.gp.rescaled
    if rescale:
        es = g.get_edges([g.ep.weight,g.ep.air])
    else:
        es = g.get_edges([g.ep.weight])
    ids = [None]*len(vs)
    lat = [None]*len(vs)
    long = [None]*len(vs)
    id2edges = []
    edges_weight = []
    edges_neighbor = []
    ns = []
    for v in vs:
        index = v[0] if rescale else int(v[0])
        ids[index] = v[1]
        lat[index] = v[2]/(10000000. if rescale else 1)
        long[index] = v[3]/(10000000. if rescale else 1)
        ns.append([])
    for e in es:
        w = e[2]/((1000.*(penalize if e[3] else 1)) if rescale else 1)
        f = e[0] if rescale else int(e[0])
        t = e[1] if rescale else int(e[1])
        ns[f].append((t,w))
        ns[t].append((f,w))
    counter = 0
    for n in ns:
        id2edges.append(counter)
        edges_weight.extend(map(lambda x:x[1],n))
        edges_neighbor.extend(map(lambda x:x[0],n))
        counter += len(n)
    id2edges.append(counter)
    h = {}
    h['ids'] = array(ids,dtype=int64)
    h['lat'] = array(lat,dtype=float64)
    h['long'] = array(long,dtype=float64)
    h['id2edges'] = array(id2edges,dtype=int32)
    h['edges_weight'] = array(edges_weight,dtype=float32)
    h['edges_neighbor'] = array(edges_neighbor,dtype=int32)
    return h

def convert_gt_npz(file_name_in,file_name_out,penalize=20):
    from limic.util import start, end, file_size, load_gt, save_npz
    start("Loading graph from",file_name_in)
    g = load_gt(file_name_in)
    end('')
    file_size(file_name_in)
    start("Initialzing id mapping and neighbours map")
    h = transform_gt_npz(g,penalize)
    end()
    start("Saving to",file_name_out)
    save_npz(file_name_out,h)
    end('')
    file_size(file_name_out)

def transform_npz_nx(g):
    ids = g['ids']
    lat = g['lat']
    long = g['long']
    id2edges = g['id2edges']
    edges_weight = g['edges_weight']
    edges_neighbor = g['edges_neighbor']
    from networkx import Graph
    h = Graph()
    index2node = {}
    for index in range(len(ids)):
        node = (ids[index],lat[index],long[index])
        index2node[index] = node
        h.add_node(node)
    for index in range(len(ids)):
        left = id2edges[index]
        right = id2edges[index+1]
        me = index2node[index]
        for i in range(left,right):
            w = edges_weight[i]
            neighbor = edges_neighbor[i]
            h.add_edge(me,index2node[neighbor],weight=w)
    return h

def convert_npz_nx(file_name_in,file_name_out):
    from limic.util import start, end, file_size, save_pickled, load_npz
    start("Loading graph from",file_name_in)
    g = load_npz(file_name_in)
    end('')
    file_size(file_name_in)
    start("Transforming to NX format")
    h = transform_npz_nx(g)
    end()
    start("Saving to",file_name_out)
    save_pickled(file_name_out,h)
    end('')
    file_size(file_name_out)            

def convert_npz_gt(file_name_in,file_name_out,rescale=False):
    from limic.util import start, end, file_size, save_gt, load_npz
    start("Loading graph from",file_name_in)
    g = load_npz(file_name_in)
    end('')
    file_size(file_name_in)
    start("Transforming to NX format")
    i = transform_npz_nx(g)
    end()
    start("Transforming to GT format")
    h = transform_nx_gt(i,rescale)
    end()
    start("Saving to",file_name_out)
    save_gt(file_name_out,h)
    end('')
    file_size(file_name_out)            

def convert_cache_dbm(file_name_in,file_name_out):
    from limic.util import start, end, file_size, status, load_pickled
    from dbm.gnu import open as dopen
    from os.path import exists
    from pickle import dumps
    start("Loading from",file_name_in)
    d = load_pickled(file_name_in)
    end('')
    file_size(file_name_in)
    start("Opening database",file_name_out)
    if not exists(file_name_out):
        db = dopen(file_name_out,"c")
        db.close()
    db = dopen(file_name_out,"c")
    end('')
    file_size(file_name_out)
    start("Computing set of entries to save")
    for key in db.keys():
        del d[key.decode("utf-8")]
    status(len(d))
    start("Saving entries to",file_name_out)
    for key, val in d.items():
        db[key.encode("utf-8")] = dumps(val)
    db.close()
    end('')
    file_size(file_name_out)

def convert_dbm_cache(file_name_in,file_name_out):
    from limic.util import start, end, file_size, status, save_pickled
    from dbm.gnu import open as dopen
    from pickle import loads
    start("Opening database",file_name_in)
    db = dopen(file_name_in,"r")
    end('')
    file_size(file_name_in)
    start("Converting to dictionary")
    d = {}
    for key in db.keys():
        d[key.decode("utf-8")] = loads(db[key])
    db.close()
    end()
    start("Saving to",file_name_out)
    save_pickled(file_name_out,d)
    end('')
    file_size(file_name_out)
