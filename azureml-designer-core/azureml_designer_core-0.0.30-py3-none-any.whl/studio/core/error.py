class UserError(Exception):
    """This is a base exception to indicate the errors that caused by unexpected user input.

    Once an exception inherited from UserError is raised,
    it could be displayed in Web UI to help the user adjust his input.
    """
    pass


class DataFrameSchemaValidationError(UserError):
    def __init__(self, detail=None):
        msg = "DataFrameSchema validation failed." \
            if not detail else f"DataFrameSchema validation failed, {detail}."
        super().__init__(msg)


class DirectoryNotExistError(UserError):
    def __init__(self, load_from_dir):
        super().__init__(f"Input path does not exist, please make sure your input is correct. Path='{load_from_dir}'.")


class DirectoryEmptyError(UserError):
    def __init__(self, load_from_dir):
        super().__init__(f"Input folder is empty, please make sure your input is correct. Path='{load_from_dir}'.")


class InvalidDirectoryError(UserError):
    def __init__(self, reason):
        super().__init__(f"Input folder is invalid, please make sure your input is correct."
                         f" Reason: {reason}")
