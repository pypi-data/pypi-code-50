GRAPH = (("file_name",),{'type':str,'help':"use graph file GRAPH",'metavar':'GRAPH'})
CACHE = (("file_name",),{'type':str,'help':"use cache file CACHE",'metavar':'CACHE'})
SOURCE = (("-s","--source"),{'type':int,'dest':'source_id','help':"set source power tower to SOURCE (default: random)",'metavar':'SOURCE'})
TARGET = (("-t","--target"),{'type':int,'dest':'target_id','help':"set target power tower to TARGET (default: random)",'metavar':'TARGET'})
OUT = (("-o","--output"),{'type':str,'dest':'out_file','help':"write path to OUT (default: stdout)",'metavar':'OUT'})

CONFIG = [
    ("npz",{'help':"route using NPZ graph",'args':[SOURCE,TARGET,OUT,GRAPH]}),
    ("nx",{'help':"route using NX graph",'args':[SOURCE,TARGET,OUT,GRAPH]}),
    ("gt",{'help':"route using GT graph",'args':[
        (("-i","--indirect"),{'action':'store_true','dest':'indirect','default':False,'help':"transform indirectly (default: False)"}),
        (("-p","--penalize"),{'type':int,'default':20,'dest':'penalize','help':"penalize air time by factor PENALTY",'metavar':'PENALTY'}),
        SOURCE,TARGET,OUT,GRAPH
    ]}),
    ("direct",{'help':"route directly",'args':[
        (("-s","--source"),{'type':int,'dest':'source_id','help':"set source power tower to SOURCE (default: random)",'metavar':'SOURCE','required':True}),
        (("-t","--target"),{'type':int,'dest':'target_id','help':"set target power tower to TARGET (default: random)",'metavar':'TARGET','required':True}),
        OUT,
        (("-u","--overpass-url"),{'type':str,'dest':'overpass_url','help':"define url for Overpass API to be URL (default: http://caracal.imada.sdu.dk/)",'metavar':'URL'}),
        (("-d","--disk-cache"),{'action':'store_true','dest':'disk_cache','default':False,'help':"use disk cache (default: False)"}),
        CACHE
    ]})
]

def astar_path_npz(lat, long, id2edges, edges_weight, edges_neighbor, source, target):
    from itertools import count
    from heapq import heappush, heappop
    from limic.util import haversine_distance
    targetlong = long[target]
    targetlat = lat[target]
    c = count()
    queue = [(0, next(c), source, 0, None)]
    enqueued = {}
    explored = {}
    while queue:
        _, __, curnode, dist, parent = heappop(queue)
        if curnode == target:
            path = [curnode]
            node = parent
            while node is not None:
                path.append(node)
                node = explored[node]
            path.reverse()
            return path
        if curnode in explored:
            if explored[curnode] is None:
                continue
            qcost, h = enqueued[curnode]
            if qcost < dist:
                continue
        explored[curnode] = parent
        left = id2edges[curnode]
        right = id2edges[curnode+1]
        for i in range(left,right):
            w = edges_weight[i]
            neighbor = edges_neighbor[i]
            ncost = dist + w
            if neighbor in enqueued:
                qcost, h = enqueued[neighbor]
                if qcost <= ncost:
                    continue
            else:
                h = haversine_distance(long[neighbor], lat[neighbor], targetlong, targetlat)
            enqueued[neighbor] = ncost, h
            heappush(queue, (ncost + h, next(c), neighbor, ncost, curnode))
    raise ValueError("node %s not reachable from %s" % (target, source))

def astar_npz(g,source_id=None,target_id=None):
    from limic.util import locate_by_id
    source, target = locate_by_id(g['ids'],source_id,target_id)
    try:
        path = astar_path_npz(g['lat'],g['long'],g['id2edges'],g['edges_weight'],g['edges_neighbor'],source,target)
    except ValueError as e:
        path = []
    ids = g['ids']
    return map(lambda x:ids[x],path)

def route_npz(file_name,source_id=None,target_id=None,out_file=None):
    from limic.util import start, end, save_path, load_npz
    start("Loading from",file_name)
    g = load_npz(file_name)
    end()
    start("Routing using NPZ")
    path = astar_npz(g,source_id,target_id)
    end()
    start("Saving path to",out_file)
    save_path(path,out_file)
    end()

def astar_nx(g,source_id=None,target_id=None):
    from limic.util import locate_by_id, haversine_distance
    from networkx import astar_path, NetworkXNoPath
    nodes = list(g.nodes())
    ids = list(map(lambda x:x[0],nodes))
    source, target = locate_by_id(ids,source_id,target_id)
    source, target = nodes[source], nodes[target]
    targetlat, targetlong = target[1], target[2]
    def distance(x,y):
        assert(target==y)
        return haversine_distance(longx=x[2],latx=x[1],longy=targetlong,laty=targetlat)
    try:
        path = astar_path(g,source,target,heuristic=distance)
    except NetworkXNoPath as e:
        path = []
    return map(lambda x:x[0],path)

def route_nx(file_name,source_id=None,target_id=None,out_file=None):
    from limic.util import start, end, load_pickled, save_path
    start("Loading from",file_name)
    g = load_pickled(file_name)
    end()
    start("Routing using NX")
    path = astar_nx(g,source_id,target_id)
    end()
    start("Saving path to",out_file)
    save_path(path,out_file)
    end()

