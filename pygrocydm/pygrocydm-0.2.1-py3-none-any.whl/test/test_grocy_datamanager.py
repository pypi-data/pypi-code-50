from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

import responses

from pygrocydm import GrocyDataManager
from pygrocydm.battery import Battery
from pygrocydm.chore import Chore
from pygrocydm.location import Location
from pygrocydm.product import Product
from pygrocydm.shopping_list import ShoppingList, ShoppingListItem


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

    @responses.activate
    def test_products_invalid_no_data(self):
        resp = []
        responses.add(responses.GET,
            '{}:{}/api/objects/products'.format(CONST_BASE_URL, CONST_PORT),
            json=resp,
            status=200)
        products = self.gdm.products().list
        assert products is None

    @responses.activate
    def test_products_error(self):
        responses.add(responses.GET,
            '{}:{}/api/objects/products'.format(CONST_BASE_URL, CONST_PORT),
            status=400)
        products = self.gdm.products().list
        assert products is None

    def test_chores_valid(self):
        chores = self.gdm.chores().list
        assert isinstance(chores, tuple)
        assert len(chores) >=1
        for chore in chores:
            assert isinstance(chore, Chore)

    def test_locations_valid(self):
        locations = self.gdm.locations().list
        assert isinstance(locations, tuple)
        assert len(locations) >=1
        for location in locations:
            assert isinstance(location, Location)

    def test_batteries_valid(self):
        batteries = self.gdm.batteries().list
        assert isinstance(batteries, tuple)
        assert len(batteries) >=1
        for battery in batteries:
            assert isinstance(battery, Battery)

    def test_shopping_list_items_valid(self):
        shopping_list_items = self.gdm.shopping_list().list
        assert isinstance(shopping_list_items, tuple)
        assert len(shopping_list_items) >=1
        for items in shopping_list_items:
            assert isinstance(items, ShoppingListItem)

    def test_shopping_lists_valid(self):
        shopping_lists = self.gdm.shopping_lists().list
        assert isinstance(shopping_lists, tuple)
        assert len(shopping_lists) >=1
        for shopping_list in shopping_lists:
            assert isinstance(shopping_list, ShoppingList)

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

    def test_edit_product_valid(self):
        fields = {}
        fields['name'] = 'Test'
        assert self.gdm.products().list[-1].edit(fields)

    def test_edit_product_error(self):
        fields = {}
        fields['nam'] = 'Test'
        assert "error_message" in self.gdm.products().list[0].edit(fields)

    def test_product_delete_valid(self):
        product = self.gdm.products().list[-1]
        old_len = len(self.gdm.products().list)
        assert product.delete()
        self.gdm.products().refresh()
        new_len = len(self.gdm.products().list)
        assert new_len == old_len - 1

    def test_product_delete_error(self):
        product = self.gdm.products().list[-1]
        product.delete()
        assert 'error' in product.delete()
