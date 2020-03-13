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
import csv
import re
import logging
from collections import defaultdict

import dendropy

from biolib.common import check_file_exists, make_sure_path_exists, is_float
from biolib.external.execute import check_dependencies
from biolib.taxonomy import Taxonomy
from biolib.newick import parse_label

from gtdb_validation_tk.common import read_gtdb_metadata, canonical_species_name, canonical_wgs_id
from gtdb_validation_tk.check_taxonomy_file import CheckTaxonomyFile
from gtdb_validation_tk.backfill import Backfill
from gtdb_validation_tk.suffix_table import SuffixTable
from gtdb_validation_tk.red_check import RED_Check
from gtdb_validation_tk.missing_genera import MissingGenera
from gtdb_validation_tk.merge_genera import MergeGenera
from gtdb_validation_tk.check_species_names import CheckSpeciesNames
from gtdb_validation_tk.validate_type_material import ValidateTypeMaterial
from gtdb_validation_tk.validate_species_by_ncbi_name import ValidateSpeciesNames
from gtdb_validation_tk.validate_gtdb_clusters_by_name import ValidateClustersNCBI
from gtdb_validation_tk.validate_species_clusters import ValidateSpeciesClusters
from gtdb_validation_tk.tree_diff import TreeDiff
from gtdb_validation_tk.tax_diff import TaxDiff
from gtdb_validation_tk.spellchecker import SpellChecker

from numpy import mean as np_mean

csv.field_size_limit(sys.maxsize)

