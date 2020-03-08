#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# JSONBible.py
#
# Module handling a set of Bible books saved as JSON files (intended for fast loading)
#
# Copyright (C) 2018-2019 Robert Hunt
# Author: Robert Hunt <Freely.Given.org@gmail.com>
# License: See gpl-3.0.txt
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Module for loading and exporting various JSON Bibles.
"""

from gettext import gettext as _

lastModifiedDate = '2019-09-15' # by RJH
shortProgramName = "JSONBible"
programName = "JSON Bible handler"
programVersion = '0.04'
programNameVersion = f'{shortProgramName} v{programVersion}'
programNameVersionDate = f'{programNameVersion} {_("last modified")} {lastModifiedDate}'

debuggingThisModule = False


import os, sys, logging
import json, zipfile
import multiprocessing

if __name__ == '__main__':
    sys.path.append( os.path.join(os.path.dirname(__file__), '../') ) # So we can run it from the above folder and still do these imports
import BibleOrgSysGlobals
from Bible import Bible
from Internals.InternalBibleInternals import BOS_ADDED_NESTING_MARKERS


# The following are all case sensitive
ZIPPED_FILENAME = '_BOSJSONBible.zip' # This is what the filename must END WITH
VERSION_FILENAME = 'BibleVersion.json' # Contains the object version number
INFO_FILENAME = 'BibleInfo.json' # Contains the Bible metadata
BOOK_FILENAME = '{}.json' # Each book is stored in a separate BBB.json file



def JSONBibleFileCheck( givenFolderName, strictCheck=True, autoLoad=False, autoLoadBooks=False ):
    """
    Given a folder, search for Pickle Bible files or folders in the folder and in the next level down.

    Returns False if an error is found.

    if autoLoad is false (default)
        returns None, or the number of Bibles found.

    if autoLoad is true and exactly one Pickle Bible is found,
        returns the loaded JSONBible object.
    """
    if BibleOrgSysGlobals.verbosityLevel > 2: print( "JSONBibleFileCheck( {}, {}, {}, {} )".format( givenFolderName, strictCheck, autoLoad, autoLoadBooks ) )
    if BibleOrgSysGlobals.debugFlag: assert givenFolderName and isinstance( givenFolderName, str )
    if BibleOrgSysGlobals.debugFlag: assert autoLoad in (True,False,) and autoLoadBooks in (True,False,)

    # Check that the given folder is readable
    if not os.access( givenFolderName, os.R_OK ):
        logging.critical( _("JSONBibleFileCheck: Given {!r} folder is unreadable").format( givenFolderName ) )
        return False
    if not os.path.isdir( givenFolderName ):
        logging.critical( _("JSONBibleFileCheck: Given {!r} path is not a folder").format( givenFolderName ) )
        return False

    # Find all the files and folders in this folder
    if BibleOrgSysGlobals.verbosityLevel > 3: print( " JSONBibleFileCheck: Looking for files in given {}".format( givenFolderName ) )
    foundFolders, foundFiles = [], []
    for something in os.listdir( givenFolderName ):
        somepath = os.path.join( givenFolderName, something )
        if os.path.isdir( somepath ):
            if something in BibleOrgSysGlobals.COMMONLY_IGNORED_FOLDERS:
                continue # don't visit these directories
            foundFolders.append( something )
        elif os.path.isfile( somepath ):
            #somethingUpper = something.upper()
            if something in (ZIPPED_FILENAME, VERSION_FILENAME):
                foundFiles.append( something )

    # See if there's an JSONBible project here in this given folder
    numFound = len( foundFiles )
    if numFound:
        if BibleOrgSysGlobals.verbosityLevel > 2: print( _("JSONBibleFileCheck got {} in {}").format( numFound, givenFolderName ) )
        if numFound == 1 and (autoLoad or autoLoadBooks):
            uB = JSONBible( givenFolderName )
            if autoLoad or autoLoadBooks: uB.preload() # Load the SSF file
            if autoLoadBooks: uB.loadBooks() # Load and process the book files
            return uB
        return numFound

    # Look one level down
    numFound = 0
    foundProjects = []
    for thisFolderName in sorted( foundFolders ):
        tryFolderName = os.path.join( givenFolderName, thisFolderName+'/' )
        if not os.access( tryFolderName, os.R_OK ): # The subfolder is not readable
            logging.warning( _("JSONBibleFileCheck: {!r} subfolder is unreadable").format( tryFolderName ) )
            continue
        if BibleOrgSysGlobals.verbosityLevel > 3: print( "    JSONBibleFileCheck: Looking for files in {}".format( tryFolderName ) )
        foundSubfolders, foundSubfiles = [], []
        for something in os.listdir( tryFolderName ):
            somepath = os.path.join( givenFolderName, thisFolderName, something )
            if os.path.isdir( somepath ): foundSubfolders.append( something )
            elif os.path.isfile( somepath ):
                #somethingUpper = something.upper()
                if something in (ZIPPED_FILENAME, VERSION_FILENAME):
                    foundSubfiles.append( something )
                    numFound += 1

    # See if there's an Pickle Bible here in this folder
    if numFound:
        if BibleOrgSysGlobals.verbosityLevel > 2: print( _("JSONBibleFileCheck foundProjects {} {}").format( numFound, foundProjects ) )
        if numFound == 1 and (autoLoad or autoLoadBooks):
            uB = JSONBible( foundProjects[0] )
            if autoLoad or autoLoadBooks: uB.preload() # Load the SSF file
            if autoLoadBooks: uB.loadBooks() # Load and process the book files
            return uB
        return numFound
# end of JSONBibleFileCheck



class JSONBible( Bible ):
    """
    Class to load and manipulate Pickle Bibles.

    """
    def __init__( self, source ):
        """
        Create the internal Pickle Bible object.

        NOTE: source can be a folder (containing several pickle files)
            or a something.json.zip filepath.
        """
         # Setup and initialise the base class first
        Bible.__init__( self )
        self.objectNameString = 'JSON Bible object'
        self.objectTypeString = 'JSONBible'

        # Now we can set our object variables
        self.jsonVersionData = {}

        def loadVersionStuff( fileObject ):
            """
            This function loads all the fields from the version file.

            NOTE: This refers to the pickle/software/object versions, not the Bible text version.
            """
            myDict = {}
            myDict['WriterVersionDate'] = pickle.load( fileObject )
            myDict['WrittenDateTime'] = pickle.load( fileObject )
            myDict['IBProgVersion'] = pickle.load( fileObject )
            myDict['IBBProgVersion'] = pickle.load( fileObject )
            myDict['IBIProgVersion'] = pickle.load( fileObject )
            myDict['workName'] = pickle.load( fileObject )
            myDict['bookList'] = pickle.load( fileObject )
            myDict['sourceURL'] = pickle.load( fileObject )
            myDict['licenceString'] = pickle.load( fileObject )
            return myDict
        # end of JSONBible.__init_ loadVersionStuff

        # Now we load the version info file
        if source.endswith( '.json.zip' ):
            self.jsonFilepath = source
            self.jsonSourceFolder = os.path.dirname( source )
            self.jsonIsZipped = True
            with zipfile.ZipFile( self.jsonFilepath ) as thisZip:
                #print( '\nnamelist', thisZip.namelist() )
                #print( '\ninfolist', thisZip.infolist() )
                with thisZip.open( VERSION_FILENAME ) as pickleInputFile:
                    self.jsonVersionData = loadVersionStuff( pickleInputFile )
        else: # assume it's a folder
            self.jsonSourceFolder = source
            self.jsonIsZipped = False
            filepath = os.path.join( self.jsonSourceFolder, VERSION_FILENAME )
            if os.path.exists( filepath ):
                if BibleOrgSysGlobals.verbosityLevel > 2:
                    print( _("Loading pickle version info from pickle file {}…").format( filepath ) )
                with open( filepath, 'rb') as pickleInputFile:
                    # The protocol version used is detected automatically, so we do not have to specify it
                    self.jsonVersionData = loadVersionStuff( pickleInputFile )
            else: logging.critical( _("JSONBible: unable to find {!r}").format( VERSION_FILENAME ) )

        #if debuggingThisModule: print( "pickleVersionData", self.jsonVersionData )
    # end of JSONBible.__init_


    def __str__( self ):
        """
        This method returns the string representation of a Bible.

        This one overrides the default one in InternalBible.py
            to handle extra source folders.

        @return: the name of a Bible object formatted as a string
        @rtype: string
        """
        set1 = ( 'Title', 'Description', 'Version', 'Revision', ) # Ones to print at verbosityLevel > 1
        set2 = ( 'Status', 'Font', 'Copyright', 'Licence', ) # Ones to print at verbosityLevel > 2
        set3 = set1 + set2 + ( 'Name', 'Abbreviation' ) # Ones not to print at verbosityLevel > 3

        result = self.objectNameString
        indent = 2
        if BibleOrgSysGlobals.debugFlag or BibleOrgSysGlobals.verbosityLevel>2: result += ' v' + programVersion
        if self.name: result += ('\n' if result else '') + ' '*indent + _("Name: {}").format( self.name )
        if self.abbreviation: result += ('\n' if result else '') + ' '*indent + _("Abbreviation: {}").format( self.abbreviation )
        if self.sourceFolder: result += ('\n' if result else '') + ' '*indent + _("Original source folder: {}").format( self.sourceFolder )
        elif self.sourceFilepath: result += ('\n' if result else '') + ' '*indent + _("Original source: {}").format( self.sourceFilepath )
        if BibleOrgSysGlobals.verbosityLevel > 1:
            for fieldName in set1:
                fieldContents = self.getSetting( fieldName )
                if fieldContents:
                    result += ('\n' if result else '') + ' '*indent + _("{}: {!r}").format( fieldName, fieldContents )
        if BibleOrgSysGlobals.verbosityLevel > 2:
            for fieldName in ( 'Status', 'Font', 'Copyright', 'Licence', ):
                fieldContents = self.getSetting( fieldName )
                if fieldContents:
                    result += ('\n' if result else '') + ' '*indent + _("{}: {!r}").format( fieldName, fieldContents )
        if (BibleOrgSysGlobals.debugFlag or debuggingThisModule) and BibleOrgSysGlobals.verbosityLevel > 3 \
        and self.suppliedMetadata and self.objectTypeString not in ('PTX7','PTX8'): # There's too much potential Paratext metadata
            for metadataType in self.suppliedMetadata:
                for fieldName in self.suppliedMetadata[metadataType]:
                    if fieldName not in set3:
                        fieldContents = self.suppliedMetadata[metadataType][fieldName]
                        if fieldContents:
                            result += ('\n' if result else '') + '  '*indent + _("{}: {!r}").format( fieldName, fieldContents )
        #if self.revision: result += ('\n' if result else '') + ' '*indent + _("Revision: {}").format( self.revision )
        #if self.version: result += ('\n' if result else '') + ' '*indent + _("Version: {}").format( self.version )
        result += ('\n' if result else '') + ' '*indent + _("Number of{} books: {}{}") \
                                        .format( '' if self.loadedAllBooks else ' loaded', len(self.books), ' {}'.format( self.getBookList() ) if 0<len(self.books)<5 else '' )
        return result
    # end of InternalBible.__str__


    def preload( self ):
        """
        Loads the BibleInfo file if it can be found.
        """
        if BibleOrgSysGlobals.debugFlag or BibleOrgSysGlobals.verbosityLevel > 2:
            print( _("preload() from {}").format( self.jsonSourceFolder ) )
            assert not self.preloadDone
            assert self.jsonIsZipped or self.jsonSourceFolder is not None
            #print( "preload1", len(dir(self)), dir(self) )

        def loadBibleAttributes( fileObject, BibleObject ):
            """
            Load the saved attributes for the BibleObject.
            """
            loadedCount = 0
            while True: # Load name/value pairs for Bible attributes
                try: attributeName = pickle.load( fileObject )
                except EOFError: break
                attributeValue = pickle.load( fileObject )
                if attributeName == 'objectNameString': attributeName = 'originalObjectNameString'
                elif attributeName == 'objectTypeString': attributeName = 'originalObjectTypeString'
                #print( "attribute: {} = {}".format( attributeName, attributeValue if attributeName!='discoveryResults' else '...' ) )
                setattr( BibleObject, attributeName, attributeValue )
                loadedCount += 1
            return loadedCount
        # end of JSONBible.preload loadBibleAttributes

        if self.jsonIsZipped:
            with zipfile.ZipFile( self.jsonFilepath ) as thisZip:
                with thisZip.open( INFO_FILENAME ) as pickleInputFile:
                    loadedCount = loadBibleAttributes( pickleInputFile, self )
        else: # it's not zipped
            filepath = os.path.join( self.jsonSourceFolder, INFO_FILENAME )
            if os.path.exists( filepath ):
                if BibleOrgSysGlobals.verbosityLevel > 2:
                    print( _("Loading Bible info from pickle file {}…").format( filepath ) )
                with open( filepath, 'rb') as pickleInputFile:
                    loadedCount = loadBibleAttributes( pickleInputFile, self )
            else: logging.critical( _("JSONBible: unable to find {!r}").format( INFO_FILENAME ) )

        if BibleOrgSysGlobals.debugFlag or BibleOrgSysGlobals.verbosityLevel > 2:
            print( _("  Loaded {} attributes").format( loadedCount ) )

        for BBB in self.jsonVersionData['bookList']:
            if BBB in self.triedLoadingBook:
                del self.triedLoadingBook[BBB] # So we can load them (again) from the pickle files

        #print( "preload2", len(dir(self)), dir(self) )
        #print( self )
        self.preloadDone = True
    # end of JSONBible.preload


    def loadBook( self, BBB ):
        """
        Load the requested book into self.books if it's not already loaded.

        NOTE: You should ensure that preload() has been called first.
        """
        if BibleOrgSysGlobals.debugFlag or BibleOrgSysGlobals.verbosityLevel > 2:
            print( "JSONBible.loadBook( {} )".format( BBB ) )
            assert self.preloadDone

        if BBB not in self.bookNeedsReloading or not self.bookNeedsReloading[BBB]:
            if BBB in self.books:
                if BibleOrgSysGlobals.debugFlag: print( "  {} is already loaded -- returning".format( BBB ) )
                return # Already loaded
            if BBB in self.triedLoadingBook:
                logging.warning( "We had already tried loading Pickle {} for {}".format( BBB, self.name ) )
                return # We've already attempted to load this book
        self.triedLoadingBook[BBB] = True

        if BibleOrgSysGlobals.verbosityLevel > 2 or BibleOrgSysGlobals.debugFlag:
            print( _("  JSONBible: Loading {} from {} from {}…").format( BBB, self.name, self.jsonSourceFolder ) )
        if self.jsonIsZipped:
            with zipfile.ZipFile( self.jsonFilepath ) as thisZip:
                with thisZip.open( BOOK_FILENAME.format( BBB ) ) as pickleInputFile:
                    bookObject = pickle.load( pickleInputFile )
        else: # not zipped
            bookObject = BibleOrgSysGlobals.unpickleObject( BOOK_FILENAME.format( BBB ), self.jsonSourceFolder )

        self.books[BBB] = bookObject
        self.bookNeedsReloading[BBB] = False
    # end of JSONBible.loadBook


    def _loadBookMP( self, BBB ):
        """
        Multiprocessing version!
        Load the requested book if it's not already loaded (but doesn't save it as that is not safe for multiprocessing)

        Returns the book info.
        """
        if BibleOrgSysGlobals.verbosityLevel > 3:
            print( _("loadBookMP( {} )").format( BBB ) )

        if BBB in self.books:
            if BibleOrgSysGlobals.debugFlag: print( "  {} is already loaded -- returning".format( BBB ) )
            return self.books[BBB] # Already loaded
        #if BBB in self.triedLoadingBook:
            #logging.warning( "We had already tried loading Pickle {} for {}".format( BBB, self.name ) )
            #return # We've already attempted to load this book
        self.triedLoadingBook[BBB] = True
        self.bookNeedsReloading[BBB] = False
        if BibleOrgSysGlobals.verbosityLevel > 2 or BibleOrgSysGlobals.debugFlag:
            print( '  ' + _("Loading {} from {} from {}…").format( BBB, self.name, self.jsonSourceFolder ) )
        if self.jsonIsZipped:
            with zipfile.ZipFile( self.jsonFilepath ) as thisZip:
                with thisZip.open( BOOK_FILENAME.format( BBB ) ) as pickleInputFile:
                    bookObject = pickle.load( pickleInputFile )
        else:
            bookObject = BibleOrgSysGlobals.unpickleObject( BOOK_FILENAME.format( BBB ), self.jsonSourceFolder )

        if BibleOrgSysGlobals.verbosityLevel > 2 or BibleOrgSysGlobals.debugFlag:
            print( _("    Finishing loading pickled book {}.").format( BBB ) )
        return bookObject
    # end of JSONBible.loadBookMP


    def loadBooks( self ):
        """
        Load all the Bible books.
        """
        if BibleOrgSysGlobals.verbosityLevel > 1: print( _("Loading {} from {}…").format( self.getAName(), self.jsonSourceFolder ) )

        if not self.preloadDone: self.preload()

        if len( self.jsonVersionData['bookList'] ) > 2:
            if BibleOrgSysGlobals.maxProcesses > 1 \
            and not BibleOrgSysGlobals.alreadyMultiprocessing: # Get our subprocesses ready and waiting for work
                # Load all the books as quickly as possible
                #parameters = [BBB for BBB,filename in self.jsonVersionData['bookList']] # Can only pass a single parameter to map
                if BibleOrgSysGlobals.verbosityLevel > 1:
                    print( _("Loading {} {} books using {} processes…").format( len(self.jsonVersionData['bookList']), 'Pickle', BibleOrgSysGlobals.maxProcesses ) )
                    print( _("  NOTE: Outputs (including error and warning messages) from loading various books may be interspersed.") )
                BibleOrgSysGlobals.alreadyMultiprocessing = True
                with multiprocessing.Pool( processes=BibleOrgSysGlobals.maxProcesses ) as pool: # start worker processes
                    results = pool.map( self._loadBookMP, self.jsonVersionData['bookList'] ) # have the pool do our loads
                    assert len(results) == len(self.jsonVersionData['bookList'])
                    for bBook in results: self.stashBook( bBook ) # Saves them in the correct order
                BibleOrgSysGlobals.alreadyMultiprocessing = False
            else: # Just single threaded
                # Load the books one by one -- assuming that they have regular Paratext style filenames
                for BBB in self.jsonVersionData['bookList']:
                    #if BibleOrgSysGlobals.verbosityLevel>1 or BibleOrgSysGlobals.debugFlag:
                        #print( _("  JSONBible: Loading {} from {} from {}…").format( BBB, self.name, self.sourceFolder ) )
                    self.loadBook( BBB ) # also saves it
        else:
            logging.critical( "JSONBible: " + _("No books to load in folder '{}'!").format( self.sourceFolder ) )
        #print( self.getBookList() )
        self.doPostLoadProcessing()
    # end of JSONBible.loadBooks

    def load( self ):
        self.loadBooks()
# end of class JSONBible



def createBOSJSONBible( self, outputFolder, controlDict ):
    """
    self here is a Bible object with _processedLines
    """
    from Internals.InternalBibleInternals import BOS_ADDED_NESTING_MARKERS, BOS_NESTING_MARKERS

    createdFilenames = []
    if not os.access( outputFolder, os.F_OK ): os.makedirs( outputFolder ) # Make the empty folder if there wasn't already one there

    # Save the individual books
    for BBB,bookObject in self.books.items():
        filename = BOOK_FILENAME.format( BBB )
        createdFilenames.append( filename )
        filepath = os.path.join( outputFolder, filename )
        jsonList = []
        for processedBibleEntry in bookObject._processedLines:
            pseudoMarker, fullText = processedBibleEntry.getMarker(), processedBibleEntry.getFullText()
            print( BBB, pseudoMarker, repr(fullText) )

            jsonList.append( {pseudoMarker:fullText} )
        print( f"Got JSON: {jsonList}" )
        with open( filepath, 'wt' ) as jsonOutputFile:
            jsonOutputFile.write( json.dumps( jsonList ) )

    # Now create a zipped version of the entire folder
    zipFilename = self.getAName( abbrevFirst=True )
    if debuggingThisModule or BibleOrgSysGlobals.debugFlag: assert zipFilename
    zipFilename = BibleOrgSysGlobals.makeSafeFilename( zipFilename+'.json.zip' )
    zipFilepath = os.path.join( outputFolder, zipFilename )
    if BibleOrgSysGlobals.verbosityLevel > 2: print( "  Zipping {} JSON files…".format( len(createdFilenames) ) )
    zf = zipfile.ZipFile( zipFilepath, 'w', compression=zipfile.ZIP_DEFLATED )
    for filename in createdFilenames:
        zf.write( os.path.join( outputFolder, filename ), filename )
    zf.close()

    if BibleOrgSysGlobals.verbosityLevel > 0 and BibleOrgSysGlobals.maxProcesses > 1:
        print( "  BibleWriter.createBOSJSONBible finished successfully." )
    return True
# end of createBOSJSONBible



def createUWJSONBibleBook( BBB, bookData, ignoredMarkerSet ):
    """
    """
    jsonDict = {}
    haveChapters = False
    C = '0'
    for processedBibleEntry in bookData._processedLines:
        pseudoMarker, fullText = processedBibleEntry.getMarker(), processedBibleEntry.getFullText()
        print( BBB, pseudoMarker, repr(fullText) )
        if '¬' in pseudoMarker or pseudoMarker in BOS_ADDED_NESTING_MARKERS or pseudoMarker=='v=':
            continue # Just ignore added markers -- not needed here
        if pseudoMarker in ('c#','vp#',):
            ignoredMarkerSet.add( pseudoMarker )
            continue

        if pseudoMarker == 'c':
            if 'chapters' not in jsonDict:
                jsonDict['chapters'] = {}
                haveChapters = True
            C = fullText
            jsonDict['chapters'][C] = {}
        elif pseudoMarker == 'v':
            V = fullText
            jsonDict['chapters'][C][V] = {'verseObjects':[]}
        elif pseudoMarker == 'v~':
            if '\\' in fullText:
                print( f"Not handled yet!!!: {fullText}" ); halt
            else: # no backslashes in the line -- it's easy
                jsonDict['chapters'][C][V]['verseObjects'].append( { 'type':'text', 'text':fullText+'\n' } )
        elif not haveChapters:
            if 'headers' not in jsonDict: jsonDict['headers'] = []
            # Ok to leave backslashes inside header content
            jsonDict['headers'].append( {'tag':pseudoMarker, 'content':fullText} )
        else:
            pass
    print( f"Got JSON: {jsonDict}" )
    return jsonDict
# end of createUWJSONBibleBook


def createUWJSONBible( self, outputFolder, controlDict ):
    """
    self here is a Bible object with _processedLines

