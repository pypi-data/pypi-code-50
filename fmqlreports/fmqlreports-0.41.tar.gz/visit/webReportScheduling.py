#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import os
import re
import json
from collections import defaultdict, Counter
from datetime import datetime
import numpy

from fmqlutils.reporter.reportUtils import MarkdownTable, reportPercent, reportAbsAndPercent
from fmqlutils.typer.reduceTypeUtils import splitTypeDatas, checkDataPresent, singleValue, muBVC, muBVCOfSTProp
from fmqlreports.webReportUtils import filteredResultIterator, reduce200, TOP_MD_TEMPL, SITE_DIR_TEMPL, keyStats, roundFloat

"""
LAST ONE other than making these work: date.weekday()
   ie/ sunday 6, saturday 5
   sum(1 for appt ... if date appt .weekday() < 5)
"""

"""
Overall: Scheduling w/VSE focus

per institution (has station number), showing scheduling based on stop codes. Additional nuance provided by normalized physical location names and, if many locations, forms/templates of locations.

Note: one of the "DSS-based" (https://github.com/vistadataproject/workload/issues/27) reports as Location is key. Part of a flow from Appointment through Visit. Reporting on both should go in tandem - the visit report <=> visit workload report.

TODO: (beyond tighten with some provider ref ... mainly wait for visit)
* per provider stuff ie/ 
    # Bldg 31, Room 151/SPO CHIROPRACTOR 3 TESSENDORF
    def muFriendlyName(hlInfo): # leaving out "physical_location"
        friendlyNames = []
        if "patient_friendly_name" in hlInfo:
            friendlyNames.append(hlInfo["patient_friendly_name"])
        if "abbreviation" in hlInfo:
            friendlyNames.append(hlInfo["abbreviation"])
        return "/".join(friendlyNames)  
* make more of credit_stop_code (is being copied into hlloc)
* tighten details: 
  * walkins -- note from locn detail table that 'WALK IN URGENT CARE PROCEDURE', 'SPO AUDIO WALK IN' almost 100%  
  * instit with norm phy loc (relate to a map)
* keystat the stops + specialized ones like ANESTHESIA PRE POST-OP CONSULT to isolate providers etc
...... wait for visit .....
* MOVE 44_003 etc into distinct "comparison" report
* hosp locn table per instit BUT only for personal locns, not 1-1 phy or STOP? ie/ distinguish them
  ... or some way in main one // ex/ PACEMAKER stop has one locn ... may not be productive though.
* NORM Physical Locn and count ie/ see against map does it match?
* Grouping (IND, GRP) variations of Workcodes + 'SOCIAL WORK SERVICE' and others with little 
* any tie to room-bed/ward for any of the 44's?
* users (before providers), see if isolated to Institutions AND within them to buildings ie/ user/provider view ... see http://vistadataproject.info/demo2/location
  ----> do in SchedulingUsers for now
* see smaller clean up TODOs below
* clean out older code (in pre-calcs up front) ... goal is nix all but SC setup once ready
* BACK TO AUTOMATION FOR CSV and Pages and too hard otherwise <---- KEY TO FUTURE WEEKS
...
- Old Appt Sync/Reduce (checkout logic) [separate func below along with old visit's old report] ... RPC tie in
- Link to Visits (V PROVIDER not used but can a link be made) [see: https://github.com/vistadataproject/Archive/blob/master/prodclones/analyze/workload/createWorkDetailMVDM.py] <--- report 
- RPCs: ... will execute in tests and see form
  - [ ] see SDEC has the most https://github.com/vistadataproject/RPCDefinitionToolkit/blob/master/Reports/PerVistA/668/rpcInterfaceDefinition.md
  - [ ] get into RPC showing sched patients to a doc
- Extra: cancel/checkin/checkout and letters AND CONSULT or not CONSULT and its origin
- [ ] 409_833 resource name -- map user name to resource name (see gather by user) ie/ resources assoc with users? see how works
  and note 409_831 resource does pt to 200 or and do those user/locn groupings add up in 409_833?
- [ ] cancel/status break down?

Comments per
# 663
  * MOUNT VERNON is first bigger one where MH is not second
  * Smaller ones like MT VERNON have obvious locations for providers "PACT CYPRESS"/"PACT ORCA" etc? OR are these trees and animals for rooms?
# 668
  * COEUR D... doesn't have MH as second (PHY THER)
  
Note that there are parameters setting stop codes for SDEC

## 8989_5 property "parameter" value "SDEC_MENTAL_HEALTH_STOP_CODES_[8989_51-816]" Report

Total Selected: 5 (0.23%)
Filtered: 2,217 (99.77%)
First IEN: 2076
Properties:
        1. value_1 - LITERAL - 5 (100%)
                1. 1 - 5 (100.0%)
        2. entity - POINTER - 5 (100%) - 9_4
                1. SCHEDULING [9_4-48] - 5 (100.0%)
        3. instance - LITERAL - 5 (100%)
                1. 195 - 1 (20.0%)
                2. 188 - 1 (20.0%)
                3. 196 - 1 (20.0%)
                4. 237 - 1 (20.0%)
                5. 247 - 1 (20.0%)
        4. parameter - POINTER - 5 (100%) - 8989_51
                1. SDEC MENTAL HEALTH STOP CODES [8989_51-816] - 5 (100.0%)

"""

