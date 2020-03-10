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
    def get_contragent_id(cls, c_a):
        params = {
            "id": c_a,
            "with": """addresses,aliases,aliases_type,contacts,staffs,bankaccounts,bankaccounts_info,
                  contacts_type,addresses_type,requisites,type,flags,flags_type,codes,requisites_files"""
        }
        response = cr.get(url=pi.get_url_host() + '/api/red/contragent/get', params=params)
        return response

    @classmethod
    def person(self, type_person):
        ip_person = ip.person()[type_person]
        name_ip = pi.get_prefix()+ip_person["name_first"]
        c_a = self.check_availability(name_ip=name_ip)
        if c_a :
            response = self.get_contragent_id(c_a)
        else:
            params = {
                "type": ip_person["type"],
                "name_first": pi.get_prefix()+ip_person["name_first"],
                "name_last": pi.get_prefix()+ip_person["name_last"],
                "name_middle": pi.get_prefix()+ip_person["name_middle"],
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
            print('Создали заинтересованную сторону ' + pi.get_prefix()+ip_person["name_first"])
            c_a = self.check_availability(name_ip=name_ip)
            response = self.get_contragent_id(c_a)
        return response.json()["data"]["item"]

