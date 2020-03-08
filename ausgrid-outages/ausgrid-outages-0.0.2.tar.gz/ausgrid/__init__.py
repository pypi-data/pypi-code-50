import requests
import re
import pprint
from datetime import datetime

endpoint = {
    "planned": "https://www.ausgrid.com.au/services/Outage/Outage.asmx/GetDetailedPlannedOutages",
    "current": "https://www.ausgrid.com.au/services/Outage/Outage.asmx/GetOutages",
}

reGetTimestamp = re.compile(r"/DATE\((\d+)\)/", re.IGNORECASE)


def fetch():
    payload = {
        "headers": {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/json;charset=utf-8",
        }
    }
    rPlanned = requests.post(endpoint["planned"], json=payload).json()
    rCurrent = requests.post(endpoint["current"], json=payload).json()

    outages = {"planned": [], "current": []}
    if rPlanned and rPlanned["d"] and rPlanned["d"]["IsSuccess"]:
        outages["planned"] = processPlanned(rPlanned["d"]["Data"])

    if rCurrent:
        outages["current"] = rCurrent

    return outages


def processPlanned(outages):
    processed = []
    for outage in outages:
        newOutage = {}
        newOutage["areas"] = outage["Area"].split(", ") or None
        newOutage["postcodes"] = outage["PostCodes"].split(", ") or None
        newOutage["streets"] = outage["Streets"].split(", ") or None
        newOutage["cause"] = outage["Cause"] or None
        newOutage["webId"] = outage["WebId"] or None
        newOutage["latitude"] = outage["CentreLat"] or None
        newOutage["longitude"] = outage["CentreLng"] or None
        newOutage["customers"] = outage["Customers"] or None
        newOutage["status"] = outage["Status"] or None
        newOutage["delay"] = outage["Delay"] or None
        newOutage["externalNotes"] = outage["ExternalNotes"] or None
        newOutage["prepareInterruptionLink"] = outage["PrepareInterruptionLink"] or None
        newOutage["relatedProjectLink"] = outage["RelatedProjectLink"] or None
        newOutage["jobId"] = outage["JobId"] or None
        endTimestamp = reGetTimestamp.match(outage["EndDateTime"])[1] or None
        startTimestamp = reGetTimestamp.match(outage["StartDateTime"])[1] or None
        if endTimestamp:
            newOutage["end"] = datetime.fromtimestamp(int(endTimestamp) / 1000)
        if startTimestamp:
            newOutage["start"] = datetime.fromtimestamp(int(startTimestamp) / 1000)
        processed.append(newOutage)
    return processed


if __name__ == "__main__":
    outages = fetch()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(outages)