"""
VSE/SDEC - VSE: VistA Scheduling Enhancements

Two PDFs:
- https://www.va.gov/vdl/documents/Clinical/Scheduling/VSE_GUI_1_5_Technical_Manual.pdf and https://usermanual.wiki/Pdf/VSEGUI15UserGuide.1029341778/view
and
- https://www.va.gov/vdl/documents/Clinical/Scheduling/VSE_GUI_1_4_User_Guide.pdf

This is where a Resource object is defined for Clinical Scheduling. A Resource Object can be a NEW PERSON, HOSPITAL LOCATION, or an SDEC ADDITIONAL RESOURCE. A Resource is linked to a HOSPITAL LOCATION (or Clinic) (=> split by it)

---------- type em, 2019 focus -------------
SDEC APPOINTMENT (409.84): 874,714 - TYPE/2019
SDEC APPT REQUEST (409.85): 806,016 - TYPE/2019 ---> note: pts to 409.84 (majority of 409_84's seem to start with this request). Minority from consults etc
---------- walk explicitly as ALL ----------
SDEC RESOURCE USER (409.833): 18,262 ... Person links TO Resource 409.831 ... split by username/ keeping resources ie/ MANY resources per user (per doctor!!!) and as many more users => resources are shared [can analyze]
SDEC CONTACT (409.86): 8,989 <--- need to cache
SDEC RESOURCE (409.831): 3,597 ... Links to 44 but have type of 200 or 44 or 409.834 [0]
<---- TYPE split by hospital_location as 1-1 with resource_type
--------------------------------------------
SDEC PREFERENCES AND SPECIAL NEEDS (409.845): 416
SDEC RESOURCE GROUP (409.832): 102
SDEC ACCESS TYPE (409.823): 3
"""
def reportAppointmentsVSE(stationNo):

    allThere, details = checkDataPresent(stationNo, [

        {"fileType": "4", "check": "ALL"},
        {"fileType": "44", "check": "ALLRF"},
        
        {"fileType": "409_84", "check": "TYPE"},
        {"fileType": "409_84", "check": "MTH3"},

        {"fileType": "409_831", "check": "ALL"},
        {"fileType": "409_833", "check": "ALL"}

    ])
    if not allThere:
        raise Exception("Some required data is missing - {}".format(details))

    institInfosByIEN = reduce4(stationNo)
    hlInfosByIEN = reduce44(stationNo)
    resourceInfosByIEN = reduce409_831(stationNo)
        
    _all, sts = splitTypeDatas(stationNo, "409_84") # SDEC Appointments
    allMTH3, stsMTH3 = splitTypeDatas(stationNo, "409_84", reductionLabel="MTH3") # resource, time of starttime
    
    # ENFORCE: Make a statement that only doing Location resources - enforce it
    def enforceResourcesAllLocation(stsMTH3):
        for st in stsMTH3:
            if "resource" not in st:
                continue
            resourceRef = singleValue(st, "resource")
            resourceIEN = re.search(r'\-(\d+)\]', resourceRef).group(1)
            resourceInfo = resourceInfosByIEN[resourceIEN]
            if resourceInfo["source_resource_class"] != "LOCATION":
                raise Exception("Expect all resources with appointments to be LOCATION")
    enforceResourcesAllLocation(stsMTH3)
        
    # Pull in hospital location props
    for st in stsMTH3:
        if "resource" not in st:
            return
        resourceRef = singleValue(st, "resource")
        resourceIEN = re.search(r'\-(\d+)\]', resourceRef).group(1)
        resourceInfo = resourceInfosByIEN[resourceIEN]
        st["_hospital_location"] = resourceInfo["hospital_location"]     
    stsMTH3 = enhanceHLocSTsByHLOC(hlInfosByIEN, stsMTH3)
                    
    try:
        PLOCMAP = json.load(open("MetaPerStation/{}/physicalLocationsNorm.json".format(stationNo)))
    except:
        PLOCMAP = None        
                
    # ############################ MU REPORT ################################
            
    mu = "VistA Scheduling Enhancements (VSE) is the package used for appointment creation and tracking. Despite the word \"Enhancements\", VSE is a new package that superceeds an older scheduling package.\n\n"
    
    # TODO: put into config for VistA ie/ last day off 9000010 next or ...
    allApptMadeYears = sorted([int(yr) for yr in _all["date_appt_made"]["byValueCount"].keys()]) # ignoring for now as fixing term above
    dataRangeMU = "the most recent three months of data"

    muProviderTotal = "Only <span class='yellowIt'>{}</span> of these \"Location Appointments\"  specify a provider".format(reportAbsAndPercent(allMTH3["provider"]["count"], allMTH3["_total"])) if "provider" in allMTH3 else "No appointments specify a provider"
    mu += "This system has <span class='yellowIt'>{:,}</span> VSE appointments, the first made in {}. From {} (property \"starttime\"), it shows <span class='yellowIt'>{}</span> appointments for <span class='yellowIt'>{:,}</span> patients and <span class='yellowIt'>{:,}</span> \"Resources\".\n\nThe software allows a \"Resource\" to be a provider or a location but in this system, all resources with appointments from 2019 are locations - in other words, appointments are only made for locations. {}.\n\n".format(
        _all["_total"],
        allApptMadeYears[0],
        dateRangeMU,
        reportAbsAndPercent(allMTH3["_total"], _all["_total"]),
        allMTH3["patient"]["rangeCount"],
        allMTH3["resource"]["rangeCount"],
        muProviderTotal # very unlikely: say in Columbus as moved on from VSE
    )
            
    mu += muByInstitutions(institInfosByIEN, stsMTH3, plocMap=PLOCMAP)
    
    mu += muAboutWorkLocation() 
    
    """
    TODO: markup or check "length of appt" and see date appt made vs
    split on appt time ie/ where one is == or < or ... (same for 44_003 below)
    
    Also appointment_type (which was removed from generic)
    """
    propsPresenceToCount=["checkin", "checkout", "noshow", "consult_link", "provider"]
    mu += muByStopCodes(allMTH3, stsMTH3, plocMap=PLOCMAP, propsPresenceToCount=propsPresenceToCount)
                    
    # #################### FINAL WRITE OUT ###########################
    userSiteDir = SITE_DIR_TEMPL.format(stationNo)
    print("Serializing Report to {}".format(userSiteDir))
    if not os.path.isdir(userSiteDir):
        raise Exception("Expect User Site to already exist with its basic contents")
    title = "VSE Appointments {}".format(stationNo)
    mu = TOP_MD_TEMPL.format(title, "VSE Appointments") + mu
    open(userSiteDir + "appointmentsVSE.md", "w").write(mu)
    
