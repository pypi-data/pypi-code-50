# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import random
import json
import pycountry

from decimal import Decimal
from dateutil.relativedelta import relativedelta
from ast import literal_eval
from unittest.mock import patch
from datetime import date

from trytond.tests.test_tryton import suite as test_suite
from trytond.tests.test_tryton import with_transaction, USER
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.config import config

from werkzeug.datastructures import Headers

from nereid.testing import NereidModuleTestCase
from nereid import current_website, current_locale
from nereid.globals import session

from trytond.modules.company.tests import create_company, set_company
from trytond.modules.nereid.tests.test_common import (create_website_locale,
    create_static_file)
from trytond.modules.payment_gateway.tests import (create_payment_gateway,
    create_payment_profile)
from trytond.modules.sale_channel.tests import (create_sale_channels,
    create_channel_sale)
from trytond.modules.nereid_cart_b2c.tests import (create_website,
    create_countries, create_pricelists, create_product_template)

config.set('email', 'from', 'from@xyz.com')


def process_sale_by_completing_payments(sales):
    """
    Process sale and complete payments.
    """
    pool = Pool()
    Sale = pool.get('sale.sale')

    Sale.process(sales)
    Sale.process_all_pending_payments()

#def create_payment_profile(self, party, gateway):
#    """
#    Create a payment profile for the party
#    """
#    AddPaymentProfileWizard = POOL.get(
#        'party.party.payment_profile.add', type='wizard'
#    )

#    # create a profile
#    profile_wiz = AddPaymentProfileWizard(
#        AddPaymentProfileWizard.create()[0]
#    )
#    profile_wiz.card_info.party = party.id
#    profile_wiz.card_info.address = party.addresses[0].id
#    profile_wiz.card_info.provider = gateway.provider
#    profile_wiz.card_info.gateway = gateway
#    profile_wiz.card_info.owner = party.name
#    profile_wiz.card_info.number = '4111111111111111'
#    profile_wiz.card_info.expiry_month = '11'
#    profile_wiz.card_info.expiry_year = '2018'
#    profile_wiz.card_info.csc = '353'

#    with Transaction().set_context(return_profile=True):
#        return profile_wiz.transition_add()

def create_registered_user_order(self, client, quantity=None):
    """
    A helper function that creates an order for a
    registered user.
    """
    pool = Pool()
    Country = pool.get('country.country')

    # Setup defaults
    # A gateway sets up a lot of configuration stuff (fiscalyear, chart,
    # etc.)
    website = create_website()
    website.save()
    gateway = create_payment_gateway()
    gateway.save()

    # Create product templates with products
    template1, = create_product_template(
        'product-1',
        [{
            'type': 'goods',
            'salable': True,
            'list_price': Decimal('10'),
        }],
        uri='product-1',
    )

    product1 = template1.products[0]

    if not quantity:
        quantity = random.randrange(10, 100)
    client.post('/en/cart/add',
        data={
            'product': product1.id,
            'quantity': quantity,
            })

    # Sign-in
    rv = client.post('/en/checkout/sign-in',
        data={
            'email': 'email@example.com',
            'password': 'password',
            'checkout_mode': 'account',
            })

    create_countries()
    countries = Country.search([])
    website.countries = countries
    website.save()
    country = countries[0]
    subdivision = country.subdivisions[0]

    rv = client.post('/en/checkout/shipping-address',
        data={
            'name': 'Max Mustermann',
            'street': 'Musterstr. 26',
            'zip': '79852',
            'city': 'Musterstadt',
            'country': country.id,
            'subdivision': subdivision.id,
        })

    # Post to payment delivery-address with same flag
    rv = client.post('/en/checkout/payment',
        data={
            'use_shipment_address': 'True',
            })


