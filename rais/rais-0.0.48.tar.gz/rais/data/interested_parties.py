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
                "object_info": "",
                "documents": [
                    {
                        "contract_num": "Композитор_РАО",
                        "kind_name": "Договор о передаче полномочий по управлению правами автора (наследника) на коллективной основе (Новый 2)",
                        "contract_date": "01.01.2015",
                        "date_begin": "01.01.2015",
                        "date_end": "",
                        "comment": "_",
                        "add_op": "ALL"
                    }
                ]
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
                "object_info": "",
                "documents":[
                    {
                        "contract_num": "Мертвец_РАО",
                        "kind_name": "Договор о передаче полномочий по управлению правами автора (наследника) на коллективной основе (Новый 2)",
                        "contract_date": "01.01.1910",
                        "date_begin": "01.01.1910",
                        "date_end": "",
                        "comment": "_",
                        "add_op": "ALL"
                    }
                ]
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
                "object_info": "",
                "documents": [
                    {
                        "contract_num": "Автор_текста_РАО",
                        "kind_name": "Договор о передаче полномочий по управлению правами автора (наследника) на коллективной основе (Новый 2)",
                        "contract_date": "01.01.2015",
                        "date_begin": "01.01.2015",
                        "date_end": "",
                        "comment": "_",
                        "add_op": "ALL"
                    }
                ]
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
                "object_info": "",
                "documents" : [
                    {
                        "contract_num": "АТК_РАО",
                        "kind_name": "Договор о передаче полномочий по управлению правами автора (наследника) на коллективной основе (Новый 2)",
                        "contract_date": "01.01.2015",
                        "date_begin": "01.01.2015",
                        "date_end": "",
                        "comment": "_",
                        "add_op": "ALL"
                    }
                ]
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
                "object_info": "",
                "documents":[

                ]
            },
            "removed_rights": {
                "type": 3,
                "name_first": "Изъявший",
                "name_last": "Изъявший",
                "name_middle": "Изъявший",
                "ip_name_number": "",
                "gender": 2,
                "date_start": "",
                "date_end": "",
                "date_not_protected": "",
                "nationality": "",
                "note": "Есть уведомление об изъятии прав на период отчета D_T_5",
                "object_info": "",
                "documents":[
                    {
                        "contract_num": "Изъявший_РАО",
                        "kind_name": "Договор о передаче полномочий по управлению правами автора (наследника) на коллективной основе (Новый 2)",
                        "contract_date": "01.01.2015",
                        "date_begin": "01.01.2015",
                        "date_end": "",
                        "comment": "_",
                        "add_op": "ALL"
                     }#,
                    # {
                    #     "contract_num": "Изъявший_Уведомление",
                    #     "kind_name": "Уведомление об изъятии",
                    #     "contract_date": "01.01.2016",
                    #     "date_begin": "01.01.2016",
                    #     "date_end": "",
                    #     "comment": "_",
                    #     "add_op": "ALL"
                    # }
                ]
            },
            "not_transferring_rights": {
                "type": 3,
                "name_first": "Не_передавший_права_РАО",
                "name_last": "Не_передавший_права_РАО",
                "name_middle": "Не_передавший_права_РАО",
                "ip_name_number": "",
                "gender": 2,
                "date_start": "",
                "date_end": "",
                "date_not_protected": "",
                "nationality": "",
                "note": "Нет договора с рао",
                "object_info": "",
                "documents": [

                ]
            }
        }
        return interested_parties_person

    @classmethod
    def rights_json(self):
        rights = """{
                  "rights": [
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "478d7663-b5d9-4d73-aed2-88f331313e8e",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "9d43fdeb-8a16-4d9d-b47b-4e0f57d06cb5",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "821db732-5dee-468b-8dde-203c10d80a24",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "761a9f72-c80b-4c86-91df-91e98fbcb9eb",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "c8da46dc-4076-4b18-9053-80476cf30901",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "bb41785c-9c31-4247-a45c-54f36b0bf0e6",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "25677bcd-ba09-4341-ad57-c8bc255f702f",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "57cccac6-aa8b-44f8-8265-792439031163",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "7db75cad-43b7-46b8-aec0-3f2a7a94ae3a",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "c89cfd68-64f2-412a-9cae-9e409d8a9312",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "99f20cce-17fa-401d-b526-3c8c165d067b",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "9cadaeb8-435c-48e1-8726-ab9877993384",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "cef7ebb2-463e-4cc8-9b1d-2914b0e6f550",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "b361266d-1973-4087-a3ac-15d171a3c252",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "dc68b51b-f924-42de-9b20-44bbfe94456f",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "958b3608-257e-47cd-8203-addb5bbf1f31",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "aaf20177-2e4b-4d20-9456-d3c0f615173c",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "50ceaa4b-adec-4f23-b101-ff4a388debfd",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "b5a4ba60-94f3-4985-8c3a-4fe5577b96aa",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "01870c68-87d8-4f05-b097-401454887492",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "045c412f-3b88-4c64-8370-84ccf12bd3dd",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "21c211fc-67ee-4b1d-86e9-20ebaa8c99f9",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "313c6940-97d6-4fdf-b299-02fc6e5c0f37",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "90770dcc-f374-4659-98fb-3e4e88317abd",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "a9453de0-02cd-401c-85a7-acfe96d8ea58",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "4073283b-8274-49be-98fc-7775132f10a0",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "fa569ea7-1155-4dca-8bfb-fe73ba4e6d4e",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "3902caff-93d7-48a7-a6a3-d7c56141c441",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "ca76e582-4f87-4ed5-8ef6-26fb6bbea796",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "029e513d-2cf9-4ca9-994a-32927d901b2d",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "8677923c-133f-4ba6-815b-ad22cd029c0b",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "c03cf92f-7673-4c53-905e-6f12ef7c5619",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "e15ff8d5-bc9d-463a-a780-0d2482ad3ef4",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "7e1e49d6-4121-4264-b69d-cf9c6de8f628",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "bc16b114-e615-4656-b051-b346f23c8265",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "f8558ee1-4c3f-4676-b608-1ac4a4864b9e",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "65473237-46bb-43d4-86e5-417483d2d330",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "afd61927-2f64-4cc6-ba9a-11afd1553c86",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "555b642a-471b-4b9b-afc0-58d0d4c613c4",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "ecfbd6e4-4b21-4731-a554-dfb90146c1ce",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "2465436e-d4d5-4ba8-9685-8609c83030dd",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "c9f7f03c-7b95-4502-8b61-f141ef5e7c33",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "a6dc694e-eb63-4fcb-b482-618ed1eefdc3",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "6dd50892-c635-49ef-903f-9d53553a48c4",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "fdf0917a-74de-4900-b5d5-585a467c869c",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "93d15319-79ac-47cc-8887-42f939b806a0",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "0efe994a-0ab1-455e-a5de-7eb27af8157e",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "ee480099-a8ba-44b5-88ba-b342a0e65bec",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "dc68c52c-2726-4b80-8d4e-f52dfc7b42e5",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "d1d667bd-100e-4171-9b5d-8638ebf7aeef",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "5cd30cfd-6e48-4818-aafb-f2e480e8ab82",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "c22b08d6-49d0-429b-9d76-309411b3aec0",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "4b5ebb01-6779-4623-8540-f7e12aecf136",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "69760ed9-39ce-46e1-9867-80348c6bc561",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "92775615-32d0-42e1-849e-c5c49110aba8",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "5c335b75-323d-4af9-b511-5d0793534427",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "7cf3346e-b3d1-499b-9af7-f02d565f38a1",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "e97a1544-0df6-4510-9f7a-fad46b7c5b03",
                      "id": ""
                    },
                    {
                      "fraction": 0,
                      "territory_id": [
                        "58d8fb3a-0000-0000-0000-00000987862e"
                      ],
                      "right_kind_id": "46f33a77-7032-41ba-941c-c5a14ccdfd12",
                      "id": ""
                    }
                  ]
                }"""

        return rights