# ############################## Legacy Form Appointments 44_003 #######################

"""
In form, this follows VPE (409_84) reports except where Legacy 44.003 has its own
properties (consult ref)

TODO: add from type of 44_003 here ala for 409_84 above
"""
def reportAppointmentsLegacy44(stationNo):

    allThere, details = checkDataPresent(stationNo, [

        {"fileType": "44", "check": "ALLRF"},
        {"fileType": "44_003", "check": "TYPE"},
        {"fileType": "44_003", "check": "MTH3"}

    ])
    if not allThere:
        raise Exception("Some required data is missing - {}".format(details))

    institInfosByIEN = reduce4(stationNo)
    hlInfosByIEN = reduce44(stationNo)

    LOCN_PROP = "appointment_container_"

    _all, sts = splitTypeDatas(stationNo, "44_003")
    allMTH3, stsMTH3 = splitTypeDatas(stationNo, "44_003", reductionLabel="MTH3", expectSubTypeProperty="appointment_container_")

    # ENFORCE: check all locations with appts have a stop code in 2019
    if sum(1 for locnRef in stsMTH3ByLocnRef if "stop_code_number" not in hlInfosByIEN[re.search(r'\-(\d+)', locnRef).group(1)]): 
        raise Exception("A location with a 2019 appointment is missing a stop code")
        
    for st in stsMTH3:
        if LOCN_PROP not in st:
            continue
        st["_hospital_location"] = hlRef
    stsMTH3 = enhanceHLocSTsByHLOC(hlInfosByIEN, stsMTH3)
            
    mu = "VistA Scheduling Legacy was the only mechanism used for managing appointments in VistA before VistA Scheduling Enhancements (VSE).\n\n"
    
    # TODO: put into config for VistA ie/ last day off 9000010 next or ...
    allApptMadeYears = sorted([int(dt.split("-")[0]) for dt in _all["date_appointment_made"]["byValueCount"].keys()]) # ignoring for now as fixing term above
    dateRangeMU = "the most recent three months of data"
    
    mu += "This system has <span class='yellowIt'>{:,}</span> legacy appointments, the first made in {}. From {} (property \"appointment_date_time\"), it shows <span class='yellowIt'>{}</span> appointments for <span class='yellowIt'>{:,}</span> patients and <span class='yellowIt'>{:,}</span> \"Locations\".\n\n".format(
        _all["_total"],
        allApptMadeYears[0],
        dateRangeMU,
        reportAbsAndPercent(allMTH3["_total"], _all["_total"]),
        allMTH3["patient"]["rangeCount"],
        allMTH3[LOCN_PROP]["rangeCount"]
    )
    
    mu += muByInstitutions(institInfosByIEN, stsMTH3, plocMap=PLOCMAP)
    
    mu += muAboutWorkLocation() 
    
    """
    TODO: markup or check "length of app't" and see date_appointment_made vs
    split on appointment_date_time ie/ where one is == or < or ...
    """
    propsPresenceToCount=["checked-in", "checked_out", "appointment_cancelled", "consult_link"]
    mu += muByStopCodes(allMTH3, stsMTH3, plocMap=PLOCMAP, propsPresenceToCount=propsPresenceToCount)
            
    # #################### FINAL WRITE OUT ###########################
    userSiteDir = SITE_DIR_TEMPL.format(stationNo)
    print("Serializing Report to {}".format(userSiteDir))
    if not os.path.isdir(userSiteDir):
        raise Exception("Expect User Site to already exist with its basic contents")
    title = "Legacy Appointments {}".format(stationNo)
    mu = TOP_MD_TEMPL.format(title, "Legacy Appointments") + mu
    open(userSiteDir + "appointmentsLegacy44.md", "w").write(mu)
    
# ################################ Comparisons ###################

