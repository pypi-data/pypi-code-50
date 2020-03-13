from unittest import TestCase, skip
from chibi_gob_mx.profeco import precios


@skip( "no implementada" )
class Test_precios( TestCase ):
    def test_simple_call( self ):
        response = precios.get()
        self.assertEqual( response.status_code, 200  )
        self.assertFalse( True )
