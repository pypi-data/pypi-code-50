from kakeibox_database_sqlite3.database.account import AccountDatabase
from faker import Faker


def test_list(account_data_dictionary):
    records = AccountDatabase().list()
    assert len(records) == len(account_data_dictionary)
    for record in records:
        assert record['uuid'] in account_data_dictionary
        element = account_data_dictionary[record['uuid']]
        assert isinstance(record, dict)
        assert record == element


def test_get_by_uuid(account_data):
    dict_response = AccountDatabase().get_by_uuid(account_data['uuid'])
    assert isinstance(dict_response, dict)
    assert account_data['uuid'] == dict_response['uuid']
    assert account_data['name'] == dict_response['name']
    assert account_data['description'] == dict_response['description']


def test_new(account_data_new):
    bridge = AccountDatabase()
    dict_response = bridge.new(account_data_new)
    assert isinstance(dict_response, dict)
    assert dict_response == account_data_new

    bridge.delete(account_data_new['uuid'])


def test_delete(account_data_new):
    bridge = AccountDatabase()
    dict_response = bridge.new(account_data_new)
    result = bridge.delete(dict_response['uuid'])
    assert isinstance(result, bool)
    assert result


def test_update(account_data_new):
    bridge = AccountDatabase()
    bridge.new(account_data_new)
    account_data_new['name'] == Faker().sentence()
    dict_response = bridge.update(account_data_new['uuid'], account_data_new)
    assert isinstance(dict_response, dict)
    assert dict_response == account_data_new

    bridge.delete(account_data_new['uuid'])
