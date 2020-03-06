#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import os
import re
import json
from collections import defaultdict, OrderedDict, Counter
from datetime import datetime, date, timedelta

from fmqlutils.cacher.cacherUtils import TMPWORKING_LOCN_TEMPL, FMQLReplyStore, FilteredResultIterator, DATA_LOCN_TEMPL 

from fmqlutils.reporter.reportUtils import MarkdownTable, reportPercent, reportAbsAndPercent

from fmqlutils.typer.reduceTypeUtils import splitTypeDatas, checkDataPresent, singleValue, combineSubTypes, muBVC, muBVCOfSTProp
from fmqlreports.webReportUtils import TOP_MD_TEMPL, SITE_DIR_TEMPL, keyStats, flattenFrequencyDistribution, roundFloat, reduce200

from moreU import flattenPropValues, printf, TOP_MD_TEMPL2 

"""
FIRST TODO: fix scaling for 663 -- st + user ... more reductions

Report TeleReading and the supporting IFCs, documents and images. Very particular IFC.

TODO: [1] fin ac [2] finish Reader Side (align consults) + [3] HL7 vs RPC + [4] neaten/finish final rep form <------ gives new template
- the biggie is FILLER: extrapolate a list as if there is a config file for "filler reading services" ... => 
- need PUG [only internal]
- combine table better ie/ see 2006.5841 ac service -- bring in its Remote Reading Site ie/ show combination.
- RPCs/HL7 attribution and code paths (static report/table) ... see below ie/ BEYOND what data shows unless there is HL7 logs?
  - telereader use lower in SPO (only Eye) but COS consistent with all remote using it!
  - MAY REWORK USER TABLE into 'roles' based on transitions AND not the one summary in queue (who is a reader? responsible? no? ...)
- [FINAL FORM] <-------------- when done beyond freps mv, note IFC in general context + TYPER use rework as neater (not lot's of random types.) MAY DO TYPER explicitly within here ie/ don't run through front end => no need to do custom there ... build in reframe to report.

TODO WORK comments RPCs and HL7 attribution (see code etc comments in reportIFC)
  > Clinical Capture provides the capability to acquire dermatology images that can be
remotely read using Inter-Facility Consults (IFCs) and TeleReader. To support this
capability, a new association has been added to Clinical Capture called “TeleReader
Consult”. JPEG and TIFF dermatology images saved to VistA using this new association
will be converted into DICOM format before storing in VistA Imaging. The images will
then be viewable in Clinical Display.
ie/ dermatology special [and there are a bunch of them]
   ---
   > - TIU Note File – this is used to automatically create a TIU note for a set of images
when the consult request is remotely completed via an Inter-facility Consult.
ie/ TIU creation from remote IFC completion.
   > MAG3 TELEREADER READ/UNRD ADD - adds a consult and image pointers to the
UNREAD/READ LIST file (#2006.5849) and DICOM GMRC TEMP LIST file
(#2006.5839)

"""

# ########################## Web Report Telereader files ####################

def webReportTelereaderFiles(stationNo, stationName, onAndAfterDay, upToDay):

    allThere, details = checkDataPresent(stationNo, [

        {"fileType": "200", "check": "ALL"},
        {"fileType": "3_081", "check": "YR1" if stationNo != "757" else "YR1E"},
        
        {"fileType": "123", "check": "ALL"},
        {"fileType": "123_5", "check": "ALL"},
        
        {"fileType": "2006_5841",  "check": "ALL"},
        {"fileType": "2006_5842", "check": "ALL"},
        {"fileType": "2006_5843", "check": "ALL"},
        {"fileType": "2006_5849", "check": "ALL"}
        
    ])
    if not allThere:
        raise Exception("Some required data is missing - {}".format(details))

    mu = """# Telereader
   
The following describes _Telereading_ in VistA _{}_ [{}]. There are three scenarios [i] _Acquisition Local, Reader Remote_, [ii] _Acquisition Remote, Reader Local_, [iii] _Acquisition Local, Reader Local_.

    
""".format(stationName, stationNo)

    mu += webReportTelereaderConfigurations(stationNo)

    mu += webReportAcquisition(stationNo, stationName, onAndAfterDay, upToDay)
    
    userSiteDir = SITE_DIR_TEMPL.format(stationNo)
    printf("Serializing Report to {}".format(userSiteDir))
    if not os.path.isdir(userSiteDir):
        raise Exception("Expect User Site to already exist with its basic contents")
    title = "Telereader {} ({})".format(stationName, stationNo)
    mu = TOP_MD_TEMPL2.format(title, mu)
    open(userSiteDir + "telereader.md", "w").write(mu)
    
