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
import csv
import sys
from collections import defaultdict, namedtuple

import biolib.seq_io as seq_io
from biolib.taxonomy import Taxonomy


def canonical_wgs_id(wgs_accession):
    """Create canonical WGS ID."""
    
    if not wgs_accession or wgs_accession == 'none':
        return 'n/a'
        
    wgs_acc, version = wgs_accession.split('.')
    idx = [ch.isdigit() for ch in wgs_acc].index(True)
    wgs_id = wgs_acc[0:idx] + str(version).zfill(2)
    
    return wgs_id
    

def canonical_taxon_name(taxon):
    """Get canonical version of taxon."""
    
    if '_' in taxon[3:]:
        taxon = taxon[0:taxon.rfind('_')]
        
    return taxon


def canonical_genus_name(genus_name):
    """Get canonical genus name from GTDB or NCBI genus name."""
    
    if genus_name == 'g__':
        return genus_name
    
    prefix = genus_name[0:3]
    genus = genus_name[3:]
    
    underscore_pos = genus.rfind('_')
    if underscore_pos != -1:
        genus = genus[0:underscore_pos]
        
    return prefix + genus
    

def canonical_species_name(species_name):
    """Get canonical species name from GTDB or NCBI species name."""
    
    if species_name == 's__':
        return species_name
    
    species_name = species_name.replace('Candidatus ', '')
    prefix = species_name[0:3]
    full_name = species_name[3:]
    genus, species = full_name.split(' ')
    
    underscore_pos = genus.rfind('_')
    if underscore_pos != -1:
        genus = genus[0:underscore_pos]
        
    underscore_pos = species.rfind('_')
    if underscore_pos != -1:
        species = species[0:underscore_pos]
        
    genus = genus.replace('[','').replace(']','')
    species = species.replace('[','').replace(']','')
        
    return prefix + genus + ' ' + species


def gtdb_canonical_species_id(gid, specific_name):
    """Check if specific name has the form sp<accession>."""
    
    canonical_name = canonical_taxon_name(specific_name)
    
    if canonical_name.startswith('sp'):
        if gid.startswith('UBA'):
            sp_id = gid[3:] + 'u'
        else:
            sp_id = gid[gid.rfind('_')+1:gid.rfind('.')]
            
        if canonical_name[2:] == sp_id:
            return True
            
    return False


def placeholder_genus(genus):
    """Determine if genus name is a placeholder name."""
    
    # get genus name without rank prefix
    genus = genus.replace('g__', '')
    
    # check if name contains any non-alphabetic
    # characters such as digits, hyphens, etc.
    if not genus.isalpha():
        return True
        
    # check if there is a capital letter other than
    # the first
    if any(ch.isupper() for ch in genus[1:]):
        return True
        
    return False
    
    
def latinized_generic_sp_name(generic_name):
    """Check if generic species name is Latinized."""
    
    return (generic_name[0].isupper() 
            and all(c.islower() for c in generic_name[1:]))
    
def latinized_specific_sp_name(specific_name):
    """Check if specific species name is Latinized."""
    
    return all(c.islower() for c in specific_name)


def parse_species_ledgers(sp_classification_ledger, sp_placeholder_ledger):
    """Parse files containing specific species names for select genomes."""
    
    valid_chrs = set(['_', ' '])
    
    gtdb_sp_ledger = {}
    for sp_file in [sp_classification_ledger, sp_placeholder_ledger]:
        if sp_file == None:
            continue
            
        with open(sp_file) as f:
            header = f.readline().strip().split('\t')
            
            gid_index = header.index('Genome ID')
            sp_index = header.index('Proposed species name')
            
            for line in f:
                line_split = line.strip().split('\t')
                
                gid = line_split[gid_index].strip()
                sp = line_split[sp_index].strip()
                sp = sp.replace('Candidatus ', '')
                if not sp.startswith('s__'):
                    sp = 's__' + sp
                    
                if any(not ch.isalpha() 
                        and not ch.isdigit() 
                        and ch not in valid_chrs for ch in sp):
                    self.logger.error('Species name {} contains unexpected characters in genome {}.'.format(
                                        sp, 
                                        gid))
                    sys.exit(-1)
                
                gtdb_sp_ledger[gid] = sp
                
    return gtdb_sp_ledger
        

