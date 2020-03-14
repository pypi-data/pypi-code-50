from kakeibox_database_sqlite3.database.transaction_category \
    import TransactionCategoryDatabase
from faker import Faker


def _test_list(transaction_category_data):
    records = TransactionCategoryDatabase().list()
    assert len(records) == len(transaction_category_data)
    for record in records:
        assert record['code'] in transaction_category_data
        element = transaction_category_data[record['code']]
        assert isinstance(record, dict)
        assert record == element
    return len(records)


def _test_new(data):
    dict_response = TransactionCategoryDatabase().new(data)
    assert isinstance(dict_response, dict)
    assert dict_response == data
    return dict_response


def _test_update(data):
    bridge = TransactionCategoryDatabase()
    dict_response = bridge.update(data['code'], data)
    assert isinstance(dict_response, dict)
    assert dict_response == data
    return dict_response


def _test_get_by_code(data):
    dict_response = TransactionCategoryDatabase().get_by_code(data['code'])
    assert isinstance(dict_response, dict)
    assert data['code'] == dict_response['code']
    assert data['name'] == dict_response['name']
    return dict_response


def _test_delete(data):
    result = TransactionCategoryDatabase().delete(data['code'])
    assert isinstance(result, bool)
    assert result


def test_transaction_category_actions(transaction_category_data):
    data = {
        'code': 'TRA',
        'name': 'Travel'
    }
    total_1 = _test_list(transaction_category_data)
    _test_new(data)
    total_2 = len(TransactionCategoryDatabase().list())
    assert (total_1 + 1) == total_2
    data['name'] == Faker().sentence()
    _test_update(data)
    _test_get_by_code(data)
    _test_delete(data)
    _test_list(transaction_category_data)
