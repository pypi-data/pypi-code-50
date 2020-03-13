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
from collections import defaultdict, Counter

from biolib.taxonomy import Taxonomy

from gtdb_validation_tk.common import read_ncbi_taxonomy


class ValidateSpeciesClusters(object):
    """Verify classification of genomes assigned to the same species cluster."""

    def __init__(self):
        """Initialization."""
        
        self.logger = logging.getLogger()
        
    def _species_clusters(self, gtdb_metadata_file):
        """Get GTDB species clusters."""
        
        self.logger.info('Identifying species clusters.')
        sp_clusters = defaultdict(set)
        genome_rep = {}
        gtdb_reps = set()
        with open(gtdb_metadata_file) as f:
            header = f.readline().strip().split('\t')

            gtdb_genome_rep_index = header.index('gtdb_representative')
            gtdb_gid_rep_index = header.index('gtdb_genome_representative')
            
            for line in f:
                line_split = line.strip().split('\t')
                
                gid = line_split[0]
                gtdb_rep = line_split[gtdb_genome_rep_index]
                gtdb_rep_gid = line_split[gtdb_gid_rep_index]
                
                if gtdb_rep == 't':
                    gtdb_reps.add(gid)
                
                if gtdb_rep_gid and gtdb_rep_gid != 'none':
                    genome_rep[gid] = gtdb_rep_gid
                    sp_clusters[gtdb_rep_gid].add(gid)
                    
        self.logger.info('Identified %d species clusters spanning %d genomes.' % (
                            len(gtdb_reps),
                            len(genome_rep)))
        
        assert(len(sp_clusters) == len(gtdb_reps))
                            
        return sp_clusters
        
    def _check_sp_assignments(self, sp_clusters, gtdb_taxonomy, output_dir):
        """Check that all genomes in a cluster have the same name as their representative."""
        
        fout = open(os.path.join(output_dir, 'check_sp_clusters.tsv'), 'w')
        fout.write('Representative ID\tGenome ID\tRepresentative taxonomy\tGenome taxonomy\n')
        num_failed = 0
        for rid in sp_clusters:
            for gid in sp_clusters[rid]:
                if gtdb_taxonomy[rid] != gtdb_taxonomy[gid]:
                    fout.write('%s\t%s\t%s\t%s\n' % (rid, gid, gtdb_taxonomy[rid], gtdb_taxonomy[gid]))
                    num_failed += 1
                    
        fout.close()
                
        if num_failed != 0:
            self.logger.info('Identified %d cases of genomes with conflicting species assignments.' % num_failed)
        else:
            self.logger.info('All genomes in taxonomy file passed validation.')

    def _check_sp_genus_name(self, gtdb_taxonomy, output_dir):
        """Check genus name of species is same as genus."""
        
        fout = open(os.path.join(output_dir, 'check_sp_genus_name.tsv'), 'w')
        fout.write('Genome ID\tGenus\tSpecies\n')
        num_failed = 0
        for gid, taxa in gtdb_taxonomy.items():
            if taxa[6] == 's__':
                continue # skip since prior to R86 this was not uncommon
                
            genus = taxa[5][3:]
            sp = taxa[6][3:]
            
            if not sp.startswith(genus):
                fout.write('%s\t%s\t%s\n' % (gid, taxa[5], taxa[6]))
                num_failed += 1

        fout.close()
        
        if num_failed != 0:
            self.logger.info('Identified %d cases of genomes with conflicting genus names.' % num_failed)
        else:
            self.logger.info('All genomes in taxonomy file passed genus name check.')
            
    def _check_gtdb_genera(self, sp_clusters, gtdb_taxonomy, ncbi_taxonomy, output_dir):
        """Check if GTDB genera have support from NCBI taxonomy."""
        
        # get all genomes in GTDB genus
        genus_gids = defaultdict(set)
        for gid, taxa in gtdb_taxonomy.items():
            genus_gids[taxa[5]].add(gid)
            
            if gid in sp_clusters:
                for cid in sp_clusters[gid]:
                    genus_gids[taxa[5]].add(cid)
                    
        # check if NCBI taxonomy supports genus assignment
        fout = open(os.path.join(output_dir, 'check_genera.tsv'), 'w')
        fout.write('GTDB genus\tMost common NCBI genus\tMost common percentage\tNCBI genera\tGenus size\tGenome IDs\n')
            
        num_failed = 0
        for gtdb_genus, gids in genus_gids.items():
            # check if specific name is a placeholder name
            is_placeholder = False
            for idx, ch in enumerate(gtdb_genus[3:]):
                if not ch.isalpha() or (idx>0 and not ch.islower()):
                    # genus contains a non-alphabetic and/or 
                    # an uppercase character besides the initial
                    # capitalization so is a placeholder name
                    is_placeholder = True
                    break

            if is_placeholder:
                continue
                
            # create canonical genus name
            canonical_gtdb_genus = gtdb_genus
            if '_' in canonical_gtdb_genus[3:]:
                canonical_gtdb_genus = canonical_gtdb_genus[0:canonical_gtdb_genus.rfind('_')]
        
            # check for support in NCBI taxonomy
            ncbi_genera = []
            for gid in gids:
                ncbi_genus = ncbi_taxonomy[gid][5]
                if ncbi_genus == 'g__':
                    continue 
                    
                ncbi_genus = ncbi_genus.replace('Candidatus ', '')
                ncbi_genera.append(ncbi_genus)
                
            if ncbi_genera:
                # consider all genera that are equally abundant
                ncbi_counter = Counter(ncbi_genera)
                prev_genus_count = 0
                for ncbi_genus_common, genus_count in ncbi_counter.most_common():
                    if genus_count < prev_genus_count:
                        break # no longer at equally abundant species name
                        
                    prev_genus_count = genus_count
                        
                    if ncbi_genus_common != canonical_gtdb_genus:
                        num_failed += 1
                        fout.write('%s\t%s\t%.2f\t%s\t%d\t%s\n' % (
                            gtdb_genus,
                            ncbi_genus_common,
                            float(genus_count)*100.0/len(ncbi_genera),
                            ', '.join(['%s:%d' % (k,v) for k,v in ncbi_counter.most_common()]),
                            len(gids),
                            ','.join(gids)))
            else:
                # no genomes with an assigned NCBI genus
                num_failed += 1
                fout.write('%s\t%s\t%.2f\t%s\t%d\t%s\n' % (
                            gtdb_genus,
                            'no assigned genera',
                            0.0,
                            '',
                            len(gids),
                            ','.join(gids)))

        fout.close()
                    
        if num_failed != 0:
            self.logger.info('Identified %d cases of potentially unsupported GTDB genus assignments.' % num_failed)
        else:
            self.logger.info('All GTDB genus assignments appear to have well-supported by the NCBI taxonomy.')
            
    def _check_sp_specific_name(self, sp_clusters, gtdb_taxonomy, ncbi_taxonomy, output_dir):
        """Check is specific name of GTDB species has support from NCBI species assignments."""

        fout = open(os.path.join(output_dir, 'check_sp_specific_name.tsv'), 'w')
        fout.write('Representative ID\tCluster size\tGTDB species')
        fout.write('\tMost common NCBI species\tMost common percentage\tNCBI species\tCluster IDs\n')
            
        num_failed = 0
        for rid, cluster_ids in sp_clusters.items():
            gtdb_sp = gtdb_taxonomy[rid][6]
            if gtdb_sp == 's__':
                continue # skip since prior to R86 this was not uncommon
                
            # get canonical version of specific name
            gtdb_specific_name = gtdb_sp.split()[-1]
            if '_' in gtdb_specific_name:
                gtdb_specific_name = gtdb_specific_name[0:gtdb_specific_name.rfind('_')]
            
            # check if specific name is a placeholder name
            is_placeholder = False
            for ch in gtdb_specific_name:
                if not ch.isalpha() or not ch.islower():
                    # specific name contains a non-alphabetic and/or 
                    # uppercase character so is a placeholder name
                    is_placeholder = True
                    break

            if is_placeholder:
                continue

            # check if NCBI taxonomy agrees with GTDB specific name
            ncbi_sp_names = []
            for gid in cluster_ids.union([rid]):
                ncbi_sp = ncbi_taxonomy[gid][6]
                if ncbi_sp == 's__':
                    continue 
                    
                ncbi_sp_names.append(ncbi_sp)
                
            if ncbi_sp_names:
                # consider all species names that are equally abundant
                ncbi_counter = Counter(ncbi_sp_names)
                prev_sp_count = 0
                for ncbi_sp_common, sp_count in ncbi_counter.most_common():
                    if sp_count < prev_sp_count:
                        break # no longer at equally abundant species name
                        
                    prev_sp_count = sp_count
                        
                    ncbi_specific_name = ncbi_sp_common.split()[-1]
                    if ncbi_specific_name != gtdb_specific_name:
                        num_failed += 1
                        fout.write('%s\t%d\t%s\t%s\t%.2f\t%s\t%s\n' % (
                                rid,
                                len(cluster_ids),
                                gtdb_sp,
                                ncbi_sp_common,
                                float(sp_count)*100.0/len(ncbi_sp_names),
                                ', '.join(['%s:%d' % (k,v) for k,v in ncbi_counter.most_common()]),
                                ','.join(cluster_ids)))
            else:
                # no genomes with an assigned NCBI species name
                num_failed += 1
                fout.write('%s\t%d\t%s\t%s\t%.2f\t%s\t%s\n' % (
                            rid,
                            len(cluster_ids),
                            gtdb_sp,
                            'no assigned species',
                            0.0,
                            '',
                            ','.join(cluster_ids)))

        fout.close()
        
        if num_failed != 0:
            self.logger.info('Identified %d cases of potentially unsupported specific species names.' % num_failed)
        else:
            self.logger.info('All clusters appear to have well-supported specific species names.')
            
    def run(self, input_taxonomy, gtdb_metadata_file, output_dir):
        """Verify classification of genomes assigned to the same species cluster."""
        
        gtdb_taxonomy = Taxonomy().read(input_taxonomy)
        ncbi_taxonomy = read_ncbi_taxonomy(gtdb_metadata_file)
        
        # check that all genomes have an assigned species 
        for gid, taxa in gtdb_taxonomy.items():
            if taxa[6] == 's__':
                # issue warning since this was common prior to R89
                self.logger.warning('Genome %s does not have an assigned species.' % gid)
                
            if taxa[5] == 'g__':
                self.logger.error('Genome %s does not have an assigned genus.' % gid)
                sys.exit(-1)
        
        # identify clusters
        sp_clusters = self._species_clusters(gtdb_metadata_file)

        # validate that genomes in the same species cluster have the same assignment
        self._check_sp_assignments(sp_clusters, gtdb_taxonomy, output_dir)
        
        # check if GTDB genera have support from NCBI taxonomy
        self._check_gtdb_genera(sp_clusters, gtdb_taxonomy, ncbi_taxonomy, output_dir)
        
        # validate genus name of species assignments
        self._check_sp_genus_name(gtdb_taxonomy, output_dir)
        
        # check is specific name of GTDB species has support from NCBI species assignments
        self._check_sp_specific_name(sp_clusters, gtdb_taxonomy, ncbi_taxonomy, output_dir)

