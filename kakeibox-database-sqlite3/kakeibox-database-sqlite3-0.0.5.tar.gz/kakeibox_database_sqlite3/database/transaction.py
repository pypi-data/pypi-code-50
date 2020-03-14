from kakeibox_database_sqlite3.models.transaction import TransactionModel
import copy


class TransactionDatabase(object):
    def __init__(self):
        self._model = TransactionModel

    def list(self, start_time, end_time):
        query = self._model.select().where(
            self._model.timestamp.between(start_time, end_time)
        )
        return [item.to_dictionary() for item in query]

    def list_all(self):
        return [item.to_dictionary() for item in self._model.select()]

    def list_per_type(self, start_time, end_time, transaction_type_code):
        type_model = self._model.get_transaction_type_by_code(
            transaction_type_code)
        query = self._model.select().select().where(
            (self._model.timestamp.between(start_time, end_time)) &
            (self._model.transaction_type_id == type_model.id)
        )
        return [item.to_dictionary() for item in query]

    def new(self, new_data_dictionary):
        new_definition = copy.deepcopy(new_data_dictionary)
        record = self._model.from_dictionary(new_definition)
        record.save()
        return record.to_dictionary()

    def delete(self, uuid):
        try:
            query = (self._model.delete().where(self._model.uuid == uuid))
            affected_rows = query.execute()
            return affected_rows > 0
        except Exception:
            return False

    def get_by_uuid(self, uuid):
        return self._model.get(self._model.uuid == uuid).to_dictionary()

    def update(self, uuid, update_dict_data):
        update_definition = copy.deepcopy(update_dict_data)
        update_record = self._model.from_dictionary(update_definition)
        query = (self._model().update(update_record.to_update_values_dict())
                 .where(self._model.uuid == uuid))
        query.execute()
        return self.get_by_uuid(uuid)
