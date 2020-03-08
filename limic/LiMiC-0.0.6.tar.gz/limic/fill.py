CONFIG = [
    (("-a","--area"),{'type':str,'dest':'area','required':True,'help':"set area to extract to AREA",'metavar':'AREA'}),
    (("-w","--max-workers"),{'type':int,'dest':'max_workers','help':"set maximum number of parallel workers to WORKERS",'metavar':'WORKERS'}),
    (("-u","--overpass-url"),{'type':str,'dest':'overpass_url','help':"define url for Overpass API to be URL",'metavar':'URL'})
]

def cache_tower(tower, around, eps, safe_dist):
    from limic.overpass import find_all_neighbours
    find_all_neighbours(tower,around,eps,safe_dist,[0],{},20)

def fill(overpass_url,file_name=None,area=None,around=1000,eps=0.01,safe_dist=100,penalty=20,max_workers=None):
    from limic.overpass import set_server, pylon, region, get_towers_by_area
    from limic.util import start, end, file_size, load_pickled, save_pickled, verbosity, get_failed, set_failed
    from networkx import Graph, relabel_nodes
    from os import replace, cpu_count
    from os.path import exists
    from concurrent.futures import ThreadPoolExecutor, wait
    from signal import signal, SIGINT
    if not area and not file_name:
        print("ERROR: specify at least area or cache name!")
        from sys import exit
        exit(-1)
    if not area:
        area = file_name.split(".")[1]
    if not file_name:
        file_name = "cache."+area
    if not max_workers:
        max_workers = cpu_count()*4
    if verbosity >= 2: print("Using",max_workers,"workers!")
    if exists(file_name):
        start("Loading",file_name)
        region.backend._cache = load_pickled(file_name)
        end('')
        file_size(file_name)
    len_cache = len(region.backend._cache)
    start("Querying overpass for",area)
    set_server(overpass_url)
    towers = get_towers_by_area(area)
    end()
    fs = []
    executor = ThreadPoolExecutor(max_workers=max_workers)
    interrupt = 0
    def shutdown(sig,frame):
        nonlocal interrupt
        interrupt += 1
        print("Shutting down ...")
        for f in fs:
            f.cancel()
        print("Cancelled all futures ...")
        running = len(fs)
        total = running
        while running:
            print("Waiting for",running,"processes to shut down ...")
            wait(fs,timeout=60)
            running = sum(0 if f.done() else 1 for f in fs)
        if len_cache != len(region.backend._cache):
            file_name_tmp = file_name+"."+str(interrupt)
            start("Emergency saving to",file_name_tmp)
            save_pickled(file_name_tmp,region.backend._cache)
            end('')
            file_size(file_name_tmp)
    signal(SIGINT,shutdown)
    set_failed(True)
    while get_failed():
        set_failed(False)
        for tower in towers:
            fs.append(executor.submit(cache_tower, tower, around, eps, safe_dist))
        running = len(fs)
        total = running
        while running:
            print("Waiting for",running,"out of",total,"processes ...")
            wait(fs,timeout=60)
            running = sum(0 if f.done() else 1 for f in fs)
    if len_cache != len(region.backend._cache):
        file_name_tmp = file_name+".tmp"
        start("Saving to",file_name,"via",file_name_tmp)
        save_pickled(file_name_tmp,region.backend._cache)
        replace(file_name_tmp,file_name)
        end('')
        file_size(file_name)