class OptionsParser():
    def __init__(self):
        """Initialization"""
        self.logger = logging.getLogger()

    def check_file(self, options):
        """Verify taxonomy file is formatted as expected."""

        check_file_exists(options.input_taxonomy)

        taxonomy = Taxonomy().read(options.input_taxonomy)
        
        p = CheckTaxonomyFile()
        p.check(taxonomy,
                check_prefixes=True,
                check_ranks=True,
                check_hierarchy=True,
                check_species=options.include_species,
                check_group_names=True,
                check_duplicate_names=True)

        self.logger.info('Finished performing validation tests.')
        
    def check_tree(self, options):
        """Validate taxonomy of decorated tree and check for polyphyletic groups."""
        
        check_file_exists(options.decorated_tree)

        # validate taxonomy
        taxonomy = Taxonomy()
        if options.taxonomy_file:
            cur_taxonomy = taxonomy.read(options.taxonomy_file)
        else:
            cur_taxonomy = taxonomy.read_from_tree(options.decorated_tree)
        
        p = CheckTaxonomyFile()
        p.check(cur_taxonomy,
                check_prefixes=True,
                check_ranks=True,
                check_hierarchy=True,
                check_species=options.include_species,
                check_group_names=True,
                check_duplicate_names=True)
                          
        # check for polyphyletic groups
        polyphyletic_groups = set()
        tree = dendropy.Tree.get_from_path(options.decorated_tree, 
                                                schema='newick', 
                                                rooting="force-rooted", 
                                                preserve_underscores=True)
                                                
        if options.taxonomy_file:
            # reduce taxonomy to taxa in tree and map taxon labels to Taxon objects
            reduced_taxonomy = {}
            taxon_map = {}
            for leaf in tree.leaf_node_iter():
                if leaf.taxon.label in cur_taxonomy: # need explicit check since tree may contain 'dummy' leaves
                    reduced_taxonomy[leaf.taxon.label] = cur_taxonomy[leaf.taxon.label]
                    taxon_map[leaf.taxon.label] = leaf.taxon
 
            # find taxa with an MRCA spanning additional taxa
            for rank_label in Taxonomy.rank_labels[1:]:
                extant_taxa = taxonomy.extant_taxa_for_rank(rank_label, reduced_taxonomy)
                for taxon, taxa_ids in extant_taxa.items():
                    mrca = tree.mrca(taxa=[taxon_map[t] for t in taxa_ids])
                    mrca_leaf_count = sum([1 for leaf in mrca.leaf_iter() if leaf.taxon.label in cur_taxonomy])
                    if mrca_leaf_count != len(taxa_ids):
                        print(taxon, mrca_leaf_count, len(taxa_ids))
                        polyphyletic_groups.add(taxon)
        else:
            # find duplicate taxon labels in tree
            taxa = set()
            
            for node in tree.preorder_node_iter(lambda n: not n.is_leaf()):
                _support, taxon_label, _aux_info = parse_label(node.label)
                if taxon_label:
                    for taxon in [t.strip() for t in taxon_label.split(';')]:
                        if taxon in taxa:
                            polyphyletic_groups.add(taxon)
                        
                        taxa.add(taxon)

        if len(polyphyletic_groups):
            print('')
            print('Tree contains polyphyletic groups:')
            for taxon in polyphyletic_groups:
                if not taxon.startswith('s__') or options.include_species:
                    print('%s' % (taxon))
            print('')
                          
        self.logger.info('Finished performing validation tests.')
        
    def check_suffix(self, options):
        """Report taxa with potentially erroneous polyphyly suffix designations."""

        check_file_exists(options.input_taxonomy)
        
        taxonomy = Taxonomy().read(options.input_taxonomy)
        
        # create set with all taxa in taxonomy
        all_taxa = set()
        for taxa in taxonomy.values():
            for taxon in taxa:
                all_taxa.add(taxon)

        # identify isolate names that may be erroneous
        suspecious_taxon_to_check = set()
        taxon_to_check = set()
        for gid, taxa in taxonomy.items():
            for taxon in taxa:
                if re.match('^[a-z][_]*[a-zA-Z0-9-]+[_]', taxon):
                    canonical_taxon = taxon[0:3] + ' '.join([t.strip() for t in re.split('_[A-Z]+(?= |$)', taxon[3:])]).strip()
                    
                    if taxon.startswith('s__'):
                        if options.include_species:
                            genus = canonical_taxon.split(' ')[0].replace('s__', 'g__')
                            if canonical_taxon in all_taxa or genus in all_taxa: 
                                # probably fine as canonical name exists in the taxonomy
                                taxon_to_check.add((taxon, canonical_taxon))
                            else:
                                suspecious_taxon_to_check.add(taxon)
                    else:
                        if canonical_taxon in all_taxa:
                            # probably fine as canonical name exists in the taxonomy
                            taxon_to_check.add((taxon, canonical_taxon))
                        else:
                            suspecious_taxon_to_check.add(taxon)

        if suspecious_taxon_to_check:
            print('\nThe following taxa may have erroneous polyphyly suffix designations:')
            for taxon in suspecious_taxon_to_check:
                print('  %s' % taxon)
        
        if not taxon_to_check and not suspecious_taxon_to_check:
            print('\nDid not identify any taxa with potentially erroneous polyphyly suffix designations.')
            
        self.logger.info('Finished performing test.')
        
    def red_check(self, options):
        """Report taxa with unexpected RED values."""
        
        check_file_exists(options.scaled_tree)
        check_file_exists(options.red_dictionary)
        
        p = RED_Check()
        p.run(options.scaled_tree,
                options.red_dictionary,
                options.output_file)
                
        self.logger.info('Results written to: %s' % options.output_file)
        self.logger.info('Finished performing validation tests.')
        
    def missing_genera(self, options):
        """Report lineages that may represent missing genus names."""
        
        check_file_exists(options.scaled_tree)
        check_file_exists(options.red_dictionary)
        check_file_exists(options.gtdb_prev_taxonomy)
        check_file_exists(options.ncbi_taxonomy)
        
        p = MissingGenera()
        p.run(options.scaled_tree,
                options.red_dictionary,
                options.gtdb_prev_taxonomy,
                options.ncbi_taxonomy,
                options.output_file)
                
        self.logger.info('Results written to: %s' % options.output_file)
        self.logger.info('Finished performing validation tests.')
        
    def merge_genera(self, options):
        """Report polyphyletic genera that are candidates for merging."""
        
        check_file_exists(options.scaled_tree)
        check_file_exists(options.red_dictionary)
        
        p = MergeGenera()
        p.run(options.scaled_tree,
                options.red_dictionary,
                options.output_file)
                
        self.logger.info('Results written to: %s' % options.output_file)
        self.logger.info('Finished performing validation tests.')

    def support(self, options):
        """Report taxa with low support values."""
        
        check_file_exists(options.decorated_tree)
        
        tree = dendropy.Tree.get_from_path(options.decorated_tree, 
                                                schema='newick', 
                                                rooting="force-rooted", 
                                                preserve_underscores=True)
                                                
        poor_support = {}
        for n in tree.preorder_node_iter():
            support, taxon, _aux_info = parse_label(n.label)
            if taxon and support < options.min_support:
                poor_support[taxon] = support
                
        if poor_support:
            print('')
            for taxon in Taxonomy().sort_taxa(poor_support):
                print('%s\t%s' % (taxon, poor_support[taxon]))
            print('')

        self.logger.info('Finished performing test.')

    def tax_diff(self, options):
        """Compare two taxonomy files."""

        check_file_exists(options.input_taxonomy1)
        check_file_exists(options.input_taxonomy2)

        td = TaxDiff()
        td.tax_diff(options.input_taxonomy1,
                    options.input_taxonomy2,
                    options.gtdb_metadata_file,
                    options.output_dir)

        self.logger.info('Done.')
        
    def tree_diff(self, options):
        """Tree diff command."""
        
        check_file_exists(options.input_tree1)
        check_file_exists(options.input_tree2)
        make_sure_path_exists(options.output_dir)

        td = TreeDiff()
        td.run(options.input_tree1,
                options.input_tree2,
                options.output_dir,
                options.min_support,
                options.min_taxa)
        
        self.logger.info('Done.')
        
    def retired_taxa(self, options):
        """Report all taxa that have been retired (lost?) between two taxonomy files.."""

        check_file_exists(options.new_taxonomy_file)
        check_file_exists(options.prev_taxonomy_file)

        # get all taxa in previous taxonomy file
        prev_taxa = defaultdict(set)
        prev_gids = defaultdict(set)
        with open(options.prev_taxonomy_file) as f:
            for line in f:
                line_split = line.strip().split('\t')
                gid = line_split[0]
                taxa = [t.strip() for t in line_split[1].split(';')]
                for taxon in taxa:
                    rank_prefix = taxon[0:3]
                    prev_taxa[rank_prefix].add(taxon)
                    prev_gids[taxon].add(gid)
                    
        # get all taxa in current taxonomy file
        cur_taxa = defaultdict(set)
        cur_taxonomy = {}
        with open(options.new_taxonomy_file) as f:
            for line in f:
                line_split = line.strip().split('\t')
                gid = line_split[0]
                taxa = [t.strip() for t in line_split[1].split(';')]
                cur_taxonomy[gid] = taxa
                for taxon in taxa:
                    rank_prefix = taxon[0:3]
                    cur_taxa[rank_prefix].add(taxon)
                    
        fout = open(options.output_table,'w')
        fout.write('Rank\tRetired taxon\tClassification in new taxonomy\tGenome IDs in previous taxonomy\n')
        for idx, rank_prefix in enumerate(Taxonomy.rank_prefixes):
            for prev_taxon in prev_taxa[rank_prefix]:
                if prev_taxon not in cur_taxa[rank_prefix]:
                    new_classification = defaultdict(int)
                    for gid in prev_gids[prev_taxon]:
                        if gid in cur_taxonomy:
                            new_classification[cur_taxonomy[gid][idx]] += 1
                            
                    new_classification_str = []
                    for taxon, count in new_classification.items():
                        new_classification_str.append('{}:{}'.format(taxon, count))
                            
                    fout.write('{}\t{}\t{}\t{}\n'.format(
                                Taxonomy.rank_labels[idx],
                                prev_taxon,
                                ', '.join(new_classification_str),
                                ', '.join(prev_gids[prev_taxon])))
                                
        fout.close()

        self.logger.info('Done.')

    def branch_len(self, options):
        """Branch length command."""
        
        check_file_exists(options.input_tree)

        tree = dendropy.Tree.get_from_path(options.input_tree, 
                                            schema='newick', 
                                            rooting='force-rooted', 
                                            preserve_underscores=True)
                                            
        leaf_root_dists = tree.calc_node_root_distances(return_leaf_distances_only=True)
        mean_branch_len = np_mean(leaf_root_dists)
        
        self.logger.info('Mean root to extant taxa branch length is %.3f.' % mean_branch_len)
        
        if mean_branch_len < 0.5 or mean_branch_len > 2.0:
            self.logger.warning('Mean root to extant taxa branch length is unusual.')
            self.logger.warning('This value depend on the rooting of the tree, but is expected to be between 0.5 and 2.0.')
        else:
            self.logger.info('This is within the range expected, [0.5, 2.0].')
        
        self.logger.info('Done.')
        
    def check_spelling(self,options):
        """Return a Levenshtein distance between ranks in 2 different taxonomy. This can be used to detect typos."""
        
        check_file_exists(options.input_taxonomy1)
        check_file_exists(options.input_taxonomy2)
        sc = SpellChecker()
        sc.spell_check(options.input_taxonomy1,
               options.input_taxonomy2,
               options.dist,
               options.output_file)
        self.logger.info('Done.')
        
    def check_distrib(self,options):
        """Return summary of group changes between 2 taxonomies."""

        check_file_exists(options.input_taxonomy1)
        check_file_exists(options.input_taxonomy2)
        make_sure_path_exists(options.output_dir)

        td = TaxDiff()
        td.check_distrib(options.input_taxonomy1,
                           options.input_taxonomy2,
                           options.output_dir,
                           options.keep_no_change,
                           options.keep_placeholder_name)
        self.logger.info('Done.')

    def ncbi_tax_diff(self, options):
        """Establish changes in NCBI taxonomy that may impact GTDB taxonomy."""

        check_file_exists(options.prev_ncbi_taxonomy)
        check_file_exists(options.cur_ncbi_taxonomy)
        check_file_exists(options.gtdb_taxonomy)

        td = TaxDiff()
        td.ncbi_tax_diff(options.prev_ncbi_taxonomy,
                            options.cur_ncbi_taxonomy,
                            options.gtdb_taxonomy,
                            options.output_dir)

        self.logger.info('Done.')
        
    def check_generic(self, options):
        """Validate generic name of species."""
        
        check_file_exists(options.input_taxonomy)
        check_file_exists(options.gtdb_metadata_file)
        check_file_exists(options.sp_classification_ledger)
        check_file_exists(options.genus_ledger)
        check_file_exists(options.gtdb_synonym_file)
        check_file_exists(options.user_genome_id_table)
        make_sure_path_exists(options.output_dir)
        
        p = CheckSpeciesNames()
        p.check_generic(options.input_taxonomy,
                            options.gtdb_metadata_file,
                            options.sp_classification_ledger,
                            options.genus_ledger,
                            options.gtdb_synonym_file,
                            options.user_genome_id_table,
                            options.output_dir)
        
        self.logger.info('Done.')
        
    def check_specific(self, options):
        """Validate specific name of species."""
        
        check_file_exists(options.input_taxonomy)
        check_file_exists(options.gtdb_metadata_file)
        check_file_exists(options.sp_classification_ledger)
        check_file_exists(options.gtdb_synonym_file)
        check_file_exists(options.user_genome_id_table)
        make_sure_path_exists(options.output_dir)
        
        p = CheckSpeciesNames()
        p.check_specific(options.input_taxonomy,
                            options.gtdb_metadata_file,
                            options.sp_classification_ledger,
                            options.gtdb_synonym_file,
                            options.user_genome_id_table,
                            options.output_dir)
        
        self.logger.info('Done.')
        
    def species_clusters(self, options):
        """Compare GTDB taxonomy to type strains."""

        check_file_exists(options.input_taxonomy)
        check_file_exists(options.gtdb_metadata_file)
        make_sure_path_exists(options.output_dir)
        
        p = ValidateSpeciesClusters()
        p.run(options.input_taxonomy, 
                options.gtdb_metadata_file,
                options.output_dir)

        self.logger.info('Done.')

    def type_strains(self, options):
        """Compare GTDB taxonomy to type strains."""

        check_file_exists(options.input_taxonomy)
        check_file_exists(options.gtdb_metadata_file)
        check_file_exists(options.sp_classification_ledger)
        check_file_exists(options.gtdb_named_type_genomes)
        check_file_exists(options.gtdb_synonym_file)
        make_sure_path_exists(options.output_dir)
        
        v = ValidateTypeMaterial()
        v.validate_type_strains(options.input_taxonomy,
                                options.gtdb_metadata_file,
                                options.sp_classification_ledger,
                                options.gtdb_named_type_genomes,
                                options.gtdb_synonym_file,
                                options.show_synonyms,
                                options.prefix,
                                options.output_dir)
                        
        self.logger.info('Done.')
        
    def type_species(self, options):
        """Compare GTDB taxonomy to type species."""

        check_file_exists(options.input_taxonomy)
        check_file_exists(options.gtdb_metadata_file)
        check_file_exists(options.gtdb_synonym_file)
        check_file_exists(options.sp_classification_ledger)
        check_file_exists(options.genus_classification_ledger)
        make_sure_path_exists(options.output_dir)
        
        v = ValidateTypeMaterial()
        v.validate_type_species(options.input_taxonomy,
                                    options.gtdb_metadata_file,
                                    options.gtdb_synonym_file,
                                    options.sp_classification_ledger,
                                    options.genus_classification_ledger,
                                    options.show_synonyms,
                                    options.prefix,
                                    options.output_dir)
                        
        self.logger.info('Done.')
        
    def val_table(self, options):
        """General validation table."""
        
        check_file_exists(options.input_taxonomy)
        check_file_exists(options.gtdb_metadata_file)
        
        gtdb_taxonomy = {}
        with open(options.input_taxonomy) as f:
            for line in f:
                line_split = line.strip().split('\t')
                gid = line_split[0]
                if gid.startswith('D-'):
                    continue # dummy genome_dir_file
                    
                taxa = [t.strip() for t in line_split[1].split(';')]
                gtdb_taxonomy[gid] = taxa
                
        fout = open(options.output_table, 'w')
        fout.write('Genome ID\tProposed taxonomy\tProposed species')
        fout.write('\tNCBI taxonomy\tNCBI species\tNCBI organism name\tNCBI infraspecific name\tNCBI WGS ID')
        fout.write('\tGTDB type designation\n')
        with open(options.gtdb_metadata_file) as f:
            header = f.readline().strip().split('\t')
            
            ncbi_taxonomy_index = header.index('ncbi_taxonomy')
            ncbi_org_name_index = header.index('ncbi_organism_name')
            ncbi_wgs_index = header.index('ncbi_wgs_master')
            ncbi_isolate_index = header.index('ncbi_isolate')
            gtdb_type_designation_index = header.index('gtdb_type_designation')
            
            for line in f:
                line_split = line.strip().split('\t')
                
                gid = line_split[0]
                if gid not in gtdb_taxonomy:
                    continue
                    
                ncbi_taxonomy = line_split[ncbi_taxonomy_index]
                ncbi_taxa = Taxonomy.rank_prefixes
                if ncbi_taxonomy and ncbi_taxonomy != 'none':
                    ncbi_taxa = [t.strip() for t in ncbi_taxonomy.split(';')]
                    
                ncbi_org_name = line_split[ncbi_org_name_index]
                if not ncbi_org_name or ncbi_org_name == 'none':
                    ncbi_org_name = 'n/a'
                    
                ncbi_isolate = line_split[ncbi_isolate_index]
                if not ncbi_isolate or ncbi_isolate == 'none':
                    ncbi_isolate = 'n/a'
                    
                ncbi_wgs_id = canonical_wgs_id(line_split[ncbi_wgs_index])
                
                gtdb_type_designation = line_split[gtdb_type_designation_index]
                
                fout.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
                            gid,
                            '; '.join(gtdb_taxonomy[gid]),
                            gtdb_taxonomy[gid][6],
                            '; '.join(ncbi_taxa),
                            ncbi_taxa[6],
                            ncbi_org_name,
                            ncbi_isolate,
                            ncbi_wgs_id,
                            gtdb_type_designation))
            
        fout.close()
        
    def backfill(self, options):
        """Fill in missing rank information."""

        check_file_exists(options.input_taxonomy)
        check_file_exists(options.prev_taxonomy)
        check_file_exists(options.gtdb_metadata_file)
        check_file_exists(options.gtdb_named_type_genomes)
        check_file_exists(options.gtdb_synonym_file)
        check_file_exists(options.sp_classification_ledger)
        check_file_exists(options.user_genome_id_table)
        make_sure_path_exists(options.output_dir)

        b = Backfill(options.prefix, options.output_dir)
        output_taxonomy = b.run(options.input_taxonomy,
                                options.prev_taxonomy,
                                options.gtdb_metadata_file,
                                options.gtdb_named_type_genomes,
                                options.gtdb_synonym_file,
                                options.sp_classification_ledger,
                                options.sp_placeholder_ledger,
                                options.genus_classification_ledger,
                                options.user_genome_id_table,
                                options.sp_cluster_file,
                                options.curation_tree_file)
                
        v = ValidateTypeMaterial()
        v.validate_type_strains(output_taxonomy,
                                options.gtdb_metadata_file,
                                options.gtdb_synonym_file,
                                False,
                                options.prefix,
                                os.path.join(options.output_dir, 'validate_type_material'))
                                
        v.validate_type_species(output_taxonomy,
                                options.gtdb_metadata_file,
                                options.gtdb_synonym_file,
                                options.genus_classification_ledger,
                                False,
                                options.prefix,
                                os.path.join(options.output_dir, 'validate_type_material'))

        self.logger.info('Done.')
                        
    def ncbi_species(self, options):
        """Report differences between GTDB and NCBI species names."""

        check_file_exists(options.input_taxonomy)
        check_file_exists(options.gtdb_metadata_file)
        make_sure_path_exists(options.output_dir)
        
        validate = ValidateSpeciesNames()
        validate.run(options.input_taxonomy,
                        options.gtdb_metadata_file, 
                        options.output_dir)
                        
        self.logger.info('Done.')
                        
    def gtdb_cluster_ncbi(self, options):
        """Report NCBI species within each GTDB-defined cluster."""

        check_file_exists(options.input_taxonomy)
        check_file_exists(options.gtdb_metadata_file)
        make_sure_path_exists(options.output_dir)
        
        validate = ValidateClustersNCBI()
        validate.run(options.input_taxonomy,
                        options.gtdb_metadata_file,
                        options.output_dir)
                        
        self.logger.info('Done.')
        
    def suffix_table(self, options):
        """Create table indicating last polyphyly suffix used for each taxon."""
        
        s = SuffixTable()
        s.run(options.input_taxonomy, options.output_table)
    
        self.logger.info('Done.')
        
    def add_dummy(self, options):
        """Add a zero branch length sister node to each current leaf node."""
        
        check_file_exists(options.input_tree)
        
        self.logger.info('Reading input tree.')
        tree = dendropy.Tree.get_from_path(options.input_tree, 
                                            schema='newick', 
                                            rooting='force-rooted', 
                                            preserve_underscores=True)
        self.logger.info(' ...identified {} leaf nodes.'.format(sum([1 for leaf in tree.leaf_node_iter()])))
        
        # create zero branch length sister node to each leaf node
        self.logger.info('Adding dummy leaf nodes to tree.')
        for leaf in tree.leaf_node_iter():
            gid = leaf.taxon.label
            
            leaf.label = None
            leaf.taxon = None
            leaf.new_child(label = gid,
                            edge_length = 0.0)
            leaf.new_child(label = 'D-' + gid,
                            edge_length = 0.0)

        # write new tree to file
        self.logger.info('Writing modified tree to: {}'.format(options.output_tree))
        tree.write_to_path(options.output_tree, 
                            schema='newick', 
                            suppress_rooting=True,
                            suppress_leaf_node_labels=False,
                            unquoted_underscores=True)

                        
        self.logger.info('Done.')
        
    def remove_dummy(self, options):
        """Remove dummy nodes from curation tree."""
        
        check_file_exists(options.input_tree)
        
        self.logger.info('Reading input tree.')
        tree = dendropy.Tree.get_from_path(options.input_tree, 
                                            schema='newick', 
                                            rooting='force-rooted', 
                                            preserve_underscores=True)
        self.logger.info(' ...identified {} leaf nodes.'.format(sum([1 for leaf in tree.leaf_node_iter()])))
        
        # find dummy nodes in tree
        self.logger.info('Identifying dummy nodes to prune.')
        dummy_nodes = set()
        for leaf in tree.leaf_node_iter():
            if leaf.taxon.label.startswith('D-'):
                dummy_nodes.add(leaf.taxon)
          
        self.logger.info('Identified %d dummy nodes to prune from tree.' % len(dummy_nodes))
        
        # prune tree
        self.logger.info('Pruning tree.')
        tree.prune_taxa(dummy_nodes)

        # write new tree to file
        self.logger.info('Writing modified tree to: {}'.format(options.output_tree))
        tree.write_to_path(options.output_tree, 
                            schema='newick', 
                            suppress_rooting=True,
                            suppress_leaf_node_labels=False,
                            unquoted_underscores=True)

                        
        self.logger.info('Done.')
 
    def parse_options(self, options):
        """Parse user options and call the correct pipeline(s)"""

        logging.basicConfig(format='', level=logging.INFO)

        if options.subparser_name == 'check_file':
            self.check_file(options)
        elif(options.subparser_name == 'check_tree'):
            self.check_tree(options)
        elif(options.subparser_name == 'check_suffix'):
            self.check_suffix(options)
        elif(options.subparser_name == 'check_spelling'):
            self.check_spelling(options)
        elif(options.subparser_name == 'check_distrib'):
            self.check_distrib(options)
            red_check
        elif options.subparser_name == 'red_check':
            self.red_check(options)
        elif options.subparser_name == 'missing_genera':
            self.missing_genera(options)
        elif options.subparser_name == 'merge_genera':
            self.merge_genera(options)
        elif options.subparser_name == 'support':
            self.support(options)
        elif options.subparser_name == 'tax_diff':
            self.tax_diff(options)
        elif(options.subparser_name == 'tree_diff'):
            self.tree_diff(options)
        elif(options.subparser_name == 'retired_taxa'):
            self.retired_taxa(options)
        elif(options.subparser_name == 'branch_len'):
            self.branch_len(options)
        elif options.subparser_name == 'ncbi_tax_diff':
            self.ncbi_tax_diff(options)
        elif options.subparser_name == 'check_generic':
            self.check_generic(options)
        elif options.subparser_name == 'check_specific':
            self.check_specific(options)
        elif options.subparser_name == 'species_clusters':
            self.species_clusters(options)
        elif options.subparser_name == 'type_strains':
            self.type_strains(options)
        elif options.subparser_name == 'type_species':
            self.type_species(options)
        elif options.subparser_name == 'val_table':
            self.val_table(options)
        elif options.subparser_name == 'backfill':
            self.backfill(options)
        elif options.subparser_name == 'ncbi_species':
            self.ncbi_species(options)
        elif options.subparser_name == 'gtdb_cluster_ncbi':
            self.gtdb_cluster_ncbi(options)
        elif options.subparser_name == 'suffix_table':
            self.suffix_table(options)
        elif options.subparser_name == 'add_dummy':
            self.add_dummy(options)
        elif options.subparser_name == 'remove_dummy':
            self.remove_dummy(options)
        else:
            self.logger.error('Unknown command: ' + options.subparser_name + '\n')
            sys.exit()

        return 0
