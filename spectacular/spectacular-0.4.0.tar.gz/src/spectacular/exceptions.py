class ValidationError(Exception):
    """
    Base exception class for validation errors.  Derive from this class to
    create custom validation errors.
    """

    def __init__(self, message):
        super().__init__(message)
        self._message = message

    def to_dict(self):
        return {"message": self._message}


class DoesNotConformToSchema(ValidationError):
    def __init__(self, errors, message=None):
        message = message or "Invalid format"
        super().__init__(message)
        self._errors = errors

    def to_dict(self):
        spec = [{"message": e.message, "path": list(e.path)} for e in self._errors]
        return {"message": self._message, "spec": spec}


class InvalidEnumCode(ValidationError):
    def __init__(self, cls, code, message=None):
        message = message or "Code {} should be one of {}".format(code, cls.codes())
        super().__init__(message)
        self._cls = cls
        self._value = code

    def to_dict(self):
        return {
            "message": self._message,
            "spec": {
                "enum": self._cls.__name__,
                "value": self._value,
                "codes": self._cls.codes(),
            },
        }
