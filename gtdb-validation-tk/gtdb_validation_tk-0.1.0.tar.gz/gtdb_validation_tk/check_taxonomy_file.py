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

from gtdb_validation_tk.common import (placeholder_genus,
                                        canonical_taxon_name,
                                        latinized_specific_sp_name)


class CheckTaxonomyFile():
    """Validate different aspects of standard taxonomy file."""

    def __init__(self, dpi=96):
        """Initialize."""
        
        self.logger = logging.getLogger()
        
    def check(self, taxonomy,
                    check_prefixes, 
                    check_ranks, 
                    check_hierarchy, 
                    check_species, 
                    check_group_names,
                    check_duplicate_names):
        """Check if taxonomy forms a strict hierarchy with all expected ranks.

        Parameters
        ----------
        taxonomy : d[unique_id] -> [d__<taxon>; ...; s__<taxon>]
            Taxonomy strings indexed by unique ids.
        check_prefixes : boolean
            Flag indicating if prefix of taxon should be validated.
        check_ranks : boolean
            Flag indicating if the presence of all ranks should be validated.
        check_hierarchy : boolean
            Flag indicating if the taxonomic hierarchy should be validated.
        check_species : boolean
            Flag indicating if the taxonomic consistency of named species should be validated.
        check_group_names : boolean
            Flag indicating if group names should be checked for invalid characters.
        check_duplicate_names : boolean
            Flag indicating if group names should be checked for duplicates.
        report_errors : boolean
            Flag indicating if errors should be written to screen.

        Returns
        -------
        dict : d[taxon_id] -> taxonomy
            Taxa with invalid number of ranks.
        dict : d[taxon_id] -> [taxon, taxonomy]
            Taxa with invalid rank prefixes.
        dict: d[taxon_id] -> [species name, error message]
            Taxa with invalid species names.
        dict: d[child_taxon_id] -> two or more parent taxon ids
            Taxa with invalid hierarchies.
        """
        
        # check for incomplete taxonomy strings or unexpected rank prefixes
        Taxonomy().validate(taxonomy,
                            check_prefixes=check_prefixes,
                            check_ranks=check_ranks,
                            check_hierarchy=check_hierarchy,
                            check_species=check_species,
                            check_group_names=check_group_names,
                            check_duplicate_names=check_duplicate_names,
                            report_errors=True)
                            
        # flag species names where the generic name is a placeholder,
        # but the specific name is Latinized
        if check_species:
            failed_genus = []
            failed_sp_form = []
            for gid, taxa in taxonomy.items():
                species = taxa[6]
                tokens = species[3:].split()
                if len(tokens) == 2:
                    generic, specific = species[3:].split()
                    
                    canonical_generic = canonical_taxon_name('g__' + generic)
                    if placeholder_genus(canonical_generic):
                        if latinized_specific_sp_name(specific):
                            failed_genus.append((gid, species))
                else:
                    failed_sp_form.append((gid, taxa[6]))

            if failed_genus:
                print('\nTaxonomy contains species with placeholder generic names and Latinized specific names:')
                for gid, species in failed_genus:
                    print('{}\t{}'.format(gid, species))
                    
            if failed_sp_form:
                print('\nTaxonomy contains species with invalidly formed species names:')
                for gid, species in failed_sp_form:
                    print('{}\t{}'.format(gid, species))
                    
        # check that sp<GID> specific names match the NCBI accession
        if check_species:
            failed = []
            for gid, taxa in taxonomy.items():
                if gid.startswith('D-') or gid.startswith('U_') or gid.startswith('UBA'):
                    continue
                
                species = taxa[6]
                tokens = species[3:].split()
                if len(tokens) == 2:
                    generic, specific = species[3:].split()
                    
                    if specific.startswith('sp') and all(ch.isdigit() for ch in specific[2:]):
                        if gid[gid.rfind('_')+1:gid.rfind('.')] != specific[2:]:
                            failed.append((gid, species))
                        
            if failed:
                print('\nTaxonomy contains specific species identifier that does not match genome identifier:')
                for gid, species in failed:
                    print('{}\t{}'.format(gid, species))
