#!/usr/bin/env python
'''
Classes to parse various aspects of charset, gene and taxon names
'''

#####################
# IMPORT OPERATIONS #
#####################

import GlobalVariables as GlobVars
import sys, os
import requests
import unidecode
import logging

import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from Bio import Entrez

from collections import Counter

try:
    from urllib.request import urlopen
except Exception as e:
    from urllib2 import urlopen

###############
# AUTHOR INFO #
###############

__author__ = 'Michael Gruenstaeudl <m.gruenstaeudl@fu-berlin.de>'
__copyright__ = 'Copyright (C) 2016-2020 Michael Gruenstaeudl'
__info__ = 'annonex2embl'
__version__ = '2020.03.08.1700'

#############
# DEBUGGING #
#############

#import ipdb
#ipdb.set_trace()

# To format warnings in a pretty, readable way:
def warning_on_one_line(message, category, filename, lineno, file=None, line=None):
    return '\n annonex2embl `%s`\n' % (message)
warnings.formatwarning = warning_on_one_line

###########
# CLASSES #
###########

class GetEntrezInfo:
    ''' This class contains functions to obtain gene information from gene
    symbols. '''

    def __init__(self, email_addr):
        self.email_addr = email_addr


    @staticmethod
    def _id_lookup(gene_sym, retmax=10):
        ''' An internal static function to convert a gene symbol to an 
            Entrez ID via ESearch.
        Args:
            gene_sym (str): a gene symbol; example: 'psbI'
        Returns:
            entrez_id_list (list): a list of Entrez IDs; 
                example: ['26835430', '26833718', '26833393', ...]
        '''
#        Examples:
#            Example 1: # Default behaviour
#                >>> gene_sym = 'psbI'
#                >>> _id_lookup(gene_sym)
#                Out: ['26835430', '26833718', '26833393', ...]

        if not gene_sym:
            msg = 'ERROR: No gene symbol detected.'
            warnings.warn(msg)
            raise Exception
        if '_' in gene_sym:
            msg = 'ERROR: Gene symbol `%s` contains an underscore, \
which is not allowed.' % (gene_sym)
            warnings.warn(msg)
            raise Exception
        if not GetEntrezInfo._serverAccessible(GlobVars.esearchUrl):
            msg = 'ERROR: The server %s is currently not \
accessible.' % ('ESearch ('+GlobVars.esearchUrl+')')
            warnings.warn(msg)
            raise Exception

        query_term = gene_sym + ' [sym]'
        try:
            logging.info("Communicating with server %s \
regarding the gene product of `%s`." \
% ('ESearch ('+GlobVars.esearchUrl+')', gene_sym))
            esearch_records = Entrez.esearch(db='gene', term=query_term,
                retmax=retmax, retmod='xml')
        except Exception as e:
            msg = 'ERROR: An error occurred while retrieving \
data from server %s: %s' % ('ESearch ('+GlobVars.esearchUrl+')', e)
            warnings.warn(msg)
            raise Exception(e)
        parsed_records = Entrez.read(esearch_records)
        entrez_id_list = parsed_records['IdList']
        return entrez_id_list


    @staticmethod
    def _gene_product_lookup(entrez_id_list, gene_sym):
        ''' An internal static function to convert a list of Entrez IDs to a
        list of Entrez gene records via EPost and ESummary.
        Args:
            entrez_id_list (list): a list of Entrez IDs; 
                example: ['26835430', '26833718', '26833393', ...]
            gene_sym (string) : string containing symbol of the gene
        Returns:
            entrez_rec_list (list): a list of Entrez gene records
        '''
