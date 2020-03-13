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
from fuzzywuzzy import fuzz
from fuzzywuzzy import process



class SpellChecker():
    
    def __init__(self):
        pass
        self.rks_dict = {'d':"Domain",'p':"Phylum",'c':"Class",'o':"Order",'f':"Family",'g':"Genus"}
        self.rks = ['d','p','c','o','f','g']
    
    def spell_check(self,t1,t2,dist,outfile):
        gtax_dict = {}
        with open(t1) as gtax:
            for line in gtax:
                genome_info = line.strip().split("\t")
                ranks = [t.strip() for t in genome_info[1].split(";")]
                rankscleaned =[]
                for rank in ranks:
                    rankscleaned.append("_".join(rank.split("_", 3)[:3]))
                if ranks[1]!="p__":
                    gtax_dict[genome_info[0]]={"d":rankscleaned[0],"p":rankscleaned[1],"c":rankscleaned[2],"o":rankscleaned[3],"f":rankscleaned[4],"g":rankscleaned[5]}
                    
        ncbi_dict = {}
        with open(t2) as ntax:
            for line in ntax:
                genome_info = line.strip().split("\t")
                ranks = [t.strip() for t in genome_info[1].split(";")]
                rankscleaned =[]
                for rank in ranks:
                    rankscleaned.append("_".join(rank.split("_", 3)[:3]))
                
                if genome_info[0] in gtax_dict:
                    ncbi_dict[genome_info[0]]={"d":rankscleaned[0],"p":rankscleaned[1],"c":rankscleaned[2],"o":rankscleaned[3],"f":rankscleaned[4],"g":rankscleaned[5]}
                    
        summary = open(outfile,"w")
        
        for rk in self.rks:
            summary.write("Check {0} rank....\n".format(self.rks_dict.get(rk)))
            ncbirank = []
            gtdbrank = []       
            for k,v in ncbi_dict.items():
                ncbirank.append(v.get(rk))
                gtdbrank.append(gtax_dict.get(k).get(rk))
                
            ncbiset = set(ncbirank)
            gtdbset = set(gtdbrank)
            
            for nc in ncbiset:
                for gt in gtdbset:
                    if fuzz.ratio(nc,gt) < 100 and fuzz.ratio(nc,gt) > dist:
                        summary.write("{0}/{1} score: {2}\n".format(nc,gt,fuzz.ratio(nc,gt)))
                        
        summary.close()

