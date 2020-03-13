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
from collections import defaultdict, namedtuple, Counter

import dendropy

from biolib.common import make_sure_path_exists
from biolib.taxonomy import Taxonomy
from biolib.newick import parse_label, create_label
from biolib.external.execute import check_dependencies

from gtdb_validation_tk.common import (placeholder_genus,
                                        canonical_taxon_name,
                                        parse_species_ledgers,
                                        parse_genus_ledger, 
                                        parse_gtdb_synonym_file)
from gtdb_validation_tk.suffix_table import SuffixTable, increment_suffix


class Backfill():
    """Fill in missing rank information."""

    def __init__(self, prefix, output_dir):
        """Initialize."""
        
        check_dependencies(['phylorank'])
        
        make_sure_path_exists(output_dir)
        self.output_dir = output_dir
        self.prefix = prefix
        
        self.logger = logging.getLogger('timestamp')
        
        self.FAMILY_INDEX = 4
        self.GENUS_INDEX = 5
        self.SP_INDEX = 6
        
        self.NCBI_INFO = namedtuple('NCBI_INFO', 'org_name strain_id wgs_id uba_id')
        
    def _backfill_placeholder_genus(self, gid, taxonomy):
        """Backfill placeholder genus name to all ranks."""
        
        taxa = taxonomy[gid]
        genus = taxa[5]
        
        if placeholder_genus(genus):
            # append genus name to any empty ranks
            for rank_index in range(1,5):
                if len(taxa[rank_index]) == 3: # just rank prefix
                    taxa[rank_index] += genus
        else:
            # *** need to modify genus name to reflect 
            # proper rank suffix???#
            pass
        
        taxonomy[gid] = taxa
        
    def _generic_sp_name(self, species):
        """Extract generic (genus) name for species designation."""
        
        if 'Candidatus ' in species:
            species = species.replace('Candidatus ', '')
            
        genus = species.split()[0].replace('s__', '')
        
        return genus
        
    def _specific_sp_name(self, species):
        """Extract specific name for species designation."""
        
        return species.split()[-1]
        
    def _has_specific_sp_name(self, species):
        """Check if species has a specific name or if this is just a placeholder."""
        
        return all(c.islower() for c in self._specific_sp_name(species))
        
    def _canonical_specific_name(self, specific_name):
        """Get canonical version of specific name."""
        
        if '_' in specific_name:
            specific_name = specific_name[0:specific_name.rfind('_')]
            
        return specific_name

    def _canonical_species_name(self, species_name):
        """Get canonical version of species name."""
        
        genus, specific = species_name.split()

        canonical_species_name = '{} {}'.format(
                                    genus,
                                    self._canonical_specific_name(specific))

        return canonical_species_name
        
    def _specific_spX_designator(self, species_name):
        """Check if specific name has the form sp<num>."""
        
        specific_name = self._specific_sp_name(species_name)
        if not specific_name.startswith('sp'):
            return False
            
        if any([not ch.isdigit() for ch in specific_name[2:]]):
            return False
            
        return True
        
    def _ncbi_polyphyletic_generic_name(self, species):
        """Check if species name contains an NCBI polyphyletic genus e.g., s__[Clostridium] aerotoleran."""

        genus = self._generic_sp_name(species)
        
        return '[' in genus and ']' in genus
        
    def _ncbi_polyphyletic_genus(self, genus):
        """Check if NCBI genus name is polyphyletic e.g., s__[Clostridium] aerotoleran."""

        return '[' in genus and ']' in genus
        
    def _get_suffix(self, taxon_suffix, taxon):
        """Get polyphyletic suffix for taxon."""
        
        if taxon in taxon_suffix:
            suffix = increment_suffix(taxon_suffix[taxon])
        else:
            suffix = 'A'
            
        taxon_suffix[taxon] = suffix
        
        return suffix
        
    def _read_gtdb_metadata(self, gtdb_metadata_file, user_genome_id_table, cur_gtdb_taxonomy):
        """Read GTDB metadata."""
        
        uba_ids = {}
        for line in open(user_genome_id_table):
            line_split = line.strip().split('\t')
            uba_ids[line_split[0]] = line_split[1]
        
        user_id_map = {}
        ncbi_info = {}
        clusters = defaultdict(set)
        type_st_of_sp = set()
        type_sp_of_genus = set()
        with open(gtdb_metadata_file) as f:
            header = f.readline().strip().split('\t')
            
            gtdb_rep_index = header.index('gtdb_representative')
            gtdb_rep_gid_index = header.index('gtdb_genome_representative')
            organism_name_index = header.index('organism_name')
            ncbi_organism_name_index = header.index('ncbi_organism_name')
            ncbi_strain_ids_index = header.index('ncbi_strain_identifiers')
            wgs_index = header.index('ncbi_wgs_master')
            gb_acc_index = header.index('ncbi_genbank_assembly_accession')
            type_st_index = header.index('gtdb_type_designation')
            type_sp_index = header.index('gtdb_type_species_of_genus')
            
            for line in f:
                line_split = line.strip().split('\t')

                gid = line_split[0]
                if gid not in cur_gtdb_taxonomy:
                    continue

                ncbi_org_name = line_split[ncbi_organism_name_index]
                if ncbi_org_name == 'none':
                    ncbi_org_name = None
                    
                ncbi_strain_id = line_split[ncbi_strain_ids_index].split(';')[0]
                if ncbi_strain_id == 'none':
                    ncbi_strain_id = None
                    
                wgs_acc = line_split[wgs_index]
                if wgs_acc == 'none':
                    wgs_acc = None
                else:
                    # create canonical ID
                    wgs_acc, version = wgs_acc.split('.')
                    idx = [ch.isdigit() for ch in wgs_acc].index(True)
                    wgs_id = wgs_acc[0:idx] + str(version).zfill(2)

                ncbi_info[gid] = self.NCBI_INFO(org_name = ncbi_org_name, 
                                strain_id = ncbi_strain_id,
                                wgs_id = wgs_id,
                                uba_id = uba_ids.get(gid, None))
                                

                rid = line_split[gtdb_rep_gid_index]
                if rid and rid != 'none':
                    clusters[rid].add(gid)
                    
                type_st = line_split[type_st_index]
                if type_st in ['type strain of species', 'type strain of neotype']:
                    type_st_of_sp.add(gid)
                    
                type_sp = line_split[type_sp_index]
                if type_sp.lower() in ['true', 't']:
                    type_sp_of_genus.add(gid)
                    
                if gid.startswith('U_'):
                    gb_acc = line_split[gb_acc_index]
                    org_name = line_split[organism_name_index]
    
                    if gb_acc and gb_acc != 'none':
                        user_id_map[gid] = gb_acc
                    elif '(UBA' in org_name:
                        uba_id = org_name[org_name.rfind('(')+1:org_name.rfind(')')]
                        user_id_map[gid] = uba_id
                
        return (clusters,
                type_st_of_sp,
                type_sp_of_genus,
                ncbi_info,
                user_id_map)
                
    def _derived_genus_placeholder(self, gid, gtdb_taxonomy, ncbi_info):
        """Determine if placeholder name was derived from the genome metadata."""
        
        if gid not in gtdb_taxonomy:
            return False
        
        genus = gtdb_taxonomy[gid][self.GENUS_INDEX].replace('g__', '')
        if ncbi_info.org_name and ncbi_info.org_name.replace('_', '-').endswith(genus):
            return True
            
        if ncbi_info.strain_id and genus == ncbi_info.strain_id.replace('_', '-'):
            return True
            
        if ncbi_info.uba_id and genus == ncbi_info.uba_id:
            return True
            
        if ncbi_info.wgs_id and genus == ncbi_info.wgs_id:
            return True
            
        return False
                
    def _placeholder_canonical_genus(self, placeholder):
        """Create canonicalized genus placeholder name."""
        
        MIN_LEN = 3
        MAX_LEN = 12
        
        if not placeholder:
            return None

        # skip cases violating maximum or minimum lengths
        if len(placeholder) > MAX_LEN or len(placeholder) < MIN_LEN:
            return None
            
        # replace underscores with hyphen since underscores
        # are used in GTDB to designate polyphyletic suffixes
        placeholder = placeholder.replace('_', '-')
            
        # skip cases with characters other than alphanumeric or hyphen
        for ch in placeholder:
            if not (ch.isalnum() or ch == '-'):
                return None

        # ensure name starts with an alphabetical character
        if not placeholder[0].isalpha():
            return None
            
        # return UPPERCASE version of name
        return placeholder.upper()
                
    def _generate_genus_placeholder_name(self, rep_id, ncbi_info, gtdb_genera_in_use):
        """Generate a new placeholder genus name from NCBI organism name and strain ID information."""

        # try to generate name from NCBI strain/isolate identifier
        if ncbi_info.strain_id:
            placeholder = ncbi_info.strain_id.replace('_', '-')
            
            placeholder = self._placeholder_canonical_genus(placeholder)
            if placeholder and 'g__' + placeholder not in gtdb_genera_in_use:
                return placeholder
                
        # try to generate name from UBA ID
        if ncbi_info.uba_id:
            placeholder = self._placeholder_canonical_genus(ncbi_info.uba_id)
            if placeholder and 'g__' + placeholder not in gtdb_genera_in_use:
                return placeholder
                
        # try to generate name from WGS ID
        if ncbi_info.wgs_id:
            placeholder = self._placeholder_canonical_genus(ncbi_info.wgs_id)
            if placeholder and 'g__' + placeholder not in gtdb_genera_in_use:
                return placeholder

        # try to generate name from NCBI organism name
        if ncbi_info.org_name:
            ncbi_org_name = ncbi_info.org_name.replace('_', '-')
            placeholder = None
            if ' sp.' in ncbi_org_name:
                placeholder = ncbi_org_name[ncbi_org_name.find('sp.')+len('sp.'):].strip()
            elif ' bacterium' in ncbi_org_name:
                placeholder = ncbi_org_name[ncbi_org_name.find('bacterium')+len('bacterium'):].strip()

            placeholder = self._placeholder_canonical_genus(placeholder)
            if placeholder and 'g__' + placeholder not in gtdb_genera_in_use:
                return placeholder
            
        return '<unresolved>'
        
    def _generate_specific_placeholder_name(self, rep_id, user_to_ncbi_acc, user_to_uba_acc):
        """Generate a new placeholder specific name from NCBI genome accession number."""
        
        acc = rep_id
        if acc.startswith('U_'):
            if acc in user_to_ncbi_acc:
                acc = user_to_ncbi_acc[acc]
            elif acc in user_to_uba_acc:
                # create accession from UBA ID of the form:
                # U_<number>u.0 which will give 'sp<number>u'
                acc = 'UBA_{}u.0'.format(user_to_uba_acc[acc].replace('UBA', ''))
            else:
                self.logger.error('Genome ID has neither a NCBI or UBA accession: {}'.format(rep_id))
                sys.exit(-1)
                
        derived_sp = 'sp{}'.format(acc[acc.rfind('_')+1:acc.rfind('.')])
            
        return derived_sp
        
    def _suffix_repeated_genus(self,
                                    genus,
                                    gtdb_genera_in_use,
                                    taxon_suffix,
                                    rule_desc):
        """Append suffix to genus if already in use."""
        
        generic_name = genus.replace('g__', '')
        if genus in gtdb_genera_in_use:
            rule_desc += '; Appended suffix to make unique'
            
            canonical_genus = canonical_taxon_name(genus)
            suffix = self._get_suffix(taxon_suffix, canonical_genus)
            generic_name = '{}_{}'.format(canonical_genus[3:], suffix)
            
        return generic_name, rule_desc
        
    def _assign_generic_name(self, 
                                clusters, 
                                cur_gtdb_taxonomy, 
                                prev_gtdb_taxonomy, 
                                ncbi_taxonomy,
                                gtdb_named_sp,
                                gtdb_sp_ledger,
                                gtdb_genus_ledger,
                                type_sp_of_genus,
                                ncbi_info,
                                taxon_suffix):
        """Assign generic name to all species representatives."""
        
        self.logger.info('Assigning generic names to all species clusters.')
        
        # determine all GTDB genera proposed in current GTDB taxonomy
        gtdb_genera_in_use = set()
        canonical_genera_in_use = set()
        gtdb_family_of_genus = {}
        for taxa in cur_gtdb_taxonomy.values():
            gtdb_genus = taxa[self.GENUS_INDEX]
            if gtdb_genus != 'g__':
                gtdb_genera_in_use.add(gtdb_genus)
                canonical_genera_in_use.add(canonical_taxon_name(gtdb_genus))
                
            gtdb_family_of_genus[gtdb_genus] = taxa[self.FAMILY_INDEX]
            
        # sort species cluster reps so type species, named species, and placeholder names derived
        # from genome metadata are processed first
        self.logger.info('Prioritizing names of type species and representative genomes of species clusters with binomial names.')
        ledger_gids = [rid for rid in clusters if rid in gtdb_genus_ledger and rid in gtdb_sp_ledger]
        processed_gids = set(ledger_gids)
        
        selected_type_sp_rids = [rid for rid in clusters if rid not in processed_gids and rid in type_sp_of_genus and rid in gtdb_named_sp]
        processed_gids.update(selected_type_sp_rids)
        
        sp_cluster_rids = [rid for rid in clusters if rid in gtdb_named_sp and rid not in processed_gids]
        processed_gids.update(sp_cluster_rids)
        
        assigned_rids = [rid for rid in clusters if rid not in processed_gids and cur_gtdb_taxonomy[rid][self.GENUS_INDEX] != 'g__']
        processed_gids.update(assigned_rids)
        
        placeholder_rids = [rid for rid in clusters if rid not in processed_gids and self._derived_genus_placeholder(rid, prev_gtdb_taxonomy, ncbi_info[rid])]
        processed_gids.update(placeholder_rids)
        
        remaining_rids = [rid for rid in clusters if rid not in processed_gids]
        
        sorted_rids = ledger_gids + selected_type_sp_rids + sp_cluster_rids + assigned_rids + placeholder_rids + remaining_rids
        self.logger.info(' ...identified {} genomes in genus or species ledgers.'.format(len(ledger_gids)))
        self.logger.info(' ...identified {} type strain genomes.'.format(len(selected_type_sp_rids)))
        self.logger.info(' ...identified {} representative genomes of species clusters with binomial names.'.format(len(sp_cluster_rids)))
        self.logger.info(' ...identified {} representative genomes of species clusters with placeholder names derived from genome.'.format(len(placeholder_rids)))
        self.logger.info(' ...identified {} representative genomes of species clusters with placeholder names not derived from genome.'.format(len(remaining_rids)))
        assert(len(clusters) == len(sorted_rids))
        
        # determine generic name for all species cluster representatives
        error_count = 0
        error_log = os.path.join(self.output_dir, '{}_generic_name_errors.tsv'.format(self.prefix))
        ferr = open(error_log, 'w')
        ferr.write('Genome ID\tNCBI genus\tNCBI species\tPrevious GTDB genus\tProposed GTDB genus\tBackfill GTDB genus\tError\tAssignment rule\n')
        
        fout = open(os.path.join(self.output_dir, '{}_generic_names.tsv'.format(self.prefix)), 'w')
        fout.write('Genome ID\tGTDB generic name\tNCBI species\tNCBI genus\tAssignment rule\n')

        novel_ncbi_genera = {}
        generic_names = {}
        new_gtdb_genera_in_use = set()
        num_unresolved_genera = 0
        genus_ledger_count = 0
        type_sp_of_genus_count = 0
        cur_gtdb_genus_count = 0
        prev_named_genus_count = 0
        poly_ncbi_genus_count = 0
        new_ncbi_genus_count = 0
        prev_placeholder_genus_count = 0
        new_placeholder_genus_count = 0
        for rid in sorted_rids:
            cur_gtdb_taxa = cur_gtdb_taxonomy[rid]
            cur_gtdb_genus = cur_gtdb_taxa[self.GENUS_INDEX]

            prev_gtdb_taxa = prev_gtdb_taxonomy.get(rid, Taxonomy.rank_prefixes)
            prev_gtdb_genus = prev_gtdb_taxa[self.GENUS_INDEX]
            
            ncbi_taxa = ncbi_taxonomy[rid]
            ncbi_genus = ncbi_taxa[self.GENUS_INDEX]
            ncbi_sp = ncbi_taxa[self.SP_INDEX]
            
            if rid in gtdb_sp_ledger:
                ledger_genus = 'g__' + self._generic_sp_name(gtdb_sp_ledger[rid])
                
                if cur_gtdb_genus != ledger_genus and cur_gtdb_genus != 'g__':
                    self.logger.error('Genus name {} in curated taxonomy conflicts with species ledger for {}.'.format(
                                        cur_gtdb_genus,
                                        rid))
                    sys.exit(-1)
                    
                cur_gtdb_genus = ledger_genus
                
            add_genus = False
            if rid in gtdb_genus_ledger:
                rule_desc = 'Assigned by genus ledger'
                genus_ledger_count += 1
                generic_name = gtdb_genus_ledger[rid][3:]
            elif rid in type_sp_of_genus:
                # genus name must reflect generic name of species at NCBI
                rule_desc = 'Type species of genus'
                type_sp_of_genus_count += 1
                generic_name = self._generic_sp_name(ncbi_sp)
                if '[' in generic_name:
                    # known issue with NCBI species name so use the genus name
                    generic_name = ncbi_genus[3:]
                    
                if cur_gtdb_genus != 'g__' and generic_name != cur_gtdb_genus[3:]:
                    error_count += 1
                    ferr.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (
                                    rid,
                                    ncbi_genus,
                                    ncbi_sp,
                                    prev_gtdb_genus,
                                    cur_gtdb_genus,
                                    'g__' + generic_name,
                                    'Genome is type species of genus. Proposed genus does not match generic species name.',
                                    rule_desc))
                elif cur_gtdb_genus == 'g__' and 'g__' + generic_name in gtdb_genera_in_use:
                    error_count += 1
                    ferr.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (
                                    rid,
                                    ncbi_genus,
                                    ncbi_sp,
                                    prev_gtdb_genus,
                                    cur_gtdb_genus,
                                    'g__' + generic_name,
                                    'Genome is type species of genus, but genus name is already used elsewhere.',
                                    rule_desc))
            elif cur_gtdb_genus != 'g__':
                # genome resides in a defined GTDB genus so must reflect
                # this in the generic name of the species
                rule_desc = 'Resides in defined GTDB genus'
                cur_gtdb_genus_count += 1
                generic_name = cur_gtdb_genus[3:]
            elif prev_gtdb_genus != 'g__' and not placeholder_genus(prev_gtdb_genus):
                # genome is the only member of the genus so does not
                # have a genus designation in the current GTDB taxonomy,
                # but was assigned a proper genus name in the previous 
                # GTDB release
                rule_desc = 'Assigned genus name in previous GTDB taxonomy'
                prev_named_genus_count += 1
                generic_name, rule_desc  = self._suffix_repeated_genus(
                                            prev_gtdb_genus,
                                            gtdb_genera_in_use,
                                            taxon_suffix,
                                            rule_desc)
            elif (ncbi_genus != 'g__' 
                    and not self._ncbi_polyphyletic_genus(ncbi_genus)
                    and ncbi_genus not in canonical_genera_in_use
                    and ncbi_genus != canonical_taxon_name(prev_gtdb_genus)):
                    # representative is the only member of a genus
                    # and is from a newly defined genus at NCBI
                    
                    # Note: the clause "ncbi_genus != canonical_taxon_name(prev_gtdb_genus)" 
                    # ensures that if the genome was previously given a placeholder name based on
                    # the NCBI genus name that this is retained between releases
                    rule_desc = 'Assigned novel NCBI genus name'
                    new_ncbi_genus_count += 1
                    generic_name = ncbi_genus[3:]
            elif prev_gtdb_genus != 'g__' and placeholder_genus(prev_gtdb_genus):
                # genome is the only member of the genus so does not
                # have a genus designation in the current GTDB taxonomy,
                # but was assigned a placeholder genus name in the previous 
                # GTDB release
                rule_desc = 'Assigned genus placeholder name in previous GTDB taxonomy'
                prev_placeholder_genus_count += 1
                generic_name, rule_desc  = self._suffix_repeated_genus(
                                            prev_gtdb_genus,
                                            gtdb_genera_in_use,
                                            taxon_suffix,
                                            rule_desc)
            elif (ncbi_genus != 'g__' 
                    and not self._ncbi_polyphyletic_genus(ncbi_genus)
                    and ncbi_sp != 's__' 
                    and cur_gtdb_taxonomy[rid][self.FAMILY_INDEX] == gtdb_family_of_genus.get(ncbi_genus, None)):
                # representative is the only member of a genus, and 
                # should be given a polyphyletic genus name since it has 
                # a proper binomial species name and the NCBI genus exists 
                # within the expected GTDB family for this genus
                rule_desc = 'Assigned polyphyletic genus name based on NCBI genus'
                poly_ncbi_genus_count += 1
                assert(ncbi_genus in canonical_genera_in_use)
                suffix = self._get_suffix(taxon_suffix, ncbi_genus)
                generic_name = '{}_{}'.format(ncbi_genus[3:], suffix)
            else:
                # taxonomic information for the representative genome is
                # insufficient to establish a genus name
            
                # need to generate a new placeholder genus name
                rule_desc = 'Generate new placeholder name'
                new_placeholder_genus_count += 1
                generic_name = self._generate_genus_placeholder_name(
                                        rid, 
                                        ncbi_info[rid],
                                        gtdb_genera_in_use.union(new_gtdb_genera_in_use))

            generic_names[rid] = generic_name

            new_generic_name = 'g__' + generic_name
            if new_generic_name == 'g__<unresolved>':
                num_unresolved_genera += 1
            elif new_generic_name not in gtdb_genera_in_use:
                if new_generic_name in new_gtdb_genera_in_use:
                    error_count += 1
                    ferr.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (
                                    rid,
                                    ncbi_genus,
                                    ncbi_sp,
                                    prev_gtdb_genus,
                                    cur_gtdb_genus,
                                    new_generic_name,
                                    'New genus name proposed multiple times during backfilling.',
                                    rule_desc))
                                    
                new_gtdb_genera_in_use.add(new_generic_name)
                
            if rid in gtdb_sp_ledger:
                ledger_genus = 'g__' + self._generic_sp_name(gtdb_sp_ledger[rid])
                if ledger_genus != new_generic_name:
                    error_count += 1
                    ferr.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (
                                    rid,
                                    ncbi_genus,
                                    ncbi_sp,
                                    prev_gtdb_genus,
                                    cur_gtdb_genus,
                                    new_generic_name,
                                    'Proposed genus name disagrees with species ledger: {}'.format(ledger_genus),
                                    'Genus name assigned by species ledger.'))
                                    
            if rid in gtdb_genus_ledger:
                if gtdb_genus_ledger[rid] != new_generic_name:
                    error_count += 1
                    ferr.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (
                                    rid,
                                    ncbi_genus,
                                    ncbi_sp,
                                    prev_gtdb_genus,
                                    cur_gtdb_genus,
                                    new_generic_name,
                                    'Proposed genus name disagrees with genus ledger: {}'.format(gtdb_genus_ledger[rid]),
                                    'Genus name assigned by genus ledger.'))

            fout.write('%s\t%s\t%s\t%s\t%s\n' % (rid, generic_name, ncbi_sp, ncbi_genus, rule_desc))

        ferr.close()
        fout.close()

        self.logger.warning('There are %d unresolved genera names.' % num_unresolved_genera)
        self.logger.warning('Identified %d errors when assigning generic species names (see: %s).' % (
                                error_count,
                                error_log))
        
        print('genus_ledger_count', genus_ledger_count)
        print('type_sp_of_genus_count', type_sp_of_genus_count)
        print('cur_gtdb_genus_count', cur_gtdb_genus_count)
        print('prev_named_genus_count', prev_named_genus_count)
        print('poly_ncbi_genus_count', poly_ncbi_genus_count)
        print('new_ncbi_genus_count', new_ncbi_genus_count)
        print('prev_placeholder_genus_count', prev_placeholder_genus_count)
        print('new_placeholder_genus_count', new_placeholder_genus_count)
        
        return generic_names
        
    def _suffix_repeated_species(self, 
                                    specific_name,
                                    generic_name,
                                    used_species_names,
                                    taxon_suffix,
                                    rule_desc):
        """Append suffix to specific name if species name already in use."""

        sp = 's__{} {}'.format(generic_name, specific_name)
        while sp in used_species_names:
            rule_desc += '; Appended suffix to make unique'
            
            canonical_species_name = self._canonical_species_name(sp)
            canonical_specific_name = self._canonical_specific_name(specific_name)
            suffix = self._get_suffix(taxon_suffix, canonical_species_name)
            specific_name = '{}_{}'.format(canonical_specific_name, suffix)
            sp = 's__{} {}'.format(generic_name, specific_name)
            
        return specific_name, rule_desc
        
    def _assign_specific_name(self, 
                                clusters,
                                generic_names,
                                prev_gtdb_taxonomy,
                                ncbi_taxonomy,
                                gtdb_named_sp,
                                synonyms,
                                gtdb_sp_ledger,
                                type_st_of_sp,
                                user_to_ncbi_acc,
                                user_to_uba_acc,
                                user_id_map,
                                taxon_suffix):
        """Assign specific name to all species representatives."""
        
        self.logger.info('Assigning specific names to all species clusters.')
        
        # sort species cluster reps so selected type strain genomes and 
        # genomes selected to represent named species are processed first
        self.logger.info('Prioritizing names of type strains and representative genomes of species clusters with binomial names.')
        selected_type_st_rids = [rid for rid in clusters if rid in type_st_of_sp and rid in gtdb_named_sp]
        processed_gids = set(selected_type_st_rids)
        sp_cluster_rids = [rid for rid in clusters if rid in gtdb_named_sp and rid not in processed_gids]
        processed_gids.update(sp_cluster_rids)
        placeholder_rids = [rid for rid in clusters if rid not in processed_gids]
        sorted_rids = selected_type_st_rids + sp_cluster_rids + placeholder_rids
        self.logger.info(' ...identified {} type strain genomes.'.format(len(selected_type_st_rids)))
        self.logger.info(' ...identified {} representative genomes of species clusters with binomial names.'.format(len(sp_cluster_rids)))
        self.logger.info(' ...identified {} representative genomes of species clusters with placeholder names.'.format(len(placeholder_rids)))
        assert(len(clusters) == len(sorted_rids))

        # determine specific name for all species cluster representatives
        error_count = 0
        error_log = os.path.join(self.output_dir, '{}_specific_name_errors.tsv'.format(self.prefix))
        ferr = open(error_log, 'w')
        ferr.write('Genome ID\tNCBI genus\tNCBI species\tPrevious GTDB species\tBackfill GTDB species\tError\tAssignment rule\n')
        
        fout = open(os.path.join(self.output_dir, '{}_specific_names.tsv'.format(self.prefix)), 'w')
        fout.write('Genome ID\tGTDB species\tNCBI species\tNCBI genus\tAssignment rule\n')

        specific_names = {}
        used_species_names = set()
        species_ledger_count = 0
        type_of_named_sp_count = 0
        prev_sp_count = 0
        derived_specific_name_count = 0
        new_placeholder_sp_count = 0
        for rid in sorted_rids:
            rule_desc = ''
            
            prev_gtdb_taxa = prev_gtdb_taxonomy.get(rid, Taxonomy.rank_prefixes)
            prev_gtdb_genus = prev_gtdb_taxa[self.GENUS_INDEX]
            prev_gtdb_sp = prev_gtdb_taxa[self.SP_INDEX]
            if prev_gtdb_sp in synonyms:
                prev_gtdb_sp = synonyms[prev_gtdb_sp].species
                rule_desc = 'Synonym; '
            
            ncbi_taxa = ncbi_taxonomy[rid]
            ncbi_sp = ncbi_taxa[self.SP_INDEX]
            if ncbi_sp in synonyms:
                ncbi_sp = synonyms[ncbi_sp].species
                rule_desc = 'Synonym; '
            
            if rid in gtdb_sp_ledger:
                # genome given explicit species assignment via species ledger
                rule_desc += 'Assigned by species ledger'
                species_ledger_count += 1
                specific_name = self._specific_sp_name(gtdb_sp_ledger[rid])
            elif rid in gtdb_named_sp:
                # genome was selected as type genome for the specified NCBI species 
                rule_desc += 'Selected type genome for named species'
                type_of_named_sp_count += 1

                specific_name, rule_desc = self._suffix_repeated_species(
                                            self._specific_sp_name(gtdb_named_sp[rid]),
                                            generic_names[rid],
                                            used_species_names,
                                            taxon_suffix,
                                            rule_desc)
                
                if ncbi_sp != gtdb_named_sp[rid] and ncbi_sp != 's__':
                    self.logger.error('Genome %s disagrees on NCBI species assignment: %s %s.' % (
                                        rid,
                                        ncbi_sp,
                                        gtdb_named_sp[rid]))
                    sys.exit(-1) # Should probably be an error
            elif (prev_gtdb_sp != 's__' 
                    and not self._specific_spX_designator(prev_gtdb_sp)):
                # genome was previously assigned a species name so
                # the specific name should be reused
                rule_desc += 'Using specific name in previous GTDB taxonomy'
                prev_sp_count += 1

                specific_name, rule_desc = self._suffix_repeated_species(
                                            self._specific_sp_name(prev_gtdb_sp),
                                            generic_names[rid],
                                            used_species_names,
                                            taxon_suffix,
                                            rule_desc)
            elif self._has_specific_sp_name(ncbi_sp):
                # genome belongs to a named NCBI species so should reuse specific name
                rule_desc += 'Deriving specific name from specific name at NCBI'
                derived_specific_name_count += 1
                
                specific_name, rule_desc = self._suffix_repeated_species(
                                            self._specific_sp_name(ncbi_sp),
                                            generic_names[rid],
                                            used_species_names,
                                            taxon_suffix,
                                            rule_desc)
            else:
                # taxonomic information for the representative genome is
                # insufficient to establish a specific name
            
                # need to generate a new placeholder name
                rule_desc += 'Generate new placeholder name'
                new_placeholder_sp_count += 1
                specific_name = self._generate_specific_placeholder_name(rid, 
                                                                            user_to_ncbi_acc,
                                                                            user_to_uba_acc)

            specific_names[rid] = specific_name
            
            gtdb_sp_name = 's__{} {}'.format(generic_names[rid], specific_name)
            if gtdb_sp_name in used_species_names:
                error_count += 1
                ferr.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (
                                rid,
                                ncbi_taxa[self.GENUS_INDEX],
                                ncbi_sp,
                                prev_gtdb_sp,
                                gtdb_sp_name,
                                'Species name proposed multiple times during backfilling.',
                                rule_desc))

            fout.write('%s\t%s\t%s\t%s\t%s\n' % (
                            rid, 
                            gtdb_sp_name, 
                            ncbi_sp, 
                            ncbi_taxa[self.GENUS_INDEX], 
                            rule_desc))

            used_species_names.add(gtdb_sp_name)
                            
        ferr.close()
        fout.close()
            
        print('species_ledger_count', species_ledger_count)
        print('type_of_named_sp_count', type_of_named_sp_count)
        print('prev_sp_count', prev_sp_count)
        print('derived_specific_name_count', derived_specific_name_count)
        print('new_placeholder_sp_count', new_placeholder_sp_count)

        self.logger.warning('Identified %d errors when assigning specific species names (see: %s).' % (
                                error_count,
                                error_log))
        
        return specific_names
        
    def _parse_cluster_file(self, sp_cluster_file, cur_taxonomy):
        """Read species cluster file."""
        
        clusters = {}
        with open(sp_cluster_file) as f:
            header = f.readline().strip().split('\t')
            type_genome_index = header.index('Type genome')
            num_clustered_index = header.index('No. clustered genomes')
            clustered_gids_index = header.index('Clustered genomes')
            
            for line in f:
                line_split = line.strip().split('\t')
                
                rid = line_split[type_genome_index]
                if rid not in cur_taxonomy:
                    continue # representative from other domain
                    
                clusters[rid] = set()
                num_clustered = int(line_split[num_clustered_index])
                if num_clustered > 0:
                    clusters[rid] = set([cid.strip() 
                                            for cid in line_split[clustered_gids_index].split(',')])
                                            
        return clusters

    def _read_gtdb_ncbi_taxonomy(self, metadata_file):
        """Parse NCBI taxonomy from GTDB metadata."""

        taxonomy = {}

        with open(metadata_file) as f:
            headers = f.readline().strip().split('\t')
            genome_index = headers.index('accession')
            taxonomy_index = headers.index('ncbi_taxonomy')
            
            for line in f:
                line_split = line.strip().split('\t')
                genome_id = line_split[genome_index]
                taxa_str = line_split[taxonomy_index].strip()
                taxa_str = taxa_str.replace('Candidatus ', '')

                if taxa_str and taxa_str != 'none':
                    taxonomy[genome_id] = map(str.strip, taxa_str.split(';'))
                else:
                    taxonomy[genome_id] = list(Taxonomy.rank_prefixes)

        return taxonomy
        
    def _gtdb_named_type_genomes(self, gtdb_named_type_genomes):
        """Get type genome for named species."""
        
        gtdb_named_sp = {}
        with open(gtdb_named_type_genomes) as f:
            header = f.readline().strip().split('\t')
            
            ncbi_sp_index = header.index('NCBI species')
            type_genome_index = header.index('Type genome')
            
            for line in f:
                line_split = line.strip().split('\t')
                
                ncbi_sp = line_split[ncbi_sp_index]
                ncbi_sp = ncbi_sp.replace('Candidatus ', '')
                gtdb_named_sp[line_split[type_genome_index]] = ncbi_sp
        
        return gtdb_named_sp
        
    def _backfill_genus(self, 
                        backfilled_taxonomy, 
                        prev_taxonomy, 
                        gtdb_named_sp,
                        type_sp_of_genus,
                        type_st_of_sp,
                        taxon_suffix):
        """Backfill genus name to empty ranks."""
        
        self.logger.info('Filling in ranks above genus.')
        
        # get list of all taxon in use
        taxon_in_use = set()
        for taxa in backfilled_taxonomy.values():
            for taxon in taxa:
                taxon_in_use.add(taxon)
                
        # sort genomes so type material is processed first
        # and thus is given canonical names if polyphyletic
        # suffixes should become necessary
        type_sp_rids = [rid for rid in backfilled_taxonomy if rid in type_sp_of_genus]
        processed_gids = set(type_sp_rids)
        type_st_rids = [rid for rid in backfilled_taxonomy if rid in type_st_of_sp and rid not in processed_gids]
        processed_gids.update(type_st_rids)
        sp_cluster_rids = [rid for rid in backfilled_taxonomy if rid in gtdb_named_sp and rid not in processed_gids]
        processed_gids.update(sp_cluster_rids)
        placeholder_rids = [rid for rid in backfilled_taxonomy if rid not in processed_gids]
        sorted_rids = type_sp_rids + type_st_rids + sp_cluster_rids + placeholder_rids
        assert(len(sorted_rids) == len(backfilled_taxonomy))
        
        # backfill ranks above genus
        fout = open(os.path.join(self.output_dir, '{}_higher_ranks.tsv'.format(self.prefix)), 'w')
        fout.write('Genome ID\tFilled taxon\tSource\tRequires manual curation\n')

        taxonomy = {}
        manual_curation_count = 0
        for gid in sorted_rids:
            taxa = backfilled_taxonomy[gid]
            taxonomy[gid] = taxa
            
            cur_genus = taxa[self.GENUS_INDEX]
            assert cur_genus != 'g__'
            prev_genus = prev_taxonomy.get(gid, Taxonomy.rank_prefixes)[self.GENUS_INDEX]
            
            for rank_index in range(self.GENUS_INDEX-1, 0, -1):
                taxon = taxa[rank_index]
                if len(taxon) == 3:
                    prev_taxon = prev_taxonomy.get(gid, Taxonomy.rank_prefixes)[rank_index]
                    proposed_taxon = None
                    manual_curation = False
                    if cur_genus == prev_genus and len(prev_taxon) != 3:
                        # use previous taxon name where available and the genus
                        # name has not changed
                        source = 'Previous GTDB taxonomy'
                        proposed_taxon = prev_taxon
                        if prev_taxon in taxon_in_use:
                            source += '; Appended suffix to make unique'
                            canonical_taxon = canonical_taxon_name(prev_taxon)
                            suffix = self._get_suffix(taxon_suffix, canonical_taxon)
                            proposed_taxon = '{}_{}'.format(canonical_taxon, suffix)
                    elif (placeholder_genus(cur_genus) and
                            (cur_genus == prev_genus or prev_genus == 'g__') and
                            taxon + cur_genus[3:] not in taxon_in_use):
                        # placeholder name can just be filled in without modification
                        proposed_taxon = taxon + cur_genus[3:]
                        source = 'Propagated genus placeholder name'
                        if proposed_taxon.startswith('p__'):
                            manual_curation = True

                    if proposed_taxon:
                        assert proposed_taxon not in taxon_in_use
                        fout.write('{}\t{}\t{}\t{}\n'.format(gid, proposed_taxon, source, manual_curation))
                        taxon_in_use.add(proposed_taxon)
                    else:
                        manual_curation = True
                        proposed_taxon = '{}<manual_curation>'.format(Taxonomy.rank_prefixes[rank_index])
                        fout.write('{}\t{}\t{}\t{}\n'.format(
                                    gid, 
                                    proposed_taxon,
                                    "Requires manual curation",
                                    manual_curation))
                        
                    if manual_curation:
                        manual_curation_count += 1
                    
                    taxonomy[gid][rank_index] = proposed_taxon
                else:
                    break
                    
        fout.close()
        
        self.logger.info(' ...identified {:,} taxon requiring manual curation.'.format(manual_curation_count))

        return taxonomy

    def _check_ledgers(self, gtdb_sp_ledger, gtdb_genus_ledger):
        """Check that ledgers are consistent."""
        
        common_gids = set(gtdb_sp_ledger.keys()).intersection(gtdb_genus_ledger.keys())
        for gid in common_gids:
            # ensure ledgers indicate the same generic name
            genus_ledger = gtdb_genus_ledger[gid]
            sp_ledger = 'g__' + self._generic_sp_name(gtdb_sp_ledger[gid])
            
            if genus_ledger != sp_ledger:
                self.logger.info('Species and genus ledgers are not consistent: {} {} {}'.format(
                                    gid,
                                    sp_ledger,
                                    genus_ledger))
                sys.exit(-1)

    def _create_backfill_tree(self, curation_tree_file, backfilled_taxonomy, clusters):
        """Create tree for inspecting results of backfilling."""
    
        self.logger.info('Creating tree for inspecting manual curation.')
        tree = dendropy.Tree.get_from_path(curation_tree_file, 
                                            schema='newick', 
                                            rooting='force-rooted', 
                                            preserve_underscores=True)
                                            
        # prune tree to representatives of species clusters
        taxa_to_retain = set()
        for leaf in tree.leaf_node_iter():
            if leaf.taxon.label in clusters:
                taxa_to_retain.add(leaf.taxon)

        self.logger.info('Pruning tree to {} representatives of species clusters.'.format(len(taxa_to_retain)))
        tree.retain_taxa(taxa_to_retain)
        
        # duplicate each genome so there is an internal node to decorate
        # with species information
        self.logger.info('Creating dummy leaf nodes so there are 2 genomes per species.')
        tmp_taxonomy = os.path.join(self.output_dir, 'tmp_taxonomy.tsv')
        fout = open(tmp_taxonomy, 'w')
        for leaf in tree.leaf_node_iter():
            gid = leaf.taxon.label
            taxonomy_str = ';'.join(backfilled_taxonomy[gid])
            fout.write('{}\t{}\n'.format(gid, taxonomy_str))
            fout.write('{}\t{}\n'.format('D-' + gid, taxonomy_str))
            
            leaf.label = None
            leaf.taxon = None
            leaf.new_child(label = gid,
                            edge_length = 0.0)
            leaf.new_child(label = 'D-' + gid,
                            edge_length = 0.0)
        
        fout.close()
        
        # strip any existing taxonomic labels
        for node in tree.internal_nodes():
            support, taxon_name, _auxiliary_info = parse_label(node.label)
            if support is not None:
                    node.label = create_label(support, None, None)
        
        # write out temporary tree
        tmp_tree = os.path.join(self.output_dir, 'tmp.tree')
        tree.write_to_path(tmp_tree, 
                            schema='newick', 
                            suppress_rooting=True,
                            suppress_leaf_node_labels=False,
                            unquoted_underscores=True)
                            
        # decorate tree
        self.logger.info('Decorating tree.')
        decorated_tree_file = os.path.join(self.output_dir, '{}_backfill_decorated.tree'.format(self.prefix))
        cmd = 'phylorank decorate {} {} {} --skip_rd_refine'.format(
                tmp_tree,
                tmp_taxonomy,
                decorated_tree_file)
        self.logger.info(cmd)
        os.system(cmd)
        
        os.remove(tmp_taxonomy)
        os.remove(tmp_tree)
        
    def _validate_sp_clusters(self, sp_clusters, cur_taxonomy):
        """Validate the curated taxonomy spans all species clusters."""
        
        for gid in sp_clusters:
            if gid not in cur_taxonomy:
                self.logger.error('Genome {} represents species cluster, but is not in taxonomy file.'.format(gid))
                sys.exit(-1)
        
    def _validate_manual_genus_names(self, cur_taxonomy, backfilled_taxonomy):
        """Make sure generic name for species agrees with manual curation."""
        
        self.logger.info('Validation: ensuring generic name for species agrees with manual curation.')
        
        for gid in backfilled_taxonomy:
            genus = backfilled_taxonomy[gid][self.GENUS_INDEX]
            cur_genus = cur_taxonomy[gid][self.GENUS_INDEX]
            
            if cur_genus != 'g__' and cur_genus != genus:
                self.logger.error('Generic name of species does not agree with manual curation: {} {} {}'.format(
                                    gid,
                                    genus,
                                    cur_genus))
                                    
    def _validate_genus_ledger(self, gtdb_genus_ledger, backfilled_taxonomy):
        """Make sure genus names agree with genus ledger."""
        
        self.logger.info('Validation: ensuring genus name agrees with genus ledger.')
        
        for gid in gtdb_genus_ledger:
            if gid not in backfilled_taxonomy:
                continue # genome is a 'validation' genome
                
            genus = backfilled_taxonomy[gid][self.GENUS_INDEX]
            genus_ledger = gtdb_genus_ledger[gid]
            
            if genus_ledger != genus:
                self.logger.error('Generic name of species does not agree with genus ledger: {} {} {}'.format(
                                    gid,
                                    genus,
                                    genus_ledger))
                                    
    def _validate_species_ledger(self, gtdb_sp_ledger, backfilled_taxonomy):
        """Make sure species names agree with species ledger."""
        
        self.logger.info('Validation: ensuring species name agrees with species ledger.')
        
        for gid in gtdb_sp_ledger:
            if gid not in backfilled_taxonomy:
                continue # genome is a 'validation' genome
                
            species = backfilled_taxonomy[gid][self.SP_INDEX]
            species_ledger = gtdb_sp_ledger[gid]
            
            if species_ledger != species:
                self.logger.error('Species name does not agree with species ledger: {} {} {}'.format(
                                    gid,
                                    species,
                                    species_ledger))
                                    
    def _validate_genus_generic_names(self, backfilled_taxonomy):
        """Make sure genus name agrees with generic name of species."""
        
        self.logger.info('Validation: ensuring genus name agrees with generic name of species.')
        
        for gid, taxa in backfilled_taxonomy.items():
            genus = taxa[self.GENUS_INDEX].replace('g__','')
            generic_name = self._generic_sp_name(taxa[self.SP_INDEX])
            
            if genus != generic_name:
                self.logger.error('Genus name does not agree with generic name of species: {} {} {}'.format(
                                    gid,
                                    genus,
                                    generic_name))
                                    
    def _validate_synonyms(self, backfilled_taxonomy, synonyms):
        """Make sure synonyms are never used as a species name."""
        
        self.logger.info('Validation: ensuring synonyms are never used as a species name.')
        
        for gid in backfilled_taxonomy:
            sp_name = backfilled_taxonomy[gid][self.SP_INDEX]
            
            if sp_name in synonyms:
                self.logger.error('Species name {} is a GTDB synonym for {}: {}'.format(
                                        sp_name,
                                        synonyms[sp_name].species,
                                        gid))
                                    
    def _validate_unique_species_names(self, backfilled_taxonomy):
        """Make sure species names occur only once."""
        
        self.logger.info('Validation: ensuring species names occur only once.')
        
        sp_names = {}
        for gid in backfilled_taxonomy:
            species = backfilled_taxonomy[gid][self.SP_INDEX]
            
            if species in sp_names:
                self.logger.error('Species name {} occurs twice: {} {}'.format(
                                        species,
                                        gid,
                                        sp_names[species]))

            sp_names[species] = gid
            
    def _validate_type_strains(self, backfilled_taxonomy, selected_type_st_genomes):
        """Ensure type strains have expected specific name."""
        
        self.logger.info('Validation: ensuring type strains have expected specific name.')
        
        
        for gid, taxa in backfilled_taxonomy.items():
            if gid in selected_type_st_genomes:
                species = backfilled_taxonomy[gid][self.SP_INDEX]
                specific_name = self._specific_sp_name(species)
                if '_' in specific_name:
                    self.logger.error('Specific name of type strain {} has polyphyletic suffix: {}'.format(gid, species))
            
    def _patch_canonical_species(self, 
                                    backfilled_taxonomy, 
                                    selected_type_st_genomes,
                                    prev_taxonomy,
                                    taxon_suffix):
        """Patch identical canonical species names without type material so they all have polyphyletic suffixes."""
        
        self.logger.info('Patching identical canonical species names without type strains so they have polyphyletic suffixes.')
        
        canonical_sp_gids = defaultdict(list)
        for gid, taxa in backfilled_taxonomy.items():
            species = backfilled_taxonomy[gid][self.SP_INDEX]
            canonical_sp = self._canonical_species_name(species)
            canonical_sp_gids[canonical_sp].append(gid)

        fout = open(os.path.join(self.output_dir, '{}_patched_nontype_specific_names.tsv'.format(self.prefix)), 'w')
        fout.write('Genome ID\tOriginal proposal\tPatched proposal\tPrevious GTDB\tConflicts\n')
        count = 0
        for canonical_sp, gids in canonical_sp_gids.items():
            if len(gids) >= 2:
                conflict_str = []
                for gid in gids:
                    conflict_str.append('{}:{}'.format(gid, backfilled_taxonomy[gid][self.SP_INDEX]))
                conflict_str = '; '.join(conflict_str)
                    
                type_st = any([gid in selected_type_st_genomes for gid in gids])
                if not type_st:
                    # sort gids by present in previous GTDB taxonomy
                    prev_gids = [gid for gid in gids if gid in prev_taxonomy]
                    gids = prev_gids + [gid for gid in gids if gid not in prev_gids]
                
                    used_specific_names = defaultdict(set)
                    for gid in gids:
                        species = backfilled_taxonomy[gid][self.SP_INDEX]
                        specific_name = self._specific_sp_name(species)
                        used_specific_names[specific_name].add(gid)
                
                    for gid in gids:
                        species = backfilled_taxonomy[gid][self.SP_INDEX]
                        specific_name = self._specific_sp_name(species)
                        
                        if '_' not in specific_name:
                            prev_species = prev_taxonomy.get(gid, Taxonomy.rank_prefixes)[self.SP_INDEX]
                            prev_specific_name = self._specific_sp_name(prev_species)
                            
                            if (prev_species != 's__' and 
                                '_' in prev_specific_name and
                                (prev_specific_name not in used_specific_names or 
                                used_specific_names[prev_specific_name].difference([gid]) == set())):
                                # genome had a polyphyletic specific name in the previous release 
                                # which can be recycled here without issue
                                new_species = 's__{} {}'.format(backfilled_taxonomy[gid][self.GENUS_INDEX][3:],
                                                                prev_specific_name)
                            else:
                                canonical_specific_name = self._canonical_specific_name(specific_name)
                                
                                while True:
                                    suffix = self._get_suffix(taxon_suffix, canonical_sp)
                                    suffixed_specific_name = '{}_{}'.format(canonical_specific_name, suffix)
                                    if suffixed_specific_name not in used_specific_names:
                                        break
           
                                new_species = 's__{} {}'.format(backfilled_taxonomy[gid][self.GENUS_INDEX][3:],
                                                                suffixed_specific_name)
                                
                            backfilled_taxonomy[gid][self.SP_INDEX] = new_species
             
                            fout.write('{}\t{}\t{}\t{}\t{}\n'.format(
                                        gid,
                                        species,
                                        new_species,
                                        prev_species,
                                        conflict_str))
                            
        fout.close()
    
    def _validate_canonical_species(self, backfilled_taxonomy, selected_type_st_genomes):
        """Ensure identical canonical species names without type material are given polyphyletic suffixes."""
        
        self.logger.info('Validation: identical canonical species names without type material are given polyphyletic suffixes.')
        
        canonical_sp_gids = defaultdict(list)
        for gid, taxa in backfilled_taxonomy.items():
            species = backfilled_taxonomy[gid][self.SP_INDEX]
            canonical_sp = self._canonical_species_name(species)
            canonical_sp_gids[canonical_sp].append(gid)

        for canonical_sp, gids in canonical_sp_gids.items():
            if len(gids) >= 2:
                type_st = any([gid in selected_type_st_genomes for gid in gids])
                if not type_st:
                    for gid in gids:
                        species = backfilled_taxonomy[gid][self.SP_INDEX]
                        specific_name = self._specific_sp_name(species)
                        if '_' not in specific_name:
                            self.logger.error('Species has no type strain so specific name of {} '
                                                'should have polyphyletic suffix: {}'.format(
                                                    gid, species))
                                                    
                            count += 1
            
    def _validate_complete_taxonomy(self, backfilled_taxonomy):
        """Ensure all genomes have a complete taxonomy string."""
        
        self.logger.info('Validation: ensuring all genomes have a complete taxonomy string.')
        
        incomplete = set()
        for gid, taxa in backfilled_taxonomy.items():
            for taxon in taxa:
                if len(taxon) == 3:
                    incomplete.add(gid)
                    
        if len(incomplete) > 0:
            self.logger.error('Identified {} genomes with incomplete taxonomy strings.'.format(len(incomplete)))
            self.logger.error(' examples: {}'.format(','.join(list(incomplete)[0:min(5,len(incomplete))])))
        
    def run(self, 
                taxonomy_file, 
                prev_taxonomy, 
                gtdb_metadata_file,
                gtdb_named_type_genomes,
                gtdb_synonyms,
                sp_classification_ledger,
                sp_placeholder_ledger,
                genus_classification_ledger,
                user_genome_id_table,
                sp_cluster_file,
                curation_tree_file):
        """Fill in missing rank information."""

        # read manually curated GTDB taxonomy
        cur_taxonomy = Taxonomy().read(taxonomy_file)
        self.logger.info('Current GTDB taxonomy spans {:,} genomes ({:,} Bacteria; {:,} Archaea).'.format(
                            len(cur_taxonomy),
                            sum([1 for taxa in cur_taxonomy.values() if taxa[0] == 'd__Bacteria']),
                            sum([1 for taxa in cur_taxonomy.values() if taxa[0] == 'd__Archaea'])))
                            
        # get list of species and genus exceptions
        self.logger.info('Reading species exceptions ledgers.')
        gtdb_sp_ledger = parse_species_ledgers(sp_classification_ledger, sp_placeholder_ledger)
        self.logger.info('Identified {:,} genomes with declared species names.'.format(len(gtdb_sp_ledger)))
        
        self.logger.info('Reading genus exceptions ledger.')
        gtdb_genus_ledger = parse_genus_ledger(genus_classification_ledger)
        self.logger.info('Identified {:,} genomes with declared genus names.'.format(len(gtdb_genus_ledger)))
        
        self._check_ledgers(gtdb_sp_ledger, gtdb_genus_ledger)
        
        # fill missing ranks in current GTDB taxonomy
        filled_taxonomy = {}
        for gid, taxa in cur_taxonomy.items():
            filled_taxonomy[gid] = Taxonomy().fill_missing_ranks(taxa)
        cur_taxonomy = filled_taxonomy
        
        prev_taxonomy = Taxonomy().read(prev_taxonomy)
        self.logger.info('Previous GTDB taxonomy spans {:,} genomes.'.format(len(prev_taxonomy)))

        # read GTDB metadata for genomes in taxonomy file 
        # (typically the validation set of Bacteria or Archaea)
        ncbi_taxonomy = self._read_gtdb_ncbi_taxonomy(gtdb_metadata_file)

        d = self._read_gtdb_metadata(gtdb_metadata_file, user_genome_id_table, cur_taxonomy)
        (clusters,
            type_st_of_sp, 
            type_sp_of_genus,
            ncbi_info,
            user_id_map) = d
            
        if sp_cluster_file:
            self.logger.info('Reading species clusters from file: {}'.format(sp_cluster_file))
            clusters = self._parse_cluster_file(sp_cluster_file, cur_taxonomy)

        self.logger.info('Read NCBI taxonomy for %d genomes.' % len(ncbi_taxonomy))
        self.logger.info('Identified %d UBA or GenBank IDs for User genomes.' % len(user_id_map))
        self.logger.info('  %d UBA identifiers' % sum([1 for v in user_id_map.values() if v.startswith('UBA')]))
        self.logger.info('Identified %d species clusters spanning %d genomes.' % (len(clusters), sum([len(v) for v in clusters.values()])))
        self.logger.info('Identified %d genomes designated as type strain of species.' % len(type_st_of_sp))
        self.logger.info('Identified %d genomes designated as type species of genus.' % len(type_sp_of_genus))
        
        # validate species clusters
        self._validate_sp_clusters(clusters, cur_taxonomy)

        # get highest alphabetic suffix for each taxon
        taxon_suffix = SuffixTable().run(taxonomy_file, None)
        self.logger.info('Identified {:,} taxon with an alphabetic suffix.'.format(len(taxon_suffix)))
        self.logger.info('  {:,} genera, {:,} species'.format(
                        sum([1 for t in taxon_suffix if t.startswith('g__')]),
                        sum([1 for t in taxon_suffix if t.startswith('s__')])))
                        
        # get map between user genome IDs and NCBI accessions
        user_to_ncbi_acc = {}
        user_to_uba_acc = {}
        for line in open(user_genome_id_table):
            line_split = line.strip().split('\t')
            user_to_uba_acc[line_split[0]] = line_split[1]
            if len(line_split) == 3:
                user_to_ncbi_acc[line_split[0]] = line_split[2]
                
        # get GTDB genomes representing species clusters with binomial names
        gtdb_named_sp = self._gtdb_named_type_genomes(gtdb_named_type_genomes)
        self.logger.info('Identified {:,} species cluster with binomial names.'.format(len(gtdb_named_sp)))
        
        selected_type_st_genomes = type_st_of_sp.intersection(gtdb_named_sp)
        self.logger.info('Identified {:,} selected type strain genomes.'.format(len(selected_type_st_genomes)))
        
        # get GTDB synonyms
        synonyms = parse_gtdb_synonym_file(gtdb_synonyms)
        self.logger.info('Identified {:,} GTDB synonyms.'.format(len(synonyms)))

        # assign genus names to all species representatives
        generic_names = self._assign_generic_name(clusters, 
                                                    cur_taxonomy, 
                                                    prev_taxonomy, 
                                                    ncbi_taxonomy,
                                                    gtdb_named_sp,
                                                    gtdb_sp_ledger,
                                                    gtdb_genus_ledger,
                                                    type_sp_of_genus,
                                                    ncbi_info,
                                                    taxon_suffix)

        # assign specific names to all species representatives
        specific_names = self._assign_specific_name(clusters,
                                                    generic_names,
                                                    prev_taxonomy,
                                                    ncbi_taxonomy,
                                                    gtdb_named_sp,
                                                    synonyms,
                                                    gtdb_sp_ledger,
                                                    type_st_of_sp,
                                                    user_to_ncbi_acc,
                                                    user_to_uba_acc,
                                                    user_id_map,
                                                    taxon_suffix)
                                                    
        # update taxonomy with species and genus names
        backfilled_taxonomy = {}
        for rid in clusters:
            taxa = cur_taxonomy[rid]
            taxa[self.GENUS_INDEX] = 'g__' + generic_names[rid]
            taxa[self.SP_INDEX] = 's__{} {}'.format(generic_names[rid], specific_names[rid])
            backfilled_taxonomy[rid] = taxa
            
        # backfill genus name as required
        backfilled_taxonomy = self._backfill_genus(backfilled_taxonomy, 
                                                    prev_taxonomy,
                                                    gtdb_named_sp,
                                                    type_sp_of_genus,
                                                    type_st_of_sp,
                                                    taxon_suffix)
                                                    
        self._patch_canonical_species(backfilled_taxonomy, 
                                        selected_type_st_genomes,
                                        prev_taxonomy,
                                        taxon_suffix)

        # sanity check: ensure generic names agree with manual curation
        self._validate_manual_genus_names(cur_taxonomy, backfilled_taxonomy)
        
        # sanity check: ensure generic names agree with genus ledger
        self._validate_genus_ledger(gtdb_genus_ledger, backfilled_taxonomy)
        
        # sanity check: ensure species names agree with species ledger
        self._validate_species_ledger(gtdb_sp_ledger, backfilled_taxonomy)
        
        # sanity check: ensure genus name agrees with generic name of species
        self._validate_genus_generic_names(backfilled_taxonomy)
        
        # sanity check: ensure GTDB synonyms are not used as species names
        self._validate_synonyms(backfilled_taxonomy, synonyms)
        
        # sanity check: validate specific name of type strains
        self._validate_type_strains(backfilled_taxonomy, selected_type_st_genomes)
        
        # sanity check: ensure identical canonical species names without 
        # type material are given polyphyletic suffixes
        self._validate_canonical_species(backfilled_taxonomy, selected_type_st_genomes)
        
        # sanity check: ensure all species names occur once
        self._validate_unique_species_names(backfilled_taxonomy)
        
        # sanity check: ensure all genomes have a complete taxonomy string
        self._validate_complete_taxonomy(backfilled_taxonomy)

        # write out new taxonomy
        output_taxonomy = os.path.join(self.output_dir, '{}_taxonomy_backfill.tsv'.format(self.prefix))
        Taxonomy().write(backfilled_taxonomy, output_taxonomy)
        
        # create tree for inspecting results of backfilling
        if curation_tree_file:
            self._create_backfill_tree(curation_tree_file, 
                                        backfilled_taxonomy, 
                                        clusters)
        
        return output_taxonomy