"""
Acquisition - local acquisition and either remote or local telereading

The key file is Telereader List (TELEREADER READ/UNREAD LIST (2006.5849)) pre-enhanced by Placer 123's audit trail and service assertion. 

It summarized from the following perspectives and these summaries are reported on:
1. By Speciality
2. By Status
3. By Reader
In addition, there should be a broad summary of consults (total for perspective) ("trqConsultSummary")

TODO: 
- Make pt on relative read/ac: 663 contrast: Pts on Config alone: see the 46 readers vs 7 in 668; 55 sites to read from vs 8.
- beyond use typer and drop dicts (NEATEN)
- HL7 vs RPC markup of transitions
- move to reproduce local/local and local/remote with transitions, some HL7 marked, some RPCed.
"""
def webReportAcquisition(stationNo, stationName, onAndAfterDay, upToDay):

    _2006_5849EFs, trqConsultSummary = enhanced2006_5849sAndConsultSummary(stationNo, onAndAfterDay, upToDay)
                           
    # ################ Before MU: Create/Load Summaries Required ################
    
    """
    Walk 2006_5849EFs and summarize from different perspectives needed below
    
    TODO: replace with standard, multi-d typer
    """
    byStatus = Counter()
    bySpecialty = Counter()
    byService = defaultdict(list)
    bySpecialtyByService = defaultdict(lambda: defaultdict(list))
    countQueueConsultsWithLocalIFC = 0
    transitionsByStatus = defaultdict(lambda: Counter())  
    addedCommentByTransitionByStatus = defaultdict(lambda: defaultdict(lambda: Counter()))
    countReadingAcquisitionSame = 0 # REM: not all as only 'READ'
    queueSummaryByReaderName = {}
    for resource in _2006_5849EFs:
    
        status = resource["status"]
        byStatus[status] += 1
        
        serviceRef = consult["to_service"]     
        byService[serviceRef].append(resource)
        
        specialty = resource["image_index_for_specialty"]
        bySpecialty[specialty] += 1
        bySpecialtyByService[specialty][serviceRef].append(resource)
        
        if "isConsultLocal" in resource:
            countQueueConsultsWithLocalIFC += 1
            
        transitions = resource["transitions"]
        addedCommentCount = resource["addedCommentCount"]
        transitionsByStatus[status][transitions] += 1
        for rl in resource["addedCommentCount"]:
            addedCommentByTransitionByStatus[status][transitions][rl] += addedCommentCount[rl]
        if "isReadingAcquisitionSame" in resource:
            countReadingAcquisitionSame += 1
            
        # TO 'FIX' ... if reader local, still get remoteId? for main or other
        if resource["full_name_of_reader"] not in queueSummaryByReaderName:
            summ = {"name": resource["full_name_of_reader"], "count": 0, "readerSiteCount": Counter(), "specialityCount": Counter(), "tiuLocals": set(), "tiuRemotes": set(), "remoteIdCount": Counter(), "roles": Counter()}
            for prop in ["full_name_of_reader", "reader_duz_at_acquisition_site"]:
                if prop in resource:
                    summ[prop] = resource[prop]
            queueSummaryByReaderName[resource["full_name_of_reader"]] = summ
        else:
            summ = queueSummaryByReaderName[resource["full_name_of_reader"]]
            if "reader_duz_at_acquisition_site" in resource and "reader_duz_at_acquisition_site" in summ and resource["reader_duz_at_acquisition_site"] != summ["reader_duz_at_acquisition_site"]:
                print("** Warning - same name {} with two acquisition site ids {} and {}".format(resource["full_name_of_reader"], summ["reader_duz_at_acquisition_site"], resource["reader_duz_at_acquisition_site"]))       
        summ["count"] += 1
        summ["specialityCount"][re.split(r' +\[', specialty)[0]] += 1
        summ["tiuLocals"] |= set(tiuLocals.keys())
        summ["tiuRemotes"] |= set(tiuRemotes.keys())
        if "reader_site" in resource:
            summ["readerSiteCount"][resource["reader_site"]] += 1
            if "reader_duz_at_reading_site" in resource:
                remoteId = "{}-{}".format(re.search(r'\-(\d+)', resource["reader_site"]).group(1), resource["reader_duz_at_reading_site"]) # make mu easy
                summ["remoteIdCount"][remoteId] += 1
                
    def sosOfUsers(stationNo, users):
        print("Loading 3.081 YR1 ...")
        type3_081, st3_081s = splitTypeDatas(stationNo, "3_081", reductionLabel="YR1" if stationNo != "757" else "YR1E", expectSubTypeProperty="user")    
        stByUserRef = dict((singleValue(st, "user"), st) for st in st3_081s if singleValue(st, "user") in users)
        print("\tLoaded and processed for {:,}".format(len(users)))
        return stByUserRef
    stByUserRef = sosOfUsers(stationNo, set(queueSummaryByReaderName.keys()))  
    
    def autoCreatedReaders(readers):
        print("Loading user information ...")
        userInfoByUserRef = reduce200(stationNo, coreOnly=True)   
        userRefsAutoCreated = set(userRef for userRef in userInfoByUserRef if "is_created_by_0" in userInfoByUserRef[userRef] if userRef in readers)
        print("\tLoaded and processed for {:,}".format(len(readers)))
        return userRefsAutoCreated
    readersAutoCreated = autoCreatedReaders(set(queueSummaryByReaderName.keys()))
                
    # ################################ Now MU ####################################
        
    mu = "## Telereader Acquisition\n\n"             
    
    """
    Overall summary uses:
    - trqConsultSummary (total - context of how many consults in teler)
    - countQueueConsultsWithLocalIFC (local vs remote)
    """
    mu += """An _Acquisition site_ imports images and submits them for telereading \"consults\". These are tracked in _TELEREADER READ/UNREAD LIST (2006.5849)_. In this site, of <span class='countHigh'>{:,}</span> total consults between {} and {}, <span class='countHigh'>{}</span> are in this LIST, <span class='countHigh'>{}</span> of these are interfacility consults (IFCs), where another facility performs the consult while the balance, <span class='countHigh'>{}</span>, are performed locally.
    
""".format(
        trqConsultSummary["total"],
        onAndAfterDay, 
        upToDay,
        reportAbsAndPercent(countQueueConsults, consultDirectory.total()), 
        reportAbsAndPercent(countQueueConsults - countQueueConsultsWithLocalIFC, countQueueConsults),
        reportAbsAndPercent(countQueueConsultsWithLocalIFC, countQueueConsults) if countQueueConsultsWithLocalIFC else "0"
    )
    
    """
    Report this misconfiguration of the Acquisition Service List ie/ consults
    expected to be in Queue are not there (rightly so). The Acquisition Service List
    is wrong. Two reasons seen:
    - Service is actually for reading for a remote site
    - Service is a Procedure (and therefore won't go in TeleReading?
    - 668 has two others, dental, may be turned on for experiment and deleted?
    """
    if "missingFromQueue" in trqConsultSummary:
        # This means service SHOULD NOT be defined for Acquisition as it 
        # is used by a remote site to send consults to this site for Reading!
        missingMU = "Acquisition configuration predicts <span class='countHigh'>{:,}</span> consults should be on the LIST but are not.".format(trqConsultSummary["missingFromQueue"])
        if "missingFromQueueFillers" in trqConsultSummary:
            missingMU += " <span class='countHigh'>{:,}</span> belong to service(s) _{}_ that are Readers for remote VistAs.".format(
                trqConsultSummary["missingFromQueueFillers"],
                ", ".join(trqConsultSummary["missingFromQueueFillersServices"])
            )
        if "missingFromQueueProcedure" in trqConsultSummary:
            missingMU += " <span class='countHigh'>{:,}</span> belong to service(s) _{}_ which involve procedures.".format(
                trqConsultSummary["missingFromQueueProcedure"],
                ", ".join(trqConsultSummary["missingFromQueueProcedureServices"])
            )           
        if "missingFromQueueLocalDiscontinue2" in trqConsultSummary:
            missingMU += " <span class='countHigh'>{:,}</span> are discontinued before they reach the queue.".format(
                trqConsultSummary["missingFromQueueLocalDiscontinue2"]
            )           
        if "otherMissing" in trqConsultSummary:
            missingMU += " <span class='countHigh'>{:,}</span> are absent for other reasons.".format(
                trqConsultSummary["otherMissing"]
            )
        mu += """{}
        
""".format(missingMU)  

    """
    Specialty (and their status) use:
    - bySpecialtyByService
    and 
    - serviceToIFC
    """
    mu += """The entries have <span class='countHigh'>{:,}</span> states, {} and <span class='countHigh'>{:,}</span> specialties, {} covering <span class='countHigh'>{:,}</span> services.
    
""".format(len(byStatus), muBVC(byStatus), len(bySpecialty), muBVC(bySpecialty), len(byService))
    for specialty in sorted(bySpecialtyByService):
        mu += "Specialty _{}_ ...\n\n".format(re.split(r' +\[', specialty)[0])
        tbl = MarkdownTable([":Service", ":Remote Reader", "Count", ":Status'"])
        for service in sorted(bySpecialtyByService[specialty], key=lambda x: len(bySpecialtyByService[specialty][x]), reverse=True):
            serviceIEN = re.search(r'\-(\d+)', service).group(1)
            byStatus = Counter()
            for resource in bySpecialtyByService[specialty][service]:
                byStatus[resource["status"]] += 1
            name = re.split(r' +\[', service)[0]
            ifcRoutingSiteMU = re.sub(r'4\-', '', serviceToIFC[serviceIEN]["ifc_routing_site"]) if serviceIEN in serviceToIFC and "ifc_routing_site" in serviceToIFC[serviceIEN] else ""
            tbl.addRow([
                "__{}__".format(name) if ifcRoutingSiteMU else name,
                ifcRoutingSiteMU,
                len(bySpecialtyByService[specialty][service]), 
                muBVC(byStatus),
            ])
        mu += tbl.md() + "\n\n"
    
    """
    Status with transition summaries use:
    - transitionsByStatus
    - addedCommentByTransitionByStatus
    """
    mu += """List entries go through one or more transitions, starting with a _CPRS RELEASED ORDER_ when the entry is first added right after its consult is created. The most common sequence moves on to _RECEIVED_ (reader site received the consult) through _COMPLETE UPDATE_ (reader site has read the image and created a document) and ends with _NEW NOTE ADDED_ (an equivalent document was created in the \"local\"/acquisition site). 
    
The following shows transitions by list entry status. The last column shows how _ADDED COMMENT_ actions accompany a specific transition. These actions may be local or remote and allow users to annotate a consult. Transitions in __bold__ represent remote reader activity ...

"""
    tbl = MarkdownTable([":Status", ":Transitions", "Count", ":Added Comments"], includeNo=False)
    currentStatus = ""
    # Not all used
    for status in ["W:Waiting", "U:Unread", "C:Cancelled", "L:Locked", "D:Deleted", "R:Read"]:
        if status not in transitionsByStatus:
            continue
        for activitySig in sorted(transitionsByStatus[status], key=lambda x: transitionsByStatus[status][x], reverse=True):
            if status != currentStatus:
                currentStatus = status
                row = ["__{}__".format(status.split(":")[1])]
            else:
                row = [""]
            row.extend([activitySig, transitionsByStatus[status][activitySig]])
            if status in addedCommentByTransitionByStatus and activitySig in addedCommentByTransitionByStatus[status]:
                row.append(muBVC(addedCommentByTransitionByStatus[status][activitySig]))
            else:
                row.append("")
            tbl.addRow(row)
    mu += tbl.md() + "\n\n"
    
    """
    Per Reader summaries use queueSummaryByReaderName
    """
    queueSummaryByReaderName = summarizeEnhanced2006_5849s(_2006_5849EFs)
    tbl = MarkdownTable([":Reader Name", "Spec(s)", "\#", "Local User Id", ":Remote User Id", ":Reader Site(s)", ":Applications (SOs)", "Roles", "Docs"])
    noLocal = 0
    noAutoCreated = 0 
    for i, summ in enumerate(sorted(queueSummaryByReaderName.values(), key=lambda x: x["count"], reverse=True), 1):
        userRef = summ["reader_duz_at_acquisition_site"]
        acquisitionUserIEN = re.search(r'\-(\d+)', userRef).group(1)
        appsMU = ""     
        if userRef in stByUserRef:
            st = stByUserRef[userRef]
            byAppCount = Counter() if "remote_app" not in st else st["remote_app"]["byValueCount"]
            if st["_total"] > sum(byAppCount[app] for app in byAppCount):
                byAppCount["UNSET"] = st["_total"] - sum(byAppCount[app] for app in byAppCount)   
            appsMU = muBVC(byAppCount)
            for f, t in [("VISTA IMAGING TELEREADER", "__TELEREADER__"), ("MEDICAL DOMAIN WEB SERVICES", "JLV"), ("VISTAWEB-PROD", "WEB"), ("VISTA IMAGING", "IMG"), ("DISPLAY", "DISP"), ("UNSET", "_UNSET_")]:
                appsMU = re.sub(f, t, appsMU)
        isLocalReader = True if ("remoteIdCount" in summ and len(summ["remoteIdCount"].keys()) == 1 and summ["remoteIdCount"].keys()[0].split("-")[1] == acquisitionUserIEN) else False # shorthand that IEN local/remote same ac/ing for site id is subclinic and not just stationNo
        if isLocalReader: 
            noLocal += 1
        nameMU = re.sub(r'\,', ', ', "__{}__".format(summ["full_name_of_reader"]) if not isLocalReader else summ["full_name_of_reader"])
        if userRef in readersAutoCreated:
            noAutoCreated += 1
        else:
            nameMU = "{}*".format(nameMU)
        roleMap = {"remote_responsible_person": "REM_RESP", "remote_entering_person": "REM_ENTR", "who_entered_activity": "LOC_ENTR", "whos_responsible_for_activity": "LOC_RESP"}
        rolesCount = Counter()
        auditProps = auditPropsByUserName[summ["name"]]
        for prop in auditProps:
            rolesCount[roleMap[prop]] = auditProps[prop]
        tbl.addRow([
            nameMU,
            re.sub(r'(ATOLOGY| CARE)', '', muBVC(summ["specialityCount"])),
            summ["count"],
            acquisitionUserIEN,
            re.sub(r'\-', ':', muBVC(summ["remoteIdCount"], forceShowCount=True)) if not isLocalReader and "remoteIdCount" in summ else "",
            re.sub(r'VA MEDICAL CENTER', 'VAMC', muBVC(summ["readerSiteCount"], forceShowCount=True)),
            appsMU,
            muBVC(rolesCount), # from properties 
            "{:,}/{:,}".format(len(summ["tiuLocals"]), len(summ["tiuRemotes"]))
        ])
    mu += """For the period considered here, the list has <span class='countHigh'>{:,}</span> Readers, <span class='countHigh'>{}</span> of which are local. The names of Readers from remote sites (_\"Remote Readers\"_) are in __bold__.
    
""".format(
        len(queueSummaryByReaderName), 
        reportAbsAndPercent(noLocal, len(queueSummaryByReaderName))
    )
    mu += """<span class='countHigh'>{}</span> of the following Readers were added automatically to this VistA - those added explicitly are marked with a _*_. \"Applications (Signons)\" gives the number of sign ons a user makes with different applications for the period under consideration. _UNSET_ means the application doesn't identify itself - _CPRS_ is the chief example of this. Note that _TeleReader_ is used by remote users.
    
""".format(
        reportAbsAndPercent(noAutoCreated, len(queueSummaryByReaderName))
    )
    mu += tbl.md() + "\n\n"
        
    return mu  
    
