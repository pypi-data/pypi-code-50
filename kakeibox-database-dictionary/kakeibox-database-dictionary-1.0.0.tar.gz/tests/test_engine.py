from kakeibox_database_dictionary.engine import TableBase, \
    TableTransactionCategory, TableTransactionSubcategory, \
    TableTransaction, TableAccount


def test_singleton_class():
    table = TableBase()
    table_2 = TableBase()
    assert id(table) == id(table_2)


def test_table_transaction_category_class():
    table = TableTransactionCategory()
    table_2 = TableTransactionCategory()
    assert id(table) == id(table_2)


def test_table_transaction_subcategory_class():
    table = TableTransactionSubcategory()
    table_2 = TableTransactionSubcategory()
    assert id(table) == id(table_2)


def test_table_transaction_class():
    table = TableTransaction()
    table_2 = TableTransaction()
    assert id(table) == id(table_2)


def test_table_account_class():
    table = TableAccount()
    table_2 = TableAccount()
    assert id(table) == id(table_2)
