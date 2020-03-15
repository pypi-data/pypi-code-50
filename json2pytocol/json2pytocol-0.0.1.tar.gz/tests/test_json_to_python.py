import json2pytocol.json_to_python_protocol as jp
import json


def test_generate_classes_text_basic():
    test_json = """
    {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
    """
    result = jp._generate_classes_text(file_name="test", parsed_json=json.loads(test_json))
    assert result == """
from typing import Protocol, Optional, List, Union


class Test(Protocol):
	GlossDiv: "Glossdiv"
	title: str


class Glossdiv(Protocol):
	GlossList: "Glosslist"
	title: str


class Glosslist(Protocol):
	GlossEntry: "Glossentry"


class Glossentry(Protocol):
	Abbrev: str
	Acronym: str
	GlossDef: "Glossdef"
	GlossSee: str
	GlossTerm: str
	ID: str
	SortAs: str


class Glossdef(Protocol):
	GlossSeeAlso: List[str]
	para: str

""".lstrip()


def test_generate_classes_text_subsets():
    test_json = """
{
    "person":{
        "address":{
            "line1":"some address"
        },
        "children":[
            {
                "address":{
                    "line1": "some address",
                    "additional_field": "more info"
                }
            }
        ]
    }
}
    """
    result = jp._generate_classes_text(file_name="test", parsed_json=json.loads(test_json))
    assert result == """
from typing import Protocol, Optional, List, Union


class Test(Protocol):
	address: "Address"
	children: List["Children"]


class Address(Protocol):
	additional_field: str
	line1: str


class Children(Protocol):
	address: "Address"

""".lstrip()


def test_generate_classes_text_spaces_in_key():
    test_json = """
{
    "person":{
        "address":{
            "line1":"some address"
        },
        "children":[
            {
                "address":{
                    "line1": "some address",
                    "additional field": "more info"
                }
            }
        ]
    }
}
    """
    result = jp._generate_classes_text(file_name="test", parsed_json=json.loads(test_json))
    assert result == """
from typing import Protocol, Optional, List, Union


class Test(Protocol):
	address: "Address"
	children: List["Children"]


class Address(Protocol):
	additional_field: str
	line1: str


class Children(Protocol):
	address: "Address"

""".lstrip()


def test_generate_classes_text_optional_fields():
    test_json = """
{
    "persons":[
        {
            "name": "Fred",
            "age": 10,
            "suffix": "jr"
        },
        {
            "name" : "Tom",
            "suffix": null
        }
    ]
}
    """
    result = jp._generate_classes_text(file_name="test", parsed_json=json.loads(test_json))
    assert result == """
from typing import Protocol, Optional, List, Union


class Test(Protocol):
	age: int
	name: str
	suffix: Optional[str]

""".lstrip()


def test_generate_classes_text_union():
    test_json = """
{
    "persons":[
        {
            "name": "Fred",
            "age": 10,
            "suffix": "jr"
        },
        {
            "name" : "Tom",
            "suffix": 10
        }

    ]
}
    """
    result = jp._generate_classes_text(file_name="test", parsed_json=json.loads(test_json))
    assert result == """
from typing import Protocol, Optional, List, Union


class Test(Protocol):
	age: int
	name: str
	suffix: Union[int,str]

""".lstrip()
