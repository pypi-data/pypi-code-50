from kakeibox_database_dictionary.engine import TableTransactionSubcategory


class TransactionSubcategoryDatabase(object):

    def list(self):
        subcategories = TableTransactionSubcategory()
        return [item for item in subcategories.table.values()]

    def list_per_category(self, code):
        subcategories = TableTransactionSubcategory()
        items = subcategories.table.values()
        return [
            item for item in items
            if item['transaction_category_code'] == code
        ]

    def get_by_code(self, code):
        subcategories = TableTransactionSubcategory()
        return subcategories.table[code]

    def delete(self, code):
        try:
            subcategories = TableTransactionSubcategory()
            del subcategories.table[code]
            return True
        except Exception:
            return False

    def new(self, new_data_dictionary):
        code = new_data_dictionary['code']
        subcategories = TableTransactionSubcategory()
        subcategories.table[code] = new_data_dictionary
        return subcategories.table[code]

    def update(self, code, update_dict_data):
        subcategories = TableTransactionSubcategory()
        if code in subcategories.table:
            subcategories.table[code] = update_dict_data
        return subcategories.table[code]
