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
import re
from collections import defaultdict
from collections import Counter

from biolib.taxonomy import Taxonomy

import dendropy

def suffix_value(suffix):
    """Get value of taxa suffix.
    
    A = 65, B = 66, ..., Z = 90
    AA = 16705, AB = 16705, BA = 16961
    """
    
    v = 0
    for idx, ch in enumerate(suffix):
        v += 256**(len(suffix)-idx-1) * ord(ch)
    
    return v
    
def increment_suffix(suffix):
    """Increment suffix by one character."""
    
    if len(suffix) > 2:
        print('[Error] Unable to handle suffixes with >2 characters.')
        sys.exit(-1)
    
    if len(suffix) == 1:
        if suffix != 'Z':
            suffix = chr(ord(suffix) + 1)
        else:
            suffix = 'AA'
    else:
        last_ch = suffix[1]
        if last_ch != 'Z':
            suffix = suffix[0] + chr(ord(last_ch) + 1)
        else:
            first_ch = suffix[0]
            first_ch = chr(ord(first_ch) + 1)
            suffix = first_ch + 'A'

    return suffix


class SuffixTable():
    """Create table indicating last polyphyly suffix used for each taxon."""

    def __init__(self):
        """Initialize."""
        
        self.prev_taxonomy_dir = '/srv/projects/gtdb/data/taxonomy_gtdb'
        self.prev_tree_dir = '/srv/projects/gtdb/data/trees_gtdb'
        
        self.logger = logging.getLogger('timestamp')

    def run(self, input_taxonomy, output_table):
        """Create table indicating last polyphyly suffix used for each taxon."""
        
        # get all previous taxonomy files
        self.logger.info('Reading previous GTDB taxonomy files in %s:' % self.prev_taxonomy_dir)
        prev_taxonomy_files = []
        taxonomies = defaultdict(lambda: {})
        for f in os.listdir(self.prev_taxonomy_dir):
            if f.endswith('.tsv') and 'gtdb' in f:
                self.logger.info('  %s' % f)
                taxonomy_file = os.path.join(self.prev_taxonomy_dir, f)
                prev_taxonomy_files.append(taxonomy_file)
                
                taxonomy_id ='_'.join(f.split('_')[0:2])
                taxonomies[taxonomy_id].update(Taxonomy().read(taxonomy_file))
            
        self.logger.info('Considering taxonomy from %d previous releases.' % len(taxonomies))
        
        # get canonical genomes in previous GTDB reference trees
        self.logger.info('Determining canonical genomes in previous GTDB trees: %s' % self.prev_tree_dir)
        prev_canonical_gids = defaultdict(set)
        for f in os.listdir(self.prev_tree_dir):
            if f.endswith('.tree'):
                tree = dendropy.Tree.get_from_path(os.path.join(self.prev_tree_dir, f), 
                                                    schema='newick', 
                                                    rooting="force-rooted", 
                                                    preserve_underscores=True)
                gids = set()
                for leaf in tree.leaf_node_iter():
                    gids.add(leaf.taxon.label)
                    
                self.logger.info('  %s contains %d genomes' % (f, len(gids)))
                
                tree_id = '_'.join(f.split('_')[0:2])
                prev_canonical_gids[tree_id].update(gids)
                
        self.logger.info('Considering trees from %d previous GTDB releases.' % len(prev_canonical_gids))

        # get highest alphabetic suffix for each taxon
        self.logger.info('Determining highest polyphyletic alphabetic suffix for each taxon.')
        taxonomy_files = prev_taxonomy_files
        if input_taxonomy:
            self.logger.info('Also considering specified taxonomy files: %s' % input_taxonomy)
            taxonomies['input_taxonomy'] = Taxonomy().read(input_taxonomy)
            
        taxon_suffix = {}
        for taxonomy in taxonomies.values():
            for taxa in taxonomy.values():
                for taxon in taxa:
                    rank_prefix = taxon[0:3]
                    taxon_name = taxon[3:]

                    if '_' in taxon_name:
                        if rank_prefix != 's__':
                            taxon_name, suffix = taxon_name.rsplit('_', 1)
                        else:
                            # check is the specific name has a suffix
                            specific_name = taxon_name.split()[-1]
                            if '_' in specific_name:
                                taxon_name, suffix = taxon_name.rsplit('_', 1)
                            else:
                                continue

                        canonical_taxon = '%s%s' % (rank_prefix, taxon_name)
                        cur_suffix = taxon_suffix.get(canonical_taxon, 'A')
                        if suffix_value(suffix) >= suffix_value(cur_suffix):
                            taxon_suffix[canonical_taxon] = suffix
                            
        # get canonical genome for each highest suffix taxon
        self.logger.info('Determining canonical exemplar genome for each taxon.')
        example_gids = defaultdict(lambda: {})
        for tree_id in prev_canonical_gids:
            if tree_id not in taxonomies:
                continue
                
            taxonomy = taxonomies[tree_id]
            taxon_exemplars = {}
            for gid, taxa in taxonomy.items():
                for taxon in taxa:
                    taxon_exemplars[taxon] = gid
            
            for taxon, suffix in taxon_suffix.items():
                taxon_name = '%s_%s' % (taxon, taxon_suffix[taxon])
                if taxon_name in taxon_exemplars:
                    example_gids[tree_id][taxon_name] = taxon_exemplars[taxon_name]

        # write out suffix table
        if output_table:
            fout = open(output_table, 'w')
            fout.write('Taxon\tSuffix')
            for tree_id in sorted(prev_canonical_gids, reverse=True):
                fout.write('\t%s' % tree_id)
            fout.write('\n')
            
            for taxon in Taxonomy().sort_taxa(taxon_suffix):
                fout.write('%s\t%s' % (taxon, taxon_suffix[taxon]))
                
                taxon_name = '%s_%s' % (taxon, taxon_suffix[taxon])
                for tree_id in sorted(prev_canonical_gids, reverse=True):
                    if tree_id in example_gids:
                        fout.write('\t%s' % example_gids[tree_id].get(taxon_name, 'n/a'))
                    else:
                        fout.write('\tn/a')
                fout.write('\n')
                
            fout.close()
        
        return taxon_suffix