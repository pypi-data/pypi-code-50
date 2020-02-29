#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `fifteenrock` package."""


import unittest

from fifteenrock.core import core
from fifteenrock import cli

class TestFifteenrock(unittest.TestCase):
    """Tests for `fifteenrock` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

        self.url = 'abc.com/data'

    def tearDown(self):
        """Tear down test fixtures, if any."""
    
    def test_master_date_portfolio_url(self):
        """Test something."""
        
        local_url1 = core.get_master_data_portfolio_url(self.url, 'ns1', 'entity1')

        self.assertEqual(self.url + '/default/ns1/entity1', local_url1)

    def test_master_date_portfolio_url_2(self):
        """Test something."""
        
        local_url1 = core.get_master_data_portfolio_url(self.url, 'ns1', 'entity1', filter_in='age>30')

        self.assertEqual(self.url + '/default/ns1/entity1?a=a&where=age>30', local_url1)

    def test_master_date_portfolio_url_3(self):
        """Test something."""
        
        local_url1 = core.get_master_data_portfolio_url(self.url, 'ns1', 'entity1', filter_in='age>30', return_='name, age')

        self.assertEqual(self.url + '/default/ns1/entity1?a=a&where=age>30&return=name, age', local_url1)

    def test_master_date_portfolio_url_4(self):
        """Test something."""
        
        local_url1 = core.get_master_data_portfolio_url(self.url, 'ns1', 'entity1', filter_in='age>30', return_='name, age', return_except='gender')

        self.assertEqual(self.url + '/default/ns1/entity1?a=a&where=age>30&return=name, age&return_except=gender', local_url1)



if __name__ == '__main__':
    unittest.main()