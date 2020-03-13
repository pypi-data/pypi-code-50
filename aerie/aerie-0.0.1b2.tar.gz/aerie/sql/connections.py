import databases

DatabaseURL = databases.DatabaseURL


class Connection(databases.Database):
    @property
    def dialect(self):
        return self._backend._dialect
