# arguments
def parse_config(config, parser, prefix):
    subs = None
    for a,b in config:
        if isinstance(a,str):
            if not subs:
                subs = parser.add_subparsers(dest='command',required=True)
            args = b.pop('args') if 'args' in b else None
            sub = subs.add_parser(a,**b)
            if not prefix:
                sub.set_defaults(mod="limic."+a)
            sub.set_defaults(func="_".join(prefix+[a]))
            if args:
                parse_config(args, sub, prefix+[a])
        else:
            parser.add_argument(*a, **b)

# timing and informational messages
import time
verbosity = 1
def set_verbosity(level):
    if level is not None:
        global verbosity
        verbosity = level
disk_cache = None
def get_disk_cache():
    return disk_cache
def set_disk_cache(file_name):
    global disk_cache
    disk_cache = file_name
failed = False
def set_failed(status):
    global failed
    failed = status
def get_failed():
    return failed
started = 0
def start(*msg):
    if verbosity > 0:
        global started
        if msg:
            print(" ".join(map(str,msg)).ljust(60),"... ",end='',flush=True)
        started = time.time()
def end(end='\n'):
    if verbosity > 0:
        global started
        print("%.3f seconds   " % (time.time()-started),end=end,flush=True)
        started = time.time()
def file_size(file_name):
    from os import stat
    if verbosity > 0:
        print("%.0fK" % (stat(file_name).st_size/1024))
def status(msg):
    if verbosity > 0:
        print(msg)


# distance between GPS positions
from math import radians, cos, sin, asin, sqrt
def haversine_distance(longx,latx,longy,laty):
    lon1, lat1, lon2, lat2 = radians(longx), radians(latx), radians(longy), radians(laty)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    m = 6371008.7714*c
    return m
def distance(x,y):
    return haversine_distance(longx=x[1],latx=x[0],longy=y[1],laty=y[0])

# working with different graph formats
def nx_is_equal(g,h,isomorphic=False):
    from networkx.algorithms.isomorphism import is_isomorphic
    if isomorphic:
        return is_isomorphic(g,h,lambda ga,ha:ga==ha)
    g_edges, h_edges = g.edges(), h.edges()
    return all(h_edge in g_edges for h_edge in h_edges) and all(g_edge in h_edges for g_edge in g_edges)
def locate_by_id(ids,source_id=None,target_id=None,length=None):
    if not length:
        length = len(ids)
    from random import randrange
    source = None if source_id else randrange(length)
    target = None if target_id else randrange(length)
    for i in range(length):
        if source:
            if target:
                return source,target
            if ids[i] == target_id:
                target = i
                continue
        else:
            if target:
                if ids[i] == source_id:
                    source = i
                    continue
            else:
                if ids[i] == source_id:
                    source = i
                    continue
                if ids[i] == target_id:
                    target = i
                    continue
    assert False, "cannot resolve all ids: %s,%s -> %s,%s" % tuple(map(str,(source_id,target_id,source,target)))

# loading and saving different formats
def save_pickled(file_name,g,compression="gzip",protocol=4):
    from pickle import dump
    if compression:
        from gzip import open as gopen
        f = gopen(file_name,"wb")
    else:
        f = open(file_name,"wb")
    dump(g,f,protocol=protocol)
    f.close()
def load_pickled(file_name,compression="gzip"):
    from pickle import Unpickler
    class RenameUnpickler(Unpickler):
        def find_class(self, module, name):
            renamed_module = module
            if module == "overpass":
                renamed_module = "limic.overpass"
            return super(RenameUnpickler, self).find_class(renamed_module, name)
    #from pickle import load
    def load(f):
        return RenameUnpickler(f).load()
    if compression:
        from gzip import open as gopen
        f = gopen(file_name,"rb")
    else:
        f = open(file_name,"rb")
    g = load(f)
    f.close()
    return g
def save_gt(file_name,g):
    g.save(file_name,fmt="gt")
def load_gt(file_name):
    from graph_tool import Graph
    g = Graph()
    g.load(file_name,fmt="gt")
    return g
def load_npz(file_name):
    from numpy import load
    return load(file_name)
def save_npz(file_name,g):
    from numpy import savez
    savez(file_name,**g)
def save_path(path,out_file=None):
    from sys import stdout
    file = open(out_file,"w") if out_file else stdout
    print("node(id:"+",".join(map(str,path))+");out;",file=file)
