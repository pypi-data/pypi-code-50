from etools_offline.fields import OfflineAttachmentField


class OfflineSerializerMixin:
    """Serializer mixin that handles OfflineAttachmentField"""

    def create(self, validated_data):
        # remove OfflineAttachmentFields from validated_data
        # as they are handled with move_file call
        for field_key, field in self.fields.items():
            if isinstance(field, OfflineAttachmentField):
                validated_data.pop(field_key)
        return super().create(validated_data)
