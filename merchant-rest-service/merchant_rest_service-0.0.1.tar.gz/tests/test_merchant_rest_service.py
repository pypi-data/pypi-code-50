
# from merchant_rest_service.cli import main
#
#
# def test_main():
#     assert main([]) == 0

from unittest import TestCase

from merchant_rest_service.src.merchant_rest_service.merchant_client_core import MerchantClientCore


class TestMerchantClientCore(TestCase):

    def setUp(self):
        super(TestMerchantClientCore, self).setUp()
        self.merchant_service = MerchantClientCore('A3878DC1-F07D-48E7-AA59-8276C3C26647',
                                                   'sQ9=5nxPkym*@Ds',
                                                   True, 'd01b26a2106d481da6aef9c8c19cc5'
                                                         '6d56aa81e7352f42178f2711669bf715adb1ebe'
                                                         '145c4bc4fff820c3786326d93b73dd61cc2b0f44'
                                                         '32aae67434b57b55c03')

    def test_get_transaction_details(self):
        response = self.merchant_service.get_transaction_detail('BP-C_20200302104201944_1707868_CJXBJ')

        print(response)

        self.assertIsNotNone(response, True)

    def test_get_transaction_detail_by_invoice_number(self):
        response = self.merchant_service.get_transaction_detail_by_invoice_number("")

        print(response)

        self.assertIsNotNone(response, True)

    def test_money_transfer(self):
        response = self.merchant_service.get_process_detail('2005187202121844')

        print(response)

        self.assertIsNotNone(response, True)

    def test_get_foreign_exchange_rate(self):
        response = self.merchant_service.get_foreign_exchange('NGN', 'USD')

        print(response)

        self.assertIsNotNone(response, True)

    def test_get_reconcilation_report(self):
        response = self.merchant_service.get_reconciliation_report('2019-07-07', '2019-08-25')

        print(response)

        self.assertIsNotNone(response, True)

    def test_refund_bill(self):
        response = self.merchant_service.refund_bill('BP-C_20200302104201944_1707868_CJXBJ',
                                                     True, True, '3105.00',
                                                     'NGN', 'Service not needed',
                                                     '07037299643')

        print(response)

        self.assertIsNotNone(response, True)

    def test_merchant_reference(self):
        response = self.merchant_service.get_transaction_details_by_merchantreference('mer-1570635017873')

        print(response)

        self.assertIsNotNone(response, True)

