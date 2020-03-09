import urllib.request, json, re
import xmltodict

BASE_URI  = "https://epdnorway.lca-data.com/resource"
DATASTOCK = "91413340-7bf0-4f88-a952-0f91cba685df"

LIFE_CYCLE_METHODS = {
    "AP":    { "id": "b4274add-93b7-4905-a5e4-2e878c4e4216", "desc": "Acidification potential" },
    "ADPF":  { "id": "804ebcdf-309d-4098-8ed8-fdaf2f389981", "desc": "Abiotic depletion potential for fossil resources" },
    "ADPE":  { "id": "f7c73bb9-ab1a-4249-9c6d-379a0de6f67e", "desc": "Abiotic depletion potential for non fossil resources" },
    "EP":    { "id": "f58827d0-b407-4ec6-be75-8b69efb98a0f", "desc": "Eutrophication potential" },
    "GWP":   { "id": "77e416eb-a363-4258-a04e-171d843a6460", "desc": "Global warming potential" },
    "ODP":   { "id": "06dcd26f-025f-401a-a7c1-5e457eb54637", "desc": "Ozone Depletion Potential" },
    "POCP":  { "id": "1e84a202-dae6-42aa-9e9d-71ea48b8be00", "desc": "Photochemical Ozone Creation Potential" },
}

EXCHANGE_FLOWS = {
    "CRU":   { "id": "4f69ed08-b1f3-4df5-acc5-4f659a288d37", "desc": "Components for re-use" },
    "EEE":   { "id": "4da0c987-2b76-40d6-9e9e-82a017aaaf29", "desc": "Exported electrical energy" },
    "EET":   { "id": "98daf38a-7a79-46d3-9a37-2b7bd0955810", "desc": "Exported thermal energy (EET)" },
    "HWD":   { "id": "430f9e0f-59b2-46a0-8e0d-55e0e84948fc", "desc": "Hazardous waste disposed" },
    "MER":   { "id": "59a9181c-3aaf-46ee-8b13-2b3723b6e447", "desc": "Materials for energy recovery" },
    "MFR":   { "id": "d7fe48a5-4103-49c8-9aae-b0b5dfdbd6ae", "desc": "Materials for recycling" },
    "FW":    { "id": "3cf952c8-f3a4-461d-8c96-96456ca62246", "desc": "Use of net fresh water" },
    "NHWD":  { "id": "b29ef66b-e286-4afa-949f-62f1a7b4d7fa", "desc": "Non hazardous waste dispose" },
    "NRSF":  { "id": "89def144-d39a-4287-b86f-efde453ddcb2", "desc": "Use of non renewable secondary fuels" },
    "PENRE": { "id": "ac857178-2b45-46ec-892a-a9a4332f0372", "desc": "Use of non renewable primary energy" },
    "PENRM": { "id": "1421caa0-679d-4bf4-b282-0eb850ccae27", "desc": "Use of non renewable primary energy resources used as raw materials" },
    "PENRT": { "id": "06159210-646b-4c8d-8583-da9b3b95a6c1", "desc": "Total use of non renewable primary energy resource" },
    "PERE":  { "id": "20f32be5-0398-4288-9b6d-accddd195317", "desc": "Use of renewable primary energy" },
    "PERM":  { "id": "fb3ec0de-548d-4508-aea5-00b73bf6f702", "desc": "Use of renewable primary energy resources used as raw materials" },
    "PERT":  { "id": "53f97275-fa8a-4cdd-9024-65936002acd0", "desc": "Total use of renewable primary energy resources" },
    "RSF":   { "id": "64333088-a55f-4aa2-9a31-c10b07816787", "desc": "Use of renewable secondary fuels" },
    "RWD":   { "id": "3449546e-52ad-4b39-b809-9fb77cea8ff6", "desc": "Radioactive waste disposed" },
    "SM":    { "id": "c6a1f35f-2d09-4f54-8dfb-97e502e1ce92", "desc": "Use of secondary material" },
}

