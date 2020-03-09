import numpy as np
from multiprocessing.pool import Pool
from threading import Event, Lock, Semaphore
import traceback
import multiprocessing

def error(msg, *args):
    return multiprocessing.get_logger().error(msg, *args)

#import collections
import igraph
import pandas as pd
import timeit
#import graphs_aux
from sklearn.neighbors.kde import KernelDensity
from numpy import linalg as LA
from sklearn import svm, datasets
from scipy import stats
#from pathlib2 import Path
import os
import sys


def entropy(a, b, n):
    from scipy.special import xlogy
    p0 = a / n
    p1 = b / n
    return -xlogy(p0, p0) - xlogy(p1, p1)

def IG_split(p, y):
    ids = np.argsort(p)
    p = p[ids]
    y = y[ids]
    n = np.array(len(y), dtype = p.dtype)

    n11 = np.cumsum(y == -1).astype(p.dtype)
    n21 = np.cumsum(y == +1).astype(p.dtype)
    n1 = n11[-1]
    n2 = n21[-1]
    n11 = n11[:-1]
    n21 = n21[:-1]
    n12 = n1 - n11
    n22 = n2 - n21

    gain_information = entropy(n1, n2, n) - (entropy(n11, n21, n11 + n21) * (n11 + n21) + 
                                          entropy(n12, n22, n12 + n22) * (n12 + n22)) / n

    id_imp = np.argmax(gain_information)
    thr = (p[id_imp] + p[id_imp + 1]) / 2
    best_gain_information = gain_information[id_imp] / (2 * np.log(2))
    acc = ((thr > p) == (y > 0)).mean()
    return thr, best_gain_information, acc



