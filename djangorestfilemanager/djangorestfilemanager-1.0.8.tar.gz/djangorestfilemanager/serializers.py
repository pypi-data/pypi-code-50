from djangorestfilemanager.models import File
from rest_framework import serializers
import logging

logger = logging.getLogger(__name__)


class DefaultFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = (
            'url', 'uuid', 'file', 'name', 'username', 'creation_date', 'last_mod_date', 'permission', 'type',
            'origin', 'share'
        )
        read_only_fields = ('uuid', 'name', 'username', 'creation_date', 'last_mod_date')

    def to_representation(self, instance):
        return DefaultFileViewSerializer(instance=instance).data


class DefaultFileViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('uuid',)
        read_only_fields = ('uuid',)
