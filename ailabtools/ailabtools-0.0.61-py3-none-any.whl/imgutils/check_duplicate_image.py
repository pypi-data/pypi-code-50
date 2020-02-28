import os
from multiprocessing import cpu_count
from collections import defaultdict
from glob import glob

import numpy as np

import nmslib
import imagehash
from ailabtools.ailab_multiprocessing import pool_worker
import networkx as nx
from PIL import Image

# __all__ = ['get_connected_component', 'baz']

#SUPPORT FUNCTIONS
def get_hash(path):
    try:
        im = Image.open(path).convert('L')
        hash_flattened = imagehash.phash(im).hash.flatten()
        hash_flattened_to_str = ' '.join([str(int(item)) for item in hash_flattened])
        return hash_flattened_to_str
    except Exception as e:
        return e
    
#get_connected_component
def DFSUtil(temp, v, visited, vertex_adj_dict):
    visited[v] = True
    temp.append(v)
    for v_adj in vertex_adj_dict[v]:
        if visited[v_adj] == False:
            temp = DFSUtil(temp, v_adj, visited, vertex_adj_dict)
    return temp

def get_connected_component(edges):
    vertex_adj_dict = defaultdict(lambda: set())
    for edge in edges:
        vertex_adj_dict[edge[0]].add(edge[1])
        vertex_adj_dict[edge[1]].add(edge[0])

    visited = {}
    for v in vertex_adj_dict:
        visited[v] = False

    connected_components = []
    for v in vertex_adj_dict:
        if visited[v] == False:
            temp = []
            connected_components.append(DFSUtil(temp, v, visited, vertex_adj_dict))
    return connected_components
#get_connected_component

def build_index(hashes):
    index = nmslib.init(method='hnsw', 
                        space='bit_hamming', 
                        dtype=nmslib.DistType.INT, 
                        data_type=nmslib.DataType.OBJECT_AS_STRING)

    index.addDataPointBatch(hashes)
    index.createIndex({'post': 2}, print_progress=True)
    return index

#CHECK INPUT FUNCTIONS
def is_PIL_readable(path):
    try:
        Image.open(path).convert('RGB')
        return True
    except:
        return False
    
def check_path(path):
    return {'is_file': os.path.isfile(path), 'is_image': is_PIL_readable(path)}

def check_path_with_report(path_infos):
    check_path_results = pool_worker(check_path, [item[1] for item in path_infos])
    problem_dict = {}
    for path_info, check_path_result in zip(path_infos, check_path_results):
        path_type, path = path_info
        if not np.all(list(check_path_result.values())):
            problem_dict[path] = {'path_source': path_type}
            if not check_path_result['is_file']:
                problem_dict[path]['prolems'] = 'is_not_file'
                #dont need to check path is image or not if it is not file
                continue
            if not check_path_result['is_image']: 
                problem_dict[path]['prolems'] = 'is_not_image'
    return problem_dict

#CHECK DUPLICATE FUNCTIONS
def check_dup_internal(new_hashes, ref_names, threshold, num_threads, k):    
    index = build_index(new_hashes)
    neighbours = index.knnQueryBatch(new_hashes, k=k, num_threads=num_threads)
    edges = set()
    for i, item in enumerate(neighbours):
        ids, distances = item
        for id, distance in zip(ids, distances):
            if distance <= threshold:
                if i != id:
                    edges.add((i, id))
            else:
                break
                
    G = nx.Graph()
    G.add_nodes_from(range(len(new_hashes)))
    for edge in edges:
        G.add_edge(*edge)
    connected_components = nx.connected_components(G)
    
    dup_dict = {}
    for connected_component in connected_components:
        min_idx = sorted(connected_component)[0]
        for idx in connected_component:
            if idx != min_idx:
                dup_dict[ref_names[idx]] = ref_names[min_idx]

    return dup_dict

def check_dup_internal_loop(new_hashes, threshold, num_threads, k):
    run_hashes = new_hashes.copy()
    remain_indexes = np.arange(len(run_hashes))
    
    dup_dicts = []
    while True:
        dup_dict = check_dup_internal(run_hashes, remain_indexes, threshold, num_threads, k)
        if dup_dict == {}:
            break
        dup_dicts.append(dup_dict)
        remain_indexes = sorted(set(remain_indexes) - set(dup_dict.keys()))
        run_hashes = [new_hashes[idx] for idx in sorted(remain_indexes)]
        
    dup_dict_merged = {}
    for i in np.arange(len(new_hashes)):
        idx_dup = i
        for dup_dict in dup_dicts:
            if idx_dup in dup_dict:
                idx_dup = dup_dict[idx_dup]
        if idx_dup !=  i:
            dup_dict_merged[i] = idx_dup
            
    return dup_dict_merged


#MAIN FUNCTION
def check_dup_perception(new_paths, old_paths=None, threshold=5, num_threads=None, k=100):
    """Extract distinct image

    Parameters
    ----------
    new_paths : list
        path of images to check duplicate internal
    old_paths: list
        path of images to check new_paths duplicated or not
    threshold: int ~ [0, 64]
        minimum distant of average hash of frame (http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html)
    num_threads: int or None
        number of worker, if None use all CPU
    k: int
        number of nearest neighbor to check, should be 100

    Returns
    -------
    list of paths of distinct image
    """

    if num_threads is None:
        num_threads = cpu_count()
    path_infos = []
    for path in new_paths:
        path_infos.append(("new_paths", path))
    if old_paths is not None:
        for path in old_paths:
            path_infos.append(("old_paths", path))
            
    print("CHECKING INPUT DATA:")
    problem_dict = check_path_with_report(path_infos)
    if problem_dict != {}:
        print("ERROR INPUT DATA")
        print("RETURN PROBLEM DICTIONARY")
        return problem_dict
    else:
        print("INPUT OK!")
    
    print("CALCULATE HASH OF NEW PATHS")
    new_hashes = pool_worker(get_hash, new_paths)
    print("DONE")
    print("CHECK DUP INTERNAL")
    dup_internal_dict = check_dup_internal_loop(new_hashes, threshold, num_threads, k)
    print("DONE")
    dup_new_dict = {}
    for idx in dup_internal_dict:
        dup_new_dict[new_paths[idx]] = new_paths[dup_internal_dict[idx]]
    if old_paths is None:
        return dup_new_dict
    
    remain_ids = sorted(set(np.arange((len(new_hashes)))) - set(dup_internal_dict))
    new_hashes = np.array(new_hashes)[remain_ids]
    
    print("CALCULATE HASH OF OLD PATHS")
    old_hashes = pool_worker(get_hash, old_paths)
    print("DONE")
    print("CHECK DUP EXTERNAL")
    index = build_index(old_hashes)
    neighbours = index.knnQueryBatch(list(new_hashes), k=k, num_threads=num_threads)
    dup_old_dict = {}
    for i_new, item in enumerate(neighbours):
        ids, distances = item
        if distances[0] <= threshold:
            dup_old_dict[new_paths[remain_ids[i_new]]] = old_paths[ids[0]]
    print("DONE")
            
    dup_dict_merged = {}
    for path in new_paths:
        run_path = path
        
        if run_path in dup_new_dict:
            run_path = dup_new_dict[run_path]
        
        is_old = False
        if run_path in dup_old_dict:
            run_path = dup_old_dict[run_path]
            is_old = True

        if run_path != path:
            dup_dict_merged[path] = (run_path, 'old_path' if is_old else 'new_path')
    print("RETURN DUPLICATED PATHS DICTIONARY")
    return dup_dict_merged