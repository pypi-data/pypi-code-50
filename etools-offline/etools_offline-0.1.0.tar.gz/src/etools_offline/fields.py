from rest_framework.fields import IntegerField

from etools_offline import validators
from etools_offline.tasks import move_file


class OfflineAttachmentField(IntegerField):
    default_validators = [validators.IntegerOrURLValidator()]
    file_type_code = None

    def __init__(self, *args, **kwargs):
        if "file_type_code" not in kwargs:
            raise Exception(
                f"Missing `file_type_code` attribute on field {self}"
            )
        self.file_type_code = kwargs.pop("file_type_code")
        super().__init__(*args, **kwargs)

    def to_internal_value(self, data):
        """If value is not integer then it is an URL,
        so need to move file to app blob storage
        """
        if not isinstance(data, int) and self.parent is not None:
            move_file(self.parent.Meta.model, self.file_type_code, data)
        return data
