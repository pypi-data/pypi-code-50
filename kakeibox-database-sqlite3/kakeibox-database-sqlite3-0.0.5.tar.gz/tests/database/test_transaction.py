from kakeibox_database_sqlite3.database.transaction import TransactionDatabase
from copy import deepcopy
from datetime import datetime
from uuid import uuid4


def _test_list(expected_data, start_time, end_time):
    records = TransactionDatabase().list(start_time, end_time)

    assert len(records) == len(expected_data)
    for record in records:
        assert record['uuid'] in expected_data
        element = expected_data[record['uuid']]
        assert record == element
    return len(records)


def _test_list_per_type(expected_data, start_time, end_time, type_code):
    bridge = TransactionDatabase()
    records = bridge.list_per_type(start_time, end_time, type_code)
    assert len(records) == len(expected_data)
    for record in records:
        assert isinstance(record, dict)
        assert record['uuid'] in expected_data
        element = expected_data[record['uuid']]
        assert record == element
    return len(records)


def _test_new(data):
    dict_response = TransactionDatabase().new(data)
    assert isinstance(dict_response, dict)
    assert dict_response == data
    return dict_response


def _test_update(data):
    data['account_uuid'] = "aaa25a55-0610-4aa2-b4d1-dee8a0936bbb"
    bridge = TransactionDatabase()
    dict_response = bridge.update(data['uuid'], data)
    assert isinstance(dict_response, dict)
    assert dict_response == data
    assert dict_response['account_uuid'] == data['account_uuid']

    data['account_uuid'] = "65725a55-0610-4aa2-b4d1-dee8a0936aaa"
    bridge = TransactionDatabase()
    dict_response = bridge.update(data['uuid'], data)
    assert isinstance(dict_response, dict)
    assert dict_response == data
    assert dict_response['account_uuid'] == data['account_uuid']
    return dict_response


def _test_get_by_code(data):
    dict_response = TransactionDatabase().get_by_code(data['code'])
    assert dict_response
    assert data['code'] == dict_response['code']
    assert data['name'] == dict_response['name']
    return dict_response


def _test_delete(data):
    result = TransactionDatabase().delete(data['uuid'])
    assert isinstance(result, bool)
    assert result


def _get_expected_data(data, start_time, end_time):
    expected_data = {}
    for key, item in data.items():
        if start_time <= item['timestamp'] <= end_time:
            expected_data[key] = item
    return expected_data


def test_transaction_list_actions(transaction_data):
    data = deepcopy(transaction_data)
    start_time = int(datetime(2019, 8, 1, 0, 0).timestamp())
    end_time = int(datetime(2019, 8, 30, 23, 59).timestamp())

    expected_data = _get_expected_data(data, start_time, end_time)
    _test_list(expected_data, start_time, end_time)


def test_transaction_actions(transaction_data):
    data = deepcopy(transaction_data)
    transaction_dict = _get_a_transaction_dict(data)
    transactions = TransactionDatabase().list_all()
    start_count = len(transactions)
    for element in transactions:
        assert isinstance(element, dict)

    new_response = _test_new(transaction_dict)

    transactions = TransactionDatabase().list_all()
    assert (start_count + 1) == len(transactions)
    _test_update(new_response)

    _test_delete(transaction_dict)
    transactions = TransactionDatabase().list_all()
    assert start_count == len(transactions)


def _get_a_transaction_dict(data):
    transaction_dict = deepcopy(next(iter(data.values())))
    transaction_dict['uuid'] = str(uuid4())
    return transaction_dict


def test_transaction_list_per_type_action(
        transaction_type_data, transaction_data):
    data = deepcopy(transaction_data)
    start_time = int(datetime(2019, 8, 1, 0, 0).timestamp())
    end_time = int(datetime(2019, 8, 30, 23, 59).timestamp())
    for type_key, type_item in transaction_type_data.items():
        expected_data = {}
        for key, item in data.items():
            if start_time <= item['timestamp'] <= end_time and \
                    item['transaction_type_code'] == type_item['code']:
                expected_data[key] = item

        _test_list_per_type(
            expected_data, start_time, end_time, type_item['code'])
