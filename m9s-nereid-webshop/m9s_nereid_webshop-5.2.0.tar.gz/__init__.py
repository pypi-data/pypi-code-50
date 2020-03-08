# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import webshop
from . import product
from . import invoice
from . import sale
from . import party
from . import shipment
from . import tree


__all__ = ['register']


def register():
    Pool.register(
        webshop.ArticleCategory,
        webshop.Company,
        webshop.BannerCategory,
        webshop.Banner,
        webshop.Article,
        webshop.MenuItem,
        webshop.WebShop,
        webshop.Website,
        product.Product,
        invoice.Invoice,
        party.Address,
        shipment.ShipmentOut,
        sale.Sale,
        sale.SaleLine,
        tree.Node,
        module='nereid_webshop', type_='model')
