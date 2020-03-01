from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL, SKIP_REAL
from typing import List
from unittest import TestCase

from pygrocydm import GrocyDataManager
from pygrocydm.chore import Chore
from pygrocydm.product import Product


class TestGrocyDataManager(TestCase):

    def setUp(self):
        self.gdm = GrocyDataManager(CONST_BASE_URL, "api_key")
        self.gdm = None
        self.gdm = GrocyDataManager(CONST_BASE_URL, "demo_mode",  verify_ssl = CONST_SSL, port = CONST_PORT)

    def test_init(self):
        assert isinstance(self.gdm, GrocyDataManager)

    def test_products_valid(self):
        products = self.gdm.products().list
        assert isinstance(products, tuple)
        assert len(products) >=1
        for product in products:
            assert isinstance(product, Product)

    def test_chores_valid(self):
        chores = self.gdm.chores().list
        assert isinstance(chores, tuple)
        assert len(chores) >=1
        for chore in chores:
            assert isinstance(chore, Chore)

    def test_add_product_valid(self):
        product_list = self.gdm.products()
        old_len = len(product_list.list)
        new_product = {}
        new_product['name'] = 'Test product'
        new_product['location_id'] = 1
        new_product['qu_id_purchase'] = 1
        new_product['qu_id_stock'] = 1
        new_product['qu_factor_purchase_to_stock'] = 1
        new_product_id = product_list.add(new_product)
        new_len = len(product_list.list)
        assert isinstance(new_product_id, int)
        assert new_len == old_len + 1

    def test_add_product_error(self):
        product_list = self.gdm.products()
        new_product = {}
        new_product['name'] = 'Test product'
        resp = product_list.add(new_product)
        assert "error_message" in resp.text
