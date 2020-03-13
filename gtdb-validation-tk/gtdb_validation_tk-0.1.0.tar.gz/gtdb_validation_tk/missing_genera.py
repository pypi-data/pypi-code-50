###############################################################################
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

import os
import sys
import logging
from collections import defaultdict

from biolib.newick import parse_label
from biolib.taxonomy import Taxonomy

import dendropy


class MissingGenera():
    """Report lineages that may represent missing genus names."""

    def __init__(self, dpi=96):
        """Initialize."""
        
        self.logger = logging.getLogger()
  
    def run(self, scaled_tree, red_dictionary, gtdb_prev_taxonomy, ncbi_taxonomy, output_file):
        """Report lineages that may represent missing genus names."""
        
        self.logger.info('Reading RED dictionary.')
        reds = eval(open(red_dictionary, 'r').read())
        genus_red = reds['genus']
        self.logger.info(' ...RED for genus=%.2f' % genus_red)
        
        self.logger.info('Reading previous GTDB taxonomy.')
        gtdb_prev_taxonomy = Taxonomy().read(gtdb_prev_taxonomy)
        self.logger.info(' ...read taxonomy for %d genomes.' % len(gtdb_prev_taxonomy))
        
        self.logger.info('Reading NCBI taxonomy.')
        ncbi_taxonomy = Taxonomy().read(ncbi_taxonomy)
        self.logger.info(' ...read taxonomy for %d genomes.' % len(ncbi_taxonomy))

        self.logger.info('Reading scaled and decorated tree.')
        tree = dendropy.Tree.get_from_path(scaled_tree, 
                                            schema='newick', 
                                            rooting='force-rooted', 
                                            preserve_underscores=True)
        
        tree.calc_node_root_distances()
        gtdb_taxonomy = Taxonomy().read_from_tree(tree)
        for gid in gtdb_taxonomy:
            if gid.startswith('D-'):
                continue # skip dummy genomes
            gtdb_taxonomy[gid] = Taxonomy().fill_missing_ranks(gtdb_taxonomy[gid])
        self.logger.info(' ...tree contains %d genomes.' % len(gtdb_taxonomy))

        # perform preorder traversal of tree to determine nodes 
        # that should likely have a genus name
        fout = open(output_file, 'w')
        fout.write('Taxonomy\tGenus\tGenome IDs\tRED of node\tRED of node - RED genus median\n')
        self.logger.info('Identifying internal nodes that may be missing a genus label.')
        s = [tree.seed_node]
        while(s):
            n = s.pop()
            
            # process node
            _support, taxon_name, _auxiliary_info = parse_label(n.label)
            if taxon_name and taxon_name.startswith('g__'):
                # no need to explore nodes below named genera
                # in the tree
                continue 
            
            if n.root_distance >= genus_red - 0.1:
                # deep enough to be a genus
                cur_gtdb_genera = set()
                prev_gtdb_genera = set()
                ncbi_genera = set()
                gids = set()
                for leaf in n.leaf_iter():
                    if leaf.taxon.label.startswith('D-'):
                        continue # skip dummy genomes
                        
                    cur_gtdb_genera.add(gtdb_taxonomy[leaf.taxon.label][5])
                    prev_gtdb_genera.add(gtdb_prev_taxonomy.get(leaf.taxon.label, Taxonomy.rank_prefixes)[5])
                    ncbi_genera.add(ncbi_taxonomy[leaf.taxon.label][5])
                    gids.add(leaf.taxon.label)
                 
                # check if all leaf nodes have an unassigned genus name in the tree
                genus = cur_gtdb_genera.pop()
                if len(cur_gtdb_genera) == 0 and genus == 'g__':
                    # check for a uniform genus name in the previous GTDB release
                    genus = prev_gtdb_genera.pop()
                    if len(prev_gtdb_genera) == 0 and genus != 'g__':
                        # looks like this should have a genus label
                        print('Previous GTDB\t%s\t%s' % (genus, gids))
                        fout.write('{}\t{}\t{}\t{}\t{}\n' % (
                                    'Previous GTDB', 
                                    genus, 
                                    gids,
                                    n.root_distance,
                                    n.root_distance - genus_red))
                        continue
                        
                    # check for a uniform genus name in the NCBI taxonomy
                    genus = ncbi_genera.pop()
                    if len(ncbi_genera) == 0 and genus != 'g__':
                        # looks like this should have a genus label
                        print('NCBI\t%s\t%s' % (genus, gids))
                        fout.write('{}\t{}\t{}\t{}\t{}\n' % (
                                    'NCBI', 
                                    genus, 
                                    gids,
                                    n.root_distance,
                                    n.root_distance - genus_red))
                        continue
                
            for child in n.child_node_iter():
                if not child.is_leaf():
                    s.append(child)