#        Examples:
#            Example 1: # Default behaviour
#                >>> entrez_id_list = ['26835430', '26833718', '26833393']
#                >>> _record_lookup(entrez_id_list)
#                Out: ???

        if not GetEntrezInfo._serverAccessible(GlobVars.epostUrl):
            msg = 'ERROR: The server %s is currently not \
accessible.' % ('EPost ('+GlobVars.epostUrl+')')
            warnings.warn(msg)
            raise Exception

        if not GetEntrezInfo._serverAccessible(GlobVars.esummaryUrl):
            msg = 'ERROR: The server %s is currently not \
accessible.' % ('ESummary ('+GlobVars.esummaryUrl+')')
            warnings.warn(msg)
            raise Exception

        try:
            logging.info("Communicating with server %s regarding the gene \
product of `%s`." % ('EPost ('+GlobVars.epostUrl+')', gene_sym))
            epost_query = Entrez.epost('gene', id=','.join(entrez_id_list))
            epost_results = Entrez.read(epost_query)
        except Exception as e:
            msg = 'ERROR: An error occurred while retrieving data \
from `%s`: %s' % ('EPost ('+GlobVars.epostUrl+')', e)
            warnings.warn(msg)
            raise Exception(e)
        webenv = epost_results['WebEnv']
        query_key = epost_results['QueryKey']
        try:
            logging.info("Communicating with server %s regarding the gene \
product of `%s`." % ('ESummary ('+GlobVars.esummaryUrl+')', gene_sym))
            esummary_records = Entrez.esummary(db='gene', webenv=webenv,
                query_key=query_key)
        except Exception as e:
            msg = 'An error occurred while retrieving data from \
`%s`: %s' % ('ESummary ('+GlobVars.esummaryUrl+')', e)
            warnings.warn(msg)
            raise Exception(e)
        entrez_rec_list = Entrez.read(esummary_records)
        return entrez_rec_list


    @staticmethod
    def _parse_gene_products(entrez_rec_list):
        ''' An internal static function to parse out relevant 
        information from an ENtrez records list.
        Args:
            entrez_rec_list (list): a list of Entrez gene records
        Returns:
            gene_info_list (list): a list of dictionaries
        '''
#        Examples:
#            Example 1: # Default behaviour
#                >>> entrez_rec_list = []
#                >>> _parse_records(entrez_rec_list)

        try:
            documentSummarySet = entrez_rec_list['DocumentSummarySet']
            docs = documentSummarySet['DocumentSummary']
        except Exception as e:
            msg = 'An error occurred while parsing the data from \
`%s`: %s' % ('ESummary ('+GlobVars.esummaryUrl+')', e)
            warnings.warn(msg)
            raise Exception(e)
        try:
            list_gene_product = [doc['Description'] for doc in docs]
            #list_gene_symbol = [doc['NomenclatureSymbol'] for doc in docs]
            #list_gene_name = [doc['Name'] for doc in docs]
            # Avoiding that spurious first hit biases gene_product:
            gene_product = Counter(list_gene_product).most_common()[0][0]
        except Exception as e:
            msg = 'An error occurred while parsing the gene product \
name: %s' % (e)
            warnings.warn(msg)
            raise Exception(e)
        return gene_product


    @staticmethod
    def _taxname_lookup_ncbi(taxon_name, retmax=1):
        ''' An internal static function to look up a taxon name at NCBI
            Taxonomy via ESearch.
        Args:
            taxon_name (str): a taxon name; example: 'Pyrus tamamaschjanae'
            retmax (int):     the number of maximally retained hits
        Returns:
            entrez_hitcount (int): an integer
        '''