\\id MAT test
\\h Matthew
\\rem Test USFM
\\mt2 The Gospel According to
\\mt1 Matthew
\\ip Intro paragraph
\\iot Header \\ior 1:1-2:2\\ior*
\\c 1
\\s Section heading
\\p
\\v 1 This is verse one. Verse two will be blank
\\v 2
\\v 3 This is verse three with some \\add added\\add* text!
\\v 4 Here is the 4th verse about \\nd Yahweh\\nd*, or should we \\bd bold that \\+nd Yahweh\\+nd*\\bd*.
\\s Another section heading
\\r (Some section reference text)
\\p
\\v 5 Verse five.
\\p Rest of v5 in a new paragraph
\\d Psalm title
\\v 6 Verse six with a footnote\\f + \\fr 1:6 \\ft Footnote text.\\f* there.
\\v 7 \\x - \\xo 1:7: \\xt 2Cor 4:6.\\x*This verse started with a cross-reference.

gives:

{"headers":
     [{"tag":"id","content":"MAT test"},
      {"tag":"h","content":"Matthew"},
      {"tag":"rem","content":"Test USFM"},
      {"tag":"mt2","content":"The Gospel According to"},
      {"tag":"mt1","content":"Matthew"},
      {"tag":"ip","content":"Intro paragraph"},
      {"tag":"iot","content":"Header \\ior 1:1-2:2\\ior*"}
      ],
 "chapters":
     {"1":
          {"1":{"verseObjects":[{"type":"text","text":"This is verse one. Verse two will be blank\n"}
                                ]},
           "2":{"verseObjects":[{"type":"text","text":"\n"}
                                ]},
           "3":{"verseObjects":[{"type":"text","text":"This is verse three with some "},
                                {"tag":"add","text":"added","endTag":"add*"},
                                {"type":"text","text":" text!\n"}
                                ]},
           "4":{"verseObjects":[{"type":"text","text":"Here is the 4th verse about "},
                                {"tag":"nd","text":"Yahweh","endTag":"nd*"},
                                {"type":"text","text":", or should we "},
                                {"tag":"bd","text":"bold that ",                                                                                                                                                                            "children":[{"tag":"+nd","text":"Yahweh","endTag":"+nd*"}],"endTag":"bd*"},{"type":"text","text":".\n"},
                                {"tag":"s","type":"section","content":"Another section heading\n"},
                                {"tag":"r","content":"(Some section reference text)\n"},
                                {"tag":"p","nextChar":"\n","type":"paragraph"}
                                ]},
           "5":{"verseObjects":[{"type":"text","text":"Verse five.\n"},
                                {"tag":"p","type":"paragraph","text":"Rest of v5 in a new paragraph\n"},
                                {"tag":"d","text":"Psalm title\n"}
                                ]},
           "6":{"verseObjects":[{"type":"text","text":"Verse six with a footnote"},
                                {"tag":"f","type":"footnote","content":"+ \\fr 1:6 \\ft Footnote text.","endTag":"f*","nextChar":" "},
                                {"type":"text","text":"there.\n"}
                                ]},
           "7":{"verseObjects":[{"tag":"x","content":"- \\xo 1:7: \\xt 2Cor 4:6.","endTag":"x*"},
                                {"type":"text","text":"This verse started with a cross-reference.\n"}
                                ]},
           "front":{"verseObjects":[{"tag":"s","type":"section","content":"Section heading\n"},
                                    {"tag":"p","nextChar":"\n","type":"paragraph"}
                                    ]}
           }
    }
}
    """
    from Internals.InternalBibleInternals import BOS_ADDED_NESTING_MARKERS, BOS_NESTING_MARKERS

    createdFilenames = []
    if not os.access( outputFolder, os.F_OK ): os.makedirs( outputFolder ) # Make the empty folder if there wasn't already one there

    ignoredMarkers = set()

    # Save the individual books
    for BBB,bookObject in self.books.items():
        #USFMAbbreviation = BibleOrgSysGlobals.BibleBooksCodes.getUSFMAbbreviation( BBB )
        #USFMNumber = BibleOrgSysGlobals.BibleBooksCodes.getUSFMNumber( BBB )
        filename = BOOK_FILENAME.format( BBB )
        createdFilenames.append( filename )
        createUWJSONBibleBook( BBB, bookObject, ignoredMarkers )
        filepath = os.path.join( outputFolder, filename )
        with open( filepath, 'wt' ) as jsonOutputFile:
            jsonOutputFile.write( json.dumps( jsonDict ) )
        break # temp ONLY PROCESS ONE BOOK ............................... XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


    if ignoredMarkers:
        logging.info( "createUWJSONBible: Ignored markers were {}".format( ignoredMarkers ) )
        if BibleOrgSysGlobals.verbosityLevel > 2:
            print( "  " + _("WARNING: Ignored createUWJSONBible markers were {}").format( ignoredMarkers ) )

    # Now create a zipped version of the entire folder
    zipFilename = self.getAName( abbrevFirst=True )
    if debuggingThisModule or BibleOrgSysGlobals.debugFlag: assert zipFilename
    zipFilename = BibleOrgSysGlobals.makeSafeFilename( zipFilename+'.json.zip' )
    zipFilepath = os.path.join( outputFolder, zipFilename )
    if BibleOrgSysGlobals.verbosityLevel > 2: print( "  Zipping {} JSON files…".format( len(createdFilenames) ) )
    zf = zipfile.ZipFile( zipFilepath, 'w', compression=zipfile.ZIP_DEFLATED )
    for filename in createdFilenames:
        zf.write( os.path.join( outputFolder, filename ), filename )
    zf.close()

    if BibleOrgSysGlobals.verbosityLevel > 0 and BibleOrgSysGlobals.maxProcesses > 1:
        print( "  BibleWriter.createUWJSONBible finished successfully." )
    return True
# end of createUWJSONBible



def demo() -> None:
    """
    Demonstrate reading and checking some Bible databases.
    """
    if BibleOrgSysGlobals.verbosityLevel > 0: print( programNameVersion )


    if 0: # demo the file checking code -- first with the whole folder and then with only one folder
        for j,testFolder in enumerate( (
                            'Tests/DataFilesForTests/JSONBibleTest1/',
                            'Tests/DataFilesForTests/JSONBibleTest2/',
                            'Tests/DataFilesForTests/JSONBibleTest3/',
                            'Tests/DataFilesForTests/PTX7Test/',
                            'OutputFiles/BOS_JSONBible_Export/',
                            'OutputFiles/BOS_JSONBible_Reexport/',
                            'MadeUpFolder/',
                            ) ):
            if BibleOrgSysGlobals.verbosityLevel > 0:
                print( "\nPickle Bible A{} testfolder is: {}".format( j+1, testFolder ) )
            result1 = JSONBibleFileCheck( testFolder )
            if BibleOrgSysGlobals.verbosityLevel > 1: print( "Pickle Bible TestAa", result1 )
            result2 = JSONBibleFileCheck( testFolder, autoLoad=True )
            if BibleOrgSysGlobals.verbosityLevel > 1: print( "Pickle Bible TestAb", result2 )
            result3 = JSONBibleFileCheck( testFolder, autoLoadBooks=True )
            if BibleOrgSysGlobals.verbosityLevel > 1: print( "Pickle Bible TestAc", result3 )
            if isinstance( result3, Bible ):
                if BibleOrgSysGlobals.strictCheckingFlag:
                    result3.check()
                    #print( result3.books['GEN']._processedLines[0:40] )
                    pBibleErrors = result3.getErrors()
                    # print( UBErrors )
                if BibleOrgSysGlobals.commandLineArguments.export:
                    result3.json()
                    ##result3.toDrupalBible()
                    result3.doAllExports( wantPhotoBible=False, wantODFs=False, wantPDFs=False )


    if 0: # Load and process some of our test versions
        for j,(name, encoding, testFolder) in enumerate( (
                        ("Test1", 'utf-8', 'Tests/DataFilesForTests/JSONBibleTest1/'),
                        ("Test2", 'utf-8', 'Tests/DataFilesForTests/JSONBibleTest2/'),
                        ("Test3", 'utf-8', 'Tests/DataFilesForTests/JSONBibleTest3/'),
                        ("Exported1", 'utf-8', 'OutputFiles/BOS_JSONBible_Export/'),
                        ("Exported2", 'utf-8', 'OutputFiles/BOS_JSONBible_Reexport/'),
                        ) ):
            if os.access( testFolder, os.R_OK ):
                if BibleOrgSysGlobals.verbosityLevel > 0: print( "\nPickle Bible B{}/".format( j+1 ) )
                pBible = JSONBible( testFolder )
                pBible.load()
                if BibleOrgSysGlobals.verbosityLevel > 1:
                    print( "Gen assumed book name:", repr( pBible.getAssumedBookName( 'GEN' ) ) )
                    print( "Gen long TOC book name:", repr( pBible.getLongTOCName( 'GEN' ) ) )
                    print( "Gen short TOC book name:", repr( pBible.getShortTOCName( 'GEN' ) ) )
                    print( "Gen book abbreviation:", repr( pBible.getBooknameAbbreviation( 'GEN' ) ) )
                if BibleOrgSysGlobals.verbosityLevel > 0: print( pBible )
                if BibleOrgSysGlobals.strictCheckingFlag:
                    pBible.check()
                    #print( pBible.books['GEN']._processedLines[0:40] )
                    pBibleErrors = pBible.getErrors()
                    # print( UBErrors )
                if BibleOrgSysGlobals.commandLineArguments.export:
                    pBible.json()
                    ##pBible.toDrupalBible()
                    pBible.doAllExports( wantPhotoBible=False, wantODFs=False, wantPDFs=False )
                    newObj = BibleOrgSysGlobals.unpickleObject( BibleOrgSysGlobals.makeSafeFilename(name) + '.json', os.path.join( "OutputFiles/", "BOS_Bible_Object_Pickle/" ) )
                    if BibleOrgSysGlobals.verbosityLevel > 0: print( "newObj is", newObj )
                if 1:
                    from Reference.VerseReferences import SimpleVerseKey
                    from Internals.InternalBibleInternals import InternalBibleEntry
                    for BBB,C,V in ( ('MAT','1','1'),('MAT','1','2'),('MAT','1','3'),('MAT','1','4'),('MAT','1','5'),('MAT','1','6'),('MAT','1','7'),('MAT','1','8') ):
                        svk = SimpleVerseKey( BBB, C, V )
                        shortText = svk.getShortText()
                        verseDataList = pBible.getVerseDataList( svk )
                        if BibleOrgSysGlobals.verbosityLevel > 0:
                            print( "\n{}\n{}".format( shortText, verseDataList ) )
                        if verseDataList is None: continue
                        for verseDataEntry in verseDataList:
                            # This loop is used for several types of data
                            assert isinstance( verseDataEntry, InternalBibleEntry )
                            marker, cleanText, extras = verseDataEntry.getMarker(), verseDataEntry.getCleanText(), verseDataEntry.getExtras()
                            adjustedText, originalText = verseDataEntry.getAdjustedText(), verseDataEntry.getOriginalText()
                            fullText = verseDataEntry.getFullText()
                            if BibleOrgSysGlobals.verbosityLevel > 0:
                                print( "marker={} cleanText={!r}{}".format( marker, cleanText,
                                                        " extras={}".format( extras ) if extras else '' ) )
                                if adjustedText and adjustedText!=cleanText:
                                    print( ' '*(len(marker)+4), "adjustedText={!r}".format( adjustedText ) )
                                if fullText and fullText!=cleanText:
                                    print( ' '*(len(marker)+4), "fullText={!r}".format( fullText ) )
                                if originalText and originalText!=cleanText:
                                    print( ' '*(len(marker)+4), "originalText={!r}".format( originalText ) )
            elif BibleOrgSysGlobals.verbosityLevel > 0:
                print( "\nSorry, test folder {!r} is not readable on this computer.".format( testFolder ) )


    if 0: # Load a zipped version
        pBible = JSONBible( 'OutputFiles/BOS_JSONBible_Export/MBTV.json.zip' )
        print( "C1a:", pBible )
        pBible.load()
        print( "C1b:", pBible )
        assert pBible.jsonIsZipped # That's what we were supposedly testing


    if 1: # Compare unfoldingWord JSON with their own JS code outputs
        from USFMBibleBook import USFMBibleBook
        testFolder = BibleOrgSysGlobals.PARALLEL_RESOURCES_BASE_FOLDERPATH.joinpath( '../../../Programming/ExternalPrograms/usfm-js-test/' )
        for original_usfm_filename in os.listdir( testFolder ):
            if original_usfm_filename.endswith( '.usfm' ) and 'roundtripped' not in original_usfm_filename:
                basename = os.path.splitext(original_usfm_filename)[0]
                #original_usfm_filepath = os.path.join( testFolder, original_usfm_filename )
                #with open( original_usfm_filepath, 'rt' ) as usfm_input_file:
                    #input_usfm = usfm_input_file.read()
                #print( "input_usfm", input_usfm )
                print( f"Loading {original_usfm_filename}…" )
                BBB = 'TST'
                UBB = USFMBibleBook( "Test", BBB )
                UBB.load( original_usfm_filename, testFolder )
                UBB.processLines()
                our_json_dict = createUWJSONBibleBook( BBB, UBB, set() )
                print( "UBB", UBB )
                with open( os.path.join( testFolder, f'{basename}.json' ), 'rt' ) as json_compare_file:
                    uwJSONdict = json.loads( json_compare_file.read() )
                #print( "Compare JSON: ", uwJSON )
                if our_json_dict == uwJSONdict:
                    print( f"Got same result for {basename}." )
                else:
                    print( f"Got DIFFERENT result for {basename}!" )
                    if our_json_dict.keys() != uwJSONdict.keys():
                        print( len(our_json_dict), our_json_dict.keys() )
                        print( len(uwJSONdict), uwJSONdict.keys() )
                    if len(our_json_dict['headers']) != len(uwJSONdict['headers']):
                        print( len(our_json_dict['headers']), our_json_dict['headers'] )
                        for j, something in enumerate(our_json_dict['headers']):
                            print( f"  BOS {j+1}/ {something}" )
                        print( len(uwJSONdict['headers']), uwJSONdict['headers'] )
                        for j, something in enumerate(uwJSONdict['headers']):
                            print( f"  unW {j+1}/ {something}" )
                    if our_json_dict['chapters'].keys() != uwJSONdict['chapters'].keys():
                        print( len(our_json_dict['chapters']), our_json_dict['chapters'].keys() )
                        print( len(our_json_dict['chapters']), uwJSONdict['chapters'].keys() )
                break


    if 0: # Test BOS JSON output
        from USFMBible import USFMBible
        for j,testFolder in enumerate( (
                            #'Tests/DataFilesForTests/USFMTest1/',
                            'Tests/DataFilesForTests/USFMTest2/',
                            #'Tests/DataFilesForTests/USFMTest3/',
                            #'Tests/DataFilesForTests/USFM2AllMarkersProject/',
                            #'Tests/DataFilesForTests/USFM3AllMarkersProject/',
                            #'Tests/DataFilesForTests/USFMErrorProject/',
                            #'Tests/DataFilesForTests/PTX7Test/',
                            ) ):
            if BibleOrgSysGlobals.verbosityLevel > 0:
                print( "\nUSFM A{} testfolder is: {}".format( j+1, testFolder ) )
            UB = USFMBible( testFolder )
            if BibleOrgSysGlobals.verbosityLevel > 1: print( "USFM TestAa", UB )
            UB.loadBooks()
            if BibleOrgSysGlobals.verbosityLevel > 1: print( "USFM TestAb", UB )
            createBOSJSONBible( UB, outputFolder='OutputFiles/BOS_JSONBible_Export/', controlDict={} )
            createUWJSONBible( UB, outputFolder='OutputFiles/unfoldingWord_JSONBible_Export/', controlDict={} )
            createBCSJSONBible( UB, outputFolder='OutputFiles/BCS_JSONBible_Export/', controlDict={} )
#end of demo

if __name__ == '__main__':
    multiprocessing.freeze_support() # Multiprocessing support for frozen Windows executables

    # Configure basic Bible Organisational System (BOS) set-up
    parser = BibleOrgSysGlobals.setup( shortProgramName, programVersion )
    BibleOrgSysGlobals.addStandardOptionsAndProcess( parser, exportAvailable=True )

    demo()

    BibleOrgSysGlobals.closedown( shortProgramName, programVersion )
# end of JSONBible.py
