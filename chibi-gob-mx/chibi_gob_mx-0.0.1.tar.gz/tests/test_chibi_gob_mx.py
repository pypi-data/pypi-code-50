#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from chibi_gob_mx import catalog
from chibi.atlas import Chibi_atlas


class Test_catalog(unittest.TestCase):
    def test_catalog_should_have_200( self ):
        response = catalog.get()
        self.assertEqual( response.status_code, 200  )
        self.assertIsInstance( response.native, list )

    def test_catalog_should_retrive_the_total_of_elements( self ):
        response = catalog.get()
        self.assertEqual( response.status_code, 200  )
        total_elements = list( response.native )
        self.assertEqual(
            len( total_elements ), response.pagination.total_elements )

    def test_should_have_the_expected_keys( self ):
        response = catalog.get()
        self.assertEqual( response.status_code, 200  )
        for n in response.native:
            self.assertIn( 'id', n )
            self.assertIn( 'count', n )
            self.assertIn( 'endpoint', n )
            self.assertIn( 'origin_url', n )
            self.assertIn( 'fields', n )


    def test_all_the_elements_should_be_dict( self ):
        response = catalog.get()
        self.assertEqual( response.status_code, 200  )
        keys = set()
        for n in response.native:
            self.assertIsInstance( n, Chibi_atlas )
            if 'variables' in n:
                v = set( n.variables )
                """
                for a in v:
                    if 'latitud' in a:
                        import pdb
                        pdb.set_trace()
                """
                keys |= v

        #for k in sorted( keys ):
            #print( k )
