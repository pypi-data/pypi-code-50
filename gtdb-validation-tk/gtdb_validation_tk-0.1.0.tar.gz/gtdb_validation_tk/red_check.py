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


class RED_Check():
    """Report taxa with unexpected RED values."""

    def __init__(self, dpi=96):
        """Initialize."""
        
        self.logger = logging.getLogger()
  
    def run(self, scaled_tree, red_dictionary, output_file):
        """Report taxa with unexpected RED values."""

        self.logger.info('Reading RED dictionary.')
        reds = eval(open(red_dictionary, 'r').read())
        reds['domain'] = 0

        self.logger.info('Reading scaled and decorated tree.')
        tree = dendropy.Tree.get_from_path(scaled_tree, 
                                            schema='newick', 
                                            rooting='force-rooted', 
                                            preserve_underscores=True)
                                            
        tree.calc_node_root_distances()
        taxonomy = Taxonomy().read_from_tree(tree)
        taxon_taxonomy = {}
        for gid, taxa in taxonomy.items():
            for idx, taxon in enumerate(taxa):
                taxon_taxonomy[taxon] = ';'.join(taxa[0:idx])

        # perform preorder traversal of tree to determine taxa that 
        # look like they should be placed on a different internal node
        self.logger.info('Identifying taxa that have more appropriate placements in tree based on RED.')
        fout = open(output_file, 'w')
        fout.write('Taxon\tRank\tMedia RED\tRED of node\tRED of node - RED median\tRED of parent\tRED of parent - RED median\tSituation\tGTDB taxonomy\n')
        s = [tree.seed_node]
        num_red_check = 0
        for n in tree.postorder_node_iter():
            cur_red = n.root_distance
            
            _support, taxa_label, _auxiliary_info = parse_label(n.label)
            if taxa_label:
                for taxon in [t.strip() for t in taxa_label.split(';')]:
                    rank_prefix = taxon[0:3]
                    rank_label = Taxonomy.rank_labels[Taxonomy.rank_prefixes.index(rank_prefix)]
                        
                    # check if taxon is too far to the right
                    if cur_red >= reds[rank_label] + 0.1:
                        # taxon is too close to the leaf nodes so check if the parent
                        # node is an improvement
                        parent_red = n.parent_node.root_distance
                        d_parent = abs(parent_red - reds[rank_label])
                        d_cur = abs(cur_red - reds[rank_label])

                        if d_parent < d_cur:
                            # parent node is closer to median RED for rank_label
                            # than the current node
                            if parent_red - reds[rank_label] > 0:
                                # parent node is to the 'right' of the median RED
                                # for the rank so should likely be given the taxon label
                                fout.write('{}\t{}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{}\t{}\n'.format(
                                            taxon,
                                            rank_label,
                                            reds[rank_label],
                                            cur_red, 
                                            cur_red - reds[rank_label],
                                            parent_red, 
                                            parent_red - reds[rank_label],
                                            'taxon is too close to the extant taxa; consider moving to parent node',
                                            taxon_taxonomy[taxon]))
                                num_red_check += 1
                    
                    # check if taxon is too far to the left
                    if cur_red <= reds[rank_label] - 0.1:
                        # taxon is too close to the root so report it
                        fout.write('{}\t{}\t{:.3f}\t{:.3f}\t{:.3f}\t{}\t{}\t{}\t{}\n'.format(
                                        taxon,
                                        rank_label,
                                        reds[rank_label],
                                        cur_red, 
                                        cur_red - reds[rank_label],
                                        'N/A', 
                                        'N/A',
                                        'taxon is too close to root; consider dividing into multiple taxa',
                                        taxon_taxonomy[taxon]))
                                        
        fout.close()
        
        self.logger.info('Identified {:,} taxa with RED value requiring verification.'.format(num_red_check))
