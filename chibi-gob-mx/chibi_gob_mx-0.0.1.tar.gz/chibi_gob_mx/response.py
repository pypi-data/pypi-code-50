import copy

from chibi.atlas import Atlas
from chibi.chain import Chibi_chain
from chibi.metaphors import Book
from chibi.metaphors.book import End_book
from chibi_requests import Response

from .serializers import Catalog as Catalog_serializer


class Catalog( Response ):
    serializer = Catalog_serializer

    @property
    def native( self ):
        try:
            return self._native
        except AttributeError:
            from chibi_gob_mx.chibi_gob_mx import catalog
            native = super().native
            results = Atlas( native )
            page = copy.copy( self.pagination )
            try:
                page.next()
                catalog = catalog + page
                chain_params = dict(
                    next_obj=catalog,
                    retrieve_next=lambda x: catalog.get().native
                )
            except End_book:
                chain_params = dict( next_obj=None, retrieve_next=None )
            self._native = Chibi_chain( results, **chain_params )
            return self._native

    @property
    def pagination( self ):
        try:
            return self._pagination
        except AttributeError:
            native = self.parse_content_type()
            page = native.pagination
            page = Book(
                total_elements=page.total, page_size=page.pageSize,
                page=page.page, offset_dict={
                    'page': 'page', 'page_size': 'pageSize' } )

            self._pagination = page
            return self._pagination

    @property
    def native_is_many( self ):
        return True