"""
Work in progress <----- TODO ... and may just replace with a combo table once
see individual reports
"""
def compareVPELegacyAppointments(stationNo):

    """
    Old < New as sometimes deleted when cancelled. ALSO check in by CONNECT,VPS not recorded in NEW but in old. 
    
    TODO: day start/on ... get 44_003 done for this; as need CONNECT,VPS check in from old? ... need to line them all up.
    
    Interpretation of appts at one location MADE on the same day ('date_appointment_made')
    ie/ correlate based on day made
    - old has 20, new has 25
      - 5 'missing' are CANCELLED in NEW
        ... KIR**,L**** L <---- cancelled by clinic ("APPOINTMENT CANCELLED" in old if date cancel < date of appt (would otherwise old deleted?))
        ... 2 x MCC****,D <---- cancelled by clinic (deleted if canceled by date is > date of appt)
        ... SAG... <--- cancelled by patient (note: date of cancelled by patient is less than start time!)
    - OLD:SC LESS ... -> NEW:REGULAR / OLD:50 to 100 -> NEW:SERVICE CONNECTED
    - checkin same
      - CONNECT,VPS is in OLD one of the sources of the checkin. No equivalent in 409_84 (elsewhere?)
    - length of appt same
    - cancel ...
      - OLD: NOTHING! -> NEW: NO SHOW (and no checkin)
      - OLD: APPOINTMENT CANCELLED -> NEW: C:CANCELLED BY CLINIC
    """
    def cacheApptsOf(locnLabel):

        from fmqlutils.cacher.cacherUtils import TMPWORKING_LOCN_TEMPL
        jsnFl = TMPWORKING_LOCN_TEMPL.format(stationNo) + "{}OldNNewAppts.json".format(re.sub(r' ', '_', locnLabel))
        try:
            onAppts = json.load(open(jsnFl))
        except:
            pass
        else:
            return onAppts

        oldApptsByDay = defaultdict(list)
        for resource in filteredResultIterator(stationNo, "44_003", useRF=True):
            print(json.dumps(resource, indent=4))
            oldApptsByDay[resource[""]].append(resource)
            
        newApptsByDay = defaultdict(list)
        for resource in filteredResultIterator(stationNo, "409_84"):
            print(json.dumps(resource, indent=4))
            newApptsByDay[resource[""]].append(resource)
            
        onAppts = {"old": oldApptsByDay, "new": newApptsByDay}
            
        json.dump(onAppts, open(jsnFl, "w"))
        
        return onAppts
            
    cacheApptsOf("SPO CHIROPRACTOR 3")
    
    """
        # Pug has 1 with only 1 appt
    legacyExtra = set(stsOld19ByLocnRef.keys()) - vpsLocations
    if len(legacyExtra):
        extraAppts = ["Appts {}".format(st["_total"]) for st in stsOld19 if re.sub(r'44\-', '', singleValue(st, "appointment_container_")) in legacyExtra]
        print("** WARNING: Legacy Appointments for 2019 exist for locations NOT supported in new VPS (but small error only?): {} - {}".format(", ".join(list(legacyExtra)), extraAppts))
    """
    
# ################################# Common MU's/ HL Enhance ###################

"""
Focus is [1] per institution and [2] stop codes as [3] work locations are combination concepts. Need to report on both [A] VPE and [B] Legacy 44.003 (and maybe per patient too)
"""
def muAboutWorkLocation(): # background blurb shared
    
    mu = "In VistA, location (\"Work Location\") represents the combination of [i] a type of work in [ii] a specific institution performed by [iii] a particular provider, group of providers or class of provider. Appointments and Visits are organized around these Work Locations.\n\n"
    
    mu += "The work type of each Work Location is formally specified with a VA-custom \"stop code number\", the key designator for VA's _Decision Support System_ (DSS) ...\n\n"
    
    # "DSS calculates the actual cost to provide patientcare services"
    mu += "> VHA collects workload data that supports the continuity of patient care, resource allocation, performance measurement, quality management, and third-party collections. Decision Support System (DSS) Identifiers assist VA medical centers in defining workload, which is critical for costing purposes. DSS Identifiers are used to identify workload for all outpatient encounters, inpatient appointments in outpatient clinics, and inpatient billable professional services. They also serve as guides to select DSS outpatient department structures.\n\n"
    
    mu += "This approach downplays physical location as one physical location may host many Work Locations. Even when specified in the system, physical location is a freeform text string that varies greatly in form and quality - it has been somewhat normalized in the tables below.\n\n"
    
    mu += "The use of Work Locations for appointments makes _stop code_ the best mechanism for describing and typing appointments.\n\n"
    
    return mu
    
"""
By Institution summary 

Expects: _institution, _stop_code_number added to st's
"""
def muByInstitutions(institInfosByIEN, sts, plocMap=None): # TODO: map ploc ala sc mu below

    stsByInstitution = defaultdict(list)
    stsNoInstitution = [] # again
    stByPhyLocByInstit = defaultdict(lambda: defaultdict(list))
    patientsByInstitution = defaultdict(set)
    apptCountByInstitution = Counter()
    apptTypeCountByInstitution = defaultdict(lambda: Counter()) # only 409_84
    for st in sts:
        if "_institution" not in st:
            stsNoInstitution.append(st)
            continue
        instit = st["_institution"]
        stsByInstitution[st["_institution"]].append(st)
        apptCountByInstitution[instit] += st["_total"]
        patientsByInstitution[st["_institution"]] |= set(st["patient"]["byValueCount"])
        if "_physical_location" in st:
            pl = st["_physical_location"].upper()
            stByPhyLocByInstit[instit][pl].append(st)
        if "appointment_type" in st: # 409_84 only
            bvc = st["appointment_type"]["byValueCount"]
            for v in bvc:
                apptTypeCountByInstitution[instit][v] += bvc[v] 

    cols = ["Institution", "Station", "Locns", "Locn Prefixes", "Phy Locns", "Stop Codes", "PTs", "Appointments"]
    if len(apptTypeCountByInstitution):
        cols.append("Appointment Types")
    tbl = MarkdownTable(cols)
    for instit in sorted(apptCountByInstitution, key=lambda x: apptCountByInstitution[x], reverse=True):
        institIEN = re.search(r'(\d+)\]$', instit).group(1)
        institInfo = institInfosByIEN[institIEN]
        isno = institInfo["station_number"] if "station_number" in institInfo else ""
        byStopCodeCount = Counter()
        hlocPrefixes = Counter
        for st in stsByInstitution[instit]:
            if "_stop_code_number" not in st:
                continue
            byStopCodeCount[st["_stop_code_number"]] += 1
            hlocPrefixes[st["_prefix"] if "_prefix" in st else "NO PREFIX"] += 1
        row = [
            "__{}__".format(re.sub(r' +$', '', instit.split(" [")[0])),
            isno,
            len(stsByInstitution[instit]),
            muBVC(hlocPrefixes),
            len(stByPhyLocByInstit[instit]) if instit in stByPhyLocByInstit else "",
            len(byStopCodeCount),
            reportAbsAndPercent(len(patientsByInstitution[instit]), allMTH3["patient"]["rangeCount"]),
            reportAbsAndPercent(apptCountByInstitution[instit], allMTH3["_total"])
        ]
        if len(apptTypeCountByInstitution):
            row.append(muBVC(apptTypeCountByInstitution[instit]))
        tbl.addRow(row)
    mu = "<span class=\"yellowIt\">{:,}</span> \"Institutions\" supported by this system have Appointments spread over <span class=\"yellowIt\">{:,}</span> locations with <span class=\"yellowIt\">{:,}</span> stop codes ...\n\n".format(
        len(apptCountByInstitution),
        sum(len(stsByInstitution[instit]) for instit in stsByInstitution),
        len(set(st["_stop_code_number"] for st in stsMTH3 if "_stop_code_number" in st))
    )
    mu += tbl.md() + "\n\n"
    
    if len(stsNoInstitution):
        mu += "__Note__: <span class=\"yellowIt\">{:,}</span> location(s), {}, with <span class=\"yellowIt\">{:,}</span> appointments either don't specify an institution or one can't be derived from its name.\n\n".format(
            len(stsNoInstitution),
            ", ".join([st["_hospital_location"].split(" [")[0] if "_hospital_location" in st else "NONE" for st in stsNoInstitution]),
            sum(st["_total"] for st in stsNoInstitution)
        )
    
    return mu
    