#        Examples:
#            Example 1: # Default behaviour
#                >>> taxon_name = 'Pyrus tamamaschjanae'
#                >>> _taxname_lookup(taxon_name)
#                Out: 0

        if not taxon_name:
            msg = 'No taxon name detected.'
            warnings.warn(msg)
            raise Exception

        if not GetEntrezInfo._serverAccessible(GlobVars.esearchUrl):
            msg = 'ERROR: The server %s is currently not \
accessible.' % ('ESearch ('+GlobVars.esearchUrl+')')
            warnings.warn(msg)
            raise Exception
        #if '_' in taxon_name:
        #    msg = 'Taxon name `%s` contains an underscore, \
        #    which is not allowed.' % (taxon_name)
        #    warnings.warn(msg)
        #    raise Exception
        query_term = taxon_name
        try:
            logging.info("Communicating with server %s \
regarding the taxonomy of `%s`.'" % 
('ESearch ('+GlobVars.esearchUrl+')', taxon_name))
            esearch_records = Entrez.esearch(db='taxonomy', 
                term=query_term, retmax=retmax, retmod='xml')
        except Exception as e:
            msg = 'An error occurred while retrieving data from \
`%s`: %s' % ('ESearch ('+GlobVars.esearchUrl+')', e)
            warnings.warn(msg)
            raise Exception(e)
        parsed_records = Entrez.read(esearch_records)
        entrez_hitcount = parsed_records['Count']
        return str(entrez_hitcount)


    @staticmethod
    def _taxname_lookup_ena(taxon_name, retmax=1):
        ''' An internal static function to look up a taxon name via 
        ENA taxonomy service.
        Args:
            taxon_name (str): a taxon name; example: 'Pyrus tamamaschjanae'
            retmax (int):     the number of maximally retained hits
        Returns:
            entrez_hitcount (int): an integer
        '''
        #        Examples:
        #            Example 1: # Default behaviour
        #                >>> taxon_name = 'Pyrus tamamaschjanae'
        #                >>> _taxname_lookup(taxon_name)
        #                Out: 0

        if not taxon_name:
            msg = 'No taxon name detected.'
            warnings.warn(msg)
            raise Exception

        if not GetEntrezInfo._serverAccessible(GlobVars.enaUrl):
            msg = 'ERROR: The server %s is currently not \
accessible.' % ('ENA ('+GlobVars.enaUrl+')')
            warnings.warn(msg)
            raise Exception
        #if '_' in taxon_name:
        #    msg = 'Taxon name `%s` contains an underscore, '\
#          'which is not allowed.' % (taxon_name)
        #    warnings.warn(msg)
        #    raise Exception

        final_url = GlobVars.enaUrl + \
                    "data/taxonomy/v1/taxon/scientific-name/" + \
                    taxon_name.replace(" ", "%20")
        if os.name == "posix":  # Linux and MacOS
            try:
                logging.info("Communicating with server %s regarding \
the taxonomy of `%s`." % ('ENA ('+GlobVars.enaUrl+')', taxon_name))
                enaTaxonomy_records = urlopen(final_url).read()
            except:
                return str(0)
        elif os.name == "nt":  # Windows ## Note: "urlopen" does not 
                               #            work well under Windows, is 
                               #            replaced with "requests"
            try:
                response = requests.get(final_url)
                if response.status_code == 200:
                    return str(1)
                else:
                    raise
            except:
                return str(0)
        entrez_hitcount = enaTaxonomy_records.decode('ascii').count(
            "taxId", 0, len(enaTaxonomy_records.decode('ascii')))
        return str(entrez_hitcount)

    @staticmethod
    def _serverAccessible(url):
        ''' An internal static function to check if the server for a 
        given url is accessible.
        Args:
            url (str): a url; example: 'https://www.ebi.ac.uk/ena/'
        Returns:
            bool: True - if server is accessible
                  False - if not
        '''

        try:
            urlopen(url)           # Linux and MacOS
            return True
        except:
            try:
                requests.get(url)  # Windows and some MacOS versions
                                   ## Note: Since "urlopen" does not 
                                   # work well under Windows and some 
                                   # MacOS versions, it is replaced 
                                   # with "requests"
                return True
            except:
                return False
        return False

#        if os.name == "posix":  # Linux and MacOS
#            try:
#                urlopen(url)
#                return True
#            except:
#                return False
#        elif os.name == "nt":  # Windows ## Note: "urlopen" does not 
#                               #            work well under Windows, is 
#                               #            replaced with "requests"
#            try:
#                requests.get(url)
#                return True
#            except:
#                return False
#        else:                   # Some MacOS versions do not register as posix
#            try:
#                urlopen(url)
#                return True
#            except:
#                return False
#        return False


    def obtain_gene_product(self, gene_sym):
        ''' This function performs something.
        '''