def create_guest_order(client, quantity=None):
    """
    A helper function that creates an order for a guest user.
    """
    pool = Pool()
    Country = pool.get('country.country')
    Template = pool.get('product.template')
    Product = pool.get('product.product')
    Party = pool.get('party.party')

    # Setup defaults
    # A gateway sets up a lot of configuration stuff (fiscalyear, chart,
    # etc.)
    website = create_website()
    website.save()
    gateway = create_payment_gateway()
    gateway.save()

    product_uri = 'product-1'
    products = Product.search([
            ('uri', '=', product_uri),
            ])
    if products:
        product1 = products[0]
    else:
        template1, = create_product_template(
            'product-1',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('10'),
            }],
            uri=product_uri,
        )

        product1 = template1.products[0]

    if not quantity:
        quantity = random.randrange(10, 100)
    client.post('/en/cart/add',
        data={
            'product': product1.id,
            'quantity': quantity,
            })

    # Sign-in
    rv = client.post('/en/checkout/sign-in',
        data={
            'email': 'new@example.com',
            'checkout_mode': 'guest',
            })

    countries = Country.search([])
    if not countries:
        create_countries()
        countries = Country.search([])
    if not website.countries:
        website.countries = countries
        website.save()
    country = countries[0]
    subdivision = country.subdivisions[0]

    rv = client.post('/en/checkout/shipping-address',
        data={
            'name': 'Max Mustermann',
            'street': 'Musterstr. 26',
            'zip': '79852',
            'city': 'Musterstadt',
            'country': country.id,
            'subdivision': subdivision.id,
        })

    # Post to payment delivery-address with same flag
    rv = client.post('/en/checkout/payment',
        data={
            'use_shipment_address': 'True',
            })
    print('ooooooooo', Party.search([
                ('name', '=', 'Max Mustermann'),
                ])
        )
    print('ooooooooo', [p.name for p in Party.search([
                ])]
        )


#def _create_cheque_payment_method(self):
#    """
#    A helper function that creates the cheque gateway and assigns
#    it to the websites.
#    """
#    PaymentGateway = POOL.get('payment_gateway.gateway')
#    NereidWebsite = POOL.get('nereid.website')
#    PaymentMethod = POOL.get('nereid.website.payment_method')
#    Journal = POOL.get('account.journal')

#    cash_journal, = Journal.search([
#        ('name', '=', 'Cash')
#    ])

#    gateway = PaymentGateway(
#        name='Offline Payment Methods',
#        journal=cash_journal,
#        provider='self',
#        method='manual',
#    )
#    gateway.save()

#    website, = NereidWebsite.search([])

#    payment_method = PaymentMethod(
#        name='Cheque',
#        gateway=gateway,
#        website=website
#    )
#    payment_method.save()
#    return payment_method

#def _create_auth_net_gateway_for_site(self):
#    """
#    A helper function that creates the authorize.net gateway and assigns
#    it to the websites.
#    """
#    PaymentGateway = POOL.get('payment_gateway.gateway')
#    NereidWebsite = POOL.get('nereid.website')
#    Journal = POOL.get('account.journal')

#    cash_journal, = Journal.search([
#        ('name', '=', 'Cash')
#    ])

#    gateway = PaymentGateway(
#        name='Authorize.net',
#        journal=cash_journal,
#        provider='authorize_net',
#        method='credit_card',
#        authorize_net_login='327deWY74422',
#        authorize_net_transaction_key='32jF65cTxja88ZA2',
#        test=True
#    )
#    gateway.save()

#    websites = NereidWebsite.search([])
#    NereidWebsite.write(websites, {
#        'accept_credit_card': True,
#        'save_payment_profile': True,
#        'credit_card_gateway': gateway.id,
#    })
#    return gateway


