# -*- coding: utf-8 -*-
from chibi_requests import Chibi_url
from chibi_gob_mx.response import Catalog


catalog = Chibi_url(
    'https://api.datos.gob.mx/v1/api-catalog', response_class=Catalog )
