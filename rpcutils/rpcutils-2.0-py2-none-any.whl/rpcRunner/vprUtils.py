#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import re 
import sys
import json
import shutil
from datetime import datetime
from collections import OrderedDict, defaultdict
import logging
from logging.handlers import RotatingFileHandler
from logging import handlers

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
from xml.etree.ElementTree import dump as dumpEl
from xml.etree.ElementTree import tostring as strEl

"""
## Invoking VPR with RPC Runner - XML into JSON

```text
from fmqlutils.fmqlIF.brokerRPC import VistARPCConnection, RPCLogger

connection = VistARPCConnection(HOSTDIRECT, PORTDIRECT, ACCESS, VERIFY, "VPR APPLICATION PROXY", RPCLogger())
tj = VPRXMLToJSON()
for patientName, patientIEN in PATIENTS:
    for dataType in TYPES:
        replyFile = dataType + ".xml"
        reply = connection.invokeRPC("VPR GET PATIENT DATA", [patientIEN, dataType])
        open(replyFile, "w").write(reply) 
        jsnData = tj.transform(replyFile, patientIEN, dataType)
        json.dump(jsnData, open(re.sub(r'\.xml$', '.json', replyFile), "w"), indent=4) 
```

Notes:
  * User (FMQL,USER being reused) must have access to "VPR APPLICATION PROXY" secondary menu option

Select VA FileMan <TEST ACCOUNT> Option: ENTER or Edit File Entries

Input to what File: NEW PERSON//          (256040 entries)

EDIT WHICH FIELD: ALL// 203  SECONDARY MENU OPTIONS  (multiple)

   EDIT WHICH SECONDARY MENU OPTIONS SUB-FIELD: ALL// .01  SECONDARY MENU OPTION

S

   THEN EDIT SECONDARY MENU OPTIONS SUB-FIELD:

THEN EDIT FIELD:

 
Select NEW PERSON NAME: USER,FMQL       FMQL   

Select SECONDARY MENU OPTIONS: CG FMQL QP USER// VPR APPLICATION PROXY       VPR

Application Proxy

  Are you adding 'VPR APPLICATION PROXY' as

    a new SECONDARY MENU OPTIONS (the 2ND for this NEW PERSON)? No// YES  (Yes)

Select SECONDARY MENU OPTIONS:

From VPRD.m (https://code.osehra.org/vivian/files/dox/Routine_VPRD_source.html)

- ALL is set for TYPE is TYPE isn't specified. Can pass > 1 type, ";" separated.
  - note: of the 27 types, only 20 are in ALL list explicitly
- synonyms are allowed so "allerg" is mapped to "reactions" etc
- opening is always: "<results version='"_$$GET^XPAR("ALL","VPR VERSION")_"' timeZone='"_$$TZ^XLFDT_"' >"
- with type specific tag inside: <D ADD("<"_VPRTAG)
- other arguments like START/STOP/MAX/ID are passed into individual handlers

\# | type | synonyms | not in ALL 
--- | --- | --- | --- 
1 | accessions | &nbsp; | NO 
2 | appointments | &nbsp; |
3 | clinicalProcedures | &nbsp; | NO
4 | consults | &nbsp; |
5 | demographics | patient | 
6 | documents | &nbsp; |
7 | educationTopics | &nbsp; |
8 | exams | &nbsp; |
9 | flags | &nbsp; |
10 | functionalMeasurements | function, fim | NO
11 | healthFactors | factor |
12 | immunizations | &nbsp; |
13 | insurancePolicies | insur, polic | 
14 | labs | &nbsp; |
15 | meds | med, pharm | 
16 | observations | &nbsp; |
17 | orders | &nbsp; | NO
18 | panels | &nbsp; | NO
19 | problems | &nbsp; |
20 | procedures | &nbsp; |
21 | radiologyExams | rad, xray | NO
22 | reactions | allerg | 
23 | reminders | &nbsp; | &nbsp; | - | NOT from FM
24 | skinTests | &nbsp; |
25 | surgeries | &nbsp; | NO
26 | visits | &nbsp; |
27 | vitals | &nbsp; |

Note: 
- code-parsing VPR Model/Report is missing 3 (clinicalProcedures), 7 (educationTopics), 8 (exams), 10 (functionalMeasurements). But there is "item" which embeds func, skin, exam, educa. (need to rerun)
- will be comparing this data against the model
"""

# TODO: ... fix the white space in flags and do all other data types
# ... then move on to the reports where they exist (/PatientRecords => split by patient ala XML and JSON in VPR)
# see Accession for FOGG ... same xml:space thing ... just do for that ie/ only allow
# for whitespace text

