#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# DigitalBibleLibraryOnline.py
#
# Module handling online DBL resources
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
This module interfaces with the online Digital Bible Library
    managed by the ETEN partners.

We have public access to over 90 open access Bibles (or portions)
    as at Nov 2018 (107 in Dec 2019).
See https://app.thedigitalbiblelibrary.org/entries/public_domain_entries?type=text

In this module:
    DBL = Digital Bible Library

More details about the system are available from
    http://app.thedigitalbiblelibrary.org/static/docs/api/index.html
    (Version 4 in Dec 2019)
"""

from gettext import gettext as _

lastModifiedDate = '2019-12-15' # by RJH
shortProgramName = "DigitalBibleLibraryOnline"
programName = "Online Digital Bible Library handler"
programVersion = '0.08'
programNameVersion = f'{shortProgramName} v{programVersion}'
programNameVersionDate = f'{programNameVersion} {_("last modified")} {lastModifiedDate}'

debuggingThisModule = False


from typing import Dict, List, Any, Optional, Union
import os
import logging
import urllib.request, http.client # Last one is just for the exception class
import json
#from collections import OrderedDict
import re

if __name__ == '__main__':
    import sys
    sys.path.append( os.path.join(os.path.dirname(__file__), '../') ) # So we can run it from the above folder and still do these imports
from Misc.singleton import singleton
import BibleOrgSysGlobals


URL_BASE = 'https://TheDigitalBibleLibrary.org/'



@singleton # Can only ever have one instance
class DBLBibles:
    """
    Class to download and manipulate online DBL Bibles.

    """
    def __init__( self ) -> None:
        """
        Create the internal Bibles object.
        """
        if BibleOrgSysGlobals.debugFlag and debuggingThisModule:
            print( "DBLBibles.__init__()" )

        self.onlineFlag = False
        self.openAccessList = self.publicEntriesList = None

        # This was too long/slow -- need to find a request with a smaller response -- RJH Dec 2019
        if 0: # See if the site is online by making a small call to get the API version
            self.URLTest = 'api/public_entries_list' # Since we're not authenticated, we don't expect a long result
            result = self.getOnlineData( self.URLTest )
            if BibleOrgSysGlobals.debugFlag and debuggingThisModule:
                #print( "URL test result1", result )
                if result:
                    print( "URL test result2", len(result) )
            if len(result)==3 and 'count' in result and 'list' in result and 'offset' in result:
                #== {'count': 0, 'list': [], 'offset': 0}:
                if BibleOrgSysGlobals.debugFlag and debuggingThisModule:
                    print( "  URL test result count", result['count'] ) # 11,090 in Dec 2019
                    #print( "  URL test result list", len(result['list']) )
                    assert len(result['list']) == result['count']
                    print( "    URL test result list start", result['list'][:3] )
                    print( "    URL test result list end", result['list'][-3:] )
                    #print( "  URL test result offset", result['offset'] )
                    assert result['offset'] == 0
                self.onlineFlag = True
            else:
                logging.critical( "DBL Bibles appears to be offline." )
        else: # Just assume we're online
            self.onlineFlag = True
    # end of DBLBibles.__init__


    def __str__( self ) -> str:
        """
        Create a string representation of the DBLBibles object.
        """
        indent = 2
        result = "DBL online Bibles object"
        if self.onlineFlag: result += ('\n' if result else '') + ' '*indent + _("Online")
        if self.openAccessList:
            result += ('\n' if result else '') + ' '*indent + _("Open access entries: {:,}").format( len(self.openAccessList) )
            if debuggingThisModule or BibleOrgSysGlobals.verbosityLevel > 2:
                for j,entry in enumerate( self.openAccessList, start=1 ):
                    result += f"\n{'  '*indent}{j} '{entry['name']}' in {entry['language_name']} in {entry['country_name']}" \
                              f"\n{'  '*indent}       ID={entry['id']} Rev={entry['revision']} {entry['href']}"
                    if BibleOrgSysGlobals.verbosityLevel > 3:
                        result += f"\n{'  '*indent}     {entry}"
        if self.publicEntriesList:
            result += ('\n' if result else '') + ' '*indent + _("Public entries: {:,}").format( len(self.publicEntriesList) )
            if debuggingThisModule or BibleOrgSysGlobals.verbosityLevel > 2:
                for j,entry in enumerate( self.publicEntriesList[:100], start=1 ):
                    result += f"\n{'  '*indent}{j} '{entry['name']}' in {entry['language_name']} in {entry['country_name']}" \
                              f"\n{'  '*indent}      ID={entry['id']} Rev={entry['revision']} {entry['href']}"
                    if BibleOrgSysGlobals.verbosityLevel > 3:
                        result += f"\n{'  '*indent}     {entry}"
                if len(self.publicEntriesList) > 100:
                        result += f"\nList truncated at 100/{len(self.publicEntriesList):,} entries"
        #if self.volumeList: result += ('\n' if result else '') + ' '*indent + _("Volumes: {}").format( len(self.volumeList) )
        #if self.volumeNameDict: result += ('\n' if result else '') + ' '*indent + _("Displayable volumes: {}").format( len(self.volumeNameDict) )
        return result
    # end of DBLBibles.__str__


    def getOnlineData( self, fieldREST:str, additionalParameters:Optional[str]=None, maxTries:int=3 ) \
                                                                                -> Optional[Union[str,bytes]]:
        """
        Given a string, e.g., "api/apiversion"
            Does an HTTP GET to our site.
            Receives the JSON result (hopefully)
            Converts the JSON bytes to a JSON string
            Loads the JSON string into a Python container.
            Returns the container.

        Returns None if the data cannot be fetched.
        """
        if BibleOrgSysGlobals.debugFlag and debuggingThisModule:
            print( "DBLBibles.getOnlineData( {!r} {!r}, {} )".format( fieldREST, additionalParameters, maxTries ) )

        requestString = '{}{}{}'.format( '' if fieldREST.lower().startswith('http') else URL_BASE,
                                    fieldREST, '&'+additionalParameters if additionalParameters else '' )
        if debuggingThisModule: print( "Request string is", repr(requestString) )

        numTries = 0
        while True:
            if numTries>0 and BibleOrgSysGlobals.verbosityLevel > 0:
                print( '  ' + _("Retrying {}…").format( requestString ) )
            numTries += 1
            try:
                HTTPResponseObject = urllib.request.urlopen( requestString )
                break
            except urllib.error.URLError as err:
                #errorClass, exceptionInstance, traceback = sys.exc_info()
                #print( '{!r}  {!r}  {!r}'.format( errorClass, exceptionInstance, traceback ) )
                if 'HTTP Error 400: Bad Request' in str(err): # No use retrying
                    logging.critical( _("DBL fatal URLError '{}' from {}").format( err, requestString ) )
                    return None
                logging.critical( _("DBL URLError '{}' from {}").format( err, requestString ) )
                if numTries >= maxTries:
                    return None
            except http.client.RemoteDisconnected as err:
                # Can get: http.client.RemoteDisconnected: Remote end closed connection without response
                #errorClass, exceptionInstance, traceback = sys.exc_info()
                #print( '{!r}  {!r}  {!r}'.format( errorClass, exceptionInstance, traceback ) )
                logging.critical( _("DBL HTTPError '{}' from {}").format( err, requestString ) )
                if numTries >= maxTries:
                    return None

        if BibleOrgSysGlobals.debugFlag and debuggingThisModule: print( "HTTPResponseObject", HTTPResponseObject )
        contentType = HTTPResponseObject.info().get( 'content-type' )
        if BibleOrgSysGlobals.debugFlag and debuggingThisModule: print( "contentType", contentType )

        numTries = 0
        while True:
            if numTries>0 and BibleOrgSysGlobals.verbosityLevel > 0:
                print( '  ' + _("Retrying {}…").format( requestString ) )
            numTries += 1
            try:
                if contentType == 'application/zip':
                    responseZIP = HTTPResponseObject.read() # Loads the entire file into memory!
                    return responseZIP # (could just return the object)
                elif contentType == 'application/json':
                    responseJSON = HTTPResponseObject.read()
                    #print( "  responseJSON {:,} bytes".format( len(responseJSON) ) )
                    #print( "responseJSON", len(responseJSON), responseJSON )
                    responseJSONencoding = HTTPResponseObject.info().get_content_charset( 'utf-8' )
                    #print( "responseJSONencoding", responseJSONencoding )
                    responseSTR = responseJSON.decode( responseJSONencoding )
                    #print( "responseSTR", len(responseSTR), repr(responseSTR) )
                    return json.loads( responseSTR ) # Convert to a Python object
                elif contentType == 'text/html; charset=utf-8':
                    responseBytes = HTTPResponseObject.read()
                    responseHTML = responseBytes.decode( 'utf-8' )
                    return responseHTML
                else:
                    print( "contentType", repr(contentType) )
                    halt # Haven't had this contentType before
            except http.client.IncompleteRead as err:
                # Can get: http.client.ImcompleteRead: ImcompleteRead(6295583 bytes read, 722273 more expected)
                #errorClass, exceptionInstance, traceback = sys.exc_info()
                #print( '{!r}  {!r}  {!r}'.format( errorClass, exceptionInstance, traceback ) )
                logging.critical( _("DBL HTTPError '{}' from {}").format( err, requestString ) )
                if numTries >= maxTries:
                    return None
    # end of DBLBibles.getOnlineData


    def fetchOpenAccessList( self ) -> List[Dict[str,Any]]:
        """
        Download the open access list (actually dict) from DBL.

        The full list (without /latest/type/text) was about 56KB (153 entries) as of Feb 2018.
        The latest text list was about 21KB (56 entries) as of Feb 2018.
        """
        if BibleOrgSysGlobals.debugFlag and debuggingThisModule:
            print( "DBLBibles.fetchOpenAccessList()" )

        if BibleOrgSysGlobals.verbosityLevel > 1:
            print( '\n' + _("Downloading list of open access resources from DBL…") )

        openAccessDict = self.getOnlineData( '/api/open_access_entries_list/latest/type/text' )
        if BibleOrgSysGlobals.debugFlag and debuggingThisModule:
            #print( "  openAccessDict1", len(openAccessDict), openAccessDict.keys() )
            print( "  openAccessDict2", len(openAccessDict) )
        assert isinstance( openAccessDict, dict )
        assert len(openAccessDict) == 3
        assert 'count' in openAccessDict and 'list' in openAccessDict and 'offset' in openAccessDict
        assert openAccessDict['offset'] == 0
        self.openAccessList = openAccessDict['list']
        #print( "openAccessList", len(self.openAccessList) )
        assert isinstance( self.openAccessList, list )
        assert len(self.openAccessList) == openAccessDict['count']
        if self.openAccessList:
            entry0 = self.openAccessList[0]
            assert len(entry0) == 12
            for fieldname in ('name','confidential', 'rights_holder', 'obsolete', 'href',
                              'language_code', 'country_name', 'language_name',
                              'latest', 'type', 'id', 'revision'):
                assert fieldname in entry0
            assert entry0['confidential'] == False
            assert entry0['latest'] == True
            assert entry0['obsolete'] == False
            assert entry0['type'] == 'text'
        #for entry in self.openAccessList: print( '  ', entry )
        return self.openAccessList
    # end of DBLBibles.fetchOpenAccessList


    def fetchPublicEntriesList( self ) -> List[Dict[str,Any]]:
        """
        Download the public entries list (actually dict) from DBL.

        The full list (without /latest/type/text) was about 3MB (7,284 entries) as of Feb 2018.
        The latest text list was about 650MB (1,694 entries) as of Feb 2018.
        """
        if BibleOrgSysGlobals.debugFlag and debuggingThisModule:
            print( "DBLBibles.fetchPublicEntriesList()" )

        if BibleOrgSysGlobals.verbosityLevel > 1:
            print( '\n' + _("Downloading list of public resources from DBL…") )

        publicEntriesDict = self.getOnlineData( '/api/public_entries_list/latest/type/text' )
        if BibleOrgSysGlobals.debugFlag and debuggingThisModule:
            #print( "  publicEntriesDict1", len(publicEntriesDict), publicEntriesDict.keys() )
            print( "  publicEntriesDict2", len(publicEntriesDict) )
        assert isinstance( publicEntriesDict, dict )
        assert len(publicEntriesDict) == 3
        assert 'count' in publicEntriesDict and 'list' in publicEntriesDict and 'offset' in publicEntriesDict
        self.publicEntriesList = publicEntriesDict['list']
        #print( "publicEntriesList", len(self.publicEntriesList) )
        assert isinstance( self.publicEntriesList, list )
        assert len(self.publicEntriesList) == publicEntriesDict['count']
        if self.publicEntriesList:
            entry0 = self.publicEntriesList[0]
            print("pEL0", entry0)
            assert len(entry0) == 12
            for fieldname in ('name','confidential', 'rights_holder', 'obsolete', 'href',
                              'language_code', 'country_name', 'language_name',
                              'latest', 'type', 'id', 'revision'):
                assert fieldname in entry0
            assert entry0['confidential'] == False
            assert entry0['latest'] == True
            assert entry0['obsolete'] == False
            assert entry0['type'] == 'text'
        #for entry in self.publicEntriesList: print( '  ', entry )
        return self.publicEntriesList
    # end of DBLBibles.fetchPublicEntriesList


    def fetchVersion( self, versionDict:Dict[str,Any], folderPath:str ) -> bool:
        """
        The version dict is something like:
            {'name': 'World Messianic Bible British Edition', 'confidential': False, 'rights_holder': 'eBible.org',
            'obsolete': False, 'href': 'http://thedigitalbiblelibrary.org/api/entries/04da588535d2f823/revisions/5',
            'language_code': 'eng', 'country_name': 'United Kingdom', 'language_name': 'English', 'latest': True,
            'type': 'text', 'id': '04da588535d2f823', 'revision': 5}
        """
        if BibleOrgSysGlobals.debugFlag and debuggingThisModule:
            print( "DBLBibles.fetchVersion( {}, {} )".format( versionDict, folderPath ) )

        if BibleOrgSysGlobals.verbosityLevel > 1:
            print( '  ' + _("Downloading {} DBL version…").format( versionDict['name'] ) )

        #href = versionDict['href']
        #deleteLen = len( 'http://thedigitalbiblelibrary.org/' )
        #href = href[deleteLen:]
        #versionResult = self.getOnlineData( href )
        #print( "versionResult1", len(versionResult), versionResult )
        """
        Gives:
            Request string is 'https://TheDigitalBibleLibrary.org/api/entries/04da588535d2f823/revisions/5'
            responseJSON 2172 bytes
            versionResult 8 {'librarian_delegates': [], 'licenser_organizations': [], 'librarian_organizations': [],
                'licenser_delegates': [], 'archivist_organizations': [], 'licenses': [], 'archivist_delegates': [],
                'revision': {'languageCode': 'eng', 'dateCompleted': '2015-05-08', 'languageScript': 'Latin',
                    'countryCode': 'GB', 'bundleProducer': 'Paratext/7.6.54.99', 'idParatextName': 'engWMBBE',
                    'validates': True, 'obsolete': False, 'idBiblica': '', 'languageLDMLId': 'en',
                    'comments': 'Updated to eBible.org text of 11 July 2016; corrected old data upload problem with last update',
                    'idParatext': '04da588535d2f823596e2ff98f6e2df732b10dc9', 'id': '04da588535d2f823',
                    'nameAbbreviation': 'WMBBE', 'relationships': [], 'idGBC': '546a4f765117ad7230055b06',
                    'languageNumerals': 'Arabic', 'typeVersion': '2.1', 'idPtreg': '',
                    'archivist': 'Michael Johnson', 'idParatextCset': 'd1b6a1d3bb5ffd333dda8371b84044f80f5d421b',
                    'pubPromoVersionInfo': '      <p>This translation is a free, public domain (not copyrighted) translation of the Holy Bible. It was created from the World English Bible mostly by substituting Hebrew forms of names for Greek forms.</p>      <p>The World Messianic Bible British Edition is available for free reading and download at <a href="http://eBible.org/wmb/">eBible.org/wmb</a>. This text matches the eBible.org text as of 8 May 2015.</p>    ',
                    'scope': 'New Testament', 'dateUpdated': '2016-07-12T05:29:26.587081',
                    'nameAbbreviationLocal': '', 'entrytype': 'text', 'languageScriptDirection': 'LTR',
                    'dateArchived': '2014-09-24T20:22:06.337926',
                    'description': 'English: World Messianic Bible British Edition New Testament',
                    'confidential': 'false', 'languageDialectCode': '', 'nameCommonLocal': '',
                    'countryName': 'United Kingdom', 'idTMS': '', 'languageName': 'English',
                    'copyrightStatement': '        <p>\n        <a href="http://ebible.org/publicdomain.htm">PUBLIC DOMAIN</a>\n      </p>      ',
                    'obsoletedby': None, 'nameCommon': 'World Messianic Bible British Edition', 'idSIL': '',
                    'idParatextFullName': 'World Messianic Bible British Edition', 'translationType': 'Revision',
                    'languageLevel': 'Common', 'revision': '5', 'languageNameLocal': '', 'latest': True}}
        """

        #versionResult = self.getOnlineData( versionDict['href'] ) # Note this is http not https
        #print( "versionResult2", len(versionResult), versionResult )
        ## Gives exactly the same as above

        #versionResult = self.getOnlineData( 'api/entries/{}/revision/latest'.format( versionDict['id'] ) )
        #print( "versionResult3", len(versionResult), versionResult )
        ## Gives exactly the same as above

        #versionResult = self.getOnlineData( 'api/entries/{}/revision/latest/license/4019'.format( versionDict['id'] ) )
        #print( "versionResult4", len(versionResult), versionResult )
        ## Fails (forbidden)

        #versionResult = self.getOnlineData( 'api/entries/{}/revision/latest/license/4019.zip'.format( versionDict['id'] ) )
        #print( "versionResult5", len(versionResult), versionResult )
        ## Fails (forbidden)

        # How are we supposed to find the license number???
        licenseDict = { # The following were scraped and manually entered here
                        'Revised Version 1885':4018,
                        'World English Bibl':4019, 'World English Bible British Edition':4015,
                        'World Messianic Bible':4016, 'World Messianic Bible British Edition':4017 }
        try: licenseNumber = licenseDict[versionDict['name']]
        except: # Seems we need to scrape the webpage!!! (Is this intentional DBL obfuscation???)
            webPage = self.getOnlineData( 'entry?id={}'.format( versionDict['id'] ) )
            if webPage is None:
                logging.critical( f"Failed to fetch DBL '{versionDict['name']}' version…" )
                return
            print( "webPage:", type(webPage), len(webPage), webPage )
            """
            2018 response abd similar Dec 2019
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset='utf-8'/>
                <!--[if IE]>
                <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
                <![endif]-->
                <title>Digital Bible Library</title>
                <!-- http://dev.w3.org/html5/markup/meta.name.html -->
                <meta name="application-name" content="dbl"/>

                <!-- Google Tag Manager -->
                <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({\'gtm.start\':
                new Date().getTime(),event:\'gtm.js\'});var f=d.getElementsByTagName(s)[0],
                j=d.createElement(s),dl=l!=\'dataLayer\'?\'&l=\'+l:\'\';j.async=true;j.src=
                \'https://www.googletagmanager.com/gtm.js?id=\'+i+dl;f.parentNode.insertBefore(j,f);
                })(window,document,\'script\',\'dataLayer\',\'GTM-KZMKLBN\');</script>
                <!-- End Google Tag Manager -->

                <!--  Mobile Viewport Fix
                j.mp/mobileviewport & davidbcalhoun.com/2010/viewport-metatag
                device-width: Occupy full width of the screen in its current orientation
                initial-scale = 1.0 retains dimensions instead of zooming out if page height > device height
                user-scalable = yes allows the user to zoom in -->
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="shortcut icon" href="/dbl/static/images/dblfavicon.ico" type="image/x-icon">
                <link rel="apple-touch-icon" href="/dbl/static/images/dblfavicon.png">
            <script src="//cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>
            <script>
                if (typeof Modernizr === \'undefined\') {
                    document.write(decodeURI("%3Cscript src=\'/static/js/modernizr-custom.js\' type=\'text/javascript\'%3E%3C/script%3E"));
                }
            </script>
            <script src="https://code.jquery.com/jquery-3.0.0.min.js"></script>
            <script src="https://code.jquery.com/jquery-migrate-3.0.0.min.js"></script>
            <script>
                if (typeof jQuery === \'undefined\') {
                    document.write(decodeURI("%3Cscript src=\'/static/jquery-3.0.0/jquery.min.js\' type=\'text/javascript\'%3E%3C/script%3E"));
                    document.write(decodeURI("%3Cscript src=\'/static/jquery-3.0.0/jquery-migrate-3.0.0.min.js\' type=\'text/javascript\'%3E%3C/script%3E"));
                }
            </script>
            <script src=\'/static/js/lodash.min.js\' type=\'text/javascript\'></script>

            <link rel="stylesheet" id="google-font-css"
                href="//fonts.googleapis.com/css?family=Open+Sans%3A400italic%2C700italic%2C400%2C700&amp;ver=3.1.2"
                type="text/css" media="all">

            <link href="/static/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
            <link href="/static/bootstrap/3.3.5/css/bootstrap-theme.min.css" rel="stylesheet">

            <script src="/static/bootstrap/3.3.5/js/bootstrap.js"></script>
            <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" rel="stylesheet">

                <link href="/dbl/static/css/dbl.css" rel="stylesheet" type="text/css">
                <script src="/dbl/static/js/dbl.js"></script>
            </head>

            <body>
            <!-- Google Tag Manager (noscript) -->
            <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KZMKLBN"
            height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
            <!-- End Google Tag Manager (noscript) -->


            <!-- Navbar ================================================== -->
            <nav class="navbar navbar-inverse navbar-fixed-top fh-fixedHeader">
                <div class="container">
                    <div class="navbar-header">
                        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-collapse">
                            <span class="sr-only">Toggle navigation</span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </button>
                        <a class="navbar-brand" href="/" style="min-width: 75px;"><img
                                src="/static/images/DBL-logo-icon48.png" alt="DBL" style="position: absolute; top:0px;"></a>
                    </div>
                    <!-- Collect the nav links, forms, and other content for toggling -->
                    <div class="collapse navbar-collapse" id="navbar-collapse">

            \t\t    <ul class="nav navbar-nav"><li class="dropdown"><a href="#">Text</a><ul class="dropdown-menu"><li><a href="/entries/public_domain_entries?type=text">Open Access Text Entries</a></li></ul></li><li class="dropdown"><a href="#">Audio</a><ul class="dropdown-menu"><li><a href="/entries/public_domain_entries?type=audio">Open Access Audio Entries</a></li></ul></li><li class="dropdown"><a href="#">Video</a><ul class="dropdown-menu"><li><a href="/entries/public_domain_entries?type=video">Open Access Video Entries</a></li></ul></li><li class="dropdown"><a href="#">Print</a><ul class="dropdown-menu"><li><a href="/entries/public_domain_entries?type=print">Open Access Print Entries</a></li></ul></li><li class="dropdown"><a href="#">Braille</a><ul class="dropdown-menu"><li><a href="/entries/public_domain_entries?type=braille">Open Access Braille Entries</a></li></ul></li><li class="web2py-menu-last"><a href="/static/docs/index.html" target="_blank">Help</a></li></ul>
            \t\t

            \t\t    <ul class="nav navbar-nav navbar-right"><li class="web2py-menu-first"><a href="/user/login">Login</a></li><li class="web2py-menu-last"><a href="/user/request_reset_password">Lost password?</a></li></ul>
            \t\t
                    </div>
                </div>
            </nav>
            <!-- place navbar js before the page content loads. -->
            <script>
                $("#login_menu_profile").click(function (ev) {
                    ajaxy.showModal("/users/edit_user.html?user=None");
                });

                // this code improves bootstrap menus and adds dropdown support
                $(function () {
                    $(\'.nav>li>a\').each(function () {
                        if ($(this).parent().find(\'ul\').length)
                            $(this).attr({
                                \'class\': \'dropdown-toggle\',
                                \'data-toggle\': \'dropdown\'
                            }).append(\'<b class="caret"></b>\');
                    });
                    $(\'.nav li li\').each(function () {
                        if ($(this).find(\'ul\').length)
                            $(this).children(\'a\').contents().before(\'<span class="glyphicon glyphicon-chevron-right"></span>\');
                    });
                    if ($(document).width() >= 980) {
                        $(\'ul.nav li.dropdown\').hover(function () {
                            $(this).find(\'.dropdown-menu\').stop(true, true).delay(200).fadeIn();
                        }, function () {
                            $(this).find(\'.dropdown-menu\').stop(true, true).delay(200).fadeOut();
                        });
                    }
                    $(\'ul.nav li.dropdown a\').click(function () {
                        window.location = $(this).attr(\'href\');
                    });
                });
            </script>

            <div class="container">
                <header class="mastheader" id="header">
                    <div id="header-vertical-space" style="min-height: 40px;"></div>
                </header>
                <section id="main" class="main clearfix">


            <h2 class="entry_header text">World Messianic Bible British Edition</h2>
            <!-- requires entry_metadata, an object of type EntryMetadata -->

            <div>
                <div id="entry-metadata-collapse5389">
                    <div>
                        <h4>Metadata</h4>
                        <div>
                            <div>
                                <span class="text-muted">Language Name</span>:
                                <span>English</span>
                            </div>

                            <div>
                                <span class="text-muted">Language Local Name</span>:
                                <span></span>
                            </div>

                            <div>
                                <span class="text-muted">Language Code</span>:
                                <span>eng</span>
                            </div>

                            <div>
                                <span class="text-muted">Script</span>:
                                <span>Latin</span>
                            </div>

                            <div>
                                <span class="text-muted">Country Name</span>:
                                <span>United Kingdom</span>
                            </div>

                            <div>
                                <span class="text-muted">Common Version Name</span>:
                                <span>World Messianic Bible British Edition</span>
                            </div>

                            <div>
                                <span class="text-muted">Version Abbreviation</span>:
                                <span>WMBBE</span>
                            </div>

                            <div>
                                <span class="text-muted">Scope</span>:
                                <span>New Testament</span>
                            </div>

                            <div>
                                <span class="text-muted">Completion Date</span>:
                                <span>2015-05-08</span>
                            </div>

                            <div>
                                <span class="text-muted">Last Archive Date</span>:
                                <span>2016-07-12T05:29:26.587081</span>
                            </div>

                            <div>
                                <span class="text-muted">Comments</span>:
                                <span>Updated to eBible.org text of 11 July 2016; corrected old data upload problem with last update</span>
                            </div>

                            <div>
                                <span class="text-muted">Project Archive ID</span>:
                                <span>04da588535d2f823</span>
                            </div>

                            <div>
                                <span class="text-muted">Revision</span>:
                                <span>5</span>
                            </div>

                            <div>
                                <span class="text-muted">Bundle Type Version</span>:
                                <span>2.1</span>
                            </div>

                            <a href="#" onclick="javascript:$(this).next(\'#other-metadata\').slideToggle(\'fast\')">More\xe2\x80\xa6</a>

                            <div style="display:none" id="other-metadata">

                                <div>
                                    <span class="text-muted">Archivist</span>:
                                    <span>Michael Johnson</span>
                                </div>

                                <div>
                                    <span class="text-muted">Bundle Producer</span>:
                                    <span>Paratext/7.6.54.99</span>
                                </div>

                                <div>
                                    <span class="text-muted">Confidential Project</span>:
                                    <span>false</span>
                                </div>

                                <div>
                                    <span class="text-muted">Rights Information Statement</span>:
                                    <span>        <p>
                    <a href="http://ebible.org/publicdomain.htm">PUBLIC DOMAIN</a>
                </p>      </span>
                                </div>

                                <div>
                                    <span class="text-muted">Country Code</span>:
                                    <span>GB</span>
                                </div>

                                <div>
                                    <span class="text-muted">Original Archive Date</span>:
                                    <span>2014-09-24T20:22:06.337926</span>
                                </div>

                                <div>
                                    <span class="text-muted">Description</span>:
                                    <span>English: World Messianic Bible British Edition New Testament</span>
                                </div>

                                <div>
                                    <span class="text-muted">Biblica Project Id</span>:
                                    <span></span>
                                </div>

                                <div>
                                    <span class="text-muted">GBC Entry Id</span>:
                                    <span>546a4f765117ad7230055b06</span>
                                </div>

                                <div>
                                    <span class="text-muted">Paratext GUID</span>:
                                    <span>04da588535d2f823596e2ff98f6e2df732b10dc9</span>
                                </div>

                                <div>
                                    <span class="text-muted">Paratext Changeset Id</span>:
                                    <span>d1b6a1d3bb5ffd333dda8371b84044f80f5d421b</span>
                                </div>

                                <div>
                                    <span class="text-muted">Paratext Project Full Name</span>:
                                    <span>World Messianic Bible British Edition</span>
                                </div>

                                <div>
                                    <span class="text-muted">Paratext Project Name</span>:
                                    <span>engWMBBE</span>
                                </div>

                                <div>
                                    <span class="text-muted">Paratext Registry Id</span>:
                                    <span></span>
                                </div>

                                <div>
                                    <span class="text-muted">SIL Project Id</span>:
                                    <span></span>
                                </div>

                                <div>
                                    <span class="text-muted">TMS Project Id</span>:
                                    <span></span>
                                </div>

                                <div>
                                    <span class="text-muted">HIS Dialect Code</span>:
                                    <span></span>
                                </div>

                                <div>
                                    <span class="text-muted">Unicode LDML Language ID</span>:
                                    <span>en</span>
                                </div>

                                <div>
                                    <span class="text-muted">Language Level</span>:
                                    <span>Common</span>
                                </div>

                                <div>
                                    <span class="text-muted">Numeral System</span>:
                                    <span>Arabic</span>
                                </div>

                                <div>
                                    <span class="text-muted">Script Direction</span>:
                                    <span>LTR</span>
                                </div>

                                <div>
                                    <span class="text-muted">Version Abbreviation Local</span>:
                                    <span></span>
                                </div>

                                <div>
                                    <span class="text-muted">Common Version Name Local</span>:
                                    <span></span>
                                </div>

                                <div>
                                    <span class="text-muted">Promotion Version Info</span>:
                                    <span>      <p>This translation is a free, public domain (not copyrighted) translation of the Holy Bible. It was created from the World English Bible mostly by substituting Hebrew forms of names for Greek forms.</p>      <p>The World Messianic Bible British Edition is available for free reading and download at <a href="http://eBible.org/wmb/">eBible.org/wmb</a>. This text matches the eBible.org text as of 8 May 2015.</p>    </span>
                                </div>

                                <div>
                                    <span class="text-muted">Translation Type</span>:
                                    <span>Revision</span>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
                <script>
                    ajaxy.convertToPanelGroup("#entry-metadata-collapse5389", "glyphicon-list-alt", true);
                </script>
            </div>

            <div id="entry-download-bundles" class="ajaxy-partial"
                data-url="/entry/download_bundles?id=04da588535d2f823">
            <div id="download-bundles-collapse">
                <div>
                    <h4>
                    Download
                    </h4>
                    <ul class="list-group">

                        <li class="list-group-item"><a href="/entry/download_listing?id=04da588535d2f823&amp;license=4017&amp;revision=">Download Publishable Project As Open Access (Public Domain [DBL])</a></li>


                    </ul>
                </div>
            </div>
            <script>

                ajaxy.convertToPanelGroup("#download-bundles-collapse", "glyphicon-download-alt");
            </script>

            </div>

            <div id="managing-organizations-accordion">
                <div>
                    <h4>Managing Organizations</h4>
                    <div>
                        <div id="ownerships-table"
                            class="ajaxy-partial"
                            data-url="/entry/entry_ownerships_table?id=04da588535d2f823">

            <table class="table table-striped" id="ownerships_table">
                <colgroup>
                    <col span="1">
                    <col span="4">
                </colgroup>
                <thead>
                <tr>
                    <th class="userPropCol">Organization</th>
                </tr>
                </thead>
                <tbody>
                <tr data-id="1154">
                    <td><a href="/orgs_catalog/org_details?org=44">eBible.org</a> <span
                            class="text-muted">(owner)</span>
                    </td>
                </tr>
                </tbody>
            </table>
                        </div>
                    </div>
                </div>
            </div>

            <script>
                ajaxy.convertToPanelGroup("#managing-organizations-accordion", "glyphicon-home");
            </script>
                </section>
            </div>
            <footer class="footer content clearfix" id="footer">
                <div class="footer-content">
                    <div class="copyright pull-left">
                    Copyright &#169; 2018 <a target="_blank" href="http://www.unitedbiblesocieties.org/">United Bible
                        Societies</a>. All rights reserved.
                    </div>
                </div>
            </footer>
            </body>
            </html>
            """
            match = re.search( '&amp;license=(\d{2,5})&amp;', webPage )
            if match:
                print( "Matched", match.start(), match.end() )
                print( repr(match.group(0)), repr(match.group(1)) )
                licenseNumber = match.group(1)
                if debuggingThisModule or BibleOrgSysGlobals.verbosityLevel > 2:
                    print( '    ' + _("License number for {!r} is {}").format( versionDict['name'], licenseNumber ) )
            else:
                logging.critical( _("Unable to find license number for {!r}").format( versionDict['name'] ) )
                if debuggingThisModule or BibleOrgSysGlobals.verbosityLevel > 2:
                    print( "Page is: {}".format( webPage ) )
                #licenseNumber = None
                return

        #downloadResult = self.getOnlineData( f"entry/download_listing?id={versionDict['id']}&license={licenseNumber}&revision={versionDict['revision']}" )
        #if downloadResult:
            #assert isinstance( downloadResult, str )
            #print( "downloadResult", type(downloadResult), len(downloadResult), downloadResult )

        # Got this link from the website for open access texts downloads
        downloadResult = self.getOnlineData( f"entry/download_archive?id={versionDict['id']}&license={licenseNumber}&revision={versionDict['revision']}&type=release" )
        if downloadResult:
            if debuggingThisModule:
                print( "downloadResult bytes", len(downloadResult), downloadResult[:5]+'…' )
            if isinstance( downloadResult, bytes ):
                #print( "downloadResult", type(downloadResult), len(downloadResult), downloadResult[:5]+'…' )
                try: os.makedirs( folderPath )
                except FileExistsError: pass
                filepath = os.path.join( folderPath, f"{versionDict['name']}.{versionDict['language_code']}.Rev{versionDict['revision']}.DBL.zip" )
                if BibleOrgSysGlobals.verbosityLevel > 0:
                    print( '    ' + _("Saving {:,} bytes to {}…").format( len(downloadResult), filepath ) )
                with open( filepath, 'wb' ) as zipFile:
                    zipFile.write( downloadResult )
                    return True
            elif isinstance( downloadResult, str ):
                if debuggingThisModule:
                    print( "downloadResult str!", len(downloadResult), downloadResult )
        return False
    # end of DBLBibles.fetchVersion


    def fetchVersionDetails( self, versionDict:Dict[str,Any] ) -> Dict[str,Any]:
        """
        The version dict is something like:
            {'name': 'World Messianic Bible British Edition', 'confidential': False, 'rights_holder': 'eBible.org',
            'obsolete': False, 'href': 'http://thedigitalbiblelibrary.org/api/entries/04da588535d2f823/revisions/5',
            'language_code': 'eng', 'country_name': 'United Kingdom', 'language_name': 'English', 'latest': True,
            'type': 'text', 'id': '04da588535d2f823', 'revision': 5}
        """
        if BibleOrgSysGlobals.debugFlag and debuggingThisModule:
            print( f"DBLBibles.fetchVersionDetails( {versionDict} )" )

        if BibleOrgSysGlobals.verbosityLevel > 1:
            print( '  ' + _("Fetching {} details from DBL…").format( versionDict['name'] ) )

        href = versionDict['href'] # Oh dear, this just gives more detailed JSON info
        assert href.startswith( 'http://thedigitalbiblelibrary.org/' )
        deleteLen = len( 'http://thedigitalbiblelibrary.org/' )
        href = href[deleteLen:]
        versionResult = self.getOnlineData( href )
        if BibleOrgSysGlobals.debugFlag and debuggingThisModule:
            print( "versionResult1", len(versionResult), versionResult )
        assert len(versionResult) == 8
        for fieldname in ('librarian_delegates','licenser_organizations', 'librarian_organizations',
                            'licenser_delegates', 'archivist_organizations',
                            'licenses', 'archivist_delegates', 'revision'):
            assert fieldname in versionResult
            if fieldname != 'revision': # All the rest are empty lists
                assert isinstance( versionResult[fieldname], list )
                assert not versionResult[fieldname]
        #print( len(versionResult['revision']), versionResult['revision'].keys() )
        assert len(versionResult['revision']) == 46
        for fieldname in ('languageCode', 'dateCompleted', 'languageScript', 'countryCode',
                          'bundleProducer', 'languageScriptCode', 'idParatextName', 'validates',
                          'obsolete', 'idBiblica', 'languageLDMLId', 'comments', 'idParatext', 'id',
                          'nameAbbreviation', 'relationships', 'idGBC', 'languageNumerals', 'typeVersion',
                          'idPtreg', 'archivist', 'idParatextCset', 'pubPromoVersionInfo', 'scope',
                          'dateUpdated', 'nameAbbreviationLocal', 'entrytype', 'languageScriptDirection',
                          'dateArchived', 'description', 'confidential', 'languageDialectCode',
                          'nameCommonLocal', 'countryName', 'idTMS', 'languageName', 'copyrightStatement',
                          'obsoletedby', 'nameCommon', 'idSIL', 'idParatextFullName', 'translationType',
                          'languageLevel', 'revision', 'languageNameLocal', 'latest'):
            assert fieldname in versionResult['revision']
        assert versionResult['revision']['confidential'] in (False, 'false') # Oops -- inadequate data checking in DBL
        assert versionResult['revision']['obsolete'] in (False, 'false')
        assert versionResult['revision']['latest'] == True
        assert versionResult['revision']['validates'] == True
        assert versionResult['revision']['obsoletedby'] is None
        return versionResult
    # end of DBLBibles.fetchVersionDetails


    def findAndFetch( self, versionName:str, folderPath:str ) -> Optional[bool]:
        """
        """
        for entry in self.openAccessList:
            if entry['name'] == versionName:
                detailsDict = self.fetchVersionDetails( entry )
                return self.fetchVersion( entry, folderPath )
        logging.warning( f"Unable to find '{versionName}' in versions list ({len(self.openAccessList)} entries)" )
# end of class DBLBibles



#class DBLBible:
    #"""
    #Class to download and manipulate an online DBL Bible.

    #Note that this Bible class is NOT based on the Bible class
        #because it's so unlike most Bibles which are local.
    #"""
    #def __init__( self, damRoot ):
        #"""
        #Create the Digital Bible Library Bible object.
            #Accepts a 6-character code which is the initial part of the DAM:
                #1-3: Language code, e.g., ENG
                #4-6: Version code, e.g., ESV
        #"""
        #if BibleOrgSysGlobals.debugFlag and debuggingThisModule:
            #print( "DBLBible.__init__( {!r} )".format( damRoot ) )
            #assert damRoot and isinstance( damRoot, str ) and len(damRoot)==6
        #self.damRoot = damRoot

         ## Setup and initialise the base class first
        ##InternalBible.__init__( self, givenFolderName, givenName, encoding )

        #self.key = getSecurityKey() # Our personal key
        #self.URLFixedData = "?v={}&key={}".format( DPB_VERSION, self.key )

        ## See if the site is online by making a small call to get the API version
        #self.URLTest = "api/apiversion"
        #self.onlineVersion = None
        #result = self.getOnlineData( self.URLTest )
        #if result:
            #if 'Version' in result: self.onlineVersion = result['Version']
        #else:
            #logging.critical( "DPBBible.__init__: Digital Bible Library appears to be offline" )
            #raise ConnectionError # What should this really be?

        #self.bookList = None
        #if self.onlineVersion: # Check that this particular resource is available by getting a list of books
            #bookList = self.getOnlineData( "library/book", "dam_id="+self.damRoot ) # Get an ordered list of dictionaries -- one for each book
            #if BibleOrgSysGlobals.debugFlag and debuggingThisModule: print( "DBLBible.__init__: bookList", len(bookList))#, bookList )

            ##if 0:# Get all book codes and English names
                ##bookCodeDictList = self.getOnlineData( "library/bookname", "language_code=ENG" )
                ### Not sure why it comes back as a dictionary in a one-element list
                ##assert isinstance( bookCodeDictList, list ) and len(bookCodeDictList)==1
                ##bookCodeDict = bookCodeDictList[0]
                ##assert isinstance( bookCodeDict, dict )
                ##print( "bookCodeDict", len(bookCodeDict), bookCodeDict )

        #self.books = {}
        #if bookList: # Convert to a form that's easier for us to use later
            #for bookDict in bookList:
                #OSISCode = bookDict['book_id']
                ##print( "OSIS", OSISCode )
                #BBB = BibleOrgSysGlobals.BibleBooksCodes.getBBBFromOSISAbbreviation( OSISCode )
                #if isinstance( BBB, list ): BBB = BBB[0] # Take the first one if we get something like ['EZR','EZN']
                ##print( "BBB", BBB )
                ##print( bookDict )
                #self.books[BBB] = bookDict
            #del bookList

        #self.cache = {}
    ## end of DBLBible.__init__


    #def __str__( self ):
        #"""
        #Create a string representation of the Bible object.
        #"""
        #indent = 2
        #result = "DBL online Bible object"
        #if self.onlineVersion: result += ('\n' if result else '') + ' '*indent + _("Online version: {}").format( self.onlineVersion )
        #result += ('\n' if result else '') + ' '*indent + _("DAM root: {}").format( self.damRoot )
        #if self.books: result += ('\n' if result else '') + ' '*indent + _("Books: {}").format( len(self.books) )
        #return result
    ## end of DBLBible.__str__


    #def __len__( self ):
        #"""
        #This method returns the number of books in the Bible.
        #"""
        #return len( self.books )
    ## end of DBLBible.__len__


    #def __contains__( self, BBB ):
        #"""
        #This method checks whether the Bible contains the BBB book.
        #Returns True or False.
        #"""
        #if BibleOrgSysGlobals.debugFlag:
            #assert isinstance(BBB,str) and len(BBB)==3

        #return BBB in self.books
    ## end of DBLBible.__contains__


    #def __getitem__( self, keyIndex ):
        #"""
        #Given an index, return the book object (or raise an IndexError)
        #"""
        #if BibleOrgSysGlobals.debugFlag and debuggingThisModule:
            #print( "DBLBible.__getitem__( {!r} )".format( keyIndex ) )

        #return list(self.books.items())[keyIndex][1] # element 0 is BBB, element 1 is the book object
    ## end of DBLBible.__getitem__


    #def getOnlineData( self, fieldREST, additionalParameters=None ):
        #"""
        #Given a string, e.g., "api/apiversion"
            #Does an HTTP GET to our site.
            #Receives the JSON result (hopefully)
            #Converts the JSON bytes to a JSON string
            #Loads the JSON string into a dictionary
            #Returns the dictionary.
        #Returns None if the data cannot be fetched.
        #"""
        #if BibleOrgSysGlobals.debugFlag and debuggingThisModule:
            #print( "DBLBible.getOnlineData( {!r} {!r} ").format( fieldREST, additionalParameters ) )

        #if BibleOrgSysGlobals.verbosityLevel > 2: print( "Requesting data from {} for {}…".format( URL_BASE, self.damRoot ) )
        #requestString = "{}{}{}{}".format( URL_BASE, fieldREST, self.URLFixedData, '&'+additionalParameters if additionalParameters else '' )
        ##print( "Request string is", repr(requestString) )
        #try: responseJSON = urllib.request.urlopen( requestString )
        #except urllib.error.URLError:
            #if BibleOrgSysGlobals.debugFlag: logging.critical( "DBLBible.getOnlineData: error fetching {!r} {!r}".format( fieldREST, additionalParameters ) )
            #return None
        #responseSTR = responseJSON.read().decode('utf-8')
        #return json.loads( responseSTR )
    ## end of DBLBible.getOnlineData


    #def getVerseDataList( self, key ):
        #"""
        #Equivalent to the one in InternalBible, except we may have to fetch the data (if it's not already cached).
        #"""
        #if BibleOrgSysGlobals.debugFlag and debuggingThisModule:
            #print( "DBLBible.getVerseDataList( {!r} ) for {!r}".format( key, self.damRoot ) )

        #if str(key) in self.cache:
            #if BibleOrgSysGlobals.debugFlag and debuggingThisModule: print( "  " + _("Retrieved from cache") )
            #self.cache.move_to_end( str(key) )
            #return self.cache[str(key)]
        #BBB = key.getBBB()
        #if BBB in self.books:
            #info = self.books[BBB]
            #rawData = self.getOnlineData( "text/verse", "dam_id={}&book_id={}&chapter_id={}&verse_start={}".format( info['dam_id']+'2ET', info['book_id'], key.getChapterNumber(), key.getVerseNumber() ) )
            #resultList = []
            #if isinstance( rawData, list ) and len(rawData)==1:
                #rawDataDict = rawData[0]
                ##print( len(rawDataDict), rawDataDict )
                #assert len(rawDataDict)==8 and isinstance( rawDataDict, dict )
                #resultList.append( ('p#','p#',rawDataDict['paragraph_number'],rawDataDict['paragraph_number'],[]) ) # Must be first for Biblelator
                #if key.getVerseNumber()=='1': resultList.append( ('c#','c#',rawDataDict['chapter_id'],rawDataDict['chapter_id'],[]) )
                #resultList.append( ('v','v',rawDataDict['verse_id'],rawDataDict['verse_id'],[]) )
                #resultList.append( ('v~','v~',rawDataDict['verse_text'].strip(),rawDataDict['verse_text'].strip(),[]) )
                #self.cache[str(key)] = resultList
                #if len(self.cache) > MAX_CACHED_VERSES:
                    ##print( "Removing oldest cached entry", len(self.cache) )
                    #self.cache.popitem( last=False )
            #return resultList
        #else: # This version doesn't have this book
            #if debuggingThisModule or BibleOrgSysGlobals.verbosityLevel > 2:
                #print( "  getVerseDataList: {} not in {} {}".format( BBB, self.damRoot, self.books.keys() ) )
    ## end of DBLBible.getVerseDataList


    #def getContextVerseData( self, key ):
        #"""
        #Given a BCV key, get the verse data.

        #(The Digital Bible Library doesn't provide the context so an empty list is always returned.)
        #"""
        #if BibleOrgSysGlobals.debugFlag and debuggingThisModule:
            #print( "DBLBible.getContextVerseData( {!r} ) for {!r}".format( key, self.damRoot ) )

        #return self.getVerseDataList( key ), [] # No context
    ## end of DBLBible.getContextVerseData
## end of class DBLBible



def demo() -> None:
    """
    Demonstrate how some of the above classes can be used.
    """
    if BibleOrgSysGlobals.verbosityLevel > 0: print( programNameVersion, end='\n\n' )

    # Test the DBLBibles class
    dbpBibles = DBLBibles()
    if BibleOrgSysGlobals.verbosityLevel > 0:
        print( "A1 dbpBibles =", dbpBibles )
    if dbpBibles.onlineFlag:
        dbpBibles.fetchOpenAccessList() # 100+ entries
        if BibleOrgSysGlobals.verbosityLevel > 0:
            print( "A2 dbpBibles =", dbpBibles, end='\n\n' )
        if 0: # This can be slow
            dbpBibles.fetchPublicEntriesList() # 2,000+ entries
            if BibleOrgSysGlobals.verbosityLevel > 0:
                print( "A3 dbpBibles =", dbpBibles, end='\n\n' )

    downloadFolder = BibleOrgSysGlobals.DOWNLOADED_RESOURCES_FOLDERPATH.joinpath( 'DBLOnline/' )
    if 0:
        if BibleOrgSysGlobals.verbosityLevel > 0:
            print( "\nDownloading {} openAccess Bibles…".format( len(dbpBibles.openAccessList) ) )
        try: os.makedirs( downloadFolder )
        except FileExistsError: pass
        for n, entry in enumerate( dbpBibles.openAccessList, start=1 ):
            print( f"{n}/" )
            dbpBibles.fetchVersion( entry, downloadFolder )


    testRefs = ( ('GEN','1','1'), ('JER','33','3'), ('MAL','4','6'),
                 ('MAT','1','1'), ('JHN','3','16'), ('JDE','1','14'), ('REV','22','21'), )

    if 1: # Test the DBLBible class with the RV
        if BibleOrgSysGlobals.verbosityLevel > 0: print()
        dbpBible1 = dbpBibles.findAndFetch( 'Revised Version 1885', downloadFolder )
        if BibleOrgSysGlobals.verbosityLevel > 0: print( "dbpBible1:", dbpBible1 )
        #for testRef in testRefs:
            #verseKey = SimpleVerseKey( *testRef )
            #print( verseKey )
            #print( " ", dbpBible1.getVerseDataList( verseKey ) )
         ## Now test the DBLBible class caching
        #for testRef in testRefs:
            #verseKey = SimpleVerseKey( *testRef )
            #print( verseKey, "cached" )
            #print( " ", dbpBible1.getVerseDataList( verseKey ) )


    #if 0: # Test the DBLBible class with the MS
        #if BibleOrgSysGlobals.verbosityLevel > 0: print()
        #dbpBible2 = DBLBible( "MBTWBT" )
        #if BibleOrgSysGlobals.verbosityLevel > 0: print( "dbpBible2:", dbpBible2 )
        #for testRef in testRefs:
            #verseKey = SimpleVerseKey( *testRef )
            #print( verseKey )
            #print( " ", dbpBible2.getVerseDataList( verseKey ) )
# end of demo

if __name__ == '__main__':
    from multiprocessing import freeze_support
    freeze_support() # Multiprocessing support for frozen Windows executables

    # Configure basic Bible Organisational System (BOS) set-up
    parser = BibleOrgSysGlobals.setup( programName, programVersion )
    BibleOrgSysGlobals.addStandardOptionsAndProcess( parser )

    demo()

    BibleOrgSysGlobals.closedown( programName, programVersion )
# end of DigitalBibleLibraryOnline.py