"""
As setup by Telereader configuration - decide how reader operates. Note that for events
from reading, can fill in many extra properties using these configurations.

TODO: 
- FOCUS ON MERGING TABLES so see AC Through Routing from two and not one file ... ALSO service == Instit + Specialty
- MORE FOR READING ie/ how do reading services (ie/ stuff in from ...) work

Note: Specialty 2006_84 (DERMATOLOGY, EYE CARE, ...) have no extra nuances except an acronym (all are active, all are CLIN) so NOT detailing in its own table
"""
def webReportTelereaderConfigurations(stationNo):

    mu = """
    
## Telereader Configuration

The client __[Telereader Configurator](https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_telereader_configuration.pdf)__ sets up the following configuration files that determine how Telereading operates in a VistA.

""".format(stationNo)

    def rowUp(resource, propMap, enforceMapAll=True, suppress=[]):
        propsDontSee = ["type", "_id", "label"]
        propsDontSee.extend(suppress)
        propsSeen = set(k for k in resource if k not in propsDontSee)
        propsMapped = set(suppress)
        row = []
        for i, pMap in enumerate(propMap, 1):
            if pMap[0] in resource:
                propsMapped.add(pMap[0])
                if len(pMap) > 3 and pMap[3]:
                    valMU = ", ".join(sorted([re.sub(r' +\[[\d\_]+\-', ' [', v[pMap[3]]) for v in resource[pMap[0]]]))
                    row.append(valMU)
                    continue
                val = resource[pMap[0]]
                if len(pMap) == 3:
                    if pMap[2] == "IEN":
                        val = re.sub(r' +\[[\d\_]+\-', ' [', val)
                    elif pMap[2] == "DROP":
                        val = re.split(r' +\[', val)[0]
                valMU = "__{}__".format(re.sub(r'\s+$', '', val)) if i == 1 else val
                row.append(valMU)
            else:
                row.append("")
        if enforceMapAll and len(propsSeen - propsMapped):
            raise Exception("Not all resource props expected were mapped")
        return row

    # TO ADD: 2005_84 total ie/ how many of the specialties are involved?
    # TO ELABORATE -- TIU defn ++ KEY CONCEPT specializing local services for IFC,
    # specifically acquisition ... add direction IN COMBINATION with IFC specialization
    # of the generic service class 123.5 ... 
    # <------------ may combine 123.5 with this for one definition from/to, specialty,
    # document, trigger table
    def mu2006_5841(dataLocn):
        _123_5sOf2006_5841s = set()    
        # dropping ("procedure", "Procedure")
        propMap = [("name", "Service", "DROP"), ("acquisition_site", "Acquisition Site", "IEN"), ("procedure_index", "Procedure Index", "DROP"), ("unread_list_creation_trigger", "Creation Trigger"), ("tiu_note_file", "TIU Note")]
        resourceIter = FilteredResultIterator(dataLocn, "2006_5841", isOrdered=False)
        bySpecialtyIndex = defaultdict(list)
        for i, resource in enumerate(resourceIter, 1):
            flattenPropValues(resource)
            bySpecialtyIndex[resource["specialty_index"]].append(resource)
            _123_5IEN = re.search(r'123_5\-(\d+)', resource["name"]).group(1)
            _123_5sOf2006_5841s.add(_123_5IEN)
        fmu = """_TELEREADER ACQUISITION SERVICE [2006.5841]_ is the key configuration file for Telereader Image __Acquisition__. All VistA Consults go to a _\"service\"_, a combination of institution that will perform a consult and the specialty required for the consult. This file [1] isolates Telereader acquisition services (_\"Telereader Acquisition Services\"_) and refines them for telereading. It [2] redefines the specialty of a service in nationally recognized terms (ex/ _Dentistry_) and [3] specifies which of the institutions of a VistA a service applies to.

Its <span class='countHigh'>{:,}</span> entries belong to <span class='countHigh'>{:,}</span> specialties.

""".format(i, len(bySpecialtyIndex))
        for si in sorted(bySpecialtyIndex):
            tbl = MarkdownTable([":{}".format(pmap[1]) for pmap in propMap])
            for resource in bySpecialtyIndex[si]:            
                tbl.addRow(rowUp(resource, propMap, True, suppress=["specialty_index", "procedure"]))
            fmu += "_{}_ has <span class='countHigh'>{:,}</span> ...\n\n".format(si.split(" [")[0], len(bySpecialtyIndex[si]))
            fmu += tbl.md() + "\n\n"
            
        fmu += "Note that _DICOM HEALTHCARE PROVIDER SERVICE [2006.5831]_ which configures the _DICOM Gateway_ also gets entries for the Telereader Acquisition Services.\n\n"
        return fmu, _123_5sOf2006_5841s
       
    """
    Probably not enough ie/ only PLACER services and not fillers! Filler Consults
    have more and different ones (what sets them up?)
    """     
    def mu123_5(dataLocn, _123_5sOf2006_5841s):
        propMap = [
                ("service_name", "Service", "DROP"),
                ("ifc_routing_site", "Remote Reading Site"),
                ("ifc_remote_name", "Remote Name"),
                ("associated_stop_code", "Stop Code(s)")
                # ("service_usage", "Status")
        ]    
        resourceIter = FilteredResultIterator(dataLocn, "123_5", isOrdered=False)
        tbl = MarkdownTable([":{}".format(pmap[1]) for pmap in propMap])
        for i, resource in enumerate(resourceIter, 1):
            ien = resource["_id"].split("-")[1]
            if ien not in _123_5sOf2006_5841s:
                continue
            flattenPropValues(resource)
            if "ifc_routing_site" in resource:
                resource["ifc_routing_site"] = re.sub(r'( VA MEDICAL CENTER| VAMC)', '', re.sub(r'4\-', '', resource["ifc_routing_site"])) # just want [SNO] and VAMC nix for easy read
            if "associated_stop_code" in resource:
                resource["associated_stop_code"] = ", ".join(sorted(list(set(sr["associated_stop_code"] for sr in resource["associated_stop_code"]))))
            tbl.addRow(rowUp(resource, propMap, False))
        # And the property remote_consult_file entry maps the id at the other site ie/
        # filler back to placer and placer over to filler.
        fmu = """_REQUEST SERVICES [123.5]_ holds this VistA's <span class='countHigh'>{:,}</span> consult services. Only <span class='countHigh'>{}</span> are referenced from _TELEREADER ACQUISITION SERVICE [2006.5841]_. Those with a _Remote Reading Site_ involve reading in a remote VistA. Those without involve local reading within this VistA. A (placer) consult created with the _Service_ name results in a (filler) consult with the service name _Remote Name_ in the _Remote Reading Site_. 

""".format(i, len(_123_5sOf2006_5841s))
        fmu += tbl.md() + "\n\n"
        return fmu
        
    # > The TELEREADER ACQUISITION SITE file (#2006.5842) contains the list of the
    # Acquisition Sites for each Reading Site. This list must also include the Reading     
    # Site itself if it is to perform image acquisition as well.
    # > ...
    
    def mu2006_5842(dataLocn):

        propMap = [("primary_site", "Primary Site", "IEN"), ("name", "Name", "DROP"), ("lock_timeout_in_minutes", "Lock Timeout")] # dropped status
        
        resourceIter = FilteredResultIterator(dataLocn, "2006_5842", isOrdered=False)
        tbl = MarkdownTable([":{}".format(pmap[1]) for pmap in propMap])
        includesItselfMU = ""
        for i, resource in enumerate(sorted(resourceIter, key=lambda x: x["primary_site"], reverse=True), 1):
            flattenPropValues(resource)
            if re.search(stationNo, resource["primary_site"]):
                includesItselfMU = ", including itself"
            tbl.addRow(rowUp(resource, propMap, True, suppress=["status"]))

        fmu = """Despite the name, _TELEREADER ACQUISITION SITE [2006.5842]_ configures a VistA for __Reading__, not acquisition. It lists the sites a VistA can read from. This list will include the Reading Site itself if it is to read images acquired locally. In this VistA, it has <span class='countHigh'>{:,}</span> entries{} ... 

""".format(i, includesItselfMU)
        fmu += tbl.md() + "\n\n"
        return fmu
        
    # Add more 200 details ie/ created explicitly or not? Presume so
    # Add -- should tie into FILLER Consults?
    def mu2006_5843(dataLocn):
    
        propMap = [("reader", "Reader"), ("acquisition_site", "Acquisition Site", "", "acquisition_site")]
        
        resourceIter = FilteredResultIterator(dataLocn, "2006_5843", isOrdered=False)
        tbl = MarkdownTable([":{}".format(pmap[1]) for pmap in propMap])
        for i, resource in enumerate(resourceIter, 1):
            flattenPropValues(resource)
            tbl.addRow(rowUp(resource, propMap, True))
    
        fmu = """_TELEREADER READER [2006.5843]_ adds information about individual users for __Reading__. It [1] identifies readers using their User file entry (200), [2] lists the  one or more _TELEREADER ACQUISITION SITE [2006.5842]_ the user can read from and [3] designates the clinical specialties a user has. In this VistA, it has <span class='countHigh'>{:,}</span> entries ... 

""".format(i)
        fmu += tbl.md() + "\n\n"
        return fmu
    
    dataLocn = DATA_LOCN_TEMPL.format(stationNo)  
    
    mu2006_5841, _123_5sOf2006_5841s = mu2006_5841(dataLocn)
    mu += mu2006_5841
    mu += mu123_5(dataLocn, _123_5sOf2006_5841s)
    mu += mu2006_5842(dataLocn)
    mu += mu2006_5843(dataLocn)
    
    return mu
    
