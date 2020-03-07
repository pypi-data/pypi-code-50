
from django.db.models import QuerySet


class CrossQuerySet(QuerySet):

    def find(self, query):
        return self.filter(src_code=query)

    def codes(self):
        return set(self.values_list('dst_code', flat=True))
