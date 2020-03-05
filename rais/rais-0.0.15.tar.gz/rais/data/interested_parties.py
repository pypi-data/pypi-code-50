__author__ = 'v.denisov'

class InterestedParties:

    def __init__(self):
        pass

    def person(self):
        interested_parties_person = {
            "composer":{
                "type": 3,
                "name_first": "Композитор",
                "name_last": "Композитор",
                "name_middle": "",
                "ip_name_number": "",
                "gender": 2,
                "date_start": "",
                "date_end": "",
                "date_not_protected": "",
                "nationality": "",
                "note": "",
                "object_info": ""
            },
            "corpse":{
                "type": 3,
                "name_first": "Мертвец",
                "name_last": "Мертвец",
                "name_middle": "",
                "ip_name_number": "",
                "gender": 1,
                "date_start": "06.11.1900",
                "date_end": "04.11.1930",
                "date_not_protected": "04.11.2000",
                "nationality": "",
                "note": "Произведения не охраняются",
                "object_info": ""
            }

        }
        return interested_parties_person