#        Examples:
#            Example 1: # Default behaviour
#                >>> gene_sym = 'psbI'
#                >>> GetGeneInfo()._entrezid_lookup(gene_sym)
#                Out: ['26835430', '26833718', '26833393', ...]

        Entrez.email = self.email_addr
        try:
            entrez_id_list = GetEntrezInfo._id_lookup(gene_sym)
        except Exception as e:
            msg = 'ERROR: An error occurred during the ID lookup \
process for gene `%s`: %s' % (gene_sym, e)
            warnings.warn(msg)
            raise Exception(e)
        try:
            entrez_rec_list = GetEntrezInfo._gene_product_lookup(
                entrez_id_list, gene_sym)
        except Exception as e:
            msg = 'ERROR: An error occurred during the gene product lookup \
process for gene `%s`: %s' % (gene_sym, e)
            warnings.warn(msg)
            raise Exception(e)
        try:
            gene_product = GetEntrezInfo._parse_gene_products(entrez_rec_list)
        except Exception as e:
            msg = 'ERROR: An error occurred during the gene product parsing \
process for gene `%s`: %s' % (gene_sym, e)
            warnings.warn(msg)
            raise Exception(e)
        return gene_product


    def does_taxon_exist(self, taxon_name):
        ''' This function calls _taxname_lookup and thus evaluates 
        if a taxon exists.
        Args:
            taxon_name (str): a taxon name; example: 'Pyrus tamamaschjanae'
            retmax (int):     the number of maximally retained hits
        Returns:
            entrez_id_list (list): a list of Entrez IDs; 
                example: ['26835430', '26833718', '26833393', ...]
        '''
        Entrez.email = self.email_addr
        try:
            entrez_hitcount = GetEntrezInfo._taxname_lookup_ena(taxon_name)
            #entrez_hitcount = GetEntrezInfo._taxname_lookup_ncbi(taxon_name)
        except Exception as e:
            warnings.warn(e)
            raise Exception(e)
        if entrez_hitcount == '0':
            return False
        elif entrez_hitcount == '1':
            return True


class ConfirmAdjustTaxonName:
    ''' This class contains functions to confirm or adjust a sequence's
    taxon name.
    '''

    def __init__(self):
        pass

    def go(self, seq_record, email_addr):
        ''' This function evaluates a taxon name against NCBI taxonomy;
            if not listed, it adjusts the taxon name and appends it
            as ecotype info.
            Args:
                seq_record (obj):   a seqRecord object
                email_addr (str):  your email address
            Returns:
                seq_record (obj):   a seqRecord object
        '''
        try:
            genus_name, specific_epithet = seq_record.name.split(' ', 1)
        except Exception as e:
            msg = 'ERROR: Could not locate a whitespace between genus \
name and specific epithet in taxon name of sequence `%s`.' % (seq_record.id)
            warnings.warn(msg)
            raise Exception(e)
        if not GetEntrezInfo(email_addr).does_taxon_exist(seq_record.name):
            msg = 'WARNING: Taxon name `%s` of sequence `%s` is not a \
name registered with the taxonomy service of ENA. Please consider \
sending a taxon request via the ENA Webin interface.' \
% (seq_record.id, seq_record.name)
            warnings.warn(msg)
            if not GetEntrezInfo(email_addr).does_taxon_exist(genus_name):
                msg = 'ERROR: The genus name `%s` of sequence `%s` \
is not registered with the ENA taxonomy service.' \
% (genus_name, seq_record.id)
                warnings.warn(msg)
                raise Exception
            else:
                species_name_orig = seq_record.name
                species_name_new = genus_name + ' sp. ' + specific_epithet
                seq_record.name = species_name_new
                seq_record.features[0].qualifiers['organism'] = species_name_new
                seq_record.description = seq_record.description.\
replace(species_name_orig, species_name_new)
                msg = 'WARNING: Taxon name of sequence `%s` is \
converted to the informal name `%s`.' \
% (seq_record.id, species_name_new)
                warnings.warn(msg)
        return seq_record