# ################################# Reducer/Reframer #############

"""
Main purpose - add consult information into 2006_5849 entries

2006_5849 red/typer - Two additions to list from its (placer) 123:
        1. lacks a to_service assertion ie/ proxy for remote. That comes later once a 
    remote comes in but at first it isn't there. Need to add the to_service
        2. flush audit trail of consult too as should add to nuance available in list ie
    could also move to list entry to reflect its activity.
        3. [EXTRA] IFC Router/Remote Site info for Services
            
Note: scales as first flush/reduce Consults and other items needed to enhance
2006_5849 entries and then flush those too
"""
def enhanced2006_5849sAndConsultSummary(stationNo, onAndAfterDay, upToDay):
    
    qefsJSNFl = TMPWORKING_LOCN_TEMPL.format(stationNo) + "2006_5849EFs{}-{}.json".format(onAndAfterDay, upToDay)
    csJSNFl = TMPWORKING_LOCN_TEMPL.format(stationNo) + "telereaderQueueConsultSummary.json"
    try:
        _2006_5849EFs = json.load(open(jsnFl))
        trqConsultSummary = json.load(open(csJSNFl))
    except:
        print("No Enhanced 2006_5849's - Must Enhance and summarize consults")
    else:
        print("Returning {:,} pre-enhanced 2006_5849's and ConsultSummary".format(len(_2006_5849EFs)))
        return _2006_5849EFs, trqConsultSummary
    
    """    
    On 123's
        ifc_role says go between facilities 
    
        remote_consult_file_entry links remote and local consults
        - no ifc_role => NONE
        - ifc_role == FILLER => YES
        - ifc_role == PLACER => MOSTLY (exception is if discontinued before remote setup)

        issue: telereader done on locals are NOT ifc's!
        ... can only pick out these 123's using acquisition service file (2006.5841)
        which isolates all services ie/ 
                    telereader is NOT <=> ifc
    
        Local/Local Telereader Service
        - service in acquisition config (2006.5841)
        - no remotes specified in the service definition (123.5)
        - 123 has no ifc_role (and no remote_consult_file_entry) ie/ not spec'ed
        as placer or filler as both and local
    """    
    def reframe123ForListAnalysis(stationNo, startDate):
        jsnFl = TMPWORKING_LOCN_TEMPL.format(stationNo) + "consultRedById{}.json".format(startDate)
        try:
            consultRedById = json.load(open(jsnFl))
        except:
            pass
        else:
            return consultRedById
                        
        dataLocn = DATA_LOCN_TEMPL.format(stationNo)     
        
        # Will enhance 123 with this: need Acquisition Service list to pick out 
        # Local:Local TeleReader
        resourceIter = FilteredResultIterator(dataLocn, "2006_5841", isOrdered=False)
        acServices = {}
        for resource in resourceIter:
            flattenPropValues(resource)
            acServices[resource["name"]] = True if "procedure" in resource else False
        
        # TODO: 
        store = FMQLReplyStore(dataLocn)
        startDateProp = "file_entry_date"
        startAtReply = store.firstReplyFileOnOrAfterCreateDay("123", startDateProp, startDate) 
        if startAtReply == "":
            raise Exception("Can't find 123 start reply")
        resourceIter = FilteredResultIterator(dataLocn, "123", isOrdered=False, startAtReply=startAtReply)
        consultRedById = {}
        for resource in resourceIter:
            flattenPropValues(resource)
            consultRedById[resource["_id"]] = {"_ien": resource["_id"].split("-")[1], "file_entry_date": resource["file_entry_date"], "to_service": resource["to_service"], "cprs_status": resource["cprs_status"]}
            if "ordering_facility" in resource:
                consultRedById[resource["_id"]]["ordering_facility"] = resource["ordering_facility"]
            """
            Quirk: if local VistA puts a service in its Acquisition Service list
            (ie/ for local acquisition) and a remote VistA has the same service
            as a Reader (ie/ lead to Filler Consults) then will see consults with
            'uses_acquisition_service' AND ifc_role=F:FILLER. Resolution would
            be to remove the service from the Acquisition Service List of the VistA
            and leave the service as a Reader Service for a remote site (unfortunately
            there is no format 'Reader Service List' for services. It has to be
            derived (see below))
            """
            if resource["to_service"] in acServices: # one of those services!
                consultRedById[resource["_id"]]["uses_acquisition_service"] = True
                if acServices[resource["to_service"]]:
                    consultRedById[resource["_id"]]["is_acquisition_service_procedure"] = True
            # add to enforce: if exists for placer to a telereader ac service and
            # placer consult not in queue/list then don't expect this - expected
            # DISCONTINUED placer that has never been sent remotely
            if "remote_consult_file_entry" in resource:
                consultRedById[resource["_id"]]["remote_consult_file_entry"] = resource["remote_consult_file_entry"]
            if "ifc_role" in resource:
                if resource["ifc_role"] == "F:FILLER" and "remote_consult_file_entry" not in resource:
                    raise Exception("Expected every FILLER IFR consult to have a remote consult reference") # WILL ENFORCE when use TYPER too
                consultRedById[resource["_id"]]["ifc_role"] = resource["ifc_role"]
            if "request_processing_activity" in resource:
                consultRedById[resource["_id"]]["request_processing_activity"] = resource["request_processing_activity"]
                
        json.dump(consultRedById, open(jsnFl, "w"))
        
        return consultRedById
        
    def reframe123_5ForListAnalysis(stationNo):
    
        jsnFl = TMPWORKING_LOCN_TEMPL.format(stationNo) + "serviceToIFC.json"
        try:
            serviceToIFC = json.load(open(jsnFl))
        except:
            pass
        else:
            return serviceToIFC
    
        resourceIter = FilteredResultIterator(dataLocn, "123_5", isOrdered=False)
        serviceToIFC = {}
        for i, resource in enumerate(resourceIter, 1):
            ien = resource["_id"].split("-")[1]
            if not ("ifc_remote_name" in resource or "ifc_routing_site" in resource):
                continue
            flattenPropValues(resource)
            serviceToIFC[ien] = {"service_name": resource["service_name"]}
            if "ifc_remote_name" in resource:
                serviceToIFC[ien]["ifc_remote_name"] = resource["ifc_remote_name"]
            if "ifc_routing_site" in resource:
                serviceToIFC[ien]["ifc_routing_site"] = resource["ifc_routing_site"]
            if "associated_stop_code" in resource:
                serviceToIFC[ien]["associated_stop_code"] = list(set(sr["associated_stop_code"] for sr in resource["associated_stop_code"]))
        
        json.dump(serviceToIFC, open(jsnFl, "w"))
        
        return serviceToIFC
            
    """
    123 Audit Trail - transitions from 123 which specialize the status of the List
    
    Note: not doing inside 123 reframe as would then do for all 123's and not
    necessary
    
    The audit trail (request processing activity (123.02)) matches list properties
    and the specific form of a list entry's 123 
    
    States of Consult Trail (SPO):
    - CPRS RELEASED ORDER [LOCAL]
    - COMPLETE_UPDATE [REMOTE]
    - NEW NOTE ADDED ... remote sync and < complete with TIU's [LOCAL]
    - ADDED COMMENT ... just a local comment? (does it carry?) [REMOTE]
      ... doesn't update last_activity in consult itself
    - RECEIVED ... note less than those above ie/ RECEIPT not noted? [REMOTE]
    - INCOMPLETE RPT ... < 10% that report marked incomplete
    - SIG FINDING UPDATE ... seems like another finding after TIU sent ... added to TIU?*
      * To see: lookup 8925-15233448 (does it get children?)
      ... always after NEW NOTE ADDED?
    - DISCONTINUED ... nearly all just CPRS and no UPDATE but there is one exception
    - DISASSOCIATE RESULT
    - SCHEDULED ... only 1
    
    "Classic" is: CPRS RELEASED ORDER, [RECEIVED], COMPLETE_UPDATE, NEW NOTE ADDED
    
    User Ids:
    - placer-side: whos_responsible_for_activity, who_entered_activity - 200Ref
    - reader-side: remote_responsible_person, remote_entering_person - Label
    
    Want times: 'date_time_of_action_entry'
    - gap from Consult entry (from listEntry) and first activity
    - gap between COMPLETE_UPDATE and NEW NOTE ADDED
    
    Want correlate list cprs_status with the activity ie/ classic => READ
    """
    def reducePlacer123Transitions(queueEntry, auditTrailOfConsult, auditPropsByUserName):
                                            
        # Added Comment can be remote or local -- others are fixed
        addedComments = [entry for entry in auditTrailOfConsult if re.match(r'ADDED COMMENT', entry["activity"])]
        addedCommentCount = Counter()               
        LOCAL_OR_REMOTE = {
        
            "CPRS RELEASED ORDER": "LOCAL",
            "RECEIVED": "BOTH", # Both only 757
            
            # Only see COMPLETE_UPDATE from 757 as LOCAL -- mainly REMOTE
            "COMPLETE_UPDATE": "BOTH",      
            
            "FORWARDED FROM": "LOCAL", # 757 only       
            
            "FWD TO REMOTE SERVICE": "LOCAL", # not 668
            "NEW NOTE ADDED": "LOCAL",
            "SIG FINDING UPDATE": "BOTH", # NEED BOTH and not just REMOTE as 663
            
            "ADDENDUM ADDED TO": "LOCAL", # 757 only
            
            "CANCELLED": "BOTH", # 757 only, 663 has BOTH
            
            "INCOMPLETE RPT": "BOTH", # Both is 757 only
            
            "DISASSOCIATE RESULT": "BOTH", # Both is 757 only
            
            "SCHEDULED": "BOTH", # RARE - 663 BOTH
            
            "DISCONTINUED": "BOTH",
            
            "ADDED COMMENT": "BOTH",
            
            "STATUS CHANGE": "BOTH"
            
        } 
                
        def recordUsers(entry, auditPropsByUserName):
            props = ["who_entered_activity", "whos_responsible_for_activity", "remote_entering_person", "remote_responsible_person"]
            if sum(1 for prop in entry if re.match(r'who', prop)) and sum(1 for prop in entry if re.match(r'remote', prop)):
                raise Exception("Combo of who_ and remote_ properties should never occur in an audit entry")
            for prop in props:
                if prop in entry:
                    userName = entry[prop].split(" [")[0]
                    auditPropsByUserName[userName][prop] += 1
                
        transitionsMUed = []
        allActivities = []
        localTIUs = Counter()
        remoteTIUs = Counter() # can be asserted > once
        for entry in auditTrailOfConsult:
            activity = entry["activity"].split(" [")[0]
            allActivities.append(activity)
            if activity not in LOCAL_OR_REMOTE:
                raise Exception("Unexpected Activity: {}".format(activity))
            # Expect results (remote or local) ONLY for status R:Read (| D:Deleted)
            # ... TODO: may expand on the readers ie/ anyone in these document
            # referencing transitions -- and enterer
            if "result" in entry or "remote_result" in entry:
                if queueEntry["status"] not in ["R:Read", "D:Deleted"]:
                    raise Exception("Expected result remote or local in transition to only come for R:Read (D:Deleted) entries".format(queueEntry["status"])) 
                if activity not in ["COMPLETE_UPDATE", "NEW NOTE ADDED", "INCOMPLETE RPT", "DISASSOCIATE RESULT", "ADDENDUM ADDED TO"]:
                    raise Exception("Unexpected activity {} for transition with a document property (result/remote_result)".format(activity))
                if "remote_result" in entry:
                    remoteTIUs[entry["remote_result"]] += 1
                if "result" in entry:
                    localTIUs[entry["result"]] += 1
            # if queueEntry["status"] not in ["W:Waiting", "U:Unread"]:
            recordUsers(entry, auditPropsByUserName)
            if LOCAL_OR_REMOTE[activity] == "LOCAL":
                if "who_entered_activity" not in entry:
                    raise Exception("Expected {} to be LOCAL".format(activity))
                transitionsMUed.append(activity)
                continue
            if LOCAL_OR_REMOTE[activity] == "REMOTE":
                if "remote_entering_person" not in entry:
                    raise Exception("Expected {} to be REMOTE".format(activity))
                transitionsMUed.append("__{}__".format(activity))
                continue
            if activity in ["COMPLETE_UPDATE", "DISCONTINUED", "INCOMPLETE RPT", "RECEIVED", "DISASSOCIATE RESULT"]: 
                if sum(1 for prop in entry if re.match(r'who', prop)):
                    transitionsMUed.append(activity)
                else:
                    transitionsMUed.append("__{}__".format(activity))
                continue
            # SIG FINDING UPDATE only 663
            if activity not in ["ADDED COMMENT", "SIG FINDING UPDATE", "SCHEDULED", "STATUS CHANGE", "CANCELLED"]:
                raise Exception("Assumed a/ced for -- by now: {}".format(activity))
            # ADDED COMMENT - not put into transitions
            if sum(1 for prop in entry if re.match(r'who', prop)):
                addedCommentCount["LOCAL"] += 1
            else:
                addedCommentCount["REMOTE"] += 1
                
        transitionsMU = "/".join(transitionsMUed)
        
        """
        Transition Combinations by List Entry Status
        
        - Always start (locally) with CPRS RELEASED ORDER
        - Generic ones for any status: 
                CPRS RELEASED ORDER, RECEIVED, FWD TO REMOTE SERVICE
        - Always a COMPLETE_UPDATE if status is R:Read and only one if R:Read or D:Deleted
        ie/ once received then work was done. Only next state would be D:Deleted.
        - If C:Cancelled then has either DISCONTINUED or CANCELLED 
          - note that D:Deleted is not enforced well and can have DISCONTINUED or no
        particular transition marking it as D:Deleted (ie/ no real asserts)
        - Others like NEW NOTE ADDED only go with R:Read (and therefore COMPLETE too)
        ... though it's possible there is a INCOMPLETE and COMPLETE not there yet?
        
        Key Reader Properties in QueueEntry:     
            full_name_of_reader ALL
            reader_site ALL
            reader_duz_at_acquisition_site (200-) ALL or nearly ALL
            [reader_duz_at_reading_site] (IEN) 40% SPO but nearly all COS
        ... full_name_of_reader
        """
               
        # First activity always "CPRS RELEASED ORDER" and consult file (entry) is
        # within 60 seconds (BG process?) of this first audit trial entry.
        setupAudit = auditTrailOfConsult[0]
        if not re.match(r'CPRS RELEASED ORDER', setupAudit["activity"]):
            raise Exception("Expected CPRS posting of 123 to be the first activity for Placer consults")
        consultEntryTime = datetime.strptime(queueEntry["consult_request"].split(" [")[0], "%Y-%m-%dT%H:%M:%SZ")
        setupAuditTime = datetime.strptime(setupAudit["date_time_of_action_entry"], "%Y-%m-%dT%H:%M:%SZ")
        if setupAuditTime < consultEntryTime or setupAuditTime - consultEntryTime > timedelta(minutes=1):
            raise Exception("Expected Setup Audit Time/CPRS Entry to be > Consult creation time and the gap to be <= 1 minutes, even 0")
            
        # COMPLETE_UPDATE: all R:Read's and only in R:Read or D:Deleted
        if not re.search(r'COMPLETE', transitionsMU):
            if queueEntry["status"] == "R:Read":
                raise Exception("If queue entry is R:Read then expect COMPLETE transition")            
            # This C:Cancellation and _reader props is used below as must exclude
            # should uses from a count of Readers
            if sum(1 for prop in queueEntry if re.search(r'reader', prop)) and queueEntry["status"] != "C:Cancelled":
                # ie/ Cancellation causes reader props to be set (really an overuse!) and
                # should remove em!
                raise Exception("Expect _reader props NOT to be in a queue entry without a COMPLETE unless C:Cancelled")
        else: # There is a Complete
            if queueEntry["status"] not in ["R:Read", "D:Deleted"]:
                raise Exception("Only expect COMPLETE UPDATE in R:Read or D:Deleted")
            if sum(1 for prop in queueEntry if re.search(r'reader', prop)) == 0 and queueEntry["status"] != "D:Deleted":
                raise Exception("Expect COMPLETE UPDATE to mean reader_ in QueueEntry unless status is D:Deleted")
        
        # R:Read (=> COMPLETE_UPDATE too) [and D:Deleted too - it's a weird one]
        if re.search(r'(NEW NOTE ADDED|INCOMPLETE RPT|DISASSOCIATE RESULT|SIG FINDING UPDATE)', transitionsMU) and queueEntry["status"] not in ["R:Read", "D:Deleted"]:
            print("** WARNING - NEW NOTE ADDED|INCOMPLETE RPT|DISASSOCIATE RESULT|SIG FINDING UPDATE only allow in R:Read (or D:Deleted) but {}".format(queueEntry["status"]))
        
        # C:Cancelled always has DISCONTINUED (and sometimes CANCELLED)
        # ... DISCONTINUED did (errorneously) appear in a R:Read to so not exclusivie
        if queueEntry["status"]  == "C:Cancelled" and not re.search(r'(DISCONTINUED|CANCELLED)', transitionsMU):       
            print("** WARNING - Expect C:Cancelled to have DISCONTINUED|CANCELLED transition")
                
        return transitionsMU, addedCommentCount, localTIUs, remoteTIUs     
        
    print("Loading consults (123) ...")
    consultRedById = reframe123ForListAnalysis(stationNo, onAndAfterDay)
    print("\t{:,} consults".format(len(consultRedById)))
    print("Loading 123_5 ...")
    serviceToIFC = reframe123_5ForListAnalysis(stationNo)
    print("\t{:,} 123_5s".format(len(serviceToIFC)))             
    
    """            
    Combination of 123.5 (has or hasn't 'Remote Reading Site') and 2006.5841 
    (identifies specifically as telereader acquisition service) identifies telereading
    location and the shape of Consults. 
    
    For all telereader acquistion services (in 2006.5841) ...
    
            Read     123.5 Has 'Remote Reading Site'    123 Role
            ----        -------------------            ----------
            LOCAL               NO                        NONE
            IFC/REMOTE          YES                     P:PLACER
            
    but there's room for error in configuration. In 757, one LOCAL site
    (acquire and read on-site locally) is never used for local reading of
    local acquisitions (ifc_role NONE). All of its consults have ifc_role
    F:FILLER which points to it being a remote reader for another site, one
    that should NOT be in 2006.5841. This can only be known by examining the
    consults of a service and excluding services from acquisition that are
    F:FILLER.
    
    Note that so far, don't see any mixed situations ie/ remote site treats
    a Local Service as its remote Reader AND the site does so itself too ie.
    2006.5841 is valid but the service is doing double duty.
    """ 
    print("Walking and enhancing 2006_5849 ...")
    dataLocn = DATA_LOCN_TEMPL.format(stationNo)  
    store = FMQLReplyStore(dataLocn)
    startAtReply = store.firstReplyFileOnOrAfterCreateDay("2006_5849", "acquisition_start", onAndAfterDay) 
    if startAtReply == "":
        raise Exception("Can't find 2006_5849 start reply")
    resourceIter = FilteredResultIterator(dataLocn, "2006_5849")
    startDT = datetime.strptime("{}T00:00:01Z".format(onAndAfterDay), "%Y-%m-%dT%H:%M:%SZ")
    _2006_5849EFs = []
    queueConsultIds = set()
    for i, resource in enumerate(resourceIter, 1): # the live queue of telereader acquired consults
    
        try: # want valid only
            dt = datetime.strptime(resource["acquisition_start"]["value"], "%Y-%m-%dT%H:%M:%SZ")
        except:
            continue
        # Want precisely those in date window - nix early ones of first reply
        if dt < startDT:
            continue  
        count += 1
                
        flattenPropValues(resource)

        status = resource["status"]
        if status not in ["W:Waiting", "U:Unread", "C:Cancelled", "L:Locked", "D:Deleted", "R:Read"]:
            raise Exception("Unexpected status for queue entry")

        # Another one of these Config to Queue checks
        if "is_acquisition_service_procedure" in resource:
            raise Exception("If a service in telereader acquisition list is marked as a procedure then don't expect it to be in the queue")

        consultId = "123-" + re.search(r'123\-([^\]]+)', resource["consult_request"]).group(1)
        consult = consultRedById[consultId]
        if "ifc_role" not in consult:
            resource["isConsultLocal"] = True
        elif consult["ifc_role"] == "P:PLACER":
            resource["isConsultIFCPlacer"] = True
        else:
            raise Exception("All Consults referenced from TeleReader queue must either be IFC/Remote P:PLACER or just a local/insite consult (no ifc_role)")
        resource["consultService"] = consult["to_service"]
        queueConsultIds.add(consultId) # for separate "missing entries"
                
        auditTrail = consult["request_processing_activity"]
        transitions, addedCommentCount, tiuLocals, tiuRemotes = reducePlacer123Transitions(resource, auditTrail, auditPropsByUserName)
        resource["transitions"] = transitions
        resource["addedCommentCount"] = addedCommentCount
                
        # Let's take all reader information if not already there ... excluding
        # cancelled and ONLY taking R:Read. Important for 668 as only cancelled
        # are locals!
        """
        TODO: move off using queue and onto ALL people who send stuff and their roles. 
        Right now, only doing capture for those who at least once appear as remote
        duz for R:Read entry. -- expansion to anyone in audit trail and would need
        to do roles beyond combo of loc|rem, entr|resp and into action and perhaps
        any effecting documents.
        
        [reflected in props - if remote clerk disassociates (not responsible)
        then just see on remote_enterer!]
        """
        if "full_name_of_reader" in resource and resource["status"] == "R:Read":
        
            if "reader_duz_at_reading_site" in resource and "reader_duz_at_acquisition_site" in resource and re.search(r'\-(\d+)', resource["reader_duz_at_acquisition_site"]).group(1) == resource["reader_duz_at_reading_site"]:
                resource["isReadingAcquisitionSame"] = True
                
        _2006_5849EFs.append(resource)

    """
    Summary of consults overall and those for services expected to have TeleR entries
    but which don't.
    """
    trqConsultSummary = {
        "total": len(consultRedById),
    }        
    acquisitionServiceIds = set(id for id in consultRedById if "uses_acquisition_service" in consultRedById[id])
    missingFromQueue = consultDirectory.acquisitionServiceIds() - queueConsultIds
    if len(missingFromQueue):
        trqConsultSummary["missingFromQueue"] = len(missingFromQueue)
        missingFromQueueFillers = set(consultId for consultId in missingFromQueue if "ifc_role" in consultRedById[consultId] and consultRedById[consultId]["ifc_role"] == "F:FILLER")
        if len(missingFromQueueFillers):
            trqConsultSummary["missingFromQueueFillers"] = len(missingFromQueueFillers)
            missingFromQueueFillersServices = set(consultRedById[consultId]["to_service"] for consultId in missingFromQueueFillers)
            trqConsultSummary["missingFromQueueFillersServices"] = sorted(list(missingFromQueueFillersServices))
        missingFromQueueProcedure = set(consultId for consultId in missingFromQueue if "is_acquisition_service_procedure" in consultRedById[consultId])
        if len(missingFromQueueProcedure):
            trqConsultSummary["missingFromQueueProcedure"] = len(missingFromQueueProcedure)
            missingFromQueueProcedureServices = set(consultRedById[consultId]["to_service"] for consultId in missingFromQueueProcedure) 
            trqConsultSummary["missingFromQueueProcedureServices"] = sorted(list(missingFromQueueProcedureServices))         
        missingFromQueueLocalDiscontinue2 = set(consultId for consultId in missingFromQueue if "ifc_role" in consultRedById[consultId] and consultRedById[consultId]["ifc_role"] == "P:PLACER" and re.match(r'DISCONTINUED', consultRedById[consultId]["cprs_status"]))
        if len(missingFromQueueLocalDiscontinue2):
            trqConsultSummary["missingFromQueueLocalDiscontinue2"] = len(missingFromQueueLocalDiscontinue2)
        otherMissing = missingFromQueue - ((missingFromQueueFillers.union(missingFromQueueProcedure)).union(missingFromQueueLocalDiscontinue2))
        if len(otherMissing):
            trqConsultSummary["otherMissing"] = len(otherMissing)
    
    json.dump(_2006_5849EFs, open(qefsJSNFl, "w"))
    json.dump(trqConsultSummary, open(csJSNFl, "w"))

    print("\tReturning {:,} Enhanced 2006_5849's for the first time along with consult summary".format(len(_2006_5849EFs)))
    return _2006_5849EFs, trqConsultSummary
                        
# ################################# DRIVER #######################
               
def main():

    assert(sys.version_info >= (2,7))
    
    if len(sys.argv) < 2:
        print("need to specify station # ex/ 442 - exiting")
        return
        
    stationNo = sys.argv[1]
        
    if stationNo == "668":
        onAndAfterDay = "2018-04-12"
        upToDay = "2019-04-12"
        stationName = "Spokane"
    elif stationNo == "663":
        onAndAfterDay = "2018-04-17"
        upToDay = "2019-04-17"
        stationName = "Puget Sound"
    elif stationNo == "757":
        onAndAfterDay = "2018-07-29"
        upToDay = "2019-07-29" # last full day 
        stationName = "Columbus"       
    else:
        raise Exception("Only 668, 663 or 757 now")
        
    webReportTelereaderFiles(stationNo, stationName, onAndAfterDay, upToDay)
        
if __name__ == "__main__":
    main()
