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

class Visualisation():
    
    def __init__(self):
        """"Initialize"""
        self.logger = logging.getLogger()
        
    def check_change(self, old_taxonomy, new_taxonomy, output_directory):
        
        for dom in ["d__Archaea","d__Bacteria"]:
            tempdict = {} #temporary dictionary for the information in old taxonomy
            olddict = {}
            newdict = {}
            mapdict = {}# dictionary of uba_mappings
            completeold ={}
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
                    completeold[gene_id]={"d":ranks[0],"p":ranks[1],"c":ranks[2],"o":ranks[3],"f":ranks[4],"g":ranks[5],"s":ranks[6],'full':genome_info[1]}
                    #go over genes starting with GCA of GCF in the old tax
                    if gene_id.startswith("GC"):
                        #compare with GCA or GCF in new tax
                        if gene_id in tempdict:
                            intersection+=1
                            newdict[gene_id] = tempdict.get(gene_id)
                            olddict[gene_id]={"d":ranks[0],"p":ranks[1],"c":ranks[2],"o":ranks[3],"f":ranks[4],"g":ranks[5],"s":ranks[6],'full':genome_info[1]}
                        #compare with U_ id in new tax
                        else:
                            if gene_id in mapdict:
                                other_id = mapdict.get(gene_id)
                                if other_id in tempdict:
                                    intersection+=1
                                    newdict[gene_id] = tempdict.get(other_id)
                                    olddict[gene_id]={"d":ranks[0],"p":ranks[1],"c":ranks[2],"o":ranks[3],"f":ranks[4],"g":ranks[5],"s":ranks[6],'full':genome_info[1]}
                    else:#go over genes starting with U_ in old tax
                        #compare with GCF or GCA ids in new tax
                        if gene_id in mapdict:
                            other_id = mapdict.get(gene_id)
                            if other_id in tempdict: 
                                intersection+=1
                                newdict[gene_id] = tempdict.get(other_id)
                                olddict[gene_id]={"d":ranks[0],"p":ranks[1],"c":ranks[2],"o":ranks[3],"f":ranks[4],"g":ranks[5],"s":ranks[6],'full':genome_info[1]}
                        else:#compare with U_ ids in new tax
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
            
            
            print("- Analysis of phyla")
            self.run_change(olddict,newdict,"p",os.path.join(output_directory,pref+"_phylum_difference_evaluation.tsv"),"phylum",completeold)
            print("- Analysis of classes")
            self.run_change(olddict,newdict,"c",os.path.join(output_directory,pref+"_class_difference_evaluation.tsv"),"class",completeold)
            print("- Analysis of orders")
            self.run_change(olddict,newdict,"o",os.path.join(output_directory,pref+"_order_difference_evualuation.tsv"),"order",completeold)
            print("- Analysis of families")
            self.run_change(olddict,newdict,"f",os.path.join(output_directory,pref+"_family_difference_evaluation.tsv"),"family",completeold)
            print("- Analysis of genera")
            self.run_change(olddict,newdict,"g",os.path.join(output_directory,pref+"_genus_difference_evaluation.tsv"),"genus",completeold)

    def run_change(self, olddict, newdict, rank, outfile, ref, complete_old):
        
        different_ranks = []
        conserved_ranks=[]
        tax1_ranks=[]
        tax2_ranks=[]
        full_old={}
        #take the different ranks in the dictionaries and then count the appearances of each pair
        #of ranks ie. ((p__Fusobacteria, p_Fusobacteriota),200)
        for k,v in newdict.items():
            tax2_ranks.append(v.get(rank))
            if k in olddict:
                tax1_ranks.append(olddict.get(k).get(rank))
                if olddict.get(k).get(rank) != v.get(rank) and olddict.get(k).get(rank)!=rank+'__' and v.get(rank)!=rank+'__': 
                    different_ranks.append((olddict.get(k).get(rank),v.get(rank)))
                    if rank=='c':
                        full_old[olddict.get(k).get(rank)]=(olddict.get(k).get('p'))
                    elif rank =='o':
                        full_old[olddict.get(k).get(rank)]=[olddict.get(k).get('p'), olddict.get(k).get('c')]
                    elif rank=='f':
                        full_old[olddict.get(k).get(rank)]=[olddict.get(k).get('p'), olddict.get(k).get('c'),olddict.get(k).get('o')]
                    elif rank=='g':
                        full_old[olddict.get(k).get(rank)]=[olddict.get(k).get('p'), olddict.get(k).get('c'),olddict.get(k).get('o'),olddict.get(k).get('f')]
                elif olddict.get(k).get(rank) == v.get(rank):
                    conserved_ranks.append((olddict.get(k).get(rank),v.get(rank)))
        
        tax1_counter = Counter(tax1_ranks).most_common()
        tax2_counter = Counter(tax2_ranks).most_common()
        order_counter =  Counter(different_ranks).most_common()
        conserved_counter = Counter(conserved_ranks).most_common()
        #print(order_counter)
        """assign change evaluations to all pairs of rank name changes"""
        assigndict={}
        for v in complete_old.values():
            for item in order_counter:
                #check change placeholder to placeholder, invalid name, valid name
                if self.isPlaceholder(item[0][0]) and item[0]not in assigndict:
                    if self.isPlaceholder(item[0][1]):
                        assigndict[item[0]]="Modified placeholder name"
                    elif item[0][1]==v.get(rank):
                        assigndict[item[0]]="Changed placeholder to taxa seen before"
                #check change name to placeholder, invalid name, valid name
                elif (not self.isPlaceholder(item[0][0])) and item[0]not in assigndict:
                    if self.isPlaceholder(item[0][1]):
                        assigndict[item[0]]="Changed to placeholder"
                    elif item[0][1]==v.get(rank):
                        assigndict[item[0]]="BAD"
        for item in order_counter:
            if item[0] not in assigndict:
                assigndict[item[0]]="OK"
 
            
        outf= open(outfile, 'w')
        outf.write("Previous Taxonomy\tPrevious {0}\tNew {0}\tChange Evaluation\tChanged total\tTotal in previous\tTotal in new\tConserved Total\n".format(ref))
        for item in order_counter:
            prev=item[0][0]
            new=item[0][1]
            c_eval=assigndict.get(item[0])
            changed_g=item[1]
            nber_conserved=0
            prev_tax=''
            if full_old.get(prev):
                for item in full_old.get(prev):
                    prev_tax = prev_tax+item+";"
            prev_tax= prev_tax[0:-2]
            #prev_tax = full_old.get(prev)
            for item in tax1_counter:
                if item[0]==prev:
                    nber_tax1=item[1]
            for item in tax2_counter:
                if item[0]==new:
                    nber_tax2=item[1]
            for item in conserved_counter:
                if item[0][0]==prev:
                    nber_conserved=item[1]
            
            outf.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\n".format(prev_tax,prev,new,c_eval,changed_g,nber_tax1,nber_tax2,nber_conserved))
        outf.close()
    def isPlaceholder(self, inputString):
        """check whether a taxonomy name has a number
        (likely a placeholder name)"""
        return any(char.isdigit() for char in inputString)
