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

from biolib.newick import parse_label
from biolib.taxonomy import Taxonomy
import dendropy

class TaxDiff():
    """Tabulate differences between two taxonomies.
    
    Every taxon label in the first taxonomy is classified
    to indicate how it has changed relative to the
    second taxonomy.
    
    This implies that every label in the first taxonomy is
    given precisely one label and that labels in the second 
    taxonomy may often be seen simply as deprecated. 
    
    Taxon are classified as follows in the order listed:
    
    retained: the exact same taxon label is in the GTDB and NCBI taxonomies
    corrected: only the suffix of the taxon has changed
    more specific: taxon has been moved down 1 or more ranks (e.g., phylum to class)
    more general: taxon has been moved up 1 or more ranks (e.g., class to phylum)
    new: the label has been introduced by the GTDB taxonomy
    deprecated: the label has been removed in the GTDB taxonomy
    
    E.g.,
    The first taxonomy has the label o__Archaeoglobales,
    but no label c__Archaeoglobi. The second taxonomy has
    the labels c__Archaeoglobi and o__Archaeoglobales. AssertionError
    such, o__Archaeoglobales will be classified as retained
    while c__Archaeoglobi will be classified as deprecated
    (and not 'more specific').
    """

    def __init__(self, dpi=96):
        """Initialize."""
        self.logger = logging.getLogger()
        
        # c__Halobacteria => o__Halobacteriales
        # c__Hadesarchaea => c__Hadesarchaeia
        # c__Archaeoglobi => o__Archaeoglobales
        
        # p__Pacearchaeota => f__Pacearchaeaceae
        
        # domain = 'a', phylum = 'aeota', class = 'ia', order = 'ales', family = 'aceae'
        self.rank_suffices = ['a', 'aeota', 'ia', 'ales', 'aceae', '']
        
    def _renamed(self, taxon, cur_rank, taxa_at_rank):
        """Determine if taxon has been renamed."""
        
        # remove paraphyletic suffix if one exists
        taxon = taxon[0:3] + taxon[3:].split('_')[0]
        
        # determine order of ranks to examine in order
        # to first identify 'more specific' and then
        # 'more general' label changes
        rank_order = [r for r in range(cur_rank-1, -1, -1)]
        rank_order += [r for r in range(cur_rank+1, len(Taxonomy.rank_prefixes))]
     
        # check if taxon has been moved up or down in rank
        # as determined by removing suffix characters and 
        # appending canonical rank prefixes
        for old_rank in rank_order:
            if old_rank >= len(self.rank_suffices):
                return None, None

            # eat suffix character by character and append canonical suffix
            old_rank_prefix = Taxonomy.rank_prefixes[old_rank]
            cur_suffix = self.rank_suffices[cur_rank]
            old_suffix = self.rank_suffices[old_rank]
            for i in range(1, max([len(s) for s in self.rank_suffices]) + 1): # eat taxon name
                if i == 0:
                    modified_taxon = taxon[3:]
                else:
                    modified_taxon = taxon[3:-i]
                    
                for j in range(0, len(old_suffix)): # eat suffix
                    old_taxon = old_rank_prefix + modified_taxon + old_suffix[j:]
                    if old_taxon in taxa_at_rank[old_rank]:
                        return old_taxon, old_rank
                        
                    old_taxon = old_rank_prefix + modified_taxon + old_suffix[0:j]
                    if old_taxon in taxa_at_rank[old_rank]:
                        return old_taxon, old_rank
        
        return None, None
        
    def _change_suffix(self, taxon, cur_rank, taxa_at_rank):
        """Change suffix of taxon."""
        
        # check if taxon name has been corrected
        for old_rank, old_suffix in enumerate(self.rank_suffices):
            # eat suffix character by character and append canonical suffix
            for i in range(0, max([len(s) for s in self.rank_suffices])): # eat taxon name
                if i == 0:
                    modified_taxon = taxon
                else:
                    modified_taxon = taxon[0:-i]
                    
                for j in range(0, len(old_suffix)): # eat suffix
                    old_taxon = modified_taxon + old_suffix[j:]
                    if old_taxon in taxa_at_rank[cur_rank]:
                        return old_taxon
  
                    old_taxon = modified_taxon + old_suffix[0:j]
                    if old_taxon in taxa_at_rank[cur_rank]:
                        return old_taxon
                        
        return None
        
    def _tax_diff_table(self, tax1, tax2, output_table):
        """Tabulate incongruency of taxonomy strings at each rank."""
        
        fout = open(output_table, 'w')
        fout.write('Lineage\tNo. Extent Taxa')
        for rank_label in Taxonomy.rank_labels:
            fout.write('\t%s (%%)' % rank_label.title())
        fout.write('\n')
        
        taxonomy = Taxonomy()
        named_lineages_at_rank = taxonomy.named_lineages_at_rank(tax1)
        for rank, taxa in named_lineages_at_rank.items():
            rank_label = Taxonomy.rank_labels[rank]
            if rank_label == 'species':
                continue
                
            extant_taxa_for_rank = taxonomy.extant_taxa_for_rank(rank_label, tax1)
            
            for taxon in taxa:
                extent_taxa = extant_taxa_for_rank[taxon]
                fout.write('%s\t%d' % (taxon, len(extent_taxa)))
                
                row = defaultdict(list)
                for genome_id in extent_taxa:
                    taxa1 = tax1[genome_id]
                    taxa2 = tax2[genome_id]
                    
                    for cur_rank, (taxa1, taxa2) in enumerate(zip(taxa1, taxa2)):
                         row[cur_rank].append(taxa1 == taxa2)
                         
                for cur_rank, matches in row.items():
                    if cur_rank <= rank:
                        fout.write('\t-')
                    else:
                        perc_match = sum(matches) * 100.0 / len(matches)
                        fout.write('\t%.1f' % (100.0 - perc_match))
                fout.write('\n')
        fout.close()
        
    def tree_tax_diff(self, tree1_file, tree2_file, output_dir):
        """Tabulate differences between two taxonomies on a tree.
        
        Parameters
        ----------
        tree1_file : str
            File with tree in Newick format.
        tree2_file : str
            File with tree in Newick format.
        output_dir : str
            Output directory.
        """
        
        tree1 = dendropy.Tree.get_from_path(tree1_file, 
                                            schema='newick', 
                                            rooting='force-rooted', 
                                            preserve_underscores=True)
                                            
        tree2 = dendropy.Tree.get_from_path(tree2_file, 
                                            schema='newick', 
                                            rooting='force-rooted', 
                                            preserve_underscores=True)
        
        # prune both trees to a set of common taxa
        taxa1 = set()
        for t in tree1.leaf_node_iter():
            taxa1.add(t.taxon.label)
            
        taxa2 = set()
        for t in tree2.leaf_node_iter():
            taxa2.add(t.taxon.label)
            
        taxa_in_common = taxa1.intersection(taxa2)
        self.logger.info('Tree 1 contains %d taxa.' % len(taxa1))
        self.logger.info('Tree 2 contains %d taxa.' % len(taxa2))
        self.logger.info('Pruning trees to the %d taxa in common.' % len(taxa_in_common))
        
        tree1.retain_taxa_with_labels(taxa_in_common)
        tree2.retain_taxa_with_labels(taxa_in_common)
        
        # get named lineages at each taxonomic rank
        taxonomy = Taxonomy()
        tax1 = taxonomy.read_from_tree(tree1)
        tax2 = taxonomy.read_from_tree(tree2)
        
        taxa_at_rank1 = taxonomy.named_lineages_at_rank(tax1)
        taxa_at_rank2 = taxonomy.named_lineages_at_rank(tax2)

        # identify retained taxonomic names
        tax_file_name = os.path.splitext(os.path.basename(tree1_file))[0]
        output_file = os.path.join(output_dir, '%s.taxa_diff.tsv' % tax_file_name)
        fout = open(output_file, 'w')
        fout.write('Rank\tClassification\tTaxonomy 1\tTaxonomy 2\n')
        taxon2_accounted_for = defaultdict(set)
        for rank, rank_label in enumerate(Taxonomy.rank_labels[0:-1]):
            for taxon in taxa_at_rank1[rank]: 
                # check if taxon has been retained
                if taxon in taxa_at_rank2[rank]:
                    fout.write('%s\t%s\t%s\t%s\n' % (rank_label, 'retained', taxon, taxon))
                    taxon2_accounted_for[rank].add(taxon)
                    continue
                    
                # check if name was simply corrected by changing suffix
                old_taxon = self._change_suffix(taxon, rank, taxa_at_rank2)  
                if old_taxon:
                    fout.write('%s\t%s\t%s\t%s\n' % (rank_label, 'corrected', taxon, old_taxon))
                    taxon2_accounted_for[rank].add(old_taxon)
                    continue
                                         
                # check if taxon has been moved up or down in rank
                old_taxon, old_rank = self._renamed(taxon, rank, taxa_at_rank2)
                if old_taxon:
                    if rank < old_rank:
                        fout.write('%s\t%s\t%s\t%s\n' % (rank_label, 'more general', taxon, old_taxon))
                    elif rank == old_rank:
                        fout.write('%s\t%s\t%s\t%s\n' % (rank_label, 'corrected', taxon, old_taxon))
                    else:
                        fout.write('%s\t%s\t%s\t%s\n' % (rank_label, 'more specific', taxon, old_taxon))
                    
                    taxon2_accounted_for[old_rank].add(old_taxon)   
                    continue
                          
                # otherwise, the taxon appears to be new
                fout.write('%s\t%s\t%s\t%s\n' % (rank_label, 'new', taxon, 'NA'))
               
        # report deprecated taxa
        for rank, rank_label in enumerate(Taxonomy.rank_labels[0:-1]):
            for taxon in taxa_at_rank2[rank]:
                if taxon not in taxon2_accounted_for[rank]:
                    fout.write('%s\t%s\t%s\t%s\n' % (rank_label, 'deprecated', 'NA', taxon))

        fout.close()
        
        # tabulate congruence of taxonomy strings
        output_table = os.path.join(output_dir, '%s.perc_diff.tsv' % tax_file_name)
        self._tax_diff_table(tax1, tax2, output_table)
        
    def _read_type_material(self, gtdb_metadata_file):
        """Read type material metadata."""
        
        metadata = {}
        with open(gtdb_metadata_file) as f:
            header = f.readline().strip().split('\t')
            
            gtdb_type_material_index = header.index('gtdb_type_material')
            gtdb_type_material_sources_index = header.index('gtdb_type_material_sources')

            for line in f:
                line_split = line.strip().split('\t')
                
                gid = line_split[0]

                gtdb_type_material = line_split[gtdb_type_material_index]
                gtdb_type_material_sources = line_split[gtdb_type_material_sources_index]
                
                metadata[gid] = [gtdb_type_material, gtdb_type_material_sources]
                
        return metadata
    
    def tax_diff(self, tax1_file, tax2_file, gtdb_metadata_file, output_dir):
        """Tabulate differences between two taxonomies.
        
        Parameters
        ----------
        tax1_file : str
            First taxonomy file.
        tax2_file : str
            Second taxonomy file.
        output_dir : str
            Output directory.
        """
        
        gtdb_metadata = None
        if gtdb_metadata_file:
            gtdb_metadata = self._read_type_material(gtdb_metadata_file)

        tax1 = Taxonomy().read(tax1_file)
        tax2 = Taxonomy().read(tax2_file)
        common_taxa = set(tax1.keys()).intersection(tax2.keys())
        
        self.logger.info('First taxonomy contains %d taxa.' % len(tax1))
        self.logger.info('Second taxonomy contains %d taxa.' % len(tax2))
        self.logger.info('Taxonomies have %d taxa in common.' % len(common_taxa))
        
        # identify differences between taxonomies
        tax_file_name1 = os.path.splitext(os.path.basename(tax1_file))[0]
        tax_file_name2 = os.path.splitext(os.path.basename(tax2_file))[0]
        output_table = os.path.join(output_dir, 'classification_table.tsv')
        
        fout = open(output_table, 'w')
        fout.write('Genome ID\tChange\tRank\t%s\t%s' % (tax_file_name1, tax_file_name2))
        if gtdb_metadata:
            fout.write('\tType material\tType material sources')
        fout.write('\n')
        
        unchanged = defaultdict(int)           # T2 = g__Bob -> T1 = g__Bob, or T2 = g__ -> T1 = g__
        active_change = defaultdict(int)       # T2 = g__Bob -> T1 = g__Jane, or T2 = g__Bob -> T1 = g__Bob_A
        passive_change = defaultdict(int)      # T2 = g__??? -> T1 = g__Jane
        unresolved_change = defaultdict(int)   # T2 = g__Box -> T1 = g__???
        for taxa in common_taxa:
            t1 = tax1[taxa]
            t2 = tax2[taxa]
            
            for rank, (taxon1, taxon2) in enumerate(zip(t1, t2)):
                bChange = False
                if taxon1 == taxon2:
                    unchanged[rank] += 1
                elif taxon1 != Taxonomy.rank_prefixes[rank] and taxon2 != Taxonomy.rank_prefixes[rank]:
                    active_change[rank] += 1
                    fout.write('%s\t%s\t%s\t%s\t%s' % (taxa, 'active', Taxonomy.rank_labels[rank], ';'.join(t1), ';'.join(t2)))
                    bChange = True
                elif taxon2 == Taxonomy.rank_prefixes[rank]:
                    passive_change[rank] += 1
                    fout.write('%s\t%s\t%s\t%s\t%s' % (taxa, 'passive', Taxonomy.rank_labels[rank], ';'.join(t1), ';'.join(t2)))
                    bChange = True
                elif taxon1 == Taxonomy.rank_prefixes[rank]:
                    unresolved_change[rank] += 1
                    fout.write('%s\t%s\t%s\t%s\t%s' % (taxa, 'unresolved', Taxonomy.rank_labels[rank], ';'.join(t1), ';'.join(t2)))
                    bChange = True
                
                if bChange:
                    if gtdb_metadata:
                        fout.write('\t%s\t%s' % (gtdb_metadata[taxa][0], gtdb_metadata[taxa][1]))
                    fout.write('\n')
                    
        fout.close()
  
        # report results
        output_table = os.path.join(output_dir, 'classification_summary_table.tsv')
        
        fout = open(output_table, 'w')
        fout.write('Rank\tUnchanged\tUnchanged (%)\tActive\t Active (%)\tPassive\tPassive (%)\tUnresolved\tUnresolved (%)\n')
        print('')
        print('Rank\tUnchanged\tActive\tPassive\tUnresolved\tTotal')
        for rank in range(0, len(Taxonomy.rank_prefixes)):
            total = unchanged[rank] + active_change[rank] + passive_change[rank] + unresolved_change[rank]
            if total != 0:
                fout.write('%s\t%d\t%.1f\t%d\t%.1f\t%d\t%.1f\t%d\t%.1f\n' %
                                    (Taxonomy.rank_labels[rank],
                                    unchanged[rank], unchanged[rank] * 100.0 / total,
                                    active_change[rank], active_change[rank] * 100.0 / total,
                                    passive_change[rank], passive_change[rank] * 100.0 / total,
                                    unresolved_change[rank], unresolved_change[rank] * 100.0 / total))
                print('%s\t%d\t%d\t%d\t%d\t%d' % (Taxonomy.rank_labels[rank],
                                                    unchanged[rank],
                                                    active_change[rank],
                                                    passive_change[rank],
                                                    unresolved_change[rank],
                                                    total))
        print('')
        
    def ncbi_tax_diff(self, 
                        prev_ncbi_tax_file, 
                        cur_ncbi_tax_file, 
                        gtdb_tax_file,
                        gtdb_metadata_file,
                        output_dir):
        """Establish changes in NCBI taxonomy that may impact GTDB taxonomy.
        
        Parameters
        ----------
        prev_ncbi_tax_file : str
            Previous NCBI taxonomy file.
        cur_ncbi_tax_file : str
            Current NCBI taxonomy file.
        gtdb_tax_file
            GTDB taxonomy file.
        output_dir : str
            Output directory.
        """
        
        # get type material metadata
        type_material = {}
        with open(gtdb_metadata_file) as f:
                header = f.readline().strip().split('\t')
                
                gtdb_type_material_index = header.index('gtdb_type_material')
                gtdb_type_material_sources_index = header.index('gtdb_type_material_sources')

                for line in f:
                    line_split = line.strip().split('\t')
                    
                    gid = line_split[0]
                    gtdb_type_material = line_split[gtdb_type_material_index]
                    if gtdb_type_material.lower() == 't' or gtdb_type_material.lower() == 'true':
                        gtdb_type_material_sources = line_split[gtdb_type_material_sources_index]
                        type_material[gid] = gtdb_type_material_sources
                    
        # identify differences in NCBI taxonomies
        prev_ncbi = Taxonomy().read(prev_ncbi_tax_file)
        cur_ncbi = Taxonomy().read(cur_ncbi_tax_file)
        gtdb = Taxonomy().read(gtdb_tax_file)
        
        fout = open(os.path.join(output_dir, 'ncbi_tax_diff.tsv'), 'w')
        fout.write('Genome ID\tPrevious NCBI taxonomy\tCurrent NCBI taxonomy\tHighest modified rank')
        fout.write('\tGTDB taxonomy\tImpact GTDB taxonomy\tGTDB type material\n')
        for gid in set(prev_ncbi).intersection(cur_ncbi):
            for r, rank_label in enumerate(Taxonomy.rank_labels):
                prev_taxon = prev_ncbi[gid][r]
                cur_taxon = cur_ncbi[gid][r]
                if cur_taxon != prev_taxon:
                    fout.write('%s\t%s\t%s\t%s' % (gid, 
                                                    '; '.join(prev_ncbi[gid]), 
                                                    '; '.join(cur_ncbi[gid]), 
                                                    rank_label))
                    
                    gtdb_id = gid
                    if gtdb_id.startswith('GCA_'):
                        gtdb_id = 'GB_' + gtdb_id
                    elif gtdb_id.startswith('GCF_'):
                        gtdb_id= 'RS_' + gtdb_id
                        
                    if gtdb_id in gtdb:
                        if gtdb[gtdb_id][r] == prev_taxon:
                            fout.write('\t%s\tTRUE' % '; '.join(gtdb[gtdb_id]))
                        else:
                            fout.write('\t%s\tFALSE' % '; '.join(gtdb[gtdb_id]))
                    else:
                        fout.write('\t-\tFALSE')
                        
                    fout.write('\t%s' % type_material.get(gtdb_id, '-'))
                    fout.write('\n')
                    break

    def check_distrib(self,old_taxonomy,new_taxonomy,output_directory, keep_no_change, keep_placeholder_name, top_change):
   
        gtogfile = open(os.path.join(output_directory,'genomes_summary.tsv'),"w")
        gtogfile.write("genome_id\tfirst_taxonomy\tsecond_taxonomy\tstatus\n")
        for dom in ["d__Archaea","d__Bacteria"]:
            tempdict = {} #temporary dictionary for the information in old taxonomy
            olddict = {}
            newdict = {}
            mapdict = {}# dictionary of uba_mappings
            oldnumber = 0 #number of genes in old_tax
            newnumber=0 #number of genes in new_tax
            intersection=0 #number of genes common to both taxonomies
            
            with open("uba_mapping/uba_mapping_v2.tsv", "r") as tax_map:
                for line in tax_map:
                    genes_id =line.strip().split("\t")
                    #IDs that start with U_
                    u_id = genes_id[0]
                    #IDs that start with GCA or GCF
                    gc_id = genes_id[2]
                    #delete GB or RS prefix to ensure id-consistency
                    if gc_id.startswith("GB") or gc_id.startswith("RS"):
                        gc_id = gc_id[3:]
                    #map k, v of all id_mappings
                    mapdict[gc_id]= u_id
                    mapdict[u_id]= gc_id
              
            with open(new_taxonomy) as taxnew:
                for line in taxnew:
                    newnumber+=1
                    genome_info = line.strip().split("\t")
                    gene_id = genome_info[0]
                    ranks = genome_info[1].split(";")
                    if gene_id.startswith("GB") or gene_id.startswith("RS"):
                        gene_id = gene_id[3:]
                    if gene_id.startswith("GC") or (gene_id.startswith("U") and gene_id in mapdict):
                        #temporary dictionary of IDs of interest in new_taxonomy
                        tempdict[gene_id]={"d":ranks[0],"p":ranks[1],"c":ranks[2],"o":ranks[3],"f":ranks[4],"g":ranks[5],"s":ranks[6],'full':genome_info[1]}
                        if tempdict.get(gene_id).get("d") != dom:
                            tempdict.pop(gene_id)
                        
            with open(old_taxonomy) as taxold:
                for line in taxold:
                    oldnumber+=1
                    genome_info = line.strip().split("\t")
                    gene_id = genome_info[0]
                    ranks = genome_info[1].split(";")
                    if gene_id.startswith("GB") or gene_id.startswith("RS"):
                        gene_id = gene_id[3:]
                    if gene_id.startswith("GC"):
                        if gene_id in tempdict:
                            intersection+=1
                            newdict[gene_id] = tempdict.get(gene_id)
                            olddict[gene_id]={"d":ranks[0],"p":ranks[1],"c":ranks[2],"o":ranks[3],"f":ranks[4],"g":ranks[5],"s":ranks[6],'full':genome_info[1]}
                        else:
                            if gene_id in mapdict:
                                other_id = mapdict.get(gene_id)
                                if other_id in tempdict:
                                    intersection+=1
                                    newdict[gene_id] = tempdict.get(other_id)
                                    olddict[gene_id]={"d":ranks[0],"p":ranks[1],"c":ranks[2],"o":ranks[3],"f":ranks[4],"g":ranks[5],"s":ranks[6],'full':genome_info[1]}
                    else:
                        if gene_id in mapdict:
                            other_id = mapdict.get(gene_id)
                            if other_id in tempdict: 
                                intersection+=1
                                newdict[gene_id] = tempdict.get(other_id)
                                olddict[gene_id]={"d":ranks[0],"p":ranks[1],"c":ranks[2],"o":ranks[3],"f":ranks[4],"g":ranks[5],"s":ranks[6],'full':genome_info[1]}
                        else:
                            if gene_id in tempdict:
                                intersection+=1
                                newdict[gene_id] = tempdict.get(gene_id)
                                olddict[gene_id]={"d":ranks[0],"p":ranks[1],"c":ranks[2],"o":ranks[3],"f":ranks[4],"g":ranks[5],"s":ranks[6],'full':genome_info[1]}

            pref = 'bac'
            if dom == "d__Archaea":
                pref = "arc"

            print("Analysis of {0}").format(dom)
            print("Number of genomes in old taxonomy: {0}").format(oldnumber)
            print("Number of genomes in new taxonomy: {0}").format(newnumber)
            print("Number of genomes present in both taxonomy: {0}").format(intersection)
            print("Number of genomes in new taxonomy, unavailable in old taxonomy: {0}").format(newnumber-intersection)
            print("Number of genomes in old taxonomy, unavailable in new taxonomy: {0}").format(oldnumber-intersection)
            
            self.genomebygenomecompare(olddict,newdict,gtogfile)
                            
            print("- Analysis of phyla")
            self.rundistrib(olddict,newdict,"p",os.path.join(output_directory,pref+"_phylum_difference.tsv"),"phylum",keep_placeholder_name,keep_no_change, top_change)
            print("- Analysis of classes")
            self.rundistrib(olddict,newdict,"c",os.path.join(output_directory,pref+"_class_difference.tsv"),"class",keep_placeholder_name,keep_no_change, top_change)
            print("- Analysis of orders")
            self.rundistrib(olddict,newdict,"o",os.path.join(output_directory,pref+"_order_difference.tsv"),"order",keep_placeholder_name,keep_no_change, top_change)
            print("- Analysis of families")
            self.rundistrib(olddict,newdict,"f",os.path.join(output_directory,pref+"_family_difference.tsv"),"family",keep_placeholder_name,keep_no_change, top_change)
            print("- Analysis of genera")
            self.rundistrib(olddict,newdict,"g",os.path.join(output_directory,pref+"_genus_difference.tsv"),"genus",keep_placeholder_name,keep_no_change, top_change)

        gtogfile.close()
                
    def genomebygenomecompare(self,olddict,newdict,gtogfile):
        orderrank=["domain","phylum","class",'order','family','genus','species']
        for k,v in newdict.items():
            if k in olddict:
                if v.get('full') == olddict.get(k).get('full'):
                    gtogfile.write("{0}\t{1}\t{2}\tidentical\n".format(k,olddict.get(k).get('full'),v.get('full')))
                else:
                    for rk in orderrank:
                        if v.get(rk[0:1]) != olddict.get(k).get(rk[0:1]):
                            gtogfile.write("{0}\t{1}\t{2}\t{3} difference\n".format(k,olddict.get(k).get('full'),v.get('full'),rk))
            else:
                gtogfile.write("{0}\tnot_available\t{1}\t\n".format(k,v.get('full')))
        for k,v in olddict.items():
            if k not in newdict:
                gtogfile.write("{0}\t{1}\tnot_available\t\n".format(k,olddict.get(k).get('full')))
                
    def rundistrib(self,olddict,newdict,rank,outfile,ref, keep_placeholder_name, keep_no_change, top_change):
        orderrank=["d","p","c",'o','f','g','s']
        different_ranks = []
        #take the different ranks in the dictionaries and then count the appearances of each pair
        #of ranks ie. (p__Fusobacteria, p_Fusobacteriota),200
        for k,v in newdict.items():
            if k in olddict:
                different_ranks.append((olddict.get(k).get(rank),v.get(rank)))
        order_counter =  Counter(different_ranks).most_common()
        results_dict = {}
        """create a dictionary with the name of the rank in olddict as key and the number of 
        genomes belonging to that rank encountered, along with different rank names on newdict
        for those genomes and how many times the different names appear."""
        for item in order_counter:
            if item[0][0] in results_dict:
                results_dict[item[0][0]]["nber_g"]= results_dict[item[0][0]]["nber_g"] +item[1]
                results_dict[item[0][0]].get("genomes").append((item[0][1],item[1]))
            else:
                results_dict[item[0][0]]={"nber_g":item[1],"genomes":[(item[0][1],item[1])]}
        
        to_pop =[] #store taxonomies to take out of the file
        for k,v in results_dict.items():
            if top_change==True:
                top_gen= results_dict[k]['genomes'][0][0]
                if top_gen==k:
                    to_pop.append(k)
                else:
                    results_dict[k]['genomes']= [results_dict[k]['genomes'][0]]
            if keep_no_change==True and k==results_dict[k]['genomes'][0][0] and results_dict[k]['nber_g']==results_dict[k]['genomes'][0][1]:
                to_pop.append(k)
            if keep_placeholder_name==True and self.hasNumber(k)==True and results_dict[k]['genomes'][0][0]==rank+"__":
                to_pop.append(k)
            elif keep_placeholder_name==True and self.hasNumber(results_dict[k]['genomes'][0][0])==True and k==rank+"__":
                to_pop.append(k)
        for k in to_pop:
            results_dict.pop(k)
            
        outf = open(outfile,"w")
        outf.write("Previous {0}\tNumber of genomes\tNumber of New {0}\tList of New {0}\n".format(ref))
        for k,v in results_dict.items():
            for sk,sv in olddict.items():
                if sv.get(rank) == k:
                    prankold = sv.get(orderrank[orderrank.index(rank)-1])
                    break
            number_sub = len(v.get("genomes"))
            
            results = []
            
            if len(v.get("genomes"))==1 and v.get("genomes")[0][0] ==k:
                continue
                
            for newg in v.get("genomes"):
                newg_name = newg[0]
                newg_numb = float(newg[1])
                for sk,sv in newdict.items():
                    if sv.get(rank) == newg_name:
                        pranknew = sv.get(orderrank[orderrank.index(rank)-1])
                        break
                res = newg_name
                if prankold != pranknew:
                    res = res + "("+pranknew+")"
                res = "{0} {1}%".format(res,round((newg_numb/v.get("nber_g"))*100,2))
                results.append(res)
            
            outf.write("{0}\t{1}\t{2}\t{3}\n".format(k,v.get("nber_g"),number_sub,", ".join(results)))
        outf.close()
        
    def hasNumber(self, inputString):
        """check whether a taxonomy name has a number
        (likely a placeholder name)"""
        return any(char.isdigit() for char in inputString)