def astar_gt(g,source_id=None,target_id=None):
    from graph_tool.search import astar_search, AStarVisitor, StopSearch
    from limic.util import locate_by_id, haversine_distance
    long = g.vp.long
    lat = g.vp.lat
    ids = list(map(lambda x:x[1],g.get_vertices([g.vp.id])))
    source, target = locate_by_id(ids,source_id,target_id)
    source, target = g.vertex(source), g.vertex(target)
    targetlong, targetlat = long[target], lat[target]
    class Visitor(AStarVisitor):
        def __init__(self, target):
            self.target = target
        def edge_relaxed(self, e):
            if e.target() == self.target:
                raise StopSearch()
    def distance(x):
        return haversine_distance(longx=long[x],latx=lat[x],longy=targetlong,laty=targetlat)
    dist, pred = astar_search(g, source, g.ep.weight, Visitor(target), heuristic=distance)
    path = []
    current = target
    while True:
        path.append(ids[int(current)])
        pre = g.vertex(pred[current])
        if pre == current:
            break
        current = pre
    path.reverse()
    return path

def route_gt(file_name,source_id=None,target_id=None,out_file=None,indirect=False,penalize=20):
    from limic.util import start, end, status, load_gt, save_path
    from limic.convert import transform_gt_npz
    start("Loading graph from",file_name)
    g = load_gt(file_name)
    end()
    start("Checking whether GT graph is rescaled")
    if g.gp.rescaled:
        indirect = True
        status("YES (forcing routing through NPZ)")
    else:
        status("NO")
    if indirect:
        start("Transforming graph to NPZ format")
        h = transform_gt_npz(g,penalize)
        end()
        start("Routing using NPZ")
        path = astar_npz(h,source_id,target_id)
        end()
    else:
        start("Routing using GT")
        path = astar_gt(g,source_id,target_id)
        end()
    start("Saving path to",out_file)
    save_path(path,out_file)
    end()

def reconstruct_path_direct(current):
    path = [current.tower.id]
    cost = current.g
    while current.origin:
        current = current.origin
        path.append(current.tower.id)
    path.reverse()
    return cost, path

def astar_tower_direct(start,end,max_fly=1000,eps=0.01,safe_dist=100,penalty=20,prec=1):
    class node:
        def __init__(self,f,g,tower,origin):
            self.f = f
            self.g = g
            self.tower = tower
            self.origin = origin
        def __lt__(self,other):
            return self.f < other.f
        def __repr__(self):
            return "node(f="+repr(self.f)+",g="+repr(self.g)+",tower="+repr(self.tower)+",origin="+repr(self.origin.tower.id if self.origin else self.origin)+")"
    from limic.overpass import find_all_neighbours
    from heapq import heappop, heappush, heapify
    from limic.util import distance, verbosity
    from math import inf
    latlon2id = {}
    minusid = [0]
    start_node = node(distance(start.latlon,end.latlon)*prec,0,start,None)
    nodes = {start.id : start_node}
    todo = [start_node]
    while todo:
        if verbosity >= 4: print("*******************\n"+str(todo)+"\n***************")
        if verbosity >= 4: print("*******************\n"+str(sorted(todo))+"\n***************")
        current = heappop(todo)
        if verbosity >= 2: print("visiting",current.f,current.tower.id,current.tower.latlon)
        if verbosity >= 2: print("full node",current)
        if current.tower.id == end.id:
            return reconstruct_path_direct(current)
        if verbosity >=2:
            print("CURRENT PATH:\nnode(id:"+(",".join(map(str,reconstruct_path(current)[1])))+");out;")
            print("FRONT:\nnode(id:"+(",".join(map(lambda n:str(n.tower.id),todo)))+");out;")
        neighbours = find_all_neighbours(current.tower, max_fly, eps, safe_dist, minusid, latlon2id, penalty)
        for neighbour in neighbours:
            g = current.g+neighbour.dist
            neighbour_node = nodes.get(neighbour.tower.id,node(None,inf,neighbour.tower,None))
            if g < neighbour_node.g:
                if not neighbour_node.f:
                    nodes[neighbour.tower.id] = neighbour_node
                must_add = neighbour_node not in todo
                neighbour_node.origin = current
                neighbour_node.g = g
                neighbour_node.f = g+distance(neighbour.tower.latlon,end.latlon)*prec
                if must_add:
                    if verbosity >= 3: print("added",neighbour_node)
                    heappush(todo,neighbour_node)
                else:
                    if verbosity >= 3: print("modified",neighbour_node)
                heapify(todo)
    return inf, None

def astar_direct(start,end):
    from limic.overpass import tower_by_id
    start_tower = tower_by_id(start)
    end_tower = tower_by_id(end)
    cost, path = astar_tower_direct(start_tower,end_tower)
    path = [start]+path+[end]
    return cost, path
    
def route_direct(file_name,source_id=None,target_id=None,out_file=None,overpass_url=None,disk_cache=False):
    from limic.util import start, end, status, file_size, load_pickled, save_pickled, save_path, set_disk_cache
    if disk_cache:
        start("Using disk cache",file_name)
        set_disk_cache(file_name)
    from limic.overpass import region, set_server
    if disk_cache:
        status("OK")
    from os.path import exists
    from os import replace
    if not disk_cache and exists(file_name):
        start("Loading",file_name)
        region.backend._cache = load_pickled(file_name)
        end('')
        file_size(file_name)
        len_cache = len(region.backend._cache)
    start("Routing using direct algorithm")
    set_server(overpass_url)
    cost,path = astar_direct(source_id,target_id)
    end('')
    status(cost)
    start("Saving path to",out_file)
    save_path(path,out_file)
    end()
    if not disk_cache and len_cache != len(region.backend._cache):
        file_name_tmp = file_name+".tmp"
        start("Saving to",file_name,"via",file_name_tmp)
        save_pickled(file_name_tmp,region.backend._cache)
        replace(file_name_tmp,file_name)
        end('')
        file_size(file_name)