class NereidCheckoutPaymentTestCase(NereidModuleTestCase):
    'Test Nereid Checkout module'
    module = 'nereid_checkout'

    def setUp(self):
        self.templates = {
            'home.jinja': '{{get_flashed_messages()}}',
            'login.jinja':
                '{{ login_form.errors }} {{get_flashed_messages()}}',
            'shopping-cart.jinja':
                'Cart:{{ cart.id }},{{get_cart_size()|round|int}},'
                '{{cart.sale.total_amount}}',
            'product.jinja':
                '{{ product.sale_price(product.id) }}',
            'address-edit.jinja':
            'Address Edit {% if address %}ID:{{ address.id }}{% endif %}'
            '{{ form.errors }}',
            'address.jinja': '',
            'checkout/signin.jinja': '{{form.errors|safe}}',
            'checkout/signin-email-in-use.jinja': '{{email}} in use',
            'checkout/shipping_address.jinja': '{{address_form.errors|safe}}',
            'checkout/billing_address.jinja': '{{address_form.errors|safe}}',
            'checkout/payment_method.jinja': '''[
                {{payment_form.errors|safe}},
                {{credit_card_form.errors|safe}},
            ]''',
            'emails/sale-confirmation-text.jinja': ' ',
            'emails/sale-confirmation-html.jinja': ' ',
            'checkout.jinja': '{{form.errors|safe}}',
            'sale.jinja': ' ',
            'sales.jinja': '''{{request.args.get('filter_by')}}
                {% for sale in sales %}#{{sale.id}}{% endfor %}
            '''
            }

        # Patch SMTP Lib
        self.smtplib_patcher = patch('smtplib.SMTP')
        self.PatchedSMTP = self.smtplib_patcher.start()

    def tearDown(self):
        # Unpatch SMTP Lib
        self.smtplib_patcher.stop()

    @with_transaction()
    def test_0005_no_skip_signin(self):
        """
        Ensure that guest orders cant directly skip to enter shipping address
        """
        pool = Pool()
        Company = pool.get('company.company')
        Sale = pool.get('sale.sale')

        # Setup defaults
        # A gateway sets up a lot of configuration stuff (fiscalyear, chart,
        # etc.)
        website = create_website()
        website.save()
        gateway = create_payment_gateway()
        gateway.save()
        company, = Company.search([])

        # Create product templates with products
        template1, = create_product_template(
            'product-1',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('10'),
            }],
            uri='product-1',
        )

        product1 = template1.products[0]
        quantity = 5

        app = self.get_app()
        with app.test_client() as c:
            rv = c.get('/en/cart')
            self.assertEqual(rv.status_code, 200)

            c.post('/en/cart/add',
                data={
                    'product': product1.id,
                    'quantity': quantity,
                }
            )
            rv = c.get('/en/checkout/payment')
            self.assertEqual(rv.status_code, 302)
            self.assertTrue(
                rv.location.endswith('/en/checkout/sign-in'))

    @with_transaction()
    def test_0010_no_skip_shipping_address(self):
        """
        Ensure that guest orders cant directly skip to payment without a
        valid shipment_address.

        Once shipment address is there, it should be possible to get the
        page even without a invoice_address
        """
        pool = Pool()
        Sale = pool.get('sale.sale')
        Party = pool.get('party.party')
        Country = pool.get('country.country')

        # Setup defaults
        # A gateway sets up a lot of configuration stuff (fiscalyear, chart,
        # etc.)
        website = create_website()
        website.save()
        gateway = create_payment_gateway()
        gateway.save()

        # Create product templates with products
        template1, = create_product_template(
            'product-1',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('10'),
            }],
            uri='product-1',
        )

        product1 = template1.products[0]
        quantity = 5

        create_countries()
        countries = Country.search([])
        website.countries = countries
        website.save()
        country = countries[0]
        subdivision = country.subdivisions[0]

        app = self.get_app()
        with app.test_client() as c:
            c.post('/en/cart/add',
                data={
                    'product': product1.id,
                    'quantity': quantity,
                    })

            # Sign-in
            rv = c.post('/en/checkout/sign-in',
                data={
                    'email': 'new@example.com',
                    'checkout_mode': 'guest',
                    })

            # redirect to shipment address page
            self.assertEqual(rv.status_code, 302)
            self.assertTrue(
                rv.location.endswith('/en/checkout/shipping-address'))

            # Shipping address page gets rendered
            rv = c.post('/en/checkout/shipping-address',
                data={
                    'name': 'Max Mustermann',
                    'street': 'Musterstr. 26',
                    'zip': '79852',
                    'city': 'Musterstadt',
                    'country': country.id,
                    'subdivision': subdivision.id,
                })
            self.assertEqual(rv.status_code, 302)
            self.assertTrue(
                rv.location.endswith('/en/checkout/validate-address'))

            sales = Sale.search([])
            self.assertEqual(len(sales), 1)

            rv = c.get('/en/checkout/payment')
            self.assertEqual(rv.status_code, 200)

    @with_transaction()
    def test_0020_no_skip_invoice_address(self):
        """
        While it is possible to view the payment_method page without a
        billing_address, it should not be possible to complete payment without
        it.
        """
        pool = Pool()
        Sale = pool.get('sale.sale')
        Party = pool.get('party.party')
        Country = pool.get('country.country')

        # Setup defaults
        # A gateway sets up a lot of configuration stuff (fiscalyear, chart,
        # etc.)
        website = create_website()
        website.save()
        gateway = create_payment_gateway()
        gateway.save()

        # Create product templates with products
        template1, = create_product_template(
            'product-1',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('10'),
            }],
            uri='product-1',
        )

        product1 = template1.products[0]
        quantity = 5

        create_countries()
        countries = Country.search([])
        website.countries = countries
        website.save()
        country = countries[0]
        subdivision = country.subdivisions[0]

        app = self.get_app()
        with app.test_client() as c:
            c.post('/en/cart/add',
                data={
                    'product': product1.id,
                    'quantity': quantity,
                    })

            # Sign-in
            rv = c.post('/en/checkout/sign-in',
                data={
                    'email': 'new@example.com',
                    'checkout_mode': 'guest',
                    })

            # redirect to shipment address page
            self.assertEqual(rv.status_code, 302)
            self.assertTrue(
                rv.location.endswith('/en/checkout/shipping-address'))

            # Shipping address page gets rendered
            rv = c.post('/en/checkout/shipping-address',
                data={
                    'name': 'Max Mustermann',
                    'street': 'Musterstr. 26',
                    'zip': '79852',
                    'city': 'Musterstadt',
                    'country': country.id,
                    'subdivision': subdivision.id,
                })
            self.assertEqual(rv.status_code, 302)
            self.assertTrue(
                rv.location.endswith('/en/checkout/validate-address'))

            sales = Sale.search([])
            self.assertEqual(len(sales), 1)

            # GET requests get served
            rv = c.get('/en/checkout/payment')
            self.assertEqual(rv.status_code, 200)


            # POST redirects to billing address
            rv = c.post('/en/checkout/payment', data={})

            # redirect to shipment address page
            self.assertEqual(rv.status_code, 302)
            self.assertTrue(
                rv.location.endswith('/en/checkout/billing-address'))

    @with_transaction()
    def test_0030_address_with_payment(self):
        """
        Send address along with the payment
        """
        pool = Pool()
        Sale = pool.get('sale.sale')
        Party = pool.get('party.party')
        Country = pool.get('country.country')

        # Setup defaults
        # A gateway sets up a lot of configuration stuff (fiscalyear, chart,
        # etc.)
        website = create_website()
        website.save()
        gateway = create_payment_gateway()
        gateway.save()

        # Create product templates with products
        template1, = create_product_template(
            'product-1',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('10'),
            }],
            uri='product-1',
        )

        product1 = template1.products[0]
        quantity = 5

        create_countries()
        countries = Country.search([])
        website.countries = countries
        website.save()
        country = countries[0]
        subdivision = country.subdivisions[0]

        app = self.get_app()
        with app.test_client() as c:
            c.post('/en/cart/add',
                data={
                    'product': product1.id,
                    'quantity': quantity,
                    })

            # Sign-in
            rv = c.post('/en/checkout/sign-in',
                data={
                    'email': 'new@example.com',
                    'checkout_mode': 'guest',
                    })

            # redirect to shipment address page
            self.assertEqual(rv.status_code, 302)
            self.assertTrue(
                rv.location.endswith('/en/checkout/shipping-address'))

            # Shipping address page gets rendered
            address_data = {
                'name': 'Max Mustermann',
                'street': 'Musterstr. 26',
                'zip': '79852',
                'city': 'Musterstadt',
                'country': country.id,
                'subdivision': subdivision.id,
                }
            rv = c.post('/en/checkout/shipping-address',
                data=address_data)
            self.assertEqual(rv.status_code, 302)
            self.assertTrue(
                rv.location.endswith('/en/checkout/validate-address'))

            sales = Sale.search([])
            self.assertEqual(len(sales), 1)

            # POST to payment delivery-address with same flag
            rv = c.post('/en/checkout/payment',
                data={
                    'use_shipment_address': 'True',
                    })
            self.assertEqual(rv.status_code, 200)

            # Assert that just one address was created
            party, = Party.search([
                ('contact_mechanisms.value', '=', 'new@example.com'),
                ('contact_mechanisms.type', '=', 'email'),
            ])
            self.assertTrue(party)
            self.assertEqual(len(party.addresses), 1)

            address, = party.addresses
            self.assertEqual(address.street, address_data['street'])

            sales = Sale.search([
                ('shipment_address', '=', address.id),
                ('invoice_address', '=', address.id),
            ])
            self.assertEqual(len(sales), 1)

    @with_transaction()
    def test_0100_guest_credit_card(self):
        """
        Guest - Credit Card
        """
        pool = Pool()
        Account = pool.get('account.account')
        Sale = pool.get('sale.sale')
        Party = pool.get('party.party')
        Company = pool.get('company.company')
        NereidWebsite = pool.get('nereid.website')

        card_data = {
            'owner': 'Joe Blow',
            'number': '4111111111111111',
            'expiry_year': '2030',
            'expiry_month': '01',
            'cvv': '911',
            }

        app = self.get_app()
        with app.test_client() as c:
            create_guest_order(c)

            # Try to pay using credit card
            rv = c.post('/en/checkout/payment',
                data=card_data)
            # Though the card is there, the website is not configured
            # to accept credit cards as there is no credit card gateway defined.
            self.assertEqual(rv.status_code, 200)

        # Define a new payment gateway
        gateway = create_payment_gateway(method='dummy')

        websites = NereidWebsite.search([])
        NereidWebsite.write(websites, {
            'accept_credit_card': True,
            'save_payment_profile': True,
            'credit_card_gateway': gateway.id,
        })

        company, = Company.search([])

        with app.test_client() as c:

            context = {
                'company': company.id,
                'use_dummy': True,
                }
            with Transaction().set_context(**context):
                create_guest_order(c)
                receivable, = Account.search([
                        ('type.receivable', '=', True),
                        ])
                parties = Party.search([])
                Party.write(parties, {
                        'account_receivable': receivable,
                        })
                print('*****************', Sale.search([]))
                # Try to pay using credit card
                rv = c.post('/en/checkout/payment',
                    data=card_data)
                print(rv.status_code)
                print(rv.data)
                print(rv.location)
                self.assertEqual(rv.status_code, 302)
                self.assertTrue('/order/' in rv.location)
                self.assertTrue('access_code' in rv.location)

                sale, = Sale.search([('state', '=', 'confirmed')])

                # Process sale with payments
                process_sale_by_completing_payments([sale])
                payment_transaction, = sale.gateway_transactions
                self.assertEqual(payment_transaction.amount, sale.total_amount)
                self.assertFalse(sale.payment_available)

    #@with_transaction()
    #def test_0102_guest_credit_card2(self):
    #    """
    #    Guest - Credit Card
    #    """
    #    pool = Pool()
    #    Sale = pool.get('sale.sale')
    #    Company = pool.get('company.company')
    #    Account = pool.get('account.account')
    #    NereidWebsite = pool.get('nereid.website')

    #    card_data = {
    #        'owner': 'Joe Blow',
    #        'number': '4111111111111111',
    #        'expiry_year': '2030',
    #        'expiry_month': '01',
    #        'cvv': '911',
    #        }

    #    app = self.get_app()

    #    # Define a new payment gateway
    #    gateway = create_payment_gateway(method='dummy')

    #    websites = NereidWebsite.search([])
    #    NereidWebsite.write(websites, {
    #        'accept_credit_card': True,
    #        'save_payment_profile': True,
    #        'credit_card_gateway': gateway.id,
    #    })

    #    company, = Company.search([])

    #    with set_company(company):
    #        context = {
    #            'company': company.id,
    #            'use_dummy': True,
    #            }
    #        with Transaction().set_context(**context):
    #            with app.test_client() as c:

    #                create_guest_order(c)

    #                print('*****************', Sale.search([]))
    #                sale, = Sale.search([])
    #                print(sale.party)
    #                receivable, = Account.search([
    #                        ('type.receivable', '=', True),
    #                        ])
    #                sale.party.account_receivable = receivable
    #                sale.party.save()
    #                # Try to pay using credit card
    #                rv = c.post('/en/checkout/payment',
    #                    data=card_data)
    #                print(rv.status_code)
    #                print(rv.data)
    #                print(rv.location)
    #                self.assertEqual(rv.status_code, 302)
    #                self.assertTrue('/order/' in rv.location)
    #                self.assertTrue('access_code' in rv.location)

    #                sale, = Sale.search([('state', '=', 'confirmed')])

    #                # Process sale with payments
    #                process_sale_by_completing_payments([sale])
    #                payment_transaction, = sale.gateway_transactions
    #                self.assertEqual(payment_transaction.amount, sale.total_amount)
    #                self.assertFalse(sale.payment_available)



