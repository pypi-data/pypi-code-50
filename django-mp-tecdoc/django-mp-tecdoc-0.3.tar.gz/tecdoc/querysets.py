
from django.db.models import QuerySet, Q


class CrossQuerySet(QuerySet):

    def find(self, query):
        return self.filter(Q(src_code=query) | Q(dst_code=query))

    def _get_codes(self):
        for cross in self.values('src_code', 'dst_code'):
            yield cross['src_code']
            yield cross['dst_code']

    def codes(self):
        return set(self._get_codes())