"""
Stop Code as Anchor - [1] separate out the non 'in person' appts from [2] TELEPHONE 
etc for the primary institutions and then all others.
    
See: https://www.va.gov/vdl/documents/Financial_Admin/Decision_Supp_Sys_(DSS)/dss_ug.pdf, http://vistadataproject.info/demo2/ and http://vistadataproject.info/demo2/location (need to rework these)
    
TODO Overall:
- more on those others (TELEPHONE etc)
- TELEHEALTH -- go beyond stops
- PRIMARY CARE broken out as secondaries won't do anything ... need more
- GROUPs of Stop Codes
    
TODO Appt Details:
- checkout etc BUT first see OLD Appts and Visits too ie/ V PROVIDER not linked explicitly but can a link be made? 
"""
def muByStopCodes(_all, sts, plocMap=None, propsPresenceToCount=[]):

    # FUTURE: consider grouping stop codes together
    SC_GROUPS = [
        ["ORTHO JOINT SURG", "PODIATRY"], # Building 1e SPECIALITY for this
        ["OPHTHALMOLOGY", "OPTOMETRY"], # Building 40 ... expect SPO EYE for first twos
        ["BROS (BLIND REHAB O P SPEC)", "PHYSICAL THERAPY", "CHIROPRACTIC CARE", "OCCUPATIONAL THERAPY", "WHEELCHAIR & ADVAN MOBILITY", "RECREATION THERAPY SERVICE", "PROSTHETICS ORTHOTICS"], # Building 31
        ["MH INTGRTD CARE GRP", "MH INTGRTD CARE IND"], # group these but not others?
        ["PSYCHOLOGICAL TESTING", "MH INTGRTD CARE IND", "PTSD - INDIVIDUAL"], # B40, BHS (not SUBSTANCE USE DISORDER IND)
        ["SUBSTANCE USE DISORDER IND", "SUBSTANCE USE DISORDR GRP"],
        
        ["MENTAL HEALTH CLINIC - IND", "MENTAL HEALTH CLINIC-GROUP", "MH INTGRTD CARE IND", "MH TEAM CASE MANAGEMENT", "PSYCHOLOGICAL TESTING", "PTSD - GROUP", "PTSD - INDIVIDUAL", "SUBSTANCE USE DISORDR GRP"]
    ]
    
    # FUTURE: more expansion for Workload Location names
    MED_ACRONYMS = {
    
        "DI": "DIAGNOSTIC IMAGING",
        "BHS": "BEHAVIORAL HEALTH SERVICES"
        
    }
                                
    def muAppointmentsOfStopCodes(instit, stsOfSC, plocMap=None, propsPresenceToCount=[], showLocations=False):
        def dashNBVC(sts, prop, valMap=None):
            cntr = Counter()
            for st in stsOfSC[sc]:
                if prop not in st:
                    val = "*NOT SET*"
                elif re.match(r'\_', prop):
                    val = re.sub(r' +$', '', st[prop].upper())
                    if valMap and val in valMap:
                        val = valMap[val]
                    cntr[val] += st["_total"]
                else:
                    for val in st[prop]["byValueCount"]:
                        cntr[val.split(" [")[0]] += st[prop]["byValueCount"][val]
            return cntr 
        def bvcSTSs(sts, prop):
            cntr = Counter()
            for st in sts:
                for val in st[prop]["byValueCount"]:
                    cntr[val.split(" [")[0]] += st[prop]["byValueCount"][val]
            return cntr
        def bvcPropsPresence(sts, props):
            cntr = Counter()
            for st in sts:
                if prop not in st:
                    continue
                cntr[prop] += st[prop]["count"]
            return cntr
        def countLocnPrefixes(sts):
            cntrAppear = Counter()
            entries = []
            for st in sts:
                locn = re.sub(r'^ +', '', re.sub(r' +$', '', st["_hospital_location"].split(" [")[0]))
                pieces = locn.split(" ")
                entry = [[], st["_total"]]
                for i in range(1, len(pieces) + 1):
                    k = " ".join(pieces[0:i])
                    cntrAppear[k] += 1
                    entry[0].append(k)
                entries.append(entry)
            cntr = Counter()
            for entry in entries: # reduce entries and count 
                ks = entry[0]
                if len(ks) >= 3 and cntrAppear[ks[2]] > 1 and not re.search(r' (\d+|[A-Z])$', ks[2]):
                    cntr[ks[2]] += entry[1]
                    continue
                if len(ks) >= 2 and cntrAppear[ks[1]] > 1:
                    cntr[ks[1]] += entry[1]
                    continue
                cntr[ks[-1]] += entry[1] 
            return cntr
        tbl = MarkdownTable(["Stop Code", "\# Locations", "Location [Roots]", "Physical Location(s)", "PTs", "Appts", "Prop Counts"])
        scs = sorted(stsOfSC.keys(), key=lambda x: sum(st["_total"] for st in stsOfSC[x]), reverse=True)
        rplocMap = {}
        if plocMap:
            for ploc in plocMap:
                for rploc in plocMap[ploc]:
                    rplocMap[rploc] = ploc
        csvs = [",".join(["Stop Code", "Location(s)", "Physical Location(s)", "PTs", "Appts"])]
        for sc in scs:
            locns = set(st["_hospital_location"] for st in stsOfSC[sc]) 
            phyLocCntr = dashNBVC(stsOfSC[sc], "_physical_location", rplocMap)     
            tbl.addRow([
                "__{}__".format(re.sub(r'\_', ' ', sc.split(" [")[0])),
                muBVC(dashNBVC(stsOfSC[sc], "_hospital_location")) if showLocations else len(locns),
                muBVC(countLocnPrefixes(stsOfSC[sc])),
                muBVC(phyLocCntr) if len(phyLocCntr) else "",
                len(bvcSTSs(stsOfSC[sc], "patient")),
                reportAbsAndPercent( # % of these appts (not total overall instits)
                    sum(st["_total"] for st in stsOfSC[sc]),
                    sum(st["_total"] for sc in scs for st in stsOfSC[sc])
                ),
                muBVC(bvcPropsPresence(sts, propsPresenceToCount))
            ])
            csvs.append(",".join([
                re.sub(r'\_', ' ', sc.split(" [")[0]),  
                str(len(locns)) if len(locns) > 1 else "\"{}\"".format(list(locns)[0].split(" [")[0]),
                str(len(phyLocCntr)) if len(phyLocCntr) > 1 else ("\"{}\"".format(phyLocCntr.keys()[0]) if len(phyLocCntr) else ""),
                str(len(bvcSTSs(stsOfSC[sc], "patient"))),
                str(sum(st["_total"] for st in stsOfSC[sc]))
            ]))
        open("{}/".format(stationNo) + re.sub(r' ', '_', instit.split(" [")[0]) + ".csv", "w").write("\n".join(csvs))
                
        return tbl.md() + "\n\n"
    
    stsWSC = [st for st in sts if "_stop_code_number" in st and "_institution" in st]
    def catagST(st):
        for mtch, catag in [
            (r'(TELEPHONE|PHONE)', "TELEPHONE"),
            (r'(COMMUNITY CARE CONSULT)', "CC"),
            (r'(ADMIN PAT ACTIVTIES)', "ADMIN"),
            (r'(HOME)', "HOME")
        ]:
            if re.match(mtch, st["_stop_code_number"]):
                return catag
        return ""
    stsByCategory = defaultdict(list)
    for st in stsWSC:
        catag = catagST(st)
        if catag:
            stsByCategory[catag].append(st)
            continue
        """
        TODO: doesn't take them ALL -- if TELEHEALTH in physical_location takes
        others w/o a secondary code
        """
        if "_credit_stop_code" in st and re.search(r' TH ', st["_credit_stop_code"]):
            stsByCategory["TELEHEALTH"].append(st)
            continue
        stsByCategory["INPERSON"].append(st)

    mu = "## By Stop Code\n\n"
    mu += "The system holds <span class='yellowIt'>{}</span> in-person, clinical appointments. There are also <span class='yellowIt'>{}</span> _TELEPHONE_, <span class='yellowIt'>{}</span> _COMMUNITY CARE_, <span class='yellowIt'>{}</span> _in home care_, <span class='yellowIt'>{}</span> _Telehealth_ and <span class='yellowIt'>{}</span> _administrative appointments_.\n\n".format(
        reportAbsAndPercent(
            sum(st["_total"] for st in stsByCategory["INPERSON"]),
            _all["_total"]
        ),
        reportAbsAndPercent(
            sum(st["_total"] for st in stsByCategory["TELEPHONE"]),
            _all["_total"]
        ),
        reportAbsAndPercent(   
            sum(st["_total"] for st in stsByCategory["CC"]),
            _all["_total"]
        ),
        reportAbsAndPercent(   
            sum(st["_total"] for st in stsByCategory["HOME"]),
            _all["_total"]
        ),
        # Undercounted as secondary not enough to break out and NO PRIMARY code
        # ... could use physical location matches but didn't for now
        reportAbsAndPercent(   
            sum(st["_total"] for st in stsByCategory["TELEHEALTH"]),
            _all["_total"]
        ),
        reportAbsAndPercent(   
            sum(st["_total"] for st in stsByCategory["ADMIN"]),
            _all["_total"]
        )
    )
    inPersonSTsByInstitBySC = defaultdict(lambda: defaultdict(list))
    for st in stsByCategory["INPERSON"]:
        instit = st["_institution"]
        inPersonSTsByInstitBySC[instit][st["_stop_code_number"]].append(st)
    for instit in sorted(inPersonSTsByInstitBySC, key=lambda x: sum(st["_total"] for sc in inPersonSTsByInstitBySC[x] for st in inPersonSTsByInstitBySC[x][sc]), reverse=True):
        institIEN = re.search(r'(\d+)\]$', instit).group(1)
        institInfo = institInfosByIEN[institIEN]
        isno = institInfo["station_number"] if "station_number" in institInfo else "No Station Number"
        mu += "Institution _{} [{}]_ uses <span class='yellowIt'>{:,}</span> stop codes for <span class='yellowIt'>{}</span> 'in-person' appointments. Where there are many Work Locations, only the root (first pieces) of those locations are shown,  ...\n\n".format(
            re.sub(r' +$', '', instit.split(" [")[0]), 
            isno,
            len(inPersonSTsByInstitBySC[instit]),
            reportAbsAndPercent(sum(st["_total"] for sc in inPersonSTsByInstitBySC[instit] for st in inPersonSTsByInstitBySC[instit][sc]), _all["_total"])
        )
        mu += muAppointmentsOfStopCodes(instit, inPersonSTsByInstitBySC[instit], plocMap, propsPresenceToCount)
        
    # TODO: more on Telehealth etc + break that out more as still inside as codes aren't enough
    
    return mu
    
