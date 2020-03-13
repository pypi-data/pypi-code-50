#!/usr/bin/env python

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
import re
import operator
import logging
from collections import defaultdict


class ValidateClustersNCBI(object):
    """Tabulate NCBI species assigned to each GTDB cluster."""

    def __init__(self):
        self.logger = logging.getLogger()

    def run(self, input_taxonomy, gtdb_metadata_file, output_dir):
        """Tabulate NCBI species assigned to each GTDB cluster."""
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        self.logger.info('Reading input taxonomy.')
        gtdb_taxonomy = {}
        gtdb_sp = {}
        with open(input_taxonomy) as f:
            for line in f:
                line_split = line.strip().split('\t')
                gtdb_taxonomy[line_split[0]] = [t.strip() for t in line_split[1].split(';')]
                gtdb_sp[line_split[0]] = gtdb_taxonomy[line_split[0]][6]
        self.logger.info(' ...read taxonomy for {:,} genomes.'.format(len(gtdb_taxonomy)))
        
        self.logger.info('Reading NCBI taxonomy from GTDB metadata file.')
        clusters = defaultdict(lambda: defaultdict(set))
        
        ncbi_sp = {}
        gtdb_type_material = set()
        type_sources = {}
        with open(gtdb_metadata_file) as f:
            header = f.readline().strip().split('\t')
            
            ncbi_taxonomy_index = header.index('ncbi_taxonomy')
            rep_id_index = header.index('gtdb_genome_representative')
            gtdb_type_material_index = header.index('gtdb_type_designation')
            gtdb_type_material_source_index = header.index('gtdb_type_designation_sources')

            for line in f:
                line_split = line.strip().split('\t')
                
                gid = line_split[0]
                if gid not in gtdb_taxonomy:
                    continue
                    
                rep_id = line_split[rep_id_index]
                if not rep_id or rep_id == 'none':
                    continue
                
                ncbi_taxonomy = line_split[ncbi_taxonomy_index]
                domain = 'd__Bacteria'
                if ncbi_taxonomy and ncbi_taxonomy != 'none':
                    ncbi_taxa = [t.strip() for t in ncbi_taxonomy.split(';')]
                    ncbi_sp[gid] = ncbi_taxa[6].replace('Candidatus ', '')
                    
                is_gtdb_type_material = line_split[gtdb_type_material_index]
                if is_gtdb_type_material.lower() == 't' or is_gtdb_type_material.lower() == 'true':
                    gtdb_type_material.add(gid)
                    
                    type_sources[gid] = line_split[gtdb_type_material_source_index]
                    
                domain = gtdb_taxonomy[gid][0]
                clusters[domain[3:]][rep_id].add(gid)
        
        for domain in ['Archaea', 'Bacteria']:
            domain_clusters = clusters[domain]
            
            fout = open(os.path.join(output_dir, '%s_gtdb_clusters_info.tsv' % domain.lower()), 'w')
            fout.write('Representative ID\tNo. genomes\tGTDB taxonomy\tNCBI species')
            fout.write('\tNo. NCBI species\tNo. NCBI species >1\tNo. incongruent with GTDB name')
            fout.write('\tCongruent type material\tIncongruent type material\n')
            for rep_id in sorted(domain_clusters, key=lambda k: len(domain_clusters[k]), reverse=True):
                fout.write('%s\t%d\t%s' % (rep_id, len(domain_clusters[rep_id]), ';'.join(gtdb_taxonomy[rep_id])))
                
                gtdb_sp = gtdb_taxonomy[rep_id][6]
                ncbi_species = defaultdict(int)
                incongruent_type_material = []
                congruent_type_material = []
                for gid in domain_clusters[rep_id]:
                    if gid in ncbi_sp:
                        ncbi_species[ncbi_sp[gid]] += 1
                        
                        if gid in gtdb_type_material and gtdb_sp == ncbi_sp[gid]:
                            congruent_type_material.append('%s [%s]' % (gid, type_sources[gid]))

                        if gid != rep_id and gid in gtdb_type_material and gtdb_sp != ncbi_sp[gid]:
                            incongruent_type_material.append('%s: %s [%s]' % (gid, ncbi_sp[gid], type_sources[gid]))
                    
                canonical_gtdb_sp = 's__' + ' '.join([t.strip() for t in re.split('_[A-Z]+', gtdb_sp[3:])]).strip()
   
                ncbi_str = []
                num_ncbi_species = 0
                num_ncbi_species_multi_genomes = 0
                num_incongruent = 0
                for sp in sorted(ncbi_species, key=lambda k: ncbi_species[k], reverse=True):
                    ncbi_str.append('%s: %d' % (sp, ncbi_species[sp]))
                    if sp != 's__':
                        num_ncbi_species += 1
                        if ncbi_species[sp] > 1:
                            num_ncbi_species_multi_genomes += 1
                            if sp != canonical_gtdb_sp:
                                num_incongruent += ncbi_species[sp]
                
                fout.write('\t%s\t%d\t%d\t%d\t%s\t%s\n' % (', '.join(ncbi_str), 
                                                            num_ncbi_species, 
                                                            num_ncbi_species_multi_genomes, 
                                                            num_incongruent,
                                                            ', '.join(congruent_type_material),
                                                            ', '.join(incongruent_type_material)))
            fout.close()
