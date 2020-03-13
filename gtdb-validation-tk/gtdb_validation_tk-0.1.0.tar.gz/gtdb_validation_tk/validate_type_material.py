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
import argparse
import logging
from collections import defaultdict, Counter

from biolib.taxonomy import Taxonomy

from gtdb_validation_tk.common import (parse_species_ledgers,
                                        parse_genus_ledger,
                                        parse_gtdb_synonym_file, 
                                        canonical_species_name)

class ValidateTypeMaterial(object):
    """Check for LPSN/DSMZ/StrainInfo type material potentially misannotated in GTDB taxonomy."""

    def __init__(self):
        self.logger = logging.getLogger()

    def validate_type_strains(self, 
                                input_taxonomy, 
                                gtdb_metadata_file,
                                sp_classification_ledger,
                                gtdb_named_type_genomes,
                                gtdb_synonym_file,
                                show_synonyms,
                                prefix,
                                output_dir):
        """Check LPSN/DSMZ/StrainInfo type strains of species against GTDB taxonomy."""
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # read species ledger
        species_ledger = parse_species_ledgers(sp_classification_ledger, None)
        
        # get selected GTDB representative genomes
        gtdb_rep_genomes = {}
        with open(gtdb_named_type_genomes) as f:
            f.readline()
            for line in f:
                line_split = line.strip().split('\t')
                species = line_split[0]
                gid = line_split[1]
                gtdb_rep_genomes[gid] = species
        
        # read GTDB synonyms
        synonyms = parse_gtdb_synonym_file(gtdb_synonym_file)
        
        # read taxonomy
        input_taxonomy = Taxonomy().read(input_taxonomy)

        # compare identified type material to GTDB taxonomy
        for domain in ['Archaea', 'Bacteria']:
            num_type_strains = 0
            modified_type_material = {}
            type_strains = defaultdict(list)
            with open(gtdb_metadata_file) as f:
                header = f.readline().strip().split('\t')
                
                ncbi_taxonomy_index = header.index('ncbi_taxonomy')
                gtdb_taxonomy_index = header.index('gtdb_taxonomy')
                gtdb_type_designation_index = header.index('gtdb_type_designation')
                gtdb_type_designation_sources_index = header.index('gtdb_type_designation_sources')

                for line in f:
                    line_split = line.strip().split('\t')
                    
                    gid = line_split[0]
                    if gid not in input_taxonomy:
                        continue # only consider genomes in the provided taxonomy file
                        
                    # get GTDB domain in database since this will
                    # be set for all genomes, and not just those
                    # in the input taxonomy file
                    gtdb_domain = [t.strip() for t in line_split[gtdb_taxonomy_index].split(';')][0]
                    if gtdb_domain[3:] != domain:
                        continue
                        
                    gtdb_type_designation = line_split[gtdb_type_designation_index]
                    if gtdb_type_designation != 'type strain of species':
                        continue

                    num_type_strains += 1
                        
                    gtdb_type_designation_sources = line_split[gtdb_type_designation_sources_index]
                    
                    # take GTDB taxonomy from input file
                    gtdb_taxa = input_taxonomy[gid]
                    gtdb_sp = gtdb_taxa[6]
                    gtdb_taxonomy = '; '.join(gtdb_taxa)

                    # get NCBI taxonomy 
                    ncbi_taxonomy = line_split[ncbi_taxonomy_index]
                    ncbi_taxa = [t.strip() for t in ncbi_taxonomy.split(';')]
                    ncbi_sp = ncbi_taxa[6]
                    
                    type_strains[ncbi_sp].append(gid)
                    
                    # check if genome is in GTDB species ledger
                    if gid in species_ledger:
                        if gtdb_sp != species_ledger[gid]:
                            self.logger.warning('GTDB species does not match species ledger: {} {} {}'.format(
                                                    gid,
                                                    gtdb_sp,
                                                    species_ledger[gid]))
                        else:
                            continue
                
                    if gtdb_sp != 's__' and ncbi_sp != gtdb_sp:
                        # check if the NCBI species is a GTDB synonym
                        is_gtdb_synonym = False
                        if ncbi_sp in synonyms and synonyms[ncbi_sp].species == canonical_species_name(gtdb_sp):
                            is_gtdb_synonym = True

                        if not is_gtdb_synonym or show_synonyms:
                            modified_type_material[gid] = [gtdb_taxonomy, ncbi_taxonomy, gtdb_type_designation_sources]

            fout = open(os.path.join(output_dir, '{}_{}_reassigned_type_strains.tsv'.format(prefix, domain.lower())), 'w')
            fout.write('Genome ID\tIncongruent specific name\tGTDB species\tNCBI species\tGTDB synonym\tSynonym ANI\tGTDB type material sources')
            fout.write('\tAdditional NCBI type material\tGTDB type genomes\tGTDB taxonomy\tNCBI taxonomy\n')
            incongruent_specific_name_count = 0
            for cur_gid in modified_type_material:
                gtdb_taxonomy, ncbi_taxonomy, gtdb_type_designation_sources = modified_type_material[cur_gid]
                gtdb_sp = [t.strip() for t in gtdb_taxonomy.split(';')][6]
                ncbi_sp = [t.strip() for t in ncbi_taxonomy.split(';')][6]

                type_genomes_in_gtdb = []
                additional_type_genomes = set(type_strains[ncbi_sp]) - set([cur_gid])
                for gid in additional_type_genomes:
                    if gid in input_taxonomy and input_taxonomy[gid][6] == ncbi_sp:
                        type_genomes_in_gtdb.append(gid)
                        
                if len(additional_type_genomes) > 0 and cur_gid not in gtdb_rep_genomes:
                    # this genome is not the selected GTDB representative
                    # even though it is assembled from the type strain
                    continue
                    
                incongruent_specific_name = gtdb_sp.split()[-1] != ncbi_sp.split()[-1]
                if incongruent_specific_name:
                    incongruent_specific_name_count += 1
                        
                fout.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
                                cur_gid,
                                incongruent_specific_name,
                                gtdb_sp, 
                                ncbi_sp,
                                synonyms[ncbi_sp].species if ncbi_sp in synonyms else 'N/A',
                                synonyms[ncbi_sp].ani if ncbi_sp in synonyms else 'N/A',
                                gtdb_type_designation_sources,
                                ', '.join(additional_type_genomes),
                                ', '.join(type_genomes_in_gtdb),
                                gtdb_taxonomy, 
                                ncbi_taxonomy))
            fout.close()
            
            print('Identified {:,} {} genomes in input taxonomy as being from the type strain of the species.'.format(num_type_strains, domain))
            print('  {:,} of these genomes do not have the expected species name'.format(len(modified_type_material)))
            print('  {:,} of these genomes have an incongruent specific name'.format(incongruent_specific_name_count))
            
    def validate_type_species(self, 
                                input_taxonomy, 
                                gtdb_metadata_file, 
                                gtdb_synonym_file,
                                sp_classification_ledger,
                                genus_classification_ledger,
                                show_synonyms,
                                prefix,
                                output_dir):
        """Check LPSN/DSMZ/StrainInfo type species of genus against GTDB taxonomy."""
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # read species ledger
        species_ledger = parse_species_ledgers(sp_classification_ledger, None)
        
        # read desired genus name for specific genomes
        gtdb_genus_ledger = parse_genus_ledger(genus_classification_ledger)
            
        # read GTDB synonyms
        synonyms = parse_gtdb_synonym_file(gtdb_synonym_file)

        # read taxonomy
        self.logger.info('Reading input GTDB taxonomy.')
        gtdb_taxonomy = Taxonomy().read(input_taxonomy)
        self.logger.info(' ...identified taxonomy for {:,} genomes.'.format(len(gtdb_taxonomy)))

        # read GTDB metadata to establish type species and NCBI taxonomy
        for domain in ['Archaea', 'Bacteria']:
            ncbi_taxonomy = {}
            type_species_gids = set()
            type_species = set()
            ncbi_sanity_check_multiple_type_species = defaultdict(set)
            gtdb_sanity_check_multiple_type_species = defaultdict(set)
            with open(gtdb_metadata_file) as f:
                header = f.readline().strip().split('\t')
                
                ncbi_taxonomy_index = header.index('ncbi_taxonomy')
                gtdb_taxonomy_index = header.index('gtdb_taxonomy')
                gtdb_type_species_index = header.index('gtdb_type_species_of_genus')

                for line in f:
                    line_split = line.strip().split('\t')
                    
                    gid = line_split[0]
                    if gid not in gtdb_taxonomy:
                        continue # only consider genomes in the provided taxonomy file
                        
                    # get GTDB domain in database since this will
                    # be set for all genomes, and not just those
                    # in the input taxonomy file
                    gtdb_taxa = [t.strip() for t in line_split[gtdb_taxonomy_index].split(';')]
                    gtdb_domain = gtdb_taxa[0]
                    if gtdb_domain[3:] != domain:
                        continue

                    gtdb_type_sp = line_split[gtdb_type_species_index]
                    if gtdb_type_sp != 't':
                        continue
 
                    type_species_gids.add(gid)

                    ncbi_taxonomy[gid] = [t.strip() for t in line_split[ncbi_taxonomy_index].split(';')]
                    type_species.add(ncbi_taxonomy[gid][6])
                    
                    ncbi_sanity_check_multiple_type_species[ncbi_taxonomy[gid][5]].add(ncbi_taxonomy[gid][6])
                    
                    gtdb_sanity_check_multiple_type_species[gtdb_taxa[5]].add(gtdb_taxa[6])

            # check if any genera have multiple type species
            for genus, species_list in ncbi_sanity_check_multiple_type_species.items():
                if len(species_list) > 1:
                    self.logger.warning('Genus {} has multiple NCBI type species: {}'.format(
                                            genus,
                                            ', '.join(species_list)))
                                            
            for genus, species_list in gtdb_sanity_check_multiple_type_species.items():
                if len(species_list) > 1:
                    self.logger.warning('Genus {} has multiple GTDB type species: {}'.format(
                                            genus,
                                            ', '.join(species_list)))
            
            # determine genera considered to be synonyms
            self.logger.info('Identifying genera that are heterotypic synonyms.')
            genus_synonyms = {}
            for synonym_sp in synonyms:
                priority_sp = synonyms[synonym_sp].species
                if synonym_sp in type_species and priority_sp in type_species:
                    synonym_genus = synonym_sp.split()[0].replace('s__', 'g__')
                    priority_genus = priority_sp.split()[0].replace('s__', 'g__')
                    genus_synonyms[synonym_genus] = priority_genus
            
            self.logger.info(' ...identified {} synonyms.'.format(len(genus_synonyms)))

            # compare identified type material to GTDB taxonomy
            modified_type_material = {}
            other_type_genomes = defaultdict(list)
            for gid in type_species_gids:
                gtdb_genus = gtdb_taxonomy[gid][5]
                ncbi_genus = ncbi_taxonomy[gid][5]
                
                # check if genome is in GTDB species ledger
                if gid in species_ledger:
                    generic_ledger = species_ledger[gid].split()[0].replace('s__', 'g__')
                    if gtdb_genus != generic_ledger:
                        self.logger.warning('GTDB genus does not match species ledger: {} {} {}'.format(
                                                gid,
                                                gtdb_genus,
                                                species_ledger[gid]))
                    else:
                        continue
                    
                # check if genome is in GTDB genus ledger
                if gid in gtdb_genus_ledger:
                    if gtdb_genus != gtdb_genus_ledger[gid]:
                        self.logger.warning('GTDB genus does not match genus ledger: {} {} {}'.format(
                                                gid,
                                                gtdb_genus,
                                                gtdb_genus_ledger[gid]))
                    else:
                        continue
                
                if gtdb_genus != 'g__'and gtdb_genus != ncbi_genus:
                    # check if the NCBI genus is a GTDB synonym
                    is_gtdb_synonym = False
                    if ncbi_genus in genus_synonyms and genus_synonyms[ncbi_genus] == gtdb_genus:
                        is_gtdb_synonym = True

                    if not is_gtdb_synonym or show_synonyms:
                        modified_type_material[gid] = [gtdb_taxonomy[gid], ncbi_taxonomy[gid]]
                        other_type_genomes[ncbi_genus].append(gid)
                        
            # write incongruent type species to file
            out_file = os.path.join(output_dir, '{}_{}_reassigned_type_species.tsv'.format(prefix, domain.lower()))
            
            print('Identified {:,} {} genomes in input taxonomy as being from the type species of the genus.'.format(
                    len(type_species_gids), 
                    domain))
            print('  {:,} of these genomes do not have the expected genus name'.format(len(modified_type_material)))

            fout = open(out_file, 'w')
            fout.write('Genome ID\tGTDB genus\tNCBI genus\tLedger genus\tGTDB genus synonym\tGTDB species\tNCBI species')
            fout.write('\tAdditional NCBI type material\tGTDB type genomes\tGTDB taxonomy\tNCBI taxonomy\n')
            for gid in modified_type_material:
                gtdb_taxa, ncbi_taxa = modified_type_material[gid]

                gtdb_genus = gtdb_taxa[5]
                ncbi_genus = ncbi_taxa[5]
                gtdb_sp = gtdb_taxa[6]
                ncbi_sp = ncbi_taxa[6]
                
                type_genomes_in_gtdb = []
                additional_type_genomes = set(other_type_genomes[ncbi_genus]) - set([gid])
                for gid in additional_type_genomes:
                    if gid in input_taxonomy and input_taxonomy[gid][6] == ncbi_genus:
                        type_genomes_in_gtdb.append(gid)
                
                fout.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
                                gid, 
                                gtdb_genus, 
                                ncbi_genus,
                                gtdb_genus_ledger.get(gid, 'N/A'),
                                genus_synonyms[ncbi_genus] if ncbi_genus in genus_synonyms else 'N/A',
                                gtdb_sp,
                                ncbi_sp,
                                ', '.join(additional_type_genomes),
                                ', '.join(type_genomes_in_gtdb),
                                '; '.join(gtdb_taxonomy[gid]), 
                                '; '.join(ncbi_taxonomy[gid])))
            fout.close()