"""
Expect: _hospital_location to be in st
Copies key HLOC props into st for ease of mu - makes sure same props for both
409_84 and 44_003 reductions.
"""
def enhanceHLocSTsByHLOC(hlInfosByIEN, sts):
    def addHLPropsToApptST(st, hlInfo):
        pieces = re.split(r'[ \-]', hlInfo["label"])
        if len(pieces) > 1:
            st["_prefix"] = pieces[0]
        for prop in ["stop_code_number", "credit_stop_code", "physical_location", "patient_friendly_name", "abbreviation", "provider", "institution"]:
            if prop in hlInfo:
                st["_" + prop] = hlInfo[prop]
        return st
    for st in sts:
        if "_hospital_location" not in st:
            continue
        hlIEN = re.search(r'\-(\d+)\]', st["_hospital_location"]).group(1)
        hlInfo = hlInfosByIEN[hlIEN]
        addHLPropsToApptST(st, hlInfo)
    return sts

# ################################# Reduce/Lookup #################

"""
Break Resource 409_831 - VPE has indirection for NEW PERSON (200) and
HOSPITAL LOCATION (44) appointments.
"""
def reduce409_831(stationNo):
    from fmqlutils.cacher.cacherUtils import TMPWORKING_LOCN_TEMPL
    jsnFl = TMPWORKING_LOCN_TEMPL.format(stationNo) + "vpeResourceReduction.json"
    try:
        infosByIEN = json.load(open(jsnFl))
    except:
        pass
    else:
        return infosByIEN
    infosByIEN = {}
    for resource in filteredResultIterator(stationNo, "409_831"):
        missingMands = set(["entered_by_user", "date_time_entered", "resource_type"]) - set(resource.keys())
        if len(missingMands):
            raise Exception("Resource 409_831 missing mandatory properties - {}".format(missingMands))
        red = {"_ien": resource["_id"].split("-")[1]}
        infosByIEN[resource["_id"].split("-")[1]] = red
        for prop in resource:
            if re.match(r'_', prop) or prop in ["label", "type"]:
                continue
            if prop == "resource_type": # VPTR to lead to two
                red["source_resource"] = "{} [{}]".format(resource[prop]["label"], resource[prop]["id"]) # no split as VPTR
                trt = resource[prop]["id"].split("-")[0] 
                # Note: perhaps ??? TODO 200's do too?
                if trt == "44" and "hospital_location" not in resource:
                    raise Exception("Expected resource 44's to have hospital location")
                if trt == "44":
                    red["source_resource_class"] = "LOCATION" 
                elif trt == "200":
                    red["source_resource_class"] = "USER"
                else: 
                    red["source_resource_class"] = "SDEC ADDITIONAL" # none in SPOKANE
                continue
            if isinstance(resource[prop], dict):
                if "value" in resource[prop]:
                    red[prop] = resource[prop]["value"]
                    continue
                if "id" in resource[prop]:
                    red[prop] = "{} [{}]".format(resource[prop]["label"], resource[prop]["id"].split("-")[1]) 
                    continue
                raise Exception("Dict Valued Prop not date or ref")
            red[prop] = resource[prop]        
    print("Dumping 409_831 reduction for first time - {:,} LOCATION's, {:,} USER's, {:,} SDEC ADDITIONALs".format(
        sum(1 for ien in infosByIEN if infosByIEN[ien]["source_resource_class"] == "LOCATION"),
        sum(1 for ien in infosByIEN if infosByIEN[ien]["source_resource_class"] == "USER"),            
        sum(1 for ien in infosByIEN if infosByIEN[ien]["source_resource_class"] == "SDEC ADDITIONAL")            
    ))
    json.dump(infosByIEN, open(jsnFl, "w"), indent=4)
    return infosByIEN

