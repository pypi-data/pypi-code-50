import pytest
from tests.fixtures.transaction_data import TRANSACTION_DATA


@pytest.fixture()
def account_data():
    return {
        "uuid": "65725a55-0610-4aa2-b4d1-dee8a0936aaa",
        "name": "Global Account",
        "description": "A global account to manage the expenses and incomes"
    }


@pytest.fixture()
def account_data_dictionary():
    return {
        "65725a55-0610-4aa2-b4d1-dee8a0936aaa": {
                "uuid": "65725a55-0610-4aa2-b4d1-dee8a0936aaa",
                "name": "Global Account",
                "description": "A global account to manage the expenses and incomes"
            },
        "aaa25a55-0610-4aa2-b4d1-dee8a0936bbb":{
                "uuid": "aaa25a55-0610-4aa2-b4d1-dee8a0936bbb",
                "name": "Account B",
                "description": "Account to manage the expenses and incomes"
            }
    }


@pytest.fixture()
def transaction_category_data():
    return {
        'SUR':
            {
                'code': 'SUR',
                'name': 'Survival'
            },
        'OPT':
            {
                'code': 'OPT',
                'name': 'Optional'
            },
        'CUL':
            {
                'code': 'CUL',
                'name': 'Culture'
            },
        'EXT':
            {
                'code': 'EXT',
                'name': 'Extra'
            }
    }


@pytest.fixture()
def transaction_subcategory_data():
    return {
        "FOD": {
            "code": "FOD",
            "name": "Food",
            "transaction_category_code": 'SUR',
        },
        "REN": {
            "code": "REN",
            "name": "Rent",
            "transaction_category_code": 'SUR',
        },
        "TRA": {
            "code": "TRA",
            "name": "Transport",
            "transaction_category_code": 'SUR',
        },
        "KID": {
            "code": "KID",
            "name": "Kids",
            "transaction_category_code": 'SUR',
        },
        "RES": {
            "code": "RES",
            "name": "Restaurant",
            "transaction_category_code": 'OPT',
        },
        "SHO": {
            "code": "SHO",
            "name": "Shopping",
            "transaction_category_code": 'OPT',
        },
        "BOK": {
            "code": "BOK",
            "name": "Books",
            "transaction_category_code": 'CUL',
        },
        "MUS": {
            "code": "MUS",
            "name": "Music",
            "transaction_category_code": 'CUL',
        },
        "SHW": {
            "code": "SHW",
            "name": "Shows",
            "transaction_category_code": 'CUL',
        },
        "MOV": {
            "code": "MOV",
            "name": "Movies",
            "transaction_category_code": 'CUL',
        },
        "MAG": {
            "code": "MAG",
            "name": "Magazines",
            "transaction_category_code": 'CUL',
        },
        "GIF": {
            "code": "GIF",
            "name": " Gifts",
            "transaction_category_code": 'EXT',
        },
        "REP": {
            "code": "REP",
            "name": "Repairs",
            "transaction_category_code": 'EXT',
        },
        "FUR": {
            "code": "FUR",
            "name": "Furniture",
            "transaction_category_code": 'EXT',
        }
    }


@pytest.fixture()
def transaction_data():
    return TRANSACTION_DATA


@pytest.fixture()
def transaction_type_data():
    return {
        1:
            {
                'code': 'EXP',
                'name': 'Expense'
            },
        2:
            {
                'code': 'INC',
                'name': 'Income'
            },
    }
