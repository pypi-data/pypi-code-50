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

from gtdb_validation_tk.common import canonical_genus_name


class MergeGenera():
    """Report polyphyletic sister genera that are candidates for merging into a single genera."""

    def __init__(self, dpi=96):
        """Initialize."""
        
        self.logger = logging.getLogger()
  
    def run(self, scaled_tree, red_dictionary, output_file):
        """Report polyphyletic sister genera that are candidates for merging into a single genera."""
        
        self.logger.info('Reading RED dictionary.')
        reds = eval(open(red_dictionary, 'r').read())
        genus_red = reds['genus']
        self.logger.info(' ...RED for genus=%.2f' % genus_red)
        
        self.logger.info('Reading scaled and decorated tree.')
        tree = dendropy.Tree.get_from_path(scaled_tree, 
                                            schema='newick', 
                                            rooting='force-rooted', 
                                            preserve_underscores=True)
        
        tree.calc_node_root_distances()
        gtdb_taxonomy = Taxonomy().read_from_tree(tree)
        for gid in gtdb_taxonomy:
            gtdb_taxonomy[gid] = Taxonomy().fill_missing_ranks(gtdb_taxonomy[gid])
        self.logger.info(' ...tree contains %d genomes.' % len(gtdb_taxonomy))

        # perform preorder traversal of tree to determine nodes 
        # that contain only genomes from the same canonical
        # genus and have an RED amendable to being a genus
        fout = open(output_file, 'w')
        fout.write('Taxonomy\tGenera\tGenome IDs\tSupport\tRED of node\tRED of node - RED genus median\n')
        self.logger.info('Identifying internal nodes that are candidates for merging polyphyletic genera.')
        s = [tree.seed_node]
        while(s):
            n = s.pop()
            
            # process node
            support, taxon_name, _auxiliary_info = parse_label(n.label)
            if taxon_name and taxon_name.startswith('g__'):
                # no need to explore nodes below named genera
                # in the tree
                continue 
            
            if genus_red + 0.1 > n.root_distance > genus_red - 0.05:
                # deep enough to be a genus
                gtdb_genera = set()
                canonical_gtdb_genera = set()
                for leaf in n.leaf_iter():
                    genera = gtdb_taxonomy[leaf.taxon.label][5]
                    gtdb_genera.add(genera)
                    canonical_gtdb_genera.add(canonical_genus_name(genera))
                 
                # check if there are multiple genera from the same canonicalized genus
                if len(gtdb_genera) >= 2 and len(canonical_gtdb_genera) == 1:
                    gids = ', '.join([leaf.taxon.label for leaf in n.leaf_iter()])

                    taxonomy_str = '; '.join(gtdb_taxonomy[leaf.taxon.label][0:5])
                    fout.write('{}\t{}\t{}\t{}\t{:.3f}\t{:.3f}\n'.format(
                                taxonomy_str,
                                ', '.join(gtdb_genera),
                                gids,
                                support,
                                n.root_distance,
                                n.root_distance - genus_red))
                                
                    continue
                
            for child in n.child_node_iter():
                if not child.is_leaf():
                    s.append(child)