class ParseCharsetName:
    ''' This class contains functions to parse charset names.
    Args:
        charset_name (str): a string that represents a charset name; 
            example: "psbI_CDS"
        email_addr (dict):  your email address
        product_lookup (bool): decision if product name shall be looked up
    '''

    def __init__(self, charset_name, email_addr, product_lookup):
        self.charset_name = charset_name
        self.email_addr = email_addr
        self.product_lookup = product_lookup

    @staticmethod
    def _extract_charset_info(charset_name):
        charset_orient = False
        charset_type = False
        charset_sym = False
        orient_present = [ori for ori in GlobVars.nex2ena_valid_orientations 
                          if ori in charset_name]
        try:
            if(len(orient_present) == 0):
                 charset_orient = 'forw'
            elif(len(orient_present) == 1):
                charset_orient = orient_present[0]
                if charset_orient == "forw":
                    charset_name = charset_name.replace("forward","")
                    charset_name = charset_name.replace("forw","")
                elif charset_orient == "rev":
                    charset_name = charset_name.replace("reverse","")
                    charset_name = charset_name.replace("rev","")
        except Exception as e:
            msg = 'ERROR: Unclear parsing of feature orientation in \
charset `%s`: %s' % (charset_name, str(e))
            warnings.warn(msg)
            raise Exception(e)
        type_present = [typ for typ in GlobVars.nex2ena_valid_INSDC_featurekeys 
                        if typ in charset_name]
        try:
            if(len(type_present) == 0):
                msg = 'ERROR: No valid feature keys in \
charset `%s`: %s' % (charset_name, str(e))
                warnings.warn(msg)
                raise Exception
            elif(len(type_present) == 1):
                charset_type = type_present[0]
                charset_name = ''.join(charset_name.split(type_present[0]))
            elif(len(type_present) > 1):
                msg = 'WARNING: More than one charset_type \
encountered in charset `%s`.' % (charset_name)
                warnings.warn(msg)
                charset_type = type_present[0]
                charset_name = ''.join(charset_name.split(type_present[0]))
        except Exception as e:
            msg = 'ERROR: Unclear parsing of features in \
charset `%s`: %s' % (charset_name, str(e))
            warnings.warn(msg)
            raise Exception(e)
        charset_sym = charset_name.strip('_').split('_')
        try:
            if len(charset_sym) == 1:
                return (charset_sym[0], charset_type, charset_orient)
        except Exception as e:
            msg = 'ERROR: Unspecified error during feature parsing in \
charset `%s`: %s' % (charset_name, str(e))
            warnings.warn(msg)
            raise Exception(e)


    def parse(self):
        ''' This function parses the charset_name.
        Returns:
            tupl.   The return consists of three strings in the order
                    "charset_sym, charset_type, charset_orient, charset_product"
        '''
        try:
            charset_sym, charset_type, charset_orient = ParseCharsetName.\
_extract_charset_info(self.charset_name)
        except Exception as e:
            msg = 'ERROR: Error while parsing the charset `%s`: %s' \
% (self.charset_name, str(e))
            warnings.warn(msg)
            raise Exception(e)
        entrez_handle = GetEntrezInfo(self.email_addr)
        if (charset_type == 'CDS' or charset_type == 'gene') and self.product_lookup:
            try:
                charset_product = entrez_handle.obtain_gene_product(charset_sym)
            except Exception as e:
                msg = 'ERROR: Error while obtaining gene product for \
charset `%s`: %s' % (self.charset_name, str(e))
                warnings.warn(msg)
                raise Exception(e)
        else:
            charset_product = None
        return (charset_sym, charset_type, charset_orient, charset_product)


class SequenceParsing:
    ''' This class contains functions to parse and modify DNA 
    sequence strings.
    '''
    def __init__(self):
        pass

    def reverseComplement(sequence):
        ''' This function reverse complements a DNA sequence string
            Args:
                sequence (str)
            Returns:
                reverse complemented sequence (str)
        '''
        reverseComplement = []
        for nucl in sequence:
            if nucl == "A":
                reverseComplement.append("T")
            elif nucl == "T":
                reverseComplement.append("A")
            elif nucl == "C":
                reverseComplement.append("G")
            elif nucl == "G":
                reverseComplement.append("C")
        return ''.join(reverseComplement)[::-1]