class graph_partition:
    def __init__(self, id_part = 0, num_parts = 1, paths = None, work_dir = ''):
        self.id_part = id_part
        self.num_parts = num_parts
        if paths is None:
            paths = [''] * num_parts
            for i in range(num_parts):
                paths[i] = 'graph_id_part_' + str(i) + '.npz'
        else:
            assert(len(paths) == num_parts)
        for i in range(num_parts):
            paths[i] = os.path.join(work_dir, paths[i])
        self.paths = paths
        self.path = paths[id_part]
        self.fit(0)
    
    def fit(self, num_vertices):
        cnt = num_vertices * (num_vertices - 1) // 2
        lens = np.tile(cnt // self.num_parts, (self.num_parts, 1))
        lens[:(cnt % self.num_parts)] += 1
        clens = np.concatenate([[0], np.cumsum(lens)])
        self.be = clens[self.id_part]
        self.en = clens[self.id_part + 1] - 1
        self.num_vertices = num_vertices
        self.length = int(np.asscalar(lens[self.id_part]))
        return self

    def get_path(self):
        return self.path

    def get_paths(self):
        return self.paths
        
    def __iter__(self):
        cur = 0
        for i in range(self.num_vertices):
            l = self.num_vertices - i - 1
            if (cur <= self.be and self.be < cur + l) or (cur <= self.en and self.en < cur + l) or (self.be <= cur and cur <= self.en):
                for j in range(self.num_vertices):
                    if i >= j: continue
                    cur_id = i * self.num_vertices + j
                    if self.be <= cur and cur <= self.en:
                        yield i, j
                    cur += 1
            else:        
                cur += l
    
    def __len__(self):
        return self.length

class graph_partition_subset:
    def __init__(self, id_part = 0, num_parts = 1, paths = None, work_dir = ''):
        self.id_part = id_part
        self.num_parts = num_parts
        if paths is None:
            paths = [''] * num_parts
            for i in range(num_parts):
                paths[i] = 'graph_id_part_' + str(i) + '.npz'
        else:
            assert(len(paths) == num_parts)
        for i in range(num_parts):
            paths[i] = os.path.join(work_dir, paths[i])
        self.paths = paths
        self.path = paths[id_part]
        self.fit(np.array([]))
    
    def fit(self, subset):
        cnt = subset.shape[0]
        lens = np.tile(cnt // self.num_parts, (self.num_parts, 1))
        lens[:(cnt % self.num_parts)] += 1
        clens = np.concatenate([[0], np.cumsum(lens)])
        self.be = clens[self.id_part]
        self.en = clens[self.id_part + 1] - 1
        self.subset = subset
        self.length = int(np.asscalar(lens[self.id_part]))
        return self

    def get_path(self):
        return self.path

    def get_paths(self):
        return self.paths
        
    def __iter__(self):
        for cur, pair in enumerate(self.subset[self.be:self.en + 1]):
            yield pair[0], pair[1]
    
    def __len__(self):
        return self.length

class classifier_kernel:
    def __init__(self, distance_threshold = 0, min_score = 0.75, by_group = False, dtype = np.float32, \
                 clf = svm.LinearSVC(C = 1, class_weight = "balanced"), distance_method = 'decision_function', \
                 score_method = 'score'):
        self.distance_threshold = distance_threshold
        self.min_score = min_score
        self.by_group = by_group
        self.dtype = dtype
        self.clf = clf
        self.distance_method = getattr(self.clf, distance_method)
        self.score_method = getattr(self.clf, score_method)
        self.G = None
        self.D = None
        #clf = svm.SVC(kernel = 'linear', C = 1, class_weight = "balanced")
    
    def fit(self, X_i, X_j, y, mask):
        #data = stats.zscore(np.array([X_i, X_j]).T)
        data = np.array([X_i, X_j]).T
        
        if self.by_group:
            classes = np.unique(y)
            G = np.zeros((len(y), ), np.bool)
            D = np.zeros((len(y), ), self.dtype)
            for c in classes:
                fit_mask = (y == c) | (mask == 1)
                if len(np.unique(y[fit_mask])) == 1:
                    continue
                self.clf.fit(data[fit_mask], y[fit_mask] == c)
                score = self.score_method(data[fit_mask], y[fit_mask] == c)
                
                G[y == c] = self.clf.predict(data[y == c]) == 1
                D[y == c] = self.distance_method(data[y == c])
                if score < self.min_score:
                    G[fit_mask] = False
                    
            G = G.reshape((1, len(G)))
        else:
            fit_mask = (mask == 0) | (mask == 1)
            
            self.clf.fit(data[fit_mask], y[fit_mask] == 0)
            G = self.clf.predict(data) == 1
            score = self.score_method(data[fit_mask], y[fit_mask] == 0)
                
            if score < self.min_score:
                G[:] = False
            G = G.reshape((1, len(G)))
            D = np.array(self.distance_method(data), dtype = self.dtype)
        self.G = G
        self.D = D
        return self
        
    def get_edges(self, thr_d = None):
        return self.G, self.D        
    
class pdf_kernel:
    # thr_type in ['best', 'one']
    def __init__(self, num_points = 10000, linearity_eps = 1.0e-9, dtype = np.float32, thr_type = 'one', division_rule = 'noncontrol', thr_p = 0.9, min_score = 0.9):
        self.num_points = num_points
        self.linearity_eps = linearity_eps
        self.dtype = dtype
        self.thr_p = thr_p
        self.min_score = min_score
        self.is_one = thr_type == 'one'
        self.is_best = thr_type == 'best'
        self.is_atypical = division_rule == 'atypical'
        self.is_noncontrol = division_rule == 'noncontrol'
        self.link = None
        self.G = None
        self.D = None
        self.p = None
        self.pr = None
        self.best_thr = None
        self.gain_information = None
        self.score = None
        self.num_samples = 0
    
    # mask == -1 - control
    # mask == +1 - deviation
    # mask == -n - expected as control, n > 1
    # mask == +n - expected as deviation, n > 1
    def fit(self, X_i, X_j, y, mask):
        self.num_samples = X_i.shape[0]
        X_prob_i, X_prob_j = X_i[mask == -1], X_j[mask == -1]
        data = np.array([X_prob_i, X_prob_j])
        det = np.linalg.det(np.corrcoef(data))

        if abs(det) < self.linearity_eps:
            if self.is_best:
                self.link = np.zeros((self.num_samples), dtype = np.bool)
                self.G = np.zeros((self.num_samples), dtype = np.bool)
                self.D = self.G.astype(self.dtype)
                self.best_thr = 0
                self.gain_information = 0
                self.score = 0
            else:
                self.pr = np.zeros((self.num_points), dtype = self.dtype)
                self.p = np.zeros((self.num_samples), dtype = self.dtype)
                self.D = np.zeros((self.num_samples), dtype = np.bool)
            return self
        kde = stats.gaussian_kde(data)
        
        data = np.array([X_i, X_j])
        p = np.array(kde(data))
        self.p = p
            
        if self.is_best:
            fit_mask = (mask == -1) | (mask == 1)
            self.best_thr, self.gain_information, self.score = IG_split(p[fit_mask], mask[fit_mask])
            self.link = np.zeros((self.num_samples), dtype = np.bool)
            control_mask = mask < 0
            deviated_mask = mask > 0
            self.link = p < self.best_thr

            if self.is_atypical:
                self.link[deviated_mask] = ~self.link[deviated_mask]

            if self.score > self.min_score:
                self.G = self.link
            else:
                self.G = np.zeros((self.num_samples), dtype = np.bool)
            self.D = self.G.astype(self.dtype)
        elif self.is_one:
            points = kde.resample(self.num_points)
            pr = np.array(kde(points))
            pr.sort()

            self.pr = pr
            self.D = np.array(p, dtype = self.dtype)
            for i, cur_p in enumerate(p):
                pos = np.searchsorted(pr, cur_p)
                self.D[i] = float(self.num_points - pos) / self.num_points
           
        return self

    def get_edges(self, thr_p = None, min_score = None):
        if self.is_best:
            if min_score is None:
                min_score = self.min_score
            
            if self.score > min_score:
                self.G = self.link
            else:
                self.G = np.zeros((self.num_samples), dtype = np.bool)
            self.D = self.G.astype(self.dtype)
        elif self.is_one:
            if thr_p is None:
                thr_p = self.thr_p
            thr_p = 1 - thr_p
            ind = int(thr_p * self.num_points)
            if ind < len(self.pr):
                q = self.pr[ind]
                #print(ind, q, self.p.min(), self.p.max())
                self.G = self.p < q
            else:
                self.G = np.ones((self.num_samples), dtype = np.bool)
        return self.G, self.D

class IG_filter:
    def __init__(self, max_score = 0.75, max_IG = 1):
        self.score = []
        self.max_score = max_score
        self.max_IG = max_IG
        self.num_good = 0

    def fit(self, X, mask, iterable):
        score = np.zeros((X.shape[1], 1), dtype = np.float32)
        gain_information = np.zeros((X.shape[1], 1), dtype = np.float32)
        for i in range(X.shape[1]):
            fit_mask = (mask == +1) | (mask == -1)
            _, gain_information[i], score[i] = IG_split(X[fit_mask, i], mask[fit_mask])
            score[i] = max(score[i], 1 - score[i])

        self.score = score
        self.gain_information = gain_information
        self.num_good = int(np.sum((self.score <= self.max_score) & (self.gain_information <= self.max_IG)))
        self.iterable = iterable
        

    def is_filtered(self, i, j):
        is_filt = (max(self.score[i], self.score[j]) > self.max_score) or (max(self.gain_information[i], self.gain_information[j]) > self.max_IG)
        return is_filt

    def __iter__(self):
        for pair in self.iterable:
            if not self.is_filtered(pair[0], pair[1]):
                yield pair[0], pair[1]
    
    def __len__(self):
        return (self.num_good - 1) * self.num_good // 2


import itertools
def chunked_iterable(iterable, size):
    it = iter(iterable)
    while True:
        chunk = list(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    sys.stderr.flush()



class parenclitic_data:
    def __init__(self, X, y, mask, kernel):
        self.X = X
        self.y = y
        self.mask = mask
        self.kernel = kernel

class parallel_calc:
    def __init__(self, verbose):
        self.verbose = verbose

    def set_stderr(self, work_dir = '../logs'):
        sys.stderr = open(work_dir + '/' + str(os.getpid()) + "_error.log", "a")

    def init(self, X, y, mask, kernel):
        if self.verbose == 1:
            self.set_stderr()
        global data
        data = parenclitic_data(X, y, mask, kernel)

    def calc_links(self, i, j):
        global data
        data.kernel.fit(data.X[:, i], data.X[:, j], data.y, data.mask)
        m, d = data.kernel.get_edges()
        if m.any():
            return m, d, i, j
        else:
            return None

    def calc_batch(self, ids):
        res = []
        ok = False
        for i, j in ids:
            cur = self.calc_links(i, j)
            res.append(cur)
            if not cur is None:
                ok = True
        if ok:
            return np.array(res)
        else:
            return len(res)

class parenclitic:
    def __init__(self, partition = graph_partition(), kernel = classifier_kernel(), pair_filter = None, verbose = 0, progress_bar = 1):
        self.partition = partition
        self.kernel = kernel
        self.pair_filter = pair_filter
        
        self.M = None
        self.D = None
        self.E = None
        self.is_fitted = False
        self.is_loaded = False
        self.graph_paths = None
        self.graphs = None
        self.parenclitics = None
        self.verbose = verbose
        self.progress_bar = progress_bar
        #self.max_edges = max_edges

                        



    def fit(self, X, y, mask, subset = None, num_workers = 1, queue_len = 2, chunk_size = 10):
        """Fit the model according to the given training data.
        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = [n_samples, n_features]
            Training vector, where n_samples in the number of samples and
            n_features is the number of features.
        y : array-like, shape = [n_samples]
            Target vector relative to X
        mask : array-like, shape = [n_samples]
            Control group mask vector relative to X, 
            where True (1) - control, False (0) - test
        sample_weight : array-like, shape = [n_samples], optional
            Array of weights that are assigned to individual
            samples. If not provided,
            then each sample is given unit weight.
        Returns
        -------
        self : object
        """
        try:
            self.X_shape = X.shape
            assert(len(self.X_shape) == 2)
            self.num_samples = self.X_shape[0]
            self.num_features = self.X_shape[1]
    
            if self.verbose == 1:
                print('parenclitic_graphs')
                sys.stdout.flush()
    
            if subset is None:
                self.partition.fit(self.num_features)
            else:
                self.partition.fit(subset)
            
            if not self.pair_filter is None:
                self.pair_filter.fit(X, mask, self.partition)
                self.pairs = self.pair_filter
            else:
                self.pairs = self.partition
    
            global num_done, num_pairs
            num_done = 0
            num_pairs = len(self.pairs)
            each_progress = int(np.sqrt(num_pairs + 0.5))
            if self.progress_bar:
                from tqdm import tqdm
                progress_bar = tqdm(total = num_pairs)
            #global fit
            #globals()['X'] = X
            #globals()['y'] = y
            #globals()['mask'] = mask
            fit = self.kernel.fit
            M, D, E = [], [], []
            
            need_parallel = num_workers > 1
            my_parallel_calc = parallel_calc(self.verbose)
            if need_parallel:
                global done_tasks, ready
                pool = Pool(num_workers, initializer = my_parallel_calc.init, initargs = (X, y, mask, self.kernel))
                done_tasks = 0
                ready = Semaphore(num_workers * queue_len)
            else:
                my_parallel_calc.init(X, y, mask, self.kernel)
                

            def upd_graph(res):
                global num_done, done_tasks, ready
                if self.verbose == 1:
                    print('upd_graphs')
                    sys.stdout.flush()
                if not type(res) is int:
                    for cur in res:
                        if not cur is None:
                            m, d, i, j = cur
                            #m, d = res.get_edges()
                            if m.any():
                                M.append(m)
                                D.append(d)
                                E.append([i, j])
                    res = len(res)
                                
                if need_parallel:
                    done_tasks += 1
                    ready.release()
    
                if self.progress_bar:
                    progress_bar.set_description('Number of edges: %i' % len(M), refresh = False)
                    progress_bar.update(res)

                num_done += 1
                if num_done % each_progress == 0 or num_done == num_pairs:
                    stop = timeit.default_timer()
                    if self.verbose == 1:
                        print('Graph for', num_done, 'pairs calculated in', stop - start)
                        sys.stdout.flush()
                
            if self.verbose == 1:
                print('start iterate')
                sys.stdout.flush()
            start = timeit.default_timer()
            num_tasks = 0
            for ids in chunked_iterable(self.pairs, chunk_size):
                #if not self.pair_filter is None:
                #    if self.pair_filter.is_filtered(i, j):
                #        continue
    
                num_tasks += 1
                if need_parallel:
                    '''
                    if self.verbose == 1:
                        print('acquire')
                        sys.stdout.flush()
                    '''
                    ready.acquire()
                    '''
                    if self.verbose == 1:
                        print('apply_async')
                        sys.stdout.flush()
                    '''
                    #pool.apply_async(self.kernel.fit, args = (X[:, i], X[:, j], y, mask), callback = upd_graph)
                    
                    #pool.apply_async(my_parallel_calc.calc_links, args = (i, j), callback = upd_graph) # 
                    pool.apply_async(my_parallel_calc.calc_batch, args = (np.array(ids), ), callback = upd_graph) # 
                    pass
                else:
                    if self.verbose == 1:
                        print('calc batch')
                        sys.stdout.flush()
                    #upd_graph(self.kernel.fit(X[:, i], X[:, j], y, mask))
                    #upd_graph(len(ids))
                    #upd_graph(my_parallel_calc.calc_links(i, j))
                    upd_graph(my_parallel_calc.calc_batch(np.array(ids)))
                    pass
    	
            if need_parallel:
                while done_tasks < num_tasks:
                    ready.acquire()
    
                pool.close()
                pool.join()
        
            if self.verbose == 1:
                print('ready done')
                sys.stdout.flush()
    
            if self.progress_bar:
                progress_bar.close()
            if M == []:
                self.M = np.zeros((self.num_samples, 0), dtype = np.bool)
                self.D = np.zeros((self.num_samples, 0), dtype = np.float32)
                self.E = np.zeros((0, 2), dtype = np.float32)
            else:    
                self.M = np.array(M).T
                self.D = np.array(D).T
                self.E = np.array(E)
            self.is_fitted = True
        except:
            if self.progress_bar:
                progress_bar.close()
            raise
        return self
        
    def save_part_graphs(self):
        np.savez_compressed(self.partition.get_path(), G = self.G, D = self.D, IDS = self.IDS, \
                            num_samples = self.num_samples, num_features = self.num_features)
        
    def load_part_graphs(self):
        if self.is_loaded:
            return
            
        if self.partition.num_parts > 1 or not self.is_fitted:
            E, D, IDS = [], [], []
            for part_path in self.partition.get_paths():
                if not os.path.exists(part_path):
                    return
                data = np.load(part_path)
                mcur, dcur, ecur = data['M'], data['D'], data['E']
                num_samples, num_features = data['num_samples'], data['num_features']
                
                M.extend(mcur.tolist())
                D.extend(dcur.tolist())
                E.extend(ecur.tolist())

            self.M = np.array(M).T
            self.D = np.array(D).T
            self.E = np.array(E)
            self.num_samples = num_samples
            self.num_features = num_features
        
        self.is_loaded = True
        
    def make_graph(self, edges, weights, mask, num_features, features_names = None):
        mask = mask.flatten()
        weights = weights.flatten()
        edges = edges[mask, :]
        weights = weights[mask]
        
        g = igraph.Graph(n = num_features, edges = list(zip(*edges.T)))
        g.es["weight"] = weights
            
        if not features_names is None:
            g.vs["name"] = features_names
            g.vs["label"] = features_names
        return g
        
    def get_graph(self, id_sample, features_names = None):
        if self.graphs is None or self.graphs[id_sample] is None:
            if self.M is None:
                M, D, E, num_samples, num_features = self.load_graph(id_sample)
                self.num_samples = num_samples
                self.num_features = num_features
            else:
                M = self.M[id_sample, :]
                D = self.D[id_sample, :]
                E = self.E
            if self.graphs is None:
                self.graphs = [None] * self.num_samples
            self.graphs[id_sample] = self.make_graph(E, D, M, self.num_features, features_names = features_names)
        return self.graphs[id_sample]

    def make_paths(self, paths, num_paths, work_dir, pref, suf):
        if paths is None:
            paths = [''] * self.num_samples
            for i in range(self.num_samples):
                paths[i] = pref + str(i) + suf
        assert(len(paths) == num_paths)
        
        for i in range(len(paths)):
            paths[i] = os.path.join(work_dir, paths[i])
        return paths

    def set_num_samples(self, num_samples):
        self.num_samples = num_samples;
    
    def set_graph_paths(self, paths = None, work_dir = 'graphs'):
        self.graph_paths = self.make_paths(paths, self.num_samples, work_dir, 'graph_id_sample_', '.npz')

    def set_parenclitic_paths(self, paths = None, work_dir = 'parenclitics'):
        self.parenclitic_paths = self.make_paths(paths, self.num_samples, work_dir, 'parenclitic_id_sample_', '.pkl')
        
    def get_graph_paths(self):
        return self.graph_paths        

    def get_parenclitic_paths(self):
        return self.parenclitic_paths

    # gtype : npz, csv
    def save_graphs(self, gtype = 'npz'):
        if self.graph_paths is None:
            self.set_graph_paths()
        for i, graph_path in enumerate(self.graph_paths):
            M = self.M[i, :].flatten()
            D = self.D[i, :].flatten()
            E = self.E
            if gtype == 'npz':
                np.savez_compressed(graph_path, M = M, D = D, E = E, \
                                    num_samples = self.num_samples, num_features = self.num_features)
            elif gtype == 'csv':
                df = pd.DataFrame({'v0': E[:, 0], 'v1': E[:, 1], 'distance': D, 'is_linked': M.astype(np.int32)})
                df.to_csv(graph_path, sep = '\t', index = None)

    def load_graph(self, id_sample = 0):
        graph_path = self.graph_paths[id_sample]
        data = np.load(graph_path)
        M, D, E = data['M'], data['D'], data['E']
        num_samples, num_features = data['num_samples'].item(0), data['num_features'].item(0)
        return M, D, E, num_samples, num_features
            
    def get_graphs(self, features_names = None):
        self.load_part_graphs()
        for id_sample in range(self.num_samples):
            self.get_graph(id_sample = id_sample, features_names = features_names)
        return self.graphs
        
    def calc_parenclitic(self, id_sample = None, need_weights = True, get_big = True):
        if id_sample is None:
            for id_sample in range(self.num_samples):
                self.calc_parenclitic(id_sample)
        else:
            g = self.get_graph(id_sample)
            if self.parenclitics is None:
                self.parenclitics = [None] * self.num_samples
            self.parenclitics[id_sample] = self.calculate_metrics(g.copy(), need_weights = need_weights, get_big = get_big)
        return self
            
    def get_parenclitic(self):
        if self.parenclitics is None:
            self.calc_parenclitic()
                        
        return pd.concat(self.parenclitics, ignore_index=True, sort=True)
        
    def save_parenclitic(self, id_sample = None):
        if self.parenclitic_paths is None:
            self.set_parenclitic_paths()
        if id_sample is None:
            for id_sample, parenclitic_path in enumerate(self.parenclitic_paths):
                if not self.parenclitics[id_sample] is None:
                    self.parenclitics[id_sample].to_pickle(parenclitic_path, compression = "gzip")
        else:
            if not self.parenclitics[id_sample] is None:
                self.parenclitics[id_sample].to_pickle(parenclitic_paths[id_sample], compression = "gzip")
            
    def robustness(self, g, weights = None):
        cnt = 0
        while g.ecount() > 0:
            degrees = np.array(g.strength(weights = weights))
            g.delete_vertices(np.argmax(degrees))
            cnt = cnt + 1
        return cnt
                
    def calculate_metrics(self, g, need_weights = True, get_big = True):
        if self.verbose == 1:
            print('Metrics')
            print(g.ecount(), g.vcount())
            weight = np.array(g.es["weight"])
            print(np.any(np.isnan(weight)))
            print(g)
            print([np.array(x.tuple) for x in g.es])
            sys.stdout.flush()

        if need_weights:
            weights = 'weight'
        else:
            weights = None
            
        if g.ecount() == 0:
            weights = None

        parenclitic = pd.DataFrame(index=[0])
        start = timeit.default_timer()

        degrees = np.array(g.strength(weights = weights))
        if get_big: 
            parenclitic['degrees'] = [degrees]
        parenclitic['min_degrees'] = np.min (degrees)
        parenclitic['max_degrees'] = np.max (degrees)
        parenclitic['mean_degrees'] = np.mean(degrees)
        parenclitic['std_degrees'] = np.std (degrees)
        degrees = None

        stop = timeit.default_timer()
        if self.verbose == 1:
            print('Parenclitic 1', stop - start)
            sys.stdout.flush()
            
        start = timeit.default_timer()

        if self.verbose == 1:
            print('here1')
            sys.stdout.flush()

        shortest_paths = np.array(g.shortest_paths(weights = weights))
        if self.verbose == 1:
            print('here2')
            sys.stdout.flush()

        shortest_paths = shortest_paths[(shortest_paths > 0) & (shortest_paths != np.inf)]
        if self.verbose == 1:
            print('here3')
            sys.stdout.flush()

        efficiency = 0
        if len(shortest_paths) > 0:
            efficiency = (1.0 / shortest_paths).sum() / (g.vcount() * (g.vcount() - 1))
        if self.verbose == 1:
            print('here4')
            sys.stdout.flush()

        # In paper Latora V., Marchiori M.: Efficient behavior of small-world networks. Phys. Rev. Lett. 87 (Article No. 198701) (2001)
        # suggested to normalize by efficiency for threshold_p = 0 (cause graph has all edges when thr_p = 0)
        parenclitic['efficiency'] = efficiency
        shortest_paths = None

        stop = timeit.default_timer()
        if self.verbose == 1:
            print('Parenclitic 2', stop - start)
            sys.stdout.flush()
            
        start = timeit.default_timer()
        if self.verbose == 1:
            print('here5')
            sys.stdout.flush()

        betweenness = g.betweenness(weights = weights)
        #betweenness = np.array([0, 0])
        if self.verbose == 1:
            print('here6')
            print(betweenness)
            sys.stdout.flush()

        if get_big: 
            parenclitic['betweenness'] = [np.array(betweenness)]
        parenclitic['min_betweenness'] = np.min (betweenness)
        parenclitic['max_betweenness'] = np.max (betweenness)
        parenclitic['mean_betweenness'] = np.mean(betweenness)
        parenclitic['std_betweenness'] = np.std (betweenness)
        betweenness = None

        if self.verbose == 1:
            print('here7')
            sys.stdout.flush()
        
        
        stop = timeit.default_timer()
        if self.verbose == 1:        
            print('Parenclitic 3', stop - start)
            sys.stdout.flush()
            
        
        start = timeit.default_timer()

        closeness = g.closeness(weights = weights)
        if get_big: 
            parenclitic['closeness'] = [np.array(closeness)]
        parenclitic['min_closeness'] = np.min (closeness)
        parenclitic['max_closeness'] = np.max (closeness)
        parenclitic['mean_closeness'] = np.mean(closeness)
        parenclitic['std_closeness'] = np.std (closeness)
        closeness = None

        stop = timeit.default_timer()
        if self.verbose == 1:
            print('Parenclitic 4', stop - start)
            sys.stdout.flush()

        start = timeit.default_timer()

        pagerank = g.pagerank(weights = weights)
        if get_big: 
            parenclitic['pagerank'] = [np.array(pagerank)]
        parenclitic['min_pagerank'] = np.min (pagerank)
        parenclitic['max_pagerank'] = np.max (pagerank)
        parenclitic['mean_pagerank'] = np.mean(pagerank)
        parenclitic['std_pagerank'] = np.std (pagerank)
        pagerank = None

        stop = timeit.default_timer()
        if self.verbose == 1:
            print('Parenclitic 5', stop - start)
            sys.stdout.flush()
            
        start = timeit.default_timer()

        # alpha centrality with alpha = 1
        
        eigenvector_centrality = g.eigenvector_centrality(weights = weights)
        if get_big: 
            parenclitic['eigenvector_centrality'] = [np.array(eigenvector_centrality)]
        parenclitic['min_eigenvector_centrality'] = np.min(eigenvector_centrality)
        parenclitic['max_eigenvector_centrality'] = np.max(eigenvector_centrality)
        parenclitic['mean_eigenvector_centrality'] = np.mean(eigenvector_centrality)
        parenclitic['std_eigenvector_centrality'] = np.std(eigenvector_centrality)
        eigenvector_centrality = None

        stop = timeit.default_timer()
        if self.verbose == 1:
            print('Parenclitic centrality', stop - start)
            sys.stdout.flush()
            
        start = timeit.default_timer()
        
        largest = g.clusters().giant()    
        m = np.array(largest.get_adjacency().data)
        sys.stdout.flush()

        eigenvalues, eigenvectors = LA.eig(m)
        #Suppose symmetric matrix
        eigenvalues = np.real(eigenvalues)
        eigenvectors = np.real(eigenvectors)
        if self.verbose == 1:
            print('Eigenvectors', stop - start)
            sys.stdout.flush()

        eigenvalues_intervals = np.diff(np.sort(eigenvalues)) 
        if self.verbose == 1:
            print('intervals', stop - start)
            sys.stdout.flush()

        eigenvalues_intervals_normalized = eigenvalues_intervals / np.mean(eigenvalues_intervals)

        if self.verbose == 1:
            print('normalized', stop - start)
            sys.stdout.flush()
        
        if get_big: 
            parenclitic['eigenvalues'] = [np.array(eigenvalues)]
            parenclitic['eigenvalues_intervals'] = [np.array(eigenvalues_intervals)]
            parenclitic['eigenvalues_intervals_normalized'] = [np.array(eigenvalues_intervals_normalized)]

        stop = timeit.default_timer()
        if self.verbose == 1:
            print('Parenclitic: eigenvalues', stop - start)
            sys.stdout.flush()
        
        IPR = np.sum(np.power(eigenvectors, 4), axis=0) / np.power(np.sum(np.power(eigenvectors, 2), axis=0), 2)
        if get_big: 
            parenclitic['IPR'] = [np.array(IPR)]
        parenclitic['max_IPR'] = np.max(IPR)
        parenclitic['mean_IPR'] = np.mean(IPR)

        stop = timeit.default_timer()
        if self.verbose == 1:
            print('Parenclitic 7', stop - start)
            sys.stdout.flush()

        eigenvectors = None
        eigenvalues = None
        IPR = None
        eigenvalues_intervals = None
        eigenvalues_intervals_normalized = None
        
        start = timeit.default_timer()
        parenclitic['num_edges'] = g.ecount()

        if g.ecount() > 0:
            weights = np.array(g.es["weight"])
            if get_big: 
                parenclitic['weights'] = [np.array(weights)]
            parenclitic['sum_weights'] = np.sum (weights)
            parenclitic['min_weights'] = np.min (weights)
            parenclitic['max_weights'] = np.max (weights)
            parenclitic['mean_weights'] = np.mean(weights)
            parenclitic['std_weights'] = np.std (weights)
            weights = None

        stop = timeit.default_timer()
        if self.verbose == 1:
            print('Parenclitic 8', stop - start)
            sys.stdout.flush()

        start = timeit.default_timer()
    #    parenclitic['community_edge_betweenness_optimal'] = g.community_edge_betweenness().optimal_count
        stop = timeit.default_timer()
        if self.verbose == 1:
            print('Parenclitic 9', stop - start)
            sys.stdout.flush()
            
        start = timeit.default_timer()
        parenclitic['robustness'] = self.robustness(g, weights)
        stop = timeit.default_timer()
        if self.verbose == 1:
            print('Parenclitic 10', stop - start)
            sys.stdout.flush()

        return parenclitic
        
    @staticmethod
    def metric_names():
        metric_names = {}
        metric_names['degrees'] = 'Degrees'
        metric_names['min_degrees'] = 'Min degrees'
        metric_names['max_degrees'] = 'Max degrees'
        metric_names['mean_degrees'] = 'Mean degrees'
        metric_names['std_degrees'] = 'Std degrees'
        
        metric_names['efficiency'] = 'Efficiency'
        metric_names['betweenness'] = 'Betweenness'
        metric_names['min_betweenness'] = 'Min betweenness'
        metric_names['max_betweenness'] = 'Max betweenness'
        metric_names['mean_betweenness'] = 'Mean betweenness'
        metric_names['std_betweenness'] = 'Std betweenness'
        
        metric_names['closeness'] = 'Closeness'
        metric_names['min_closeness'] = 'Min closeness'
        metric_names['max_closeness'] = 'Max closeness'
        metric_names['mean_closeness'] = 'Mean closeness'
        metric_names['std_closeness'] = 'Std closeness'
        
        metric_names['pagerank'] = 'Pagerank'
        metric_names['min_pagerank'] = 'Min pagerank'
        metric_names['max_pagerank'] = 'Max pagerank'
        metric_names['mean_pagerank'] = 'Mean pagerank'
        metric_names['std_pagerank'] = 'Std pagerank'
        
        metric_names['eigenvalues'] = 'Eigenvalues'
        metric_names['min_eigenvector_centrality'] = 'Min eigenvector centrality'
        metric_names['max_eigenvector_centrality'] = 'Max eigenvector centrality'
        metric_names['mean_eigenvector_centrality'] = 'Mean eigenvector centrality'
        metric_names['std_eigenvector_centrality'] = 'Std eigenvector centrality'
        metric_names['eigenvector_centrality'] = 'Eigenvector centrality'
        metric_names['num_edges'] = 'Number of edges'

        metric_names['eigenvalues_intervals'] = 'Eigenvalues intervals'
        metric_names['eigenvalues_intervals_normalized'] = 'Eigenvalues intervals normalized'

        metric_names['IPR'] = 'IPR'
        metric_names['max_IPR'] = 'Max IPR'
        metric_names['mean_IPR'] = 'Mean IPR'

        metric_names['weights'] = 'Weights'
        metric_names['sum_weights'] = 'Sum weights'
        metric_names['min_weights'] = 'Min weights'
        metric_names['max_weights'] = 'Max weights'
        metric_names['mean_weights'] = 'Mean weights'
        metric_names['std_weights'] = 'Std weights'
        
        metric_names['community_edge_betweenness_optimal'] = 'Community edge betweenness: optimal count'
            
        metric_names['robustness'] = 'Robustness'
        return metric_names    
