from kakeibox_database_dictionary.engine import TableTransactionCategory


class TransactionCategoryDatabase(object):

    def list(self):
        categories = TableTransactionCategory()
        return [item for item in categories.table.values()]

    def new(self, new_data_dictionary):
        code = new_data_dictionary['code']
        categories = TableTransactionCategory()
        categories.table[code] = new_data_dictionary
        return categories.table[code]

    def delete(self, code):
        try:
            categories = TableTransactionCategory()
            del categories.table[code]
            return True
        except Exception:
            return False

    def get_by_code(self, code):
        categories = TableTransactionCategory()
        return categories.table[code]

    def update(self, code, update_dict_data):
        categories = TableTransactionCategory()
        table = categories.table
        if code in table:
            table[code] = update_dict_data
        return table[code]
