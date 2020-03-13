class Row:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __data__(self):
        return {
            k: v if not isinstance(v, Row) else v.__data__()
            for k, v in self.__dict__.items()
            if not k.startswith("_")
        }

    def __str__(self):
        cols_limit = 5
        data = ", ".join(
            [
                f"{k}={v}"
                for k, v in list(self.__dict__.items())[:cols_limit]
                if not k.startswith("_") or not k.isupper()
            ]
        )
        total_keys = len(self.__dict__.keys())
        if total_keys > cols_limit:
            data += f" and {total_keys - cols_limit} columns more"
        return f"<Row: {data}>"
