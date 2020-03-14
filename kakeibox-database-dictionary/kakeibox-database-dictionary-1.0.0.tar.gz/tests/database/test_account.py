from kakeibox_database_dictionary.engine import TableAccount
from kakeibox_database_dictionary.database.account import AccountDatabase
from uuid import uuid4
from faker import Faker


def _before_execute_test():
    database = TableAccount()
    database.table = {}


def test_account_new(account_data):
    _before_execute_test()
    bridge = AccountDatabase()
    result = bridge.new(account_data)
    assert isinstance(result, dict)
    assert account_data == result

    database = TableAccount()
    assert 1 == len(database.table)

    expected = database.table[account_data['uuid']]
    assert expected == account_data


def test_account_list(account_data_dictionary):
    _before_execute_test()
    database = TableAccount()
    database.table = account_data_dictionary

    bridge = AccountDatabase()
    item_list = bridge.list()

    assert len(database.table) == len(item_list) == 2

    for element in item_list:
        expected = database.table[element['uuid']]
        assert expected == element
        assert isinstance(element, dict)


def test_account_delete(account_data_dictionary):
    _before_execute_test()
    database = TableAccount()
    database.table = account_data_dictionary
    total = len(database.table)
    uuid = list(account_data_dictionary)[0]
    assert uuid in database.table

    bridge = AccountDatabase()
    result = bridge.delete(uuid)
    assert isinstance(result, bool)
    assert result

    assert uuid not in database.table
    assert (total - 1) == len(database.table)


def test_account_update(account_data_dictionary):
    _before_execute_test()
    faker = Faker()
    database = TableAccount()
    database.table = account_data_dictionary
    uuid = list(account_data_dictionary)[0]

    item = account_data_dictionary[uuid]
    item['uuid'] = str(uuid4())
    item['name'] = faker.name()
    item['description'] = faker.text()

    bridge = AccountDatabase()
    result = bridge.update(uuid, item)

    assert isinstance(result, dict)
    assert result == item
