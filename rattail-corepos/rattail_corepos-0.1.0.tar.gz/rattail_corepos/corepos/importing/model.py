# -*- coding: utf-8; -*-
"""
CORE-POS model importers
"""

from __future__ import unicode_literals, absolute_import

from rattail import importing

from corepos.db import model as corepos
from corepos.trans.db import model as coretrans


class ToCore(importing.ToSQLAlchemy):
    """
    Base class for all CORE (operational) model importers
    """
    # TODO: should we standardize on the 'id' primary key? (can we even?)
    # key = 'id'


class ToCoreTrans(importing.ToSQLAlchemy):
    pass


########################################
# CORE Operational
########################################

class DepartmentImporter(ToCore):
    model_class = corepos.Department
    key = 'number'


class SubdepartmentImporter(ToCore):
    model_class = corepos.Subdepartment
    key = 'number'


class VendorImporter(ToCore):
    model_class = corepos.Vendor
    key = 'id'


class VendorContactImporter(ToCore):
    model_class = corepos.VendorContact
    key = 'vendor_id'


class ProductImporter(ToCore):
    model_class = corepos.Product
    key = 'id'


class ProductFlagImporter(ToCore):
    model_class = corepos.ProductFlag
    key = 'bit_number'


class EmployeeImporter(ToCore):
    model_class = corepos.Employee
    key = 'number'


class CustomerImporter(ToCore):
    model_class = corepos.Customer
    key = 'id'


class MemberTypeImporter(ToCore):
    model_class = corepos.MemberType
    key = 'id'


class MemberInfoImporter(ToCore):
    model_class = corepos.MemberInfo
    key = 'card_number'


class MemberDateImporter(ToCore):
    model_class = corepos.MemberDate
    key = 'card_number'


class MemberContactImporter(ToCore):
    model_class = corepos.MemberContact
    key = 'card_number'


class HouseCouponImporter(ToCore):
    model_class = corepos.HouseCoupon
    key = 'coupon_id'


########################################
# CORE Transactions
########################################

class TransactionDetailImporter(ToCoreTrans):
    """
    CORE-POS transaction data importer.
    """
    model_class = coretrans.TransactionDetail
