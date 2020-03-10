from minutes.models import Edition

from .serializers.edition import EditionSerializer, EditionListSerializer
from ..common.viewsets.base import BaseApiReadOnlyViewset


class EditionViewset(BaseApiReadOnlyViewset):
    queryset = Edition.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return EditionSerializer
        else:
            return EditionListSerializer