KNOWN_MODULES = ["A1", "A2", "A3", "A1-A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "C1", "C2", "C3", "C4", "D"]

def list_all():
    with urllib.request.urlopen("{}/datastocks/{}/processes?format=json&search=true&startIndex=0&pageSize=300&sortOrder=true&sortBy=name".format(BASE_URI, DATASTOCK)) as url:
        data = json.loads(url.read().decode())
        return data["data"]

def list_query(q):
    with urllib.request.urlopen("{}/datastocks/{}/processes?format=json&search=true&startIndex=0&pageSize=300&sortOrder=true&sortBy=name".format(BASE_URI, DATASTOCK)) as url:
        data = json.loads(url.read().decode())
        return [item for item in data["data"] if re.search(q, item["name"]+item.get("classific",""), re.IGNORECASE)]

def fetch(uuid):
    with urllib.request.urlopen("{}/datastocks/{}/processes/{}?format=xml&lang=en".format(BASE_URI, DATASTOCK, uuid)) as url:
        return xmltodict.parse(url.read())

def ensure_list(obj):
    if isinstance(obj, list):
        return obj
    else:
        return [obj]

def short_desc(elem):
    return elem["common:shortDescription"]

def filterShortDescByLang(arr, lang):
    el = [el for el in arr if el["common:shortDescription"]["@xml:lang"] == lang]
    return el

def filterByLang(arr, lang):
    el = [el for el in arr if el["@xml:lang"] == lang]
    return el

def filterByProp(arr, prop):
    el = [el for el in arr if el["@id"] == prop]
    return el

''' Are we sure we want to fallback to 0.0 ? '''
def forceFloat(val):
    return float(0.0 if val is None else val)

class DataSet:
    '''  exchanges '''
    def __getExchangeFlows(self, exchange):
        flows = {}
        for ex in exchange:
            ''' only add flows with functionType '''
            if "functionType" in ex:
                for flow in EXCHANGE_FLOWS:
                    if ex["referenceToFlowDataSet"]["@refObjectId"] == EXCHANGE_FLOWS[flow]["id"]:
                        amounts = {}
                        for mod in KNOWN_MODULES:
                            for y in [y for y in ensure_list(ex["common:other"]["epd:amount"]) if y.get("@epd:module", "") == mod]:
                                amounts[mod] = float(y.get("#text", 0))
                        flows[flow] = ExchangeFlow({
                            "id": EXCHANGE_FLOWS[flow]["id"],
                            "name": EXCHANGE_FLOWS[flow]["desc"],
                            "meanAmount": ex["meanAmount"],
                            "direction": ex["exchangeDirection"],
                            "unit": ex["common:other"]["epd:referenceToUnitGroupDataSet"]["common:shortDescription"],
                            "amounts": amounts,
                        })
            else:
                ''' first element is usually result flow? '''
                self.referenceFlow = ReferenceFlow({
                    "id": ex["referenceToFlowDataSet"]["@refObjectId"],
                    "name": ex["referenceToFlowDataSet"]["common:shortDescription"]["#text"], #TODO lanugages
                    "meanAmount": ex["meanAmount"],
                    "resultingAmount": ex["resultingAmount"],
                    "version": ex["referenceToFlowDataSet"]["@version"],
                })
        return flows

    '''  lcia '''
    def __getImpactAssessments(self, lcia):
        imps = {}
        for l in lcia:
            for lcm in LIFE_CYCLE_METHODS:
                if l["referenceToLCIAMethodDataSet"]["@refObjectId"] == LIFE_CYCLE_METHODS[lcm]["id"]:

                    amounts = {}
                    for mod in KNOWN_MODULES:
                        for y in [y for y in ensure_list(l["common:other"]["epd:amount"]) if y.get("@epd:module", "") == mod]:
                            amounts[mod] = float(y.get("#text", 0))
                    imps[lcm] = ImpactAssessment({
                        "id": LIFE_CYCLE_METHODS[lcm]["id"],
                        "name": LIFE_CYCLE_METHODS[lcm]["desc"],
                        "meanAmount": l["meanAmount"],
                        "unit": l["common:other"]["epd:referenceToUnitGroupDataSet"]["common:shortDescription"],
                        "amounts": amounts,
                    })
        return imps

    def __extractLifeCycle(self, exchange):
        r = {
            "direction": exchange["exchangeDirection"],
            "unit": exchange["common:other"]["epd:referenceToUnitGroupDataSet"]["common:shortDescription"]
        }

        for x in [x for x in ensure_list(exchange["referenceToFlowDataSet"]["common:shortDescription"]) if x["@xml:lang"] == "en"]:
            r["indicator"] = x.get("#text")

        for mod in KNOWN_MODULES:
            for x in [x for x in ensure_list(exchange["common:other"]["epd:amount"]) if x.get("@epd:module", "") == mod]:
                r[mod] = float(x.get("#text", 0)) # TODO missing values = 0, or undef key?

        return r

    ''' lcia '''
    def __extractImpactAssessment(self, result):
        r = {
            "unit": result["common:other"]["epd:referenceToUnitGroupDataSet"]["common:shortDescription"],
        }

        for x in [x for x in ensure_list(result["referenceToLCIAMethodDataSet"]["common:shortDescription"]) if x["@xml:lang"] == "en"]:
            r["indicator"] = x.get("#text")

        for mod in KNOWN_MODULES:
            for x in [x for x in ensure_list(result["common:other"]["epd:amount"]) if x["@epd:module"] == mod]:
                r[mod] = float(x.get("#text", 0))

        return r

    def availableFlows(self):
        flows = []
        for fl in self.exchangeFlows.keys():
            flows.append({fl: EXCHANGE_FLOWS[fl]["desc"]})
        return flows

    def availableImpactAssessments(self):
        lcias = []
        for lc in self.impactAssessments.keys():
            lcias.append({lc: LIFE_CYCLE_METHODS[lc]["desc"]})
        return lcias

    def getFlow(self, flow):
        fl = self.exchangeFlows[flow]
        if fl:
            fl.ref = fl.fetchRef()
            return fl

    def getImpact(self, lcia):
        ia = self.impactAssessments[lcia]
        if ia:
            ia.ref = ia.fetchRef()
            return ia

    def __init__(self, uuid):
        raw = fetch(uuid)
        info = raw["processDataSet"]["processInformation"]["dataSetInformation"]
        name = filterByLang(ensure_list(info["name"]["baseName"]), "no")
        desc = filterByLang(ensure_list(info["common:generalComment"]), "no")
        self.raw = raw # TODO: remove when no longer needed
        self.id = uuid
        self.name = name[0].get("#text")
        self.description = desc[0].get("#text")
        self.tags = [c["#text"] for c in ensure_list(info["classificationInformation"]["common:classification"]["common:class"])]

        self.exchangeFlows = self.__getExchangeFlows(raw["processDataSet"]["exchanges"]["exchange"])
        self.impactAssessments = self.__getImpactAssessments(raw["processDataSet"]["LCIAResults"]["LCIAResult"])

    def dump_json(self):
        return json.dumps(self.raw)

class ExchangeFlow():
    def __init__(self, data):
        self.data = data
        self.id = data.get("id")
        self.name = data.get("name")
        self.meanAmount = data.get("meanAmount")
        self.direction = data.get("direction")
        self.unit = data.get("unit")
        self.amounts = data.get("amounts")

''' for some reason reference flow seems to be first object in exchangesdataset '''
class ReferenceFlow():
    def __init__(self, data):
        self.data = data
        self.id = data.get("id")
        self.name = data.get("name")
        self.meanAmount = data.get("meanAmount")
        self.resultingAmount = data.get("resultingAmount")
        self.version = data.get("version")

        flowRef = self.__fetchRef()
        if flowRef:
            self.units = flowRef.materialUnits

    def __fetchRef(self):
        with urllib.request.urlopen("{}/flows/{}?format=xml".format(BASE_URI, self.data.get("id"))) as url:
            ref = xmltodict.parse(url.read())
            if ref:
                return FlowDataSet(ref)

class ImpactAssessment():
    def __init__(self, data):
        self.data = data
        self.id = data.get("id")
        self.name = data.get("name")
        self.meanAmount = data.get("meanAmount")
        self.unit = data.get("unit")
        self.amounts = data.get("amounts")

    ''' fetch then referenced life cycle dataset '''
    def fetchRef(self):
        with urllib.request.urlopen("{}/lciamethods/{}?format=xml".format(BASE_URI, self.data.get("id"))) as url:
            return xmltodict.parse(url.read())

class FlowDataSet():
    def __init__(self, data):
        info = data["f:flowDataSet"]["f:flowInformation"]["f:dataSetInformation"]
        name = filterByLang(ensure_list(info["f:name"]["f:baseName"]), "no")
        self.data = data
        self.id = info["common:UUID"]
        self.name = name[0].get("#text")
        self.materialUnits = self.__fetchMaterialUnits(info)

    def __fetchMaterialUnits(self, info):
        if info["common:other"] and info.get("common:other", {}).get("mat:MatML_Doc"):
            matml = info["common:other"]["mat:MatML_Doc"]
            units = []
            for x in ensure_list(matml["mat:Material"]["mat:BulkDetails"]["mat:PropertyData"]):
                prop = x["@property"]
                v = x["mat:Data"]["#text"]
                u = filterByProp(ensure_list(matml["mat:Metadata"]["mat:PropertyDetails"]), prop)
                units.append({
                    "name": u[0]["mat:Name"],
                    "desc": u[0]["mat:Units"]["@description"],
                    "unit": u[0]["mat:Units"]["@name"],
                    "value": x["mat:Data"]["#text"],
                })
            return units
