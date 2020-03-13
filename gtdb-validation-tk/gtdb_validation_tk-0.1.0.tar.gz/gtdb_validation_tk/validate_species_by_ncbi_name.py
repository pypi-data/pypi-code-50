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


class ValidateSpeciesNames(object):
    """Find discrepancies between GTDB and NCBI species names."""

    def __init__(self):
        self.logger = logging.getLogger()

    def run(self, gtdb_taxonomy_file, gtdb_metadata_file, output_dir):
        """Find discrepancies between GTDB and NCBI species names.."""
        
        # identify genomes of sufficient quality to be considered
        genomes_to_consider = set()
        ncbi_species = {}
        canonical_ncbi_species = defaultdict(lambda: {})
        ncbi_sp_genomes = defaultdict(list)
        type_strain = set()
        type_sources = {}
        with open(gtdb_metadata_file) as f:
            header = f.readline().strip().split('\t')

            ncbi_taxonomy_index = header.index('ncbi_taxonomy')
            gtdb_rep_index = header.index('gtdb_representative')
            gtdb_type_designation_index = header.index('gtdb_type_designation')
            gtdb_type_designation_sources_index = header.index('gtdb_type_designation_sources')
            
            for line in f:
                line_split = line.strip().split('\t')
                
                gid = line_split[0]
                if gid.startswith('U_'):
                    continue
                
                # only consider GTDB representative genomes
                gtdb_rep = line_split[gtdb_rep_index]
                if not gtdb_rep.lower().startswith('t'):
                    continue

                genomes_to_consider.add(gid)
                
                gtdb_type_designation = line_split[gtdb_type_designation_index]
                if gtdb_type_designation == 'type strain of species':
                    type_strain.add(gid)
                        
                gtdb_type_designation_sources = line_split[gtdb_type_designation_sources_index]
                type_sources[gid] = gtdb_type_designation_sources

                # get NCBI taxonomy information
                ncbi_taxonomy = line_split[ncbi_taxonomy_index]
                if ncbi_taxonomy and ncbi_taxonomy != 'none':
                    ncbi_taxa = [t.strip() for t in ncbi_taxonomy.split(';')]
                    domain = ncbi_taxa[0][3:]
                    sp = ncbi_taxa[6]
                    
                    canonical_sp = sp.replace('Candidatus ', '').replace('[', '').replace(']', '')
                    canonical_sp = ' '.join(canonical_sp.split()[0:2]).strip()
                    ncbi_species[gid] = canonical_sp
                    canonical_ncbi_species[domain][canonical_sp] = sp
                    ncbi_sp_genomes[sp].append(gid)

        self.logger.info('Identified {:,} species assembled from type material.'.format(len(ncbi_sp_genomes)))

        # get GTDB species designations
        gtdb_species = defaultdict(lambda: {})
        unique_gtdb_species = defaultdict(lambda: set())
        canonical_gtdb_species = defaultdict(lambda: set())
        for line in open(gtdb_taxonomy_file):
            line_split = line.strip().split('\t')
            
            gid = line_split[0]
            if gid not in genomes_to_consider:
                continue
                
            taxonomy = [t.strip() for t in line_split[1].split(';')]
            domain = taxonomy[0][3:]
            sp = taxonomy[6]

            # get canonical species names by removing polyphyly suffices
            canonical_sp = 's__' + ' '.join([t.strip() for t in re.split('_[A-Z]+(?=\s|$)', sp[3:])]).strip()
            gtdb_species[domain][gid] = (sp, canonical_sp)

            unique_gtdb_species[domain].add(sp)
            canonical_gtdb_species[domain].add(canonical_sp)

        for domain in ['Archaea', 'Bacteria']:
            discrepancies = {}
            for gid in gtdb_species[domain]:
                gtdb_sp, gtdb_canonical_sp = gtdb_species[domain][gid]
                ncbi_sp = ncbi_species.get(gid, 's__')
                
                if gtdb_canonical_sp != ncbi_sp and ncbi_sp != 's__':
                    discrepancies[gid] = (gtdb_sp, 
                                            gtdb_canonical_sp, 
                                            ncbi_sp, 
                                            str(gid in type_strain), 
                                            type_sources[gid])

            self.logger.info('[{}] There are {:,} unique GTDB species.'.format(domain.capitalize(),
                                                                            len(unique_gtdb_species[domain])))
            self.logger.info('[{}] There are {:,} canonical GTDB species.'.format(domain.capitalize(),
                                                                            len(canonical_gtdb_species[domain])))
            self.logger.info('[{}] There are {:,} genomes with different NCBI and GTDB species names.'.format(domain.capitalize(),
                                                                                                        len(discrepancies)))
                    
            fout = open(os.path.join(output_dir, '{}_gtdb_species_discrepancies.tsv'.format(domain.lower())), 'w')
            fout.write('Genome ID\tGTDB species\tGTDB canonical\tNCBI species\tType strain\tGTDB type material sources\n')
            
            sorted_d = sorted(discrepancies.items(), key=lambda x: x[1][1])
            for gid, info in sorted_d:
                fout.write('{}\t{}\n'.format(gid, '\t'.join(info)))
            fout.close()
            
            fout = open(os.path.join(output_dir, '{}_missing_ncbi_species.tsv'.format(domain.lower())), 'w')
            fout.write('Canonical Name\tUnmodified Name\tType strain\tNCBI genomes\tGTDB taxonomy\n')
            missing_sp = 0
            for ncbi_sp in set(canonical_ncbi_species[domain]) - canonical_gtdb_species[domain]:
                missing_sp += 1
                sp_gids = ncbi_sp_genomes[canonical_ncbi_species[domain][ncbi_sp]]
                
                gtdb_sps = defaultdict(int)
                for gid in sp_gids:
                    if gid in gtdb_species[domain]:
                        gtdb_sps[gtdb_species[domain][gid][0]] += 1
                    
                gtdb_sp_str = []
                for sp, count in gtdb_sps.items():
                    gtdb_sp_str.append('{}:{}'.format(sp, count))
                
                fout.write('{}\t{}\t{}\t{}\t{}\n'.format(ncbi_sp, 
                                                canonical_ncbi_species[domain][ncbi_sp],
                                                any([gid in type_strain for gid in sp_gids]),
                                                ', '.join(gtdb_sp_str),
                                                ', '.join(sp_gids)))
                                                
            self.logger.info('[{}] Missing {:,} NCBI species names in GTDB taxonomy.'.format(domain.capitalize(), missing_sp))
            fout.close()
