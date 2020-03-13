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

from biolib.taxonomy import Taxonomy

from gtdb_validation_tk.common import (parse_species_ledgers,
                                        parse_genus_ledger,
                                        parse_gtdb_synonym_file,
                                        gtdb_canonical_species_id,
                                        canonical_taxon_name,
                                        canonical_species_name,
                                        canonical_wgs_id,
                                        latinized_generic_sp_name,
                                        latinized_specific_sp_name)


class CheckSpeciesNames():
    """Validate species names."""

    def __init__(self):
        """Initialize."""
        
        self.logger = logging.getLogger()
        
    def read_user_genome_table(self, user_genome_id_table):
        """Read user genome ID table."""
        
        uba_map = {}
        ncbi_map = {}
        for line in open(user_genome_id_table):
            line_split = line.strip().split('\t')
            if len(line_split) == 3:
                ncbi_map[line_split[0]] = line_split[2]
                uba_map[line_split[0]] = line_split[1]
            else:
                uba_map[line_split[0]] = line_split[1]
                
        return uba_map, ncbi_map
        
    def gtdb_species_id(self, gid, specific_name):
        """Check if specific name has the form sp<accession>."""
        
        canonical_name = canonical_taxon_name(sspecific_name)
        
        if canonical_name.startswith('sp'):
            sp_id = gid[gid.find('_')+1:gid.rfind('.')]
            if canonical_name[2:] == sp_id:
                return True
                
        return False

    def check_generic(self,
                        input_taxonomy,
                        gtdb_metadata_file,
                        sp_classification_ledger,
                        genus_ledger,
                        gtdb_synonym_file,
                        user_genome_id_table,
                        output_dir):
        """Validate generic name of species."""
        
        # read user genome ID table
        uba_map, ncbi_map = self.read_user_genome_table(user_genome_id_table)
        
        # read species ledger
        species_ledger = parse_species_ledgers(sp_classification_ledger, None)
        
        # read genus ledger
        genus_ledger = parse_genus_ledger(genus_ledger)
        
        # get genomes in each GTDB genus
        gtdb_genera = defaultdict(list)
        gtdb_taxonomy = {}
        for line in open(input_taxonomy):
            line_split = line.strip().split('\t')
            
            gid = line_split[0]
            taxa = [t.strip() for t in line_split[1].split(';')]
            gtdb_genera[taxa[5]].append(gid)
            gtdb_taxonomy[gid] = taxa
        
        # read NCBI metadata from GTDB metadata
        ncbi_species = {}
        ncbi_genus = {}
        ncbi_org_names = {}
        ncbi_isolate = {}
        wgs_id = {}
        with open(gtdb_metadata_file, 'rt') as f:
            header = f.readline().strip().split('\t')
            
            ncbi_taxonomy_index = header.index('ncbi_taxonomy')
            ncbi_org_name_index = header.index('ncbi_organism_name')
            ncbi_isolate_index = header.index('ncbi_isolate')
            wgs_acc_index = header.index('ncbi_wgs_master')
            
            for line in f:
                line_split = line.strip().split('\t')

                gid = line_split[0]

                ncbi_taxonomy = line_split[ncbi_taxonomy_index]
                if ncbi_taxonomy != 'none':
                    ncbi_species[gid] = [t.strip() for t in ncbi_taxonomy.split(';')][6]
                    ncbi_genus[gid] = [t.strip() for t in ncbi_taxonomy.split(';')][5]
                else:
                    ncbi_species[gid] = 's__'
                    ncbi_genus[gid] = 'g__'
                    
                ncbi_org_names[gid] = line_split[ncbi_org_name_index].replace('_', '-').upper()
                ncbi_isolate[gid] = line_split[ncbi_isolate_index].replace('_', '-').replace(' ', '-').upper()
                wgs_id[gid] = canonical_wgs_id(line_split[wgs_acc_index])

                if gid in uba_map:
                    ncbi_isolate[gid] = uba_map[gid]

        # validate generic species names in taxonomy file
        fout_pass = open(os.path.join(output_dir, 'supported_generic_names.tsv'), 'w')
        fout_pass.write('GTDB genus\tGenomes in genus\tGenomes supporting name\tReasons for support\n')
        
        fout_fail = open(os.path.join(output_dir, 'unsupported_generic_names.tsv'), 'w')
        fout_fail.write('GTDB genus\tGenomes in genus\tGenome IDs\n')
        
        for genus, gids in gtdb_genera.items():
            support = {}
            num_genomes = 0
            for gid in gids:
                if gid.startswith('D-'):
                    continue # skip dummy genomes
                    
                num_genomes += 1
                species = gtdb_taxonomy[gid][6]
                generic = species.split()[0].replace('s__', '')
                canonical_generic_name = canonical_taxon_name(generic)
                
                if generic != genus.replace('g__', ''):
                    self.logger.error('Generic species and genus names do not match: {} {} {}'.format(
                                        gid,
                                        species,
                                        genus))
                    sys.exit(-1)
                    
                # get valid genus names derived from NCBI genome accession
                cur_gid = gid
                if cur_gid in ncbi_map:
                    cur_gid = ncbi_map[gid]
                    
                genus_from_accession = []
                canonical_gid = cur_gid.replace('GB_', '').replace('RS_', '').replace('_', '-')
                canonical_gid = canonical_gid[0:canonical_gid.rfind('.')]
                genus_from_accession.append(canonical_gid)
                
                # accession without leading zeros
                t = canonical_gid[0:4]
                for idx, ch in enumerate(canonical_gid[4:]):
                    if ch != '0':
                        t += canonical_gid[4+idx:]
                        break
                    
                genus_from_accession.append(t)
                
                # check species ledger
                name_passed = False
                reason = None
                if gid in species_ledger:
                    ledger_species = species_ledger[gid]
                    ledger_generic = ledger_species.split()[0].replace('s__', '')
                    canonical_ledger_generic = canonical_taxon_name(ledger_generic)
                    if canonical_generic_name == canonical_ledger_generic:
                        support[gid] = 'Generic name specified in species ledger'
                elif gid in genus_ledger:
                    ledger_genus = genus_ledger[gid]
                    ledger_generic = ledger_genus.replace('g__', '')
                    canonical_ledger_generic = canonical_taxon_name(ledger_generic)
                    if canonical_generic_name == canonical_ledger_generic:
                        support[gid] = 'Generic name specified in genus ledger'
                elif (latinized_generic_sp_name(canonical_generic_name) 
                        and canonical_generic_name == ncbi_genus[gid].replace('g__', '')):
                    support[gid] = 'Congruent with NCBI genus name'
                elif canonical_generic_name.upper() in ncbi_org_names[gid]:
                    support[gid] = 'Generic name derived from NCBI organism name'
                elif canonical_generic_name.upper() in ncbi_isolate[gid]:
                    support[gid] = 'Generic name derived from NCBI infraspecific name'
                elif canonical_generic_name == wgs_id[gid]:
                    support[gid] = 'Generic name derived from NCBI WGS ID'
                elif canonical_generic_name in genus_from_accession:
                    support[gid] = 'Generic name derived from NCBI genome accession number'

            if len(support) > 0:
                support_str = []
                for k, v in support.items():
                    support_str.append('{}:{}'.format(k,v))
                fout_pass.write('{}\t{}\t{}\t{}\n'.format(
                                        genus, 
                                        num_genomes,
                                        len(support),
                                        '; '.join(support_str)))
            else:
                fout_fail.write('{}\t{}\t{}\n'.format(
                                genus, 
                                num_genomes, 
                                '; '.join(gids)))

        fout_fail.close()
        fout_pass.close()
        
    def check_specific(self, 
                    input_taxonomy,
                    gtdb_metadata_file,
                    sp_classification_ledger,
                    gtdb_synonym_file,
                    user_genome_id_table,
                    output_dir):
        """Validate specific name of species."""
        
        # read user genome ID table
        uba_map, ncbi_map = self.read_user_genome_table(user_genome_id_table)

        # read species ledger
        species_ledger = parse_species_ledgers(sp_classification_ledger, None)
        
        # read synonyms
        synonyms = parse_gtdb_synonym_file(gtdb_synonym_file)
                
        # read NCBI species from GTDB metadata
        ncbi_species = {}
        ncbi_subspecies = {}
        with open(gtdb_metadata_file, 'rt') as f:
            header = f.readline().strip().split('\t')
            
            ncbi_taxonomy_index = header.index('ncbi_taxonomy')
            ncbi_unfiltered_index = header.index('ncbi_taxonomy_unfiltered')
            
            for line in f:
                line_split = line.strip().split('\t')

                gid = line_split[0]
                if gid in ncbi_map:
                    gid = ncbi_map[gid]
                elif gid in uba_map:
                    gid = uba_map[gid]
                    
                ncbi_taxonomy = line_split[ncbi_taxonomy_index]
                if ncbi_taxonomy != 'none':
                    ncbi_species[gid] = [t.strip() for t in ncbi_taxonomy.split(';')][6]

                ncbi_unfiltered = line_split[ncbi_unfiltered_index]
                if ncbi_unfiltered != 'none':
                    taxa = [t.strip() for t in ncbi_unfiltered.split(';')]
                    for taxon in taxa:
                        if taxon.startswith('sb__'):
                            ncbi_subspecies[gid] = taxon
                            break

        # validate specific name of genomes in taxonomy file
        fout_pass = open(os.path.join(output_dir, 'valid_specific_names.tsv'), 'w')
        fout_pass.write('Genome ID\tProposed species\tNCBI species\tReason for accepting\n')
        
        fout_fail = open(os.path.join(output_dir, 'invalid_specific_names.tsv'), 'w')
        fout_fail.write('Genome ID\tProposed species\tNCBI species\tReason\n')
        
        for line in open(input_taxonomy):
            line_split = line.strip().split('\t')
            
            gid = line_split[0]
            if gid.startswith('D-'):
                continue # skip dummy genomes
                
            if gid in ncbi_map:
                gid = ncbi_map[gid]
            elif gid in uba_map:
                gid = uba_map[gid]
                    
            species = line_split[1].split(';')[6].strip()
            specific_name = species.split()[1]
            canonical_specific_name = canonical_taxon_name(specific_name)
            
            # check synonyms
            canonical_sp_name = canonical_species_name(species)
            if canonical_sp_name in synonyms:
                fout_fail.write('{}\t{}\t{}\t{}\n'.format(
                                    gid, 
                                    species, 
                                    ncbi_species.get(gid, 's__'), 
                                    'Canonical species name is considered GTDB synonym of %s' % synonyms[canonical_sp_name].species))
                continue
            
            # check species ledger
            if gid in species_ledger:
                ledger_species = species_ledger[gid]
                ledger_specific = ledger_species.split()[1]
                canonical_ledger_specific = canonical_taxon_name(ledger_specific)
                if canonical_specific_name == canonical_ledger_specific:
                    fout_pass.write('{}\t{}\t{}\t{}\n'.format(gid, species, ncbi_species.get(gid, 's__'), 'Specific name specified in species ledger'))
                else:
                    fout_fail.write('{}\t{}\t{}\t{}\n'.format(gid, species, ncbi_species.get(gid, 's__'), 'Specific name conflicts with species ledger'))
                    
                continue

            if gtdb_canonical_species_id(gid, specific_name):
                # check for canonical GTDB identifier (i.e. sp<accession>)
                fout_pass.write('{}\t{}\t{}\t{}\n'.format(gid, species, ncbi_species.get(gid, 's__'), 'Canonical GTDB species ID'))
            elif (latinized_specific_sp_name(canonical_specific_name) 
                    and canonical_specific_name in ncbi_species[gid]):
                # check for agreement with NCBI
                fout_pass.write('{}\t{}\t{}\t{}\n'.format(gid, species, ncbi_species.get(gid, 's__'), 'Congruent with NCBI specific name.'))
            elif (latinized_specific_sp_name(canonical_specific_name) 
                    and canonical_specific_name in ncbi_subspecies.get(gid, '')):
                # check for agreement with NCBI
                fout_pass.write('{}\t{}\t{}\t{}\n'.format(gid, species, ncbi_species.get(gid, 's__'), 'Congruent with NCBI subspecies name.'))
            elif (latinized_specific_sp_name(canonical_specific_name) 
                    and canonical_specific_name not in ncbi_species[gid] 
                    and ncbi_species[gid] != 's__'):
                # check for disagreement with NCBI
                fout_fail.write('{}\t{}\t{}\t{}\n'.format(gid, species, ncbi_species.get(gid, 's__'), 'Incongruent with NCBI specific name.'))
            else:
                fout_fail.write('{}\t{}\t{}\t{}\n'.format(gid, species, ncbi_species.get(gid, 's__'), 'Unknown source for specific name'))

        fout_fail.close()
        fout_pass.close()