def reduce44(stationNo): # do from RF

    from fmqlutils.cacher.cacherUtils import TMPWORKING_LOCN_TEMPL
    jsnFl = TMPWORKING_LOCN_TEMPL.format(stationNo) + "hlReduction.json"
    try:
            infosByIEN = json.load(open(jsnFl))
    except:
        pass
    else:
        return infosByIEN
    infosByIEN = {}
    countWProvider = 0
    countDefaultProviderNotInProvider = 0
    def copyMProp(resource, red, mprop):
        if mprop not in resource:
            return None
        red[mprop] = set()
        for mresource in resource[mprop]:
            pref = "{} [{}]".format(mresource[mprop]["label"], mresource[mprop]["id"].split("-")[1])
            red[mprop].add(pref)
        red[mprop] = list(red[mprop])
        return red
    institutionsByHPrefix = defaultdict(set) # for mapping
    for resource in filteredResultIterator(stationNo, "44", useRF=True):
        ien = resource["_id"].split("-")[1]
        red = {"ien": ien, "label": resource["name"]}
        infosByIEN[ien] = red
        for litProp in ["abbreviation", "patient_friendly_name", "physical_location", "length_of_appointment", "default_appointment_type", "noncount_clinic_y_or_n", "clinic_meets_at_this_facility"]: # includes enum
            if litProp not in resource:
                continue
            red[litProp] = resource[litProp]
        for dtProp in ["inactivate_date", "reactivate_date", "availability_flag"]:
            if dtProp not in resource:
                continue
            red[dtProp] = resource[dtProp]["value"]
        for refProp in ["stop_code_number", "credit_stop_code", "institution", "division", "type_extension", "default_provider"]:
            if refProp not in resource:
                continue
            refv = resource[refProp]
            ref = "{} [{}]".format(refv["label"], refv["id"].split("-")[1])
            red[refProp] = ref
            if refProp == "institution":
                hprefix = resource["name"].split(" ")[0]
                institutionsByHPrefix[hprefix].add(ref)
        # Mult Availability - note many exs where no appts
        if "availability" in resource: # want to see if always there if appointments too
            red["has_availability"] = True
        if copyMProp(resource, red, "provider"):
            if "default_provider" in red and red["default_provider"] not in red["provider"]:
                countDefaultProviderNotInProvider += 1
            countWProvider += 1
        copyMProp(resource, red, "privileged_user") # the clerks etc
        # Note: appointment FLIPPED/REDUCED so won't know that?
        
    # Fill in missing instit links based on prefix mappings from those with an instit
    noMissing = 0
    noFilled = 0
    for ien in infosByIEN:
        info = infosByIEN[ien]
        if "institution" in info:
            continue
        noMissing += 1
        hprefix = info["label"].split(" ")[0]
        if hprefix in institutionsByHPrefix and len(institutionsByHPrefix[hprefix]) == 1:
            info["institution"] = list(institutionsByHPrefix[hprefix])[0]
            noFilled += 1
    print("Of {:,} locations missing an institution link, {:,} were filled by heuristic".format(noMissing, noFilled))
        
    print("Dumping {:,} locations, {:,} have providers with {:,} having default provider not in provider list".format(len(infosByIEN), countWProvider, countDefaultProviderNotInProvider))
    json.dump(infosByIEN, open(jsnFl, "w"), indent=4)
    return infosByIEN

