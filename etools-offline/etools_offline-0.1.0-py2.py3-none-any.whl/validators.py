from django.core.validators import URLValidator


class IntegerOrURLValidator(URLValidator):
    def __call__(self, value):
        if not isinstance(value, int):
            super().__call__(value)
