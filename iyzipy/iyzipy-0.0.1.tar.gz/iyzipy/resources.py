
from .pki_builder import PKIBuilder


class IyzipyResource:
    def __init__(self, iyzipy):
        from .iyzipy import Iyzipy

        self.iyzipy: Iyzipy = iyzipy

    def request(self, method, url, request=None, pki=None):
        return self.iyzipy.client.request(method, url, request, pki=pki)

    @staticmethod
    def buyer_pki(buyer):
        pki_builder = PKIBuilder('')
        pki_builder.append('id', buyer.get('id'))
        pki_builder.append('name', buyer.get('name'))
        pki_builder.append('surname', buyer.get('surname'))
        pki_builder.append('identityNumber', buyer.get('identityNumber'))
        pki_builder.append('email', buyer.get('email'))
        pki_builder.append('gsmNumber', buyer.get('gsmNumber'))
        pki_builder.append('registrationDate', buyer.get('registrationDate'))
        pki_builder.append('lastLoginDate', buyer.get('lastLoginDate'))
        pki_builder.append('registrationAddress', buyer.get('registrationAddress'))
        pki_builder.append('city', buyer.get('city'))
        pki_builder.append('country', buyer.get('country'))
        pki_builder.append('zipCode', buyer.get('zipCode'))
        pki_builder.append('ip', buyer.get('ip'))
        return pki_builder.get_request_string()

    @staticmethod
    def address_pki(address):
        pki_builder = PKIBuilder('')
        pki_builder.append('address', address.get('address'))
        pki_builder.append('zipCode', address.get('zipCode'))
        pki_builder.append('contactName', address.get('contactName'))
        pki_builder.append('city', address.get('city'))
        pki_builder.append('country', address.get('country'))
        return pki_builder.get_request_string()

    @staticmethod
    def basket_pki(basket_items):
        basket_items_pki = []
        for item in basket_items:
            pki_builder = PKIBuilder('')
            pki_builder.append('id', item.get('id'))
            pki_builder.append_price('price', item.get('price'))
            pki_builder.append('name', item.get('name'))
            pki_builder.append('category1', item.get('category1'))
            pki_builder.append('category2', item.get('category2'))
            pki_builder.append('itemType', item.get('itemType'))
            pki_builder.append('subMerchantKey', item.get('subMerchantKey'))
            pki_builder.append_price('subMerchantPrice', item.get('subMerchantPrice'))
            basket_items_pki.append(pki_builder.get_request_string())
        return basket_items_pki

    @staticmethod
    def payment_card_pki(payment_card):
        pki_builder = PKIBuilder('')
        pki_builder.append('cardHolderName', payment_card.get('cardHolderName'))
        pki_builder.append('cardNumber', payment_card.get('cardNumber'))
        pki_builder.append('expireYear', payment_card.get('expireYear'))
        pki_builder.append('expireMonth', payment_card.get('expireMonth'))
        pki_builder.append('cvc', payment_card.get('cvc'))
        pki_builder.append('registerCard', payment_card.get('registerCard'))
        pki_builder.append('cardAlias', payment_card.get('cardAlias'))
        pki_builder.append('cardToken', payment_card.get('cardToken'))
        pki_builder.append('cardUserKey', payment_card.get('cardUserKey'))
        return pki_builder.get_request_string()

    @classmethod
    def installment_details_pki(cls, installment_details):
        installments_pki = []
        for item in installment_details:
            pki_builder = PKIBuilder('')
            pki_builder.append('bankId', item.get('bankId'))
            pki_builder.append_array('installmentPrices',
                                     cls.installment_prices_pki(item.get('installmentPrices')))
            installments_pki.append(pki_builder.get_request_string())
        return installments_pki

    @staticmethod
    def installment_prices_pki(installment_prices):
        installments_pki = []
        for item in installment_prices:
            pki_builder = PKIBuilder('')
            pki_builder.append('installmentNumber', item.get('installmentNumber'))
            pki_builder.append_price('totalPrice', item.get('totalPrice'))
            installments_pki.append(pki_builder.get_request_string())
        return installments_pki

    @staticmethod
    def card_pki(card):
        pki_builder = PKIBuilder('')
        pki_builder.append('cardAlias', card.get('cardAlias'))
        pki_builder.append('cardNumber', card.get('cardNumber'))
        pki_builder.append('expireYear', card.get('expireYear'))
        pki_builder.append('expireMonth', card.get('expireMonth'))
        pki_builder.append('cardHolderName', card.get('cardHolderName'))
        return pki_builder.get_request_string()


class SubscriptionProduct(IyzipyResource):
    def create(self, request):
        return self.request('POST', '/v2/subscription/products', request)

    def retrieve(self, reference_code):
        return self.request('GET', f'/v2/subscription/products/{reference_code}')

    def list(self):
        return self.request('GET', '/v2/subscription/products/')


class SubscriptionCustomer(IyzipyResource):
    def create(self, request):
        return self.request('POST', '/v2/subscription/customers', request)


class Subscription(IyzipyResource):
    def checkout_form(self, request):
        return self.request('POST', '/v2/subscription/checkoutform/initialize', request)


class CheckoutForm(IyzipyResource):
    def initialize(self, request):
        pki = self.to_pki_string(request)
        return self.request('POST', '/payment/iyzipos/checkoutform/initialize/auth/ecom', request, pki)

    def to_pki_string(self, request):
        pki_builder = PKIBuilder(self.iyzipy.client.resource_pki(request))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append('basketId', request.get('basketId'))
        pki_builder.append('paymentGroup', request.get('paymentGroup'))
        pki_builder.append('buyer', self.buyer_pki(request.get('buyer')))
        pki_builder.append('shippingAddress', self.address_pki(request.get('shippingAddress')))
        pki_builder.append('billingAddress', self.address_pki(request.get('billingAddress')))
        pki_builder.append_array('basketItems', self.basket_pki(request.get('basketItems')))
        pki_builder.append('callbackUrl', request.get('callbackUrl'))
        pki_builder.append('paymentSource', request.get('paymentSource'))
        pki_builder.append('currency', request.get('currency'))
        pki_builder.append('posOrderId', request.get('posOrderId'))
        pki_builder.append_price('paidPrice', request.get('paidPrice'))
        pki_builder.append('forceThreeDS', request.get('forceThreeDS'))
        pki_builder.append('cardUserKey', request.get('cardUserKey'))
        pki_builder.append_array('enabledInstallments', request.get('enabledInstallments'))
        pki_builder.append('debitCardAllowed', request.get('debitCardAllowed'))

        return pki_builder.get_request_string()