def reduce4(stationNo):
    from fmqlutils.cacher.cacherUtils import TMPWORKING_LOCN_TEMPL
    jsnFl = TMPWORKING_LOCN_TEMPL.format(stationNo) + "4Reduction.json"
    try:
            infosByIEN = json.load(open(jsnFl))
    except:
        pass
    else:
        return infosByIEN
    infosByIEN = {}
    for resource in filteredResultIterator(stationNo, "4"):
        ien = resource["_id"].split("-")[1]
        red = {"ien": ien, "label": resource["name"]}
        infosByIEN[ien] = red
        if "reporting_station" in resource:
            red["reporting_station"] = "{} [{}]".format(resource["reporting_station"]["label"], resource["reporting_station"]["id"].split("-")[1]) 
        for prop in ["va_type_code", "status", "npi", "official_va_name", "station_number"]:
            if prop not in resource:
                continue
            red[prop] = resource[prop]
    json.dump(infosByIEN, open(jsnFl, "w"), indent=4)
    return infosByIEN
   
# ################################# Flippers ######################

def flipAppointments(stationNo):
    from fmqlutils.cacher.cacherUtils import flip
    flip(stationNo, "44", "appointment", "44_001", "APPOINTMENT")
    # Note: leaving container prop == hospital location as is so pulled
    # in explicitly. 
    flip(stationNo, "44_001", "patient", "44_003", "PATIENT APPOINTMENT", explicitInheritProps=["appointment_datetime"], useRF=True)

def flipAppointmentsPatient(stationNo):
    from fmqlutils.cacher.cacherUtils import flip
    flip(stationNo, "2", "appointment", "2_98", "PATIENT APPOINTMENT")
    
def recacheFor2_98(stationNo):
    from fmqlutils.cacher.cacherUtils import recacheForCSTOPs
    from fmqlutils.fmqlIF.fmqlIF import FMQLRESTIF
    fmqlIF = FMQLRESTIF("http://10.247.121.13:9000/fmqlEP", "fmql")
    recacheForCSTOPs(stationNo, "2", fmqlIF)
        
# ################################# DRIVER #######################

def main():

    assert(sys.version_info >= (2,7))

    if len(sys.argv) < 2:
        print("need to specify station # ex/ 442 - exiting")
        return

    stationNo = sys.argv[1]

    # recacheFor2_98(stationNo)
    # flipAppointmentsPatient(stationNo)
    # return

    reportAppointmentsVSE(stationNo)
    # reportAppointmentsLegacy44(stationNo)

if __name__ == "__main__":
    main()

