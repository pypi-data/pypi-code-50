__author__ = 'v.denisov'


class InterestedParties:

    def __init__(self):
        pass

    @classmethod
    def person(self):
        interested_parties_person = {
            "composer": {
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
            "corpse": {
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
            },
            "scriptwriter": {
                "type": 3,
                "name_first": "Автор_текста",
                "name_last": "Автор_текста",
                "name_middle": "Автор_текста",
                "ip_name_number": "",
                "gender": 1,
                "date_start": "",
                "date_end": "",
                "date_not_protected": "",
                "nationality": "",
                "note": "",
                "object_info": ""
            },
            "atk": {
                "type": 3,
                "name_first": "АТК",
                "name_last": "АТК",
                "name_middle": "АТК",
                "ip_name_number": "",
                "gender": 2,
                "date_start": "",
                "date_end": "",
                "date_not_protected": "",
                "nationality": "",
                "note": "В алгоритмне может использоваться коэф 0.5 для автора АТК",
                "object_info": ""
            },
            "foreigner": {
                "type": 3,
                "name_first": "Иностранец",
                "name_last": "Иностранец",
                "name_middle": "Иностранец",
                "ip_name_number": "",
                "gender": 2,
                "date_start": "",
                "date_end": "",
                "date_not_protected": "",
                "nationality": "",
                "note": "Передал права ИНОКУП",
                "object_info": ""
            }
        }
        return interested_parties_person
