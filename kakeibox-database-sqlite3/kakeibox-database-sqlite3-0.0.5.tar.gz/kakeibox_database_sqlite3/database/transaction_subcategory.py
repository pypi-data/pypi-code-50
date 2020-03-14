from kakeibox_database_sqlite3.models.transaction_subcategory \
    import TransactionSubcategoryModel
import copy


class TransactionSubcategoryDatabase(object):
    def __init__(self):
        self._model = TransactionSubcategoryModel

    def list(self):
        return [item.to_dictionary() for item in self._model.select()]

    def list_per_category(self, transaction_category_code):
        category_model = self._model.\
            get_transaction_category_by_code(transaction_category_code)
        return [item.to_dictionary() for item in self._model.select().where(
                    self._model.transaction_category_id == category_model.id
                )]

    def new(self, new_data_dictionary):
        new_definition = copy.deepcopy(new_data_dictionary)
        record = self._model.from_dictionary(new_definition)
        record.save()
        return record.to_dictionary()

    def delete(self, code):
        try:
            query = (self._model.delete().where(self._model.code == code))
            affected_rows = query.execute()
            return affected_rows > 0
        except Exception:
            return False

    def get_by_code(self, code):
        return self._model.get(self._model.code == code).to_dictionary()

    def update(self, code, update_dict_data):
        update_definition = copy.deepcopy(update_dict_data)
        update_record = self._model.from_dictionary(update_definition)
        query = (self._model().update(update_record.to_update_values_dict()).
                 where(self._model.code == code))
        query.execute()
        return self.get_by_code(code)
