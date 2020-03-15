import sys
import re
import random
from math import ceil
from pathlib import Path
from .helpers import log


class Mlnods:
    def __init__(self, splits:int, cutoff:int, nodes:list=None, edges:list=None, nodes_file:Path=None, edges_file:Path=None, limit:int=0, abundance:bool=False, edges_format:str="self5", random:int=None, outfolder:Path=None):
        self.splits = splits
        self.cutoff = cutoff
        self.nodes = nodes
        self.nodes_file = nodes_file
        self.edges = edges
        self.edges_file = edges_file
        self.limit = limit
        self.use_abundance = abundance
        self.format = edges_format
        self.random = random
        self.outfolder = outfolder

        self.out_jacked, self.out_deleted, self.f_temp = None, None, None
        self.traversed, self.res, self.res_del = [], {}, []
        self.cluster_count, self.line_num = 1, 2 
        self.total, self.limit, self.max, self.max_number,  self.number_, self.del_, self.sum_, self.total_raw, self.muts_count = 0, 0, 0, 0, 0, 0, 0, 0, 0

        self.genes = {}    # list ids and corresponding weights
        self.tree = {}     # tree contains linked node information
        self.links = {}    # links contains the number of links for each node
        self.head = {}     # head is the hash of knowledge where the node in the tree came from
        self.number = {}   # number is the hash of sequence number of each node
        self.cluster = {}  # accessory hash for printing cluster information
        self.muts = {}     # accessory hash for printing cluster information

        self.init()

    def init(self):
        # create output dependecies
        if self.outfolder:
            self.outfolder.mkdir(parents=True, exist_ok=True)
            self.out_jacked = self.outfolder / f'{self.edges_file.stem}.jack.csv'
            self.out_deleted = self.outfolder / f'{self.edges_file.stem}.del.csv'
            self.f_temp = self.outfolder / f'{self.edges_file.stem}.table'
        if self.format[0:4] == 'self':
            self.line_num = int(self.format[4]) - 1

        if self.random != None:
            log(f'setting random seed = {self.random}', level=1, prefix=' ==> ')
            random.seed(self.random)

    def parse_node_file(self):
        with self.nodes_file.open() as fin:
            pattern_id = re.compile(r'^>([^\s]*)[\s,\,,\;]*(.*)$')
            pattern_id_score = re.compile(r'^>([^\s]*)[\s,\,]*(.*)$')
            for line in fin:
                if line[0] == '>':
                    name = line.rstrip()
                    if self.use_abundance:
                        match = pattern_id.match(name)
                        name = f' {match[1].upper()}'
                        self.muts_count += 1
                        gene_info = self.genes.get(name, None)
                        if gene_info:
                            gene_info['seq'] += line
                            gene_info['score'] += 1
                        else:
                            gene_info = {'seq': line, 'score': 1}
                    else:
                        match = pattern_id_score.match(name)
                        name = f' {match[1].upper()}'
                        score = float(match[2]) if len(match.groups()) > 1 and match[2] else 50.0
                        gene_info = {'seq': line, 'score': score}
                else:
                    gene_info = self.genes.get(name, {'seq': ''})
                    gene_info['seq'] += line
                self.genes[name] = gene_info

    def parse_node_list(self):
        for n in self.nodes:
            name = f' {n[0].upper()}'
            if self.use_abundance:
                detail = ' '.join(n[1:]) if len(n) > 0 else name
                self.muts_count += 1
                gene_info = self.genes.get(name, None)
                if gene_info:
                    gene_info['seq'] += detail
                    gene_info['score'] += 1
                else:
                    gene_info = {'seq': detail, 'score': 1}
            else:
                score = float(n[1]) if len(n) > 1 and n[1] else 50.0
                detail = ' '.join(n[2:]) if len(n) > 2 else f'{name} {score}'
                gene_info = {'seq': detail, 'score': score}
            self.genes[name] = gene_info

    def parse_table_file(self):
        if self.format == 'blast':
            blast_table = Path(f'{self.f_temp}.blast')
            if blast_table.exists():
                log(f'reading from file: {blast_table} (similarity is %id)', level=1)
            else:
                self.get_blast()
            self.edges_file = blast_table
        elif self.format == 'hssp':
            hssp_table = Path(f'{self.f_temp}.hssp')
            if hssp_table.exists():
                log(f'reading from file: {hssp_table} (similarity is hssp distance)', level=1)
            else:
                self.get_hssp()
            self.edges_file = hssp_table
            self.line_num = 4

    def get_blast(self):
        # TODO implement
        log('NOT IMPLEMENTED: get_blast', prefix=' ! ')
        pass

    def get_hssp(self):
        # TODO implement
        _ = f'perl m8ToRdb.pl {self.edges_file} {self.f_temp}.hssp'
        log('NOT IMPLEMENTED: get_hssp', prefix=' ! ')
        pass

    def parse_edge_file(self):
        pattern_split = re.compile(r"[\w'\.\,]+")
        with self.edges_file.open() as fin:
            for line in fin:
                line = line.strip()
                if line:
                    row = pattern_split.findall(line)
                    if len(row) != 3:
                        log(f'Skipping - wrong format -> {line}', prefix=' ! ')
                        continue
                    node1, node2 = row[0:2]
                    try:
                        weight = float(row[2])
                    except ValueError as err:
                        log(f'Skipping - {err} -> {line}', prefix=' ! ')
                        continue
                    node1 = f' {node1}'
                    node2 = f' {node2}'
                    node_removed = []
                    for node in [node1, node2]:
                        if node not in self.genes:
                            node_removed.append(node)
                    if node_removed:
                        log(f'Skipping edge [ {node1} -> {node2} ({weight}) ] - {node_removed} not in ID list', level=1, prefix=' ! ')
                        continue
                    
                    if node1 == node2:
                        log(f'Skipping edge [ {node1} -> {node2} ({weight}) ] - self edge', level=1, prefix=' ! ')
                        continue
                    
                    if weight >= self.cutoff and not node2 in self.tree.get(node1, []):
                        self.add_node(node1, node2)

    def parse_edge_list(self):
        for e in self.edges:
            if len(e) != 3:
                log(f'Skipping - wrong format -> {e}', prefix=' ! ')
                continue
            node1, node2 = e[0:2]
            try:
                weight = float(e[2])
            except ValueError as err:
                log(f'Skipping - {err} -> {e}', prefix=' ! ')
                continue
            node1 = f' {node1}'
            node2 = f' {node2}'
            node_removed = []
            for node in [node1, node2]:
                if node not in self.genes:
                    node_removed.append(node)
            if node_removed:
                log(f'Skipping edge [ {node1} -> {node2} ({weight}) ] - {node_removed} not in ID list', level=1, prefix=' ! ')
                continue
            
            if node1 == node2:
                log(f'Skipping edge [ {node1} -> {node2} ({weight}) ] - self edge', level=1, prefix=' ! ')
                continue
            
            if weight >= self.cutoff and not node2 in self.tree.get(node1, []):
                self.add_node(node1, node2)
                    
    def add_node(self, node, node_prime):
        # in all cases establish a link between node and node_prime going both ways
        self.tree[node] = self.tree.get(node, []) + [node_prime]
        self.tree[node_prime] = self.tree.get(node_prime, []) + [node]
        self.links[node] = self.links.get(node, 1) + 1
        self.links[node_prime] = self.links.get(node_prime, 1) + 1

    def get_stats(self):
        self.total = len(self.genes)
        # the limit of number of genes that can be in a single cluster
        self.limit = ceil(self.total/self.splits)

    def store_result(self, result, cluster):
        size = 0
        self.res[cluster] = []
        for clus in result:
            self.res[cluster] += [clus.strip()]
            if cluster in self.cluster:
                self.cluster[cluster]['seq'] += self.genes[clus]['seq']
                self.cluster[cluster]['count'] += self.genes[clus]['score'] if self.use_abundance else 1
            else:
                self.cluster[cluster] = {'seq': self.genes[clus]['seq'], 'count': self.genes[clus]['score'] if self.use_abundance else 1}
            if self.cluster[cluster]['count'] > self.max:
                self.max = self.cluster[cluster]['count']
                self.max_number = cluster
            self.delete_node(clus)
            size += 1
        return size

    def delete_node(self, node, flag=False, max_=False):
        # flag: a max node being deleted
        # max: the max being deletes
        
        # delete the node's links
        self.tree.pop(node, None)
        # delete the count of node's links
        self.links.pop(node, None)
        # delete the mutants
        if self.use_abundance and flag:
            self.muts_count -= self.genes[node]['score']
        self.genes.pop(node)
        
        # delete number stuff
        if not max_:
            # delete head stuff
            self.head.pop(node, None)
            for key, val in self.number.items():
                if val == node:
                    self.number.pop(key)
                    break
        for key, val in self.tree.items():
            if node in val:
                self.links[key] -= 1
                val.remove(node)
        if flag:
            self.total -= 1
            self.limit = ceil(self.total/self.splits)

    def process(self):
        self.total_raw = self.total
        while len(self.links) >= 2:
            # start at random node V with minimal number of links and highest score
            array = sorted(self.links.keys(), key=lambda x: (-self.links[x], self.genes[x]['score'], random.random()), reverse=True)
            orgnode = array[0]
            # if this is a node with no links other than to itself, just save it as a cluster
            if self.links[orgnode] == 1:
                self.sum_ += self.store_result([orgnode], self.cluster_count)
                self.cluster_count += 1
                next
            # else if this node hasn't yet been deleted
            elif orgnode in self.tree:
                # reset all calculations to starting point
                # variables changed in other subs are $traversed and $number
                self.traversed, self.number_ = [], 1
                # reset the starting point to 0 here
                self.head[orgnode] = 0
                # get the tree 
                # (passes name of node, number of node, head of node, option of backtacking, note that this is the original traversion)
                result = self.depthFirst(orgnode, 1, 0, 0, 1)
                # if there's stuff in the traversed line, something is wrong
                if not self.traversed:
                    log('Uuups... this should not have happend! Please submit an issue report. [ Error: 3 ]', prefix=' ! ')
                    sys.exit(1)
                # if everything is fine
                if result[2] == 0:
                    # get rid of the nodes with more than set limit
                    if self.limit:
                        self.shake_links()
                    # store the clusters
                    self.sum_ += self.store_result(self.traversed, self.cluster_count)
                    self.cluster_count += 1
                else:
                    log('Uuups... this should not have happend! Please submit an issue report. [ Error: 4 ]', prefix=' ! ')
                    sys.exit(1)
        
        # for the remaining genes, just store them
        remaining = list(self.genes.keys())
        for key in remaining:
            self.sum_ += self.store_result([key], self.cluster_count)
            self.cluster_count += 1

    def post_process(self):
        # if counting instances, reset the limit_muts by the number of instances,
        # not number of genes - else just get the remaining stuff
        limit_muts = self.get_limit_muts()

        # set the limits
        order = 1
        while order <= self.splits:
            self.muts[order] = {'diff': limit_muts}
            order += 1

        # now cluster mutants starting from largest cluster
        order = 1
        org_splits = self.splits
        for key in sorted(self.cluster.keys(), key=lambda x: (self.cluster[x]['count']), reverse=True):
            # this loop ends only when entry is placed
            while True:
                # if these instances fit into the current bin - place them
                # else is the number of instances is more than can fit into any bin
                # place them into a new one
                # else just go on to next bin
                if self.muts[order]['diff'] >= self.cluster[key]['count']:
                    self.muts[order]['diff'] -= self.cluster[key]['count']
                    self.muts[order]['seq'] = self.muts[order].get('seq', '') + self.cluster[key]['seq']
                    # reset the flag
                    flag = 0
                    break
                elif self.cluster[key]['count'] > limit_muts:
                    log(f'jctMutsorder file is larger than normal: size {self.cluster[key]["count"]} instead of limit_muts', prefix=' ==> ')
                    log(f'	Look for a smaller size last jctMuts file [default: jctMutsorg{org_splits}]', prefix=' ==> ')
                    self.muts[order]['seq'] = self.cluster[key]['seq']
                    self.muts[order]['diff'] = 0
                    order += 1
                    break
                else:
                    if order == self.splits:
                        if flag == 0:
                            flag = 1
                            order = 1
                        else:
                            log(f'Extra jctMuts cluster will be created', prefix=' ==> ')
                            self.splits += 1
                            self.muts[self.splits]['diff'] = limit_muts
                            order += 1
                    else:
                        order += 1

    def get_limit_muts(self):
        return ceil(self.muts_count/self.splits) if self.use_abundance else ceil(self.sum_/self.splits)

    def shake_links(self):
        # getting rid of the nodes with more than the limit links
        limit = self.limit + 1
        for clus in sorted(self.traversed, key=lambda x: (self.links[x], -self.genes[x]['score']), reverse=True):
            if self.links[clus] > limit:
                self.res_del.append(f'{clus.strip()},{self.links[clus]},exceeding_link_limit [{self.limit}]') 
                self.delete_node(clus, True)
                self.traversed.remove(clus)

    def depthFirst(self, head, order, order_head, stop, high):
        """
        this is the actual traversion function

        head: node name we are at right now
        order: node number we are at right now
        order_head: node number of the head of this node
        stop: node to stop number going back to, if we are going back
        high: note whether this is from an original call or from the inside call
        """

        # if we haven't exceeded the limit
        if self.number_ <= self.limit:
            # set the number of node
            self.number[order] = head
            # set the head of node
            self.head[head] = order_head
            # add name to traversed path
            self.traversed.append(head)
            # increase the number in subtree
            self.number_ += 1
            # get the linked nodes in order of number of links
            for key in self.tree[head]:
                if key not in self.links:
                    log('Uuups... this should not have happend! Please submit an issue report. [ Error: 1 ]', prefix=' ! ')
                    sys.exit(1)
            if len(self.tree[head]) > 1:
                array = sorted(self.tree[head], key=lambda x: (-self.links[x], self.genes[x]['score']), reverse=True)
            else:
                array = self.tree[head]
            # foreach of the nodes
            i, c_order = 0, order + 1
            while i < len(array):
                key = array[i]
                # if the node still exists and isn't in the traversed path
                if key in self.tree.get(head, []) and not key in self.traversed:
                    # this should return temp, highest score of node reached
                    # the cue to return if needed, and the number of the node at which to stop if needed
                    temp, c_order, cue2, stop2 = self.depthFirst(key, c_order, order, 0, 0)
                    # if the first node of the tree has been deleted, restart
                    if cue2 == 1:
                        if order > stop2:
                            return ('', c_order, 1, stop2)
                        elif stop2 >= order:
                            # erase everything that was done after and including max
                            # and up to the node that we are at right now
                            c_order -= 1
                            while c_order > stop2:
                                temp = self.number[c_order]
                                self.traversed = list(filter(lambda x: x != temp, self.traversed))
                                self.number_ -= 1
                                self.number.pop(c_order)
                                self.head.pop(temp)
                                c_order -= 1
                            # and just repeat this node over
                            i = -1
                i += 1
            return ('', c_order, 0, 0)
        else:
            # delete the maximal linker
            self.del_ += 1           
            for i in self.traversed:
                if i not in self.links:
                    log('Uuups... this should not have happend! Please submit an issue report. [ Error: 2 ]', prefix=' ! ')
                    sys.exit(1)
            # if this is the only node in remaining then skip the rest
            if len(self.traversed) > 1:
                # sort on the highest number of links, lowest score, and highest head, which is ladder-most location
                sort = sorted(self.traversed, key=lambda x: (self.links[x], -self.genes[x]['score'], self.head[x]), reverse=True)
                max_key = sort[0]
            else:
                max_key = self.traversed[0]
            t = self.links[max_key] - 1
            stop2 = self.head[max_key]
            self.traversed.remove(max_key)
            self.res_del.append(f'{max_key.strip()},{t},maximal_key')
            self.delete_node (max_key, True, True)
            return ('', order, 1, stop2)

    def save_output(self):
        # save instances sorted
        for key in self.muts:
            with open(self.outfolder / f'jctMuts{key}', 'w') as fout:
                fout.write(f'{self.muts[key].get("seq", "")}\n')
        with self.out_jacked.open('w') as fout_res, self.out_deleted.open('w') as fout_del:
            for cluster, ids in self.res.items():
                fout_res.write(f'cluster_{cluster},{",".join(ids)}\n')
            fout_del.writelines([f'{l}\n' for l in self.res_del])

    def run(self):
        if self.nodes_file:
            self.parse_node_file()
        elif self.nodes:
            self.parse_node_list()
        self.parse_table_file()
        if self.edges_file:
            self.parse_edge_file()
        elif self.edges:
            self.parse_edge_list()
        self.get_stats()
        self.process()
        self.post_process()
        return (self.res, self.muts, self.res_del)
    