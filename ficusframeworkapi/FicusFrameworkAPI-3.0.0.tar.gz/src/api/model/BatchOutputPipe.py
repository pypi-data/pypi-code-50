class BatchOutputPipe:

    def clean(self):
        pass


    def flush(self):
        pass

    def output_for_insert(self, serializable):
        pass

    def output_for_delete(self, query):
        pass

    def output_for_update(self, serializable):
        pass

    def output_for_upsert(self, serializable):
        pass

    def skip_output(self):
        pass

    def is_all_empty(self):
        pass
