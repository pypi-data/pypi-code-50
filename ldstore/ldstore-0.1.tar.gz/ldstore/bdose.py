from parse import *

import numpy as np
import pandas as pd
import sys
import zstd

class bdose:
        
    ##-----------------------------------##
    ## Initialize BDOSE instance         ##
    ##-----------------------------------##
    def __init__( self, fname ):
        self.__fname = fname
        try:
            self.__fh = open( self.__fname, 'rb' )
            self.__readHeader ()
            self.__readMeta   ()
            if self.__version == 0:
                self.__readMissingness()
            elif self.__version == 1:
                self.__readSamples()
            self.__readOffsets()
        except IOError:
            raise
    
    ##-----------------------------------##
    ## Getters                           ##
    ##-----------------------------------##
    def getFname       ( self ): return self.__fname
    def getFsize       ( self ): return self.__fsize
    def getMeta        ( self ): return self.__meta
    def getMissingness ( self ):
        if self.__version == 0:
            return self.__missingness
        else:
            print 'File "' + self.__fname + '" is a BDOSE v1.' + str( self.__version ) + ' file. Can only get missingness information from a BDOSE v1.0 file!'
            return
    def getNumOfSNPs   ( self ): return self.__nSNPs
    def getNumOfSamples( self ): return self.__nSamples
    def getOffsets     ( self ): return self.__offsets
    def getSamples     ( self ):
        if self.__version == 1:
            return self.__samples
        else:
            print 'File "' + self.__fname + '" is a BDOSE v1.' + str( self.__version ) + ' file. Can only get sample identifiers from a BDOSE v1.1 file!'
            return
    
    ##-----------------------------------##
    ## Read dosages in a BDOSE v1.0 file ##
    ##-----------------------------------##
    def __readDosages_v10( self, snps ):
        if type( snps ) is not list:
            print 'Need to input "snps" as a list!'
            return
        
        areSNPsIncluded( snps, self.__nSNPs, self.__fname )
        
        dosages = np.zeros( [ self.__nSamples, len( snps ) ] )
        for snp, index in zip( snps, range( len( snps ) ) ):
            self.__fh.seek( self.__offsets[ snp ] )
            dosages[ :, index ] = np.fromfile( self.__fh, np.float64, self.__nSamples )
        
        return dosages
    
    ##-----------------------------------##
    ## Read dosages in a BDOSE v1.1 file ##
    ##-----------------------------------##
    def __readDosages_v11( self, snps ):
        if type( snps ) is not list:
            print 'Need to input "snps" as a list!'
            return
        
        areSNPsIncluded( snps, self.__nSNPs, self.__fname )
        
        dosages = np.zeros( [ self.__nSamples, len( snps ) ] )
        for snp, index in zip( snps, range( len( snps ) ) ):
            self.__fh.seek( self.__offsets[ snp ] )
            compressed_size   = np.fromfile( self.__fh, np.uint32, 1 )[ 0 ]
            uncompressed_size = np.fromfile( self.__fh, np.uint32, 1 )[ 0 ]
            buffer_compr      = self.__fh.read( compressed_size - 4 )
            buffer_uncompr    = zstd.decompress( buffer_compr )
            if self.__compression == 0:
                dosages_int         = np.frombuffer( buffer_uncompr, np.uint16, uncompressed_size / 2 )
                dosages[ :, index ] = convertIntToFloat( dosages_int, 2 )
            elif self.__compression == 1:
                dosages_int         = np.frombuffer( buffer_uncompr, np.uint32, uncompressed_size / 4 )
                dosages[ :, index ] = convertIntToFloat( dosages_int, 4 )
            elif self.__compression == 2:
                dosages_int         = np.frombuffer( buffer_uncompr, np.uint64, uncompressed_size / 8 )
                dosages[ :, index ] = convertIntToFloat( dosages_int, 8 )
            else:
                dosages_int         = np.frombuffer( buffer_uncompr, np.uint8, uncompressed_size )
                dosages[ :, index ] = convertIntToFloat( dosages_int, 1 )
        
        return dosages
    
    ##-----------------------------------##
    ## Read dosages in a BDOSE file      ##
    ##-----------------------------------##
    def readDosages( self, snps ):
        if self.__version == 0:
            return self.__readDosages_v10( snps )
        elif self.__version == 1:
            return self.__readDosages_v11( snps )
    
    ##-----------------------------------##
    ## Read header block                 ##
    ##-----------------------------------##
    def __readHeader( self ):
        magic = self.__fh.read( 8 )
        if magic == 'bdose1.0':
            self.__version = 0
        elif magic == 'bdose1.1':
            self.__version = 1
        else:
            print 'File "' + self.__fname + '" is not from LDStore!'
            return
        
        L_bgenFname     = np.fromfile ( self.__fh, np.uint32, 1  )[ 0 ]
        bgenFname       = self.__fh.read( L_bgenFname            )
        bgenFsize       = np.fromfile ( self.__fh, np.uint64, 1  )[ 0 ]
        bgenFirstBytes  = self.__fh.read( min( 1000, bgenFsize ) )
        self.__fsize    = np.fromfile ( self.__fh, np.uint64, 1  )[ 0 ]
        self.__nSamples = np.fromfile ( self.__fh, np.uint32, 1  )[ 0 ]
        self.__nSNPs    = np.fromfile ( self.__fh, np.uint32, 1  )[ 0 ]
        
        if self.__version == 1:
            self.__compression          = np.fromfile ( self.__fh, np.uint8,  1  )[ 0 ]
            self.__samples_block_offset = np.fromfile ( self.__fh, np.uint64, 1  )[ 0 ]
            self.__offsets_block_offset = np.fromfile ( self.__fh, np.uint64, 1  )[ 0 ]
            self.__dosages_block_offset = np.fromfile ( self.__fh, np.uint64, 1  )[ 0 ]
    
    ##-----------------------------------##
    ## Read meta information block       ##
    ##-----------------------------------##
    def __readMeta( self ):
        rsid       = []
        position   = np.zeros( self.__nSNPs )
        chromosome = []
        allele1    = []
        allele2    = []
        
        for snp in range( self.__nSNPs ):
            L_buffer          = np.fromfile( self.__fh, np.uint32, 1 )[ 0 ]
            index             = np.fromfile( self.__fh, np.uint32, 1 )[ 0 ]
            L_rsid            = np.fromfile( self.__fh, np.uint16, 1 )[ 0 ]
            rsid.append( self.__fh.read( L_rsid ) )
            position[ snp ]   = np.fromfile( self.__fh, np.uint32, 1 )[ 0 ]
            L_chromosome      = np.fromfile( self.__fh, np.uint16, 1 )[ 0 ]
            chromosome.append( self.__fh.read( L_chromosome ) )
            L_allele1         = np.fromfile( self.__fh, np.uint32, 1 )[ 0 ]
            allele1.append( self.__fh.read( L_allele1 ) )
            L_allele2         = np.fromfile( self.__fh, np.uint32, 1 )[ 0 ]
            allele2.append( self.__fh.read( L_allele2 ) )
            assert( L_buffer == ( 20 + L_rsid + L_chromosome + L_allele1 + L_allele2 ) )
        
        self.__meta = pd.concat( [
            pd.DataFrame( rsid,       columns = [ 'rsid'       ] ),
            pd.DataFrame( position,   columns = [ 'position'   ] ),
            pd.DataFrame( chromosome, columns = [ 'chromosome' ] ),
            pd.DataFrame( allele1,    columns = [ 'allele1'    ] ),
            pd.DataFrame( allele2,    columns = [ 'allele2'    ] )
        ], axis = 1 )
    
    ##-----------------------------------##
    ## Read sample missingness in a      ##
    ## BDOSE v1.0 file                   ##
    ##-----------------------------------##
    def __readMissingness( self ):
        self.__missingness = np.fromfile( self.__fh, np.uint32, self.__nSNPs )
    
    ##-----------------------------------##
    ## Read file offsets where dosages   ##
    ## on each variant start in BDOSE    ##
    ## file                              ##
    ##-----------------------------------##
    def __readOffsets( self ):
        self.__offsets = np.fromfile( self.__fh, np.uint64, self.__nSNPs )
    
    ##-----------------------------------##
    ## Read sample identifiers in a      ##
    ## BDOSE v1.1 file                   ##
    ##-----------------------------------##
    def __readSamples( self ):
        self.__samples = []
        for self.sample in range( self.__nSamples ):
            L_samples = np.fromfile( self.__fh, np.uint32, 1 )[ 0 ]
            self.__samples.append( self.__fh.read( L_samples ) )
    
    ##-----------------------------------##
    ## Compute Pearson correlations      ##
    ##-----------------------------------##
    def computeCorr( self, snps ):
        df = pd.DataFrame( self.readDosages( snps ) )
        
        return df.fillna( df.mean() ).corr()
