from kakeibox_database_sqlite3.models.transaction_subcategory \
    import TransactionSubcategoryModel


def test_transaction_subcategory_model_from_dictionary(
        transaction_subcategory_data):
    data = next(iter(transaction_subcategory_data.values()))
    model = TransactionSubcategoryModel.from_dictionary(data)

    assert data['code'] == model.code
    assert data['name'] == model.name
    assert data['transaction_category_code'] == \
        model.transaction_category_id.code


def test_transaction_subcategory_to_dictionary(transaction_subcategory_data):
    data = next(iter(transaction_subcategory_data.values()))
    model = TransactionSubcategoryModel.from_dictionary(data)
    model_dict = model.to_dictionary()

    assert data['code'] == model_dict['code']
    assert data['name'] == model_dict['name']
