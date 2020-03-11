__author__ = 'v.denisov'

from rais.data.interested_parties import InterestedParties as ip
from rais.parameter_initialization import ParameterInitialization as pi
from rais.client_reguest import ClientReguest as cr



class CreateInterestedParties:

    def __init__(self):
        pass

    @classmethod
    def check_availability(self, name_ip):
        params = {
            "with": "aliases,requisites,type,orgs",
            "total": 0,
            "limit": 25,
            "page": 1,
            "search_blike": name_ip,
            "no_count": 1
        }
        response = cr.get(url=pi.get_url_host() + '/api/red/contragent/list', params=params)
        r_json = response.json()
        if len(r_json["data"]["list"])>0:
            print('Заинтересованная сторона '+name_ip+' уже существует')
            return r_json["data"]["list"][0]["id"]
        else:
            return False

    @classmethod
    def check_availability_contract(self, name_contract):
        params = {
            "with": "contragent,type,usagetype_group",
            "limit": 25,
            "page": 1,
            "search_like": name_contract,
            "descendants": 1,
            "kind_id_not": "5a69d5bf-0000-0000-0000-000070eeb9fa"
        }
        response = cr.get(url=pi.get_url_host() + '/api/red/contract/list', params=params)
        r_json = response.json()
        if len(r_json["data"]["list"]) > 0:
            print('Документ ' + name_contract + ' уже существует')
            return True
        else:
            return False

    @classmethod
    def get_contragent_id(cls, c_a):
        params = {
            "id": c_a,
            "with": """addresses,aliases,aliases_type,contacts,staffs,bankaccounts,bankaccounts_info,
                  contacts_type,addresses_type,requisites,type,flags,flags_type,codes,requisites_files"""
        }
        response = cr.get(url=pi.get_url_host() + '/api/red/contragent/get', params=params)
        return response

    @classmethod
    def document_kind_id(self, kind_name):
        kind_id = None
        params = {
            "category.is_contragent_docs": "true",
            "is_creatable": 1,
            "limit": 500,
            "with": "ckrt"
        }
        response = cr.get(url=pi.get_url_host() + '/api/red/thesaurus/contract/kind/list', params=params)
        r_json = response.json()
        for g_n in r_json["data"]["list"]:
            if (kind_name in g_n["name"]) and (len(kind_name) == len(g_n["name"])):
                kind_id = g_n["id"]
                break
        return kind_id

    @classmethod
    def person(self, type_person, prefix='_'):
        if type_person in ip.person():
            ip_person = ip.person()[type_person]
        else:
            print("Нет такого типа Заинтересованной стороны >>"+type_person)
            assert False
        name_ip = pi.get_prefix()+prefix+ip_person["name_first"]
        c_a = self.check_availability(name_ip=name_ip)
        if c_a :
            response_person = self.get_contragent_id(c_a)
        else:
            params = {
                "type": ip_person["type"],
                "name_first": pi.get_prefix()+prefix+ip_person["name_first"],
                "name_last": pi.get_prefix()+prefix+ip_person["name_last"],
                "name_middle": pi.get_prefix()+prefix+ip_person["name_middle"],
                "ip_name_number": ip_person["ip_name_number"],
                "gender": ip_person["gender"],
                "date_start": ip_person["date_start"],
                "date_end": ip_person["date_end"],
                "date_not_protected": ip_person["date_not_protected"],
                "nationality": ip_person["nationality"],
                "note": ip_person["note"],
                "object_info": ip_person["object_info"]
            }
            cr.post(url=pi.get_url_host() + '/api/red/contragent/add', params=params)
            print('Создали заинтересованную сторону ' + pi.get_prefix()+prefix+ip_person["name_first"])
            c_a = self.check_availability(name_ip=name_ip)
            response_person = self.get_contragent_id(c_a)
        for l_o_r in ip_person["documents"]:
            if self.check_availability_contract(name_contract=pi.get_prefix()+prefix+l_o_r["contract_num"]):
                print('name_contract=', pi.get_prefix()+prefix+l_o_r["contract_num"])
                continue
            contragent_id = response_person.json()["data"]["item"]["id"]
            kind_id = self.document_kind_id(l_o_r["kind_name"])
            rights = ip.rights_json()
            params = {
                "contract_num": pi.get_prefix()+prefix+l_o_r["contract_num"],
                "kind_id": kind_id,
                "contragent_id": contragent_id,
                "org_id": 1,
                "rao_departament": "f5d7fb63-7675-4f8f-a5c5-0776c83b96ce",
                "date_begin": l_o_r["date_begin"],
                "date_end": l_o_r["date_end"],
                "contract_date": l_o_r["contract_date"],
                "rights": rights,
                "comment": l_o_r["comment"]
            }
            response = cr.post(url=pi.get_url_host() + '/api/red/contract/add', data=params)
            print('Создали документ ' + pi.get_prefix()+prefix+l_o_r["contract_num"], response.ok)
        return response_person.json()["data"]["item"]