def parse_genus_ledger(genus_classification_ledger):
    """Parse file containing specific genus names for select genomes."""
    
    valid_chrs = set(['_', ' '])
        
    gtdb_genus_ledger = {}
    with open(genus_classification_ledger) as f:
        header = f.readline().strip().split('\t')
        
        gid_index = header.index('Genome ID')
        genus_index = header.index('Proposed genus name')
        
        for line in f:
            line_split = line.strip().split('\t')
            
            gid = line_split[gid_index].strip()
            genus = line_split[genus_index].strip()
            genus = genus.replace('Candidatus ', '')
            if not genus.startswith('g__'):
                genus = 'g__' + genus
                
            if any(not ch.isalpha() and ch not in valid_chrs for ch in genus):
                    self.logger.error('Species name {} contains unexpected characters in genome {}.'.format(
                                        genus,
                                        gid))
                    sys.exit(-1)
            
            gtdb_genus_ledger[gid] = genus
                
    return gtdb_genus_ledger


def parse_gtdb_synonym_file(gtdb_synonym_file):
    """Get GTDB synonyms."""
    
    SynonymInfo = namedtuple('SynonymInfo', 'species ani af')
    
    synonyms = {}
    with open(gtdb_synonym_file) as f:
        header = f.readline().strip().split('\t')
        
        gtdb_sp_index = header.index('NCBI species')
        gtdb_synonym_index = header.index('Synonym')
        ani_index = header.index('ANI')
        af_index = header.index('AF')
        
        for line in f:
            line_split = line.strip().split('\t')
            
            gtdb_sp = line_split[gtdb_sp_index]
            gtdb_synonym = line_split[gtdb_synonym_index]
            ani = float(line_split[ani_index])
            af = float(line_split[af_index])
            
            synonyms[gtdb_synonym] = SynonymInfo(gtdb_sp, ani, af)
            
    return synonyms
    
    
def read_gtdb_metadata(metadata_file, fields):
    """Parse genome quality from GTDB metadata.

    Parameters
    ----------
    metadata_file : str
        Metadata for all genomes in TSV file.
    fields : iterable
        Fields  to read.

    Return
    ------
    dict : d[genome_id] -> namedtuple
        Value for fields indicted by genome IDs.
    """

    gtdb_metadata = namedtuple('gtdb_metadata', ' '.join(fields))
    
    m = {}
    with open(metadata_file) as f:
        header = f.readline().strip().split('\t')
        
        genome_index = header.index('accession')
        indices = []
        for field in fields:
            indices.append(header.index(field))

        for line in f:
            line_split = line.strip().split('\t')
            genome_id = line_split[genome_index]

            values = []
            for i in indices:
                # save values as floats or strings
                v = line_split[i]
                try:
                    values.append(float(v))
                except ValueError:
                    if v is None or v == '' or v == 'none':
                        values.append(None)
                    else:
                        values.append(v)
            m[genome_id] = gtdb_metadata._make(values)

    return m
    
def read_ncbi_taxonomy(metadata_file):
    """Parse NCBI taxonomy from GTDB metadata.

    Parameters
    ----------
    metadata_file : str
        Metadata for all genomes.

    Return
    ------
    dict : d[genome_id] -> taxonomy list
    """

    taxonomy = {}

    with open(metadata_file) as f:
        headers = f.readline().strip().split('\t')
        genome_index = headers.index('accession')
        taxonomy_index = headers.index('ncbi_taxonomy')
        
        for line in f:
            line_split = line.strip().split('\t')
            genome_id = line_split[genome_index]
            taxa_str = line_split[taxonomy_index].strip()

            if taxa_str and taxa_str != 'none':
                taxonomy[genome_id] = map(str.strip, taxa_str.split(';'))
            else:
                taxonomy[genome_id] = list(Taxonomy.rank_prefixes)

    return taxonomy