"""
https://docs.python.org/2/library/xml.etree.elementtree.html
"""

"""
<x a=4 b=5 ... ----> x: {a: 4, b: 5 ...
<xs><x a=4... ----> xs: [ { a: 4 
<x value=4> ... ----> x: 4
<xs><x value=4> ... ----> xs: [4
(other than 'results', only expect a total in first tag - otherwise no attributes)

<x ...
  <ys> 
    <y
--->
[{"type": "y" ...

KEY: all have "id" at top level of result EXCEPT vital. VPR does a grouper which doesn't get an id/ien. ien belong to FileMan derived measurements.
"""
class VPRXMLToJSON:

    def __init__(self):
        self.__transformed = defaultdict(int)
    
    def transform(self, xmlQFl, patientIEN, typ): # pass type as may differ from tag
                                
        tree = ET.parse(xmlQFl)
        root = tree.getroot()
        if not (root.tag == "results" and root.attrib.keys() == ["timeZone", "version"]):
            raise Exception("Unexpected root in XML reply")
            
        typEls = [typEl for typEl in root]
        if not (len(typEls) == 1 and typEls[0].attrib.keys() == ["total"]):
            raise Exception("Expect one type element under root with a total")
        typEl = typEls[0]
        
        # Entry by Entry - TODO: consider forcing all to have "id" 
        results = []
        for entryEl in typEl:
            etag, evalue = self.__transformEl(entryEl)
            if evalue == None:
                continue # empty
            if "patientIEN" in evalue:
                raise Exception("Patient IEN is reserved")
            evalue["patientIEN"] = patientIEN # not in VPR itself, want self contained
            if "type" in evalue: # qualify before reusing
                evalue[etag + "Type"] = evalue["type"]
            # ies -> y, s remove
            evalue["type"] = re.sub(r's$', '', re.sub(r'ies$', 'y', typ[0].upper() + typ[1:])) # brand top level with a type (reserved!)
            self.__transformed[evalue["type"]] += 1
            results.append(evalue) # replacing etag with "results"
            
        return results

    """
    Handle attributes in line and dive for children ...
    """
    def __transformEl(self, el):

        attribs = el.attrib

        """
        Case 1: word processing
        
        Except for word processing, no <x>TEXT</x> - uses <x value="TEXT"/>
        """
        if not (el.text == None or re.match(r'\S*$', el.text)):
            if not (len(attribs) == 1 and re.search(r'space$', attribs.keys()[0]) and attribs[attribs.keys()[0]] == "preserve"):
                raise Exception("Only text allowed should be word processing field with space:preserve attribute")
            return el.tag, el.text
    
        # Grab children (attribs grabbed above) (can have both or one or the other)
        children = [] 
        for childEl in el:
            ctag, cvalue = self.__transformEl(childEl)
            if cvalue == None:
                continue # empty tag
            children.append((ctag, cvalue))
        
        """
        Case 2: no children, only attribs
        - 2.1: one attrib, expect 'value' to be tag
        - 2.2: many attribs, none 'value'
        """
        if len(children) == 0 and len(attribs):
            if len(attribs) == 1 and attribs.keys()[0] == "value":
                return el.tag, attribs[attribs.keys()[0]]
            return el.tag, attribs
                        
        """
        Case 3: children, no attribs
        
        Two cases:
        - <xs><x ...><x ...></xs> LIST ie. one tag type 
        - <x><y ...><z ...></x> DICT ie. tag types are properties
        """
        if len(children) and len(attribs) == 0:
            ctags = set(ctag for ctag, cvalue in children)
            if len(ctags) == 1: # List (may be just of one but need to be safe)
                return el.tag, [cvalue for ctag, cvalue in children]
            elif len(ctags) != len(children):
                raise Exception("Less tags than values - shouldn't be for dictionary")
            # ensure "type" is a reserved value
            return el.tag, dict((ctag, cvalue) for ctag, cvalue in children)
            
        """
        Case 4: children and attribs
        ex/ in demographics of <pcProvider code=...><address street="" ...
        """
        if len(children) and len(attribs):
            value = dict((aprop, attribs[aprop]) for aprop in attribs)
            for ctag, cvalue in children:
                value[ctag] = cvalue
            return el.tag, value
          
        """
        Case 5: no attributes and empty tag
        """  
        # Possible that vaGeneric and vaProduct in med are empty. 26583:3456007
        return el.tag, None
        
    def transformed(self):
        return self.__transformed
                            
