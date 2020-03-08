CONFIG = [
    (("-u","--overpass-url"),{'type':str,'dest':'overpass_url','help':"define url for Overpass API to be URL",'metavar':'URL'}),
    (("-a","--area"),{'type':str,'dest':'area','help':"set area to extract to AREA",'metavar':'AREA'}),
    (("file_name_in",),{'type':str,'help':"read map data from cache file CACHE",'metavar':'CACHE'}),
    (("file_name_out",),{'type':str,'help':"save extracted graph to file GRAPH",'metavar':'GRAPH'})    
]

def prune_incomplete(g):
    to_prune = set()
    for k in g.nodes():
        for l in g.neighbors(k):
            if k < l:
                for m in g.neighbors(l):
                    if g.has_edge(k,m) and g[k][l]['weight'] > g[k][m]['weight']+g[m][l]['weight']:
                        to_prune.add((k,l))
    for u,v in to_prune:
        if g.has_edge(u,v):
            g.remove_edge(u,v)

def prune_complete(g):
    from networkx import astar_path_length
    to_prune = set()
    for k in g.nodes():
        for l in g.neighbors(k):
            if k < l and g[k][l]['weight'] > astar_path_length(g,k,l):
                to_prune.add((k,l))
    for u,v in to_prune:
        if g.has_edge(u,v):
            g.remove_edge(u,v)

def extract(file_name_in,file_name_out,overpass_url,area=None,around=1000,eps=0.01,safe_dist=100,penalty=20):
    from limic.overpass import distance, find_all_neighbours, is_safe, set_server, pylon, region, get_towers_by_area
    from limic.util import start, end, file_size, load_pickled, save_pickled, verbosity
    from networkx import Graph, relabel_nodes
    from os import replace
    start("Loading",file_name_in)
    region.backend._cache = load_pickled(file_name_in)
    len_cache = len(region.backend._cache)
    end('')
    file_size(file_name_in)
    if not area:
        area = file_name_in.split(".")[1]
    start("Querying overpass for",area)
    set_server(overpass_url)
    towers = get_towers_by_area(area)
    end()
    start("Building safe nodes")
    g=Graph()
    for tower in towers:
        if not is_safe(tower,safe_dist):
            if verbosity >= 2: print("NOT safe!")
        else:
            g.add_node(tower)
    end('')
    total = len(g.nodes())
    if verbosity >= 1:
        print(total)
    start("Building edges")
    count = 0
    neighbours2intersection = {}
    minusid = [0]
    latlon2id = {}
    for tower in list(g.nodes()):
        count += 1
        if verbosity >= 2: print(count,"of",total)
        for neighbour in find_all_neighbours(tower,around,eps,safe_dist,minusid,latlon2id,penalty):
            if neighbour.tower in g or neighbour.tower.id < 0:
                if verbosity >= 2: print("adding",neighbour)
                g.add_edge(tower,pylon(neighbour.tower.id,neighbour.tower.latlon),weight=neighbour.dist)
                if neighbour.tower.id < 0:
                    for intersection in neighbours2intersection.setdefault(neighbour.tower.neighbours,[]):
                        if intersection.latlon != neighbour.tower.latlon:
                            if verbosity >= 2: print("double intersection:",intersection.latlon,neighbour.tower.latlon)
                            g.add_edge(intersection,neighbour.tower,weight=distance(intersection.latlon,neighbour.tower.latlon))
                    neighbours2intersection[neighbour.tower.neighbours].append(neighbour.tower)
    end('')
    if verbosity >= 1:
        print(len(g.edges()))
    if len_cache != len(region.backend._cache):
        file_name_tmp = file_name_in+".tmp"
        start("Saving to",file_name_in,"via",file_name_tmp)
        save_pickled(file_name_tmp,region.backend._cache)
        replace(file_name_tmp,file_name_in)
        end('')
        file_size(file_name_in)
    start("Prune redundant edges (incomplete)")
    prune_incomplete(g)
    end('')
    if verbosity >= 1:
        print(len(g.edges()))
    start("Prune redundant edges (complete)")
    prune_complete(g)
    end('')
    if verbosity >= 1:
        print(len(g.edges()))
    start("Cleaning up graph")
    relabel = dict(map(lambda tower:(tower,(tower.id,tower.latlon[0],tower.latlon[1])),g.nodes()))
    relabel_nodes(g,relabel,copy=False)
    end()
    start("Saving graph to",file_name_out)
    save_pickled(file_name_out,g)
    end('')
    file_size(file_name_out)
