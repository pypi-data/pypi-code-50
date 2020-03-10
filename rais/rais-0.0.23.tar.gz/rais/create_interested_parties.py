__author__ = 'v.denisov'
from rais.data.interested_parties import InterestedParties as ip
from rais.parameter_initialization import ParameterInitialization as pi

class CreateInterestedParties:

    def __init__(self):
        pass

    def check_availability(self, name_ip):
        params = {
            "with": "aliases,requisites,type,orgs",
            "total": 769611,
            "limit": 25,
            "page": 1,
            "search_blike": name_ip,
            "no_count": 1
        }
        response = self.app.regusts.get(url=self.app.base_url + 'api/red/contragent/list', params=params)
        r_json = response.json()
        print('r_json=', r_json)
        if len(r_json["data"]["list"])>0:
            print('Заинтересованная сторона '+name_ip+' уже существует')
            return True
        else:
            return False

    @classmethod
    def person(self, type_person):
        ip_person = ip[type_person]
        # if ip_person[name_first]:
        #     pass
        print(ip_person)
        return ip_person