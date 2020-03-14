from kakeibox_database_sqlite3.database.transaction_subcategory \
    import TransactionSubcategoryDatabase
from faker import Faker


def _test_list(transaction_subcategory_data):
    records = TransactionSubcategoryDatabase().list()
    assert len(records) == len(transaction_subcategory_data)
    for record in records:
        assert record['code'] in transaction_subcategory_data
        element = transaction_subcategory_data[record['code']]
        assert record == element
    return len(records)


def _test_new(data):
    dict_response = TransactionSubcategoryDatabase().new(data)
    assert dict_response == data
    return dict_response


def _test_update(data):
    bridge = TransactionSubcategoryDatabase()
    dict_response = bridge.update(data['code'], data)
    assert dict_response == data
    return dict_response


def _test_get_by_code(data):
    bridge = TransactionSubcategoryDatabase()
    dict_response = bridge.get_by_code(data['code'])
    assert dict_response
    assert data['code'] == dict_response['code']
    assert data['name'] == dict_response['name']
    return dict_response


def _test_delete(data):
    result = TransactionSubcategoryDatabase().delete(data['code'])
    assert result


def test_transaction_subcategory_actions(transaction_subcategory_data):
    data = {
        'transaction_category_code': 'EXT',
        'code': 'TRV',
        'name': 'Travel'
    }
    total_1 = _test_list(transaction_subcategory_data)
    data = _test_new(data)
    total_2 = len(TransactionSubcategoryDatabase().list())
    assert (total_1 + 1) == total_2
    data['name'] == Faker().sentence()
    _test_update(data)
    _test_get_by_code(data)
    _test_delete(data)
    _test_list(transaction_subcategory_data)

    categories = ['SUR', 'OPT', 'CUL', 'EXT']
    subcategory_elements = transaction_subcategory_data.values()
    for value in categories:
        expected = {
            sub['code']: sub for sub in subcategory_elements
            if sub['transaction_category_code'] == value
        }

        bridge = TransactionSubcategoryDatabase()
        subcategories = bridge.list_per_category(value)

        assert len(expected) == len(subcategories)
        for subcategory in subcategories:
            assert subcategory['code'] in expected
            expected_item = expected[subcategory['code']]
            assert expected_item['code'] == subcategory['code']
            assert expected_item['name'] == subcategory['name']
            assert expected_item['transaction_category_code'] == subcategory[
                'transaction_category_code']
