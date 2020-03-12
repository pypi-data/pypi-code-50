from kakeibox_database_dictionary.engine import TableTransactionSubcategory
from kakeibox_database_dictionary.database.transaction_subcategory import \
    TransactionSubcategoryDatabase
from faker import Faker


def _before_execute_test():
    database = TableTransactionSubcategory()
    database.table = {}


def test_transaction_subcategory_new(transaction_subcategory_data):
    _before_execute_test()
    count = 1
    for dictionary in transaction_subcategory_data.values():
        bridge = TransactionSubcategoryDatabase()
        result = bridge.new(dictionary)
        assert isinstance(result, dict)

        database = TableTransactionSubcategory()
        assert count == len(database.table)

        expected = database.table[dictionary['code']]
        assert expected == dictionary
        count += 1


def test_transaction_subcategory_list(transaction_subcategory_data):
    _before_execute_test()
    database = TableTransactionSubcategory()
    database.table = transaction_subcategory_data

    bridge = TransactionSubcategoryDatabase()
    item_list = bridge.list()

    assert len(database.table) == len(item_list)

    for element in item_list:
        expected = database.table[element['code']]
        assert expected == element
        assert isinstance(element, dict)


def test_transaction_subcategory_list_per_category(
        transaction_category_data, transaction_subcategory_data):
    _before_execute_test()
    database = TableTransactionSubcategory()
    database.table = transaction_subcategory_data
    for category_code in transaction_category_data:
        bridge = TransactionSubcategoryDatabase()
        item_list = bridge.list_per_category(category_code)
        for element in item_list:
            assert category_code == element['transaction_category_code']
            assert  isinstance(element, dict)


def test_transaction_subcategory_update(transaction_subcategory_data):
    _before_execute_test()
    faker = Faker()
    database = TableTransactionSubcategory()
    database.table = transaction_subcategory_data
    code = list(transaction_subcategory_data)[0]

    item = transaction_subcategory_data[code]
    item['code'] = faker.month()
    item['name'] = faker.name()

    bridge = TransactionSubcategoryDatabase()
    result = bridge.update(code, item)

    assert isinstance(result, dict)
    assert result == item


def test_transaction_category_delete(transaction_subcategory_data):
    _before_execute_test()
    database = TableTransactionSubcategory()
    database.table = transaction_subcategory_data
    total = len(database.table)
    code = list(transaction_subcategory_data)[0]
    assert code in database.table

    bridge = TransactionSubcategoryDatabase()
    result = bridge.delete(code)
    assert isinstance(result, bool)

    assert code not in database.table
    assert (total - 1) == len(database.table)
