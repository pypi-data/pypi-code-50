# -*- coding: utf-8; -*-
################################################################################
#
#  pyCOREPOS -- Python Interface to CORE POS
#  Copyright © 2018-2020 Lance Edgar
#
#  This file is part of pyCOREPOS.
#
#  pyCOREPOS is free software: you can redistribute it and/or modify it under
#  the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option)
#  any later version.
#
#  pyCOREPOS is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  pyCOREPOS.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
CORE POS Data Model
"""

from __future__ import unicode_literals, absolute_import

import six
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy


Base = declarative_base()


@six.python_2_unicode_compatible
class Parameter(Base):
    """
    Represents a "parameter" value.
    """
    __tablename__ = 'parameters'

    store_id = sa.Column(sa.SmallInteger(), primary_key=True, nullable=False)

    lane_id = sa.Column(sa.SmallInteger(), primary_key=True, nullable=False)

    param_key = sa.Column(sa.String(length=100), primary_key=True, nullable=False)

    param_value = sa.Column(sa.String(length=255), nullable=True)

    is_array = sa.Column(sa.Boolean(), nullable=True)

    def __str__(self):
        return "{}-{} {}".format(self.store_id, self.lane_id, self.param_key)


@six.python_2_unicode_compatible
class Department(Base):
    """
    Represents a department within the organization.
    """
    __tablename__ = 'departments'

    number = sa.Column('dept_no', sa.SmallInteger(), primary_key=True, autoincrement=False, nullable=False)

    name = sa.Column('dept_name', sa.String(length=30), nullable=True)

    tax = sa.Column('dept_tax', sa.Boolean(), nullable=True)

    food_stampable = sa.Column('dept_fs', sa.Boolean(), nullable=True)

    limit = sa.Column('dept_limit', sa.Float(), nullable=True)

    minimum = sa.Column('dept_minimum', sa.Float(), nullable=True)

    discount = sa.Column('dept_discount', sa.Boolean(), nullable=True)

    # TODO: probably should rename this attribute, but to what?
    dept_see_id = sa.Column(sa.Boolean(), nullable=True)

    modified = sa.Column(sa.DateTime(), nullable=True)

    modified_by_id = sa.Column('modifiedby', sa.Integer(), nullable=True)

    margin = sa.Column(sa.Float(), nullable=False, default=0)

    sales_code = sa.Column('salesCode', sa.Integer(), nullable=False, default=0)

    member_only = sa.Column('memberOnly', sa.SmallInteger(), nullable=False, default=0)

    def __str__(self):
        return self.name or ''


@six.python_2_unicode_compatible
class Subdepartment(Base):
    """
    Represents a subdepartment within the organization.
    """
    __tablename__ = 'subdepts'
    __table_args__ = (
        sa.ForeignKeyConstraint(['dept_ID'], ['departments.dept_no']),
    )

    number = sa.Column('subdept_no', sa.SmallInteger(), primary_key=True, autoincrement=False, nullable=False)

    name = sa.Column('subdept_name', sa.String(length=30), nullable=True)

    department_number = sa.Column('dept_ID', sa.SmallInteger(), nullable=True)
    department = orm.relationship(
        Department,
        doc="""
        Reference to the parent :class:`Department` for this subdepartment.
        """)

    def __str__(self):
        return self.name or ''


@six.python_2_unicode_compatible
class Vendor(Base):
    """
    Represents a vendor from which product may be purchased.
    """
    __tablename__ = 'vendors'
    
    id = sa.Column('vendorID', sa.Integer(), primary_key=True, autoincrement=False, nullable=False)

    name = sa.Column('vendorName', sa.String(length=50), nullable=True)

    abbreviation = sa.Column('vendorAbbreviation', sa.String(length=10), nullable=True)

    discount_rate = sa.Column('discountRate', sa.Float(), nullable=True)

    contact = orm.relationship(
        'VendorContact',
        uselist=False, doc="""
        Reference to the :class:`VendorContact` instance for this vendor.
        """)

    phone = association_proxy(
        'contact', 'phone',
        creator=lambda p: VendorContact(phone=p))

    fax = association_proxy(
        'contact', 'fax',
        creator=lambda f: VendorContact(fax=f))

    email = association_proxy(
        'contact', 'email',
        creator=lambda e: VendorContact(email=e))

    website = association_proxy(
        'contact', 'website',
        creator=lambda w: VendorContact(website=w))

    notes = association_proxy(
        'contact', 'notes',
        creator=lambda n: VendorContact(notes=n))

    def __str__(self):
        return self.name or ''


class VendorContact(Base):
    """
    A general contact record for a vendor.
    """
    __tablename__ = 'vendorContact'

    vendor_id = sa.Column('vendorID', sa.Integer(), sa.ForeignKey('vendors.vendorID'), primary_key=True, autoincrement=False, nullable=False)

    phone = sa.Column(sa.String(length=15), nullable=True)

    fax = sa.Column(sa.String(length=15), nullable=True)

    email = sa.Column(sa.String(length=50), nullable=True)

    website = sa.Column(sa.String(length=100), nullable=True)

    notes = sa.Column(sa.Text(), nullable=True)


@six.python_2_unicode_compatible
class Product(Base):
    """
    Represents a product, purchased and/or sold by the organization.
    """
    __tablename__ = 'products'
    __table_args__ = (
        sa.ForeignKeyConstraint(['department'], ['departments.dept_no']),
    )

    id = sa.Column(sa.Integer(), primary_key=True, autoincrement=True, nullable=False)

    upc = sa.Column(sa.String(length=13), nullable=True)

    description = sa.Column(sa.String(length=30), nullable=True)

    brand = sa.Column(sa.String(length=30), nullable=True)

    formatted_name = sa.Column(sa.String(length=30), nullable=True)

    normal_price = sa.Column(sa.Float(), nullable=True)

    price_method = sa.Column('pricemethod', sa.SmallInteger(), nullable=True)

    group_price = sa.Column('groupprice', sa.Float(), nullable=True)

    quantity = sa.Column(sa.SmallInteger(), nullable=True)

    special_price = sa.Column(sa.Float(), nullable=True)

    special_price_method = sa.Column('specialpricemethod', sa.SmallInteger(), nullable=True)

    special_group_price = sa.Column('specialgroupprice', sa.Float(), nullable=True)

    special_quantity = sa.Column('specialquantity', sa.SmallInteger(), nullable=True)

    start_date = sa.Column(sa.DateTime(), nullable=True)

    end_date = sa.Column(sa.DateTime(), nullable=True)

    department_number = sa.Column('department', sa.SmallInteger(), nullable=True)

    size = sa.Column(sa.String(length=9), nullable=True)

    tax = sa.Column(sa.SmallInteger(), nullable=True)

    foodstamp = sa.Column(sa.Boolean(), nullable=True)

    scale = sa.Column(sa.Boolean(), nullable=True)

    scale_price = sa.Column('scaleprice', sa.Boolean(), nullable=True, default=False)

    mix_match_code = sa.Column('mixmatchcode', sa.String(length=13), nullable=True)

    modified = sa.Column(sa.DateTime(), nullable=True)

    # advertised = sa.Column(sa.Boolean(), nullable=True)

    tare_weight = sa.Column('tareweight', sa.Float(), nullable=True)

    discount = sa.Column(sa.SmallInteger(), nullable=True)

    discount_type = sa.Column('discounttype', sa.SmallInteger(), nullable=True)

    line_item_discountable = sa.Column(sa.Boolean(), nullable=True)

    unit_of_measure = sa.Column('unitofmeasure', sa.String(length=15), nullable=True)

    wicable = sa.Column(sa.SmallInteger(), nullable=True)

    quantity_enforced = sa.Column('qttyEnforced', sa.Boolean(), nullable=True)

    id_enforced = sa.Column('idEnforced', sa.Boolean(), nullable=True)

    cost = sa.Column(sa.Float(), nullable=True, default=0)

    in_use = sa.Column('inUse', sa.Boolean(), nullable=True)

    flags = sa.Column('numflag', sa.Integer(), nullable=True, default=0)

    subdepartment_number = sa.Column('subdept', sa.SmallInteger(), nullable=True)

    deposit = sa.Column(sa.Float(), nullable=True)

    local = sa.Column(sa.Integer(), nullable=True, default=0)

    store_id = sa.Column(sa.SmallInteger(), nullable=True, default=0)

    default_vendor_id = sa.Column(sa.Integer(), nullable=True, default=0)

    current_origin_id = sa.Column(sa.Integer(), nullable=True, default=0)

    department = orm.relationship(
        Department,
        primaryjoin=Department.number == department_number,
        foreign_keys=[department_number],
        doc="""
        Reference to the :class:`Department` to which the product belongs.
        """)

    vendor = orm.relationship(
        Vendor,
        primaryjoin=Vendor.id == default_vendor_id,
        foreign_keys=[default_vendor_id],
        doc="""
        Reference to the default :class:`Vendor` from which the product is obtained.
        """)

    @property
    def full_description(self):
        fields = ['brand', 'description', 'size']
        fields = [getattr(self, f) or '' for f in fields]
        fields = filter(bool, fields)
        return ' '.join(fields)

    def __str__(self):
        return self.description or ''


@six.python_2_unicode_compatible
class ProductFlag(Base):
    """
    Represents a product flag attribute.
    """
    __tablename__ = 'prodFlags'

    bit_number = sa.Column(sa.SmallInteger(), primary_key=True, autoincrement=False, nullable=False, default=0)

    description = sa.Column(sa.String(length=50), nullable=True)

    active = sa.Column(sa.Boolean(), nullable=True, default=True)

    def __str__(self):
        return self.description or ''


@six.python_2_unicode_compatible
class Employee(Base):
    """
    Represents an employee within the organization.
    """
    __tablename__ = 'employees'

    number = sa.Column('emp_no', sa.SmallInteger(), primary_key=True, autoincrement=False, nullable=False)

    cashier_password = sa.Column('CashierPassword', sa.String(length=50), nullable=True)

    admin_password = sa.Column('AdminPassword', sa.String(length=50), nullable=True)

    first_name = sa.Column('FirstName', sa.String(length=255), nullable=True)

    last_name = sa.Column('LastName', sa.String(length=255), nullable=True)

    job_title = sa.Column('JobTitle', sa.String(length=255), nullable=True)

    active = sa.Column('EmpActive', sa.Boolean(), nullable=True)

    frontend_security = sa.Column('frontendsecurity', sa.SmallInteger(), nullable=True)

    backend_security = sa.Column('backendsecurity', sa.SmallInteger(), nullable=True)

    birth_date = sa.Column('birthdate', sa.DateTime(), nullable=True)

    def __str__(self):
        return ' '.join([self.first_name or '', self.last_name or '']).strip()


@six.python_2_unicode_compatible
class MemberType(Base):
    """
    Represents a type of membership within the organization.
    """
    __tablename__ = 'memtype'

    id = sa.Column('memtype', sa.SmallInteger(), primary_key=True, nullable=False, default=0)

    description = sa.Column('memDesc', sa.String(length=20), nullable=True)

    customer_type = sa.Column('custdataType', sa.String(length=10), nullable=True)

    discount = sa.Column(sa.SmallInteger(), nullable=True)

    staff = sa.Column(sa.Boolean(), nullable=True)

    ssi = sa.Column(sa.Boolean(), nullable=True)

    # TODO: this was apparently added "recently" - isn't present in all DBs
    # (need to figure out how to conditionally include it in model?)
    # sales_code = sa.Column('salesCode', sa.Integer(), nullable=True)

    def __str__(self):
        return self.description or ""


@six.python_2_unicode_compatible
class Customer(Base):
    """
    Represents a customer of the organization.
    """
    __tablename__ = 'custdata'

    id = sa.Column(sa.Integer(), primary_key=True, autoincrement=True, nullable=False)

    card_number = sa.Column('CardNo', sa.Integer(), nullable=True)

    person_number = sa.Column('personNum', sa.SmallInteger(), nullable=False, default=1)

    first_name = sa.Column('FirstName', sa.String(length=30), nullable=True)

    last_name = sa.Column('LastName', sa.String(length=30), nullable=True)

    cash_back = sa.Column('CashBack', sa.Float(), nullable=False, default=60)

    balance = sa.Column('Balance', sa.Float(), nullable=False, default=0)

    discount = sa.Column('Discount', sa.SmallInteger(), nullable=True)

    member_discount_limit = sa.Column('MemDiscountLimit', sa.Float(), nullable=False, default=0)

    charge_limit = sa.Column('ChargeLimit', sa.Float(), nullable=False, default=0)
    
    charge_ok = sa.Column('ChargeOk', sa.Boolean(), nullable=False, default=False)

    write_checks = sa.Column('WriteChecks', sa.Boolean(), nullable=False, default=True)

    store_coupons = sa.Column('StoreCoupons', sa.Boolean(), nullable=False, default=True)

    type = sa.Column('Type', sa.String(length=10), nullable=False, default='pc')

    member_type_id = sa.Column('memType', sa.SmallInteger(), nullable=True)
    member_type = orm.relationship(
        MemberType,
        primaryjoin=MemberType.id == member_type_id,
        foreign_keys=[member_type_id],
        doc="""
        Reference to the :class:`MemberType` to which this member belongs.
        """)

    staff = sa.Column(sa.Boolean(), nullable=False, default=False)

    ssi = sa.Column('SSI', sa.Boolean(), nullable=False, default=False)

    purchases = sa.Column('Purchases', sa.Float(), nullable=False, default=0)

    number_of_checks = sa.Column('NumberOfChecks', sa.SmallInteger(), nullable=False, default=0)

    member_coupons = sa.Column('memCoupons', sa.Integer(), nullable=False, default=1)

    blue_line = sa.Column('blueLine', sa.String(length=50), nullable=True)

    shown = sa.Column('Shown', sa.Boolean(), nullable=False, default=True)

    last_change = sa.Column('LastChange', sa.DateTime(), nullable=False)

    member_info = orm.relationship(
        'MemberInfo',
        primaryjoin='MemberInfo.card_number == Customer.card_number',
        foreign_keys=[card_number],
        uselist=False,
        back_populates='customers',
        doc="""
        Reference to the :class:`MemberInfo` instance for this customer.
        """)

    def __str__(self):
        return "{} {}".format(self.first_name or '', self.last_name or '').strip()


@six.python_2_unicode_compatible
class MemberInfo(Base):
    """
    Contact info regarding a member of the organization.
    """
    __tablename__ = 'meminfo'

    card_number = sa.Column('card_no', sa.Integer(), primary_key=True, autoincrement=False, nullable=False)

    last_name = sa.Column(sa.String(length=30), nullable=True)

    first_name = sa.Column(sa.String(length=30), nullable=True)

    other_last_name = sa.Column('othlast_name', sa.String(length=30), nullable=True)

    other_first_name = sa.Column('othfirst_name', sa.String(length=30), nullable=True)

    street = sa.Column(sa.String(length=255), nullable=True)

    city = sa.Column(sa.String(length=20), nullable=True)

    state = sa.Column(sa.String(length=2), nullable=True)

    zip = sa.Column(sa.String(length=10), nullable=True)

    phone = sa.Column(sa.String(length=30), nullable=True)

    email = sa.Column('email_1', sa.String(length=50), nullable=True)

    email2 = sa.Column('email_2', sa.String(length=50), nullable=True)

    ads_ok = sa.Column('ads_OK', sa.Boolean(), nullable=True, default=True)

    customers = orm.relationship(
        Customer,
        primaryjoin=Customer.card_number == card_number,
        foreign_keys=[Customer.card_number],
        back_populates='member_info',
        remote_side=Customer.card_number,
        doc="""
        List of :class:`Customer` instances which are associated with this member info.
        """)

    dates = orm.relationship(
        'MemberDate',
        primaryjoin='MemberDate.card_number == MemberInfo.card_number',
        foreign_keys='MemberDate.card_number',
        cascade='all, delete-orphan',
        doc="""
        List of date records for the member.
        """,
        backref=orm.backref(
            'member',
            doc="""
            Reference to the member to whom the date record applies.
            """))

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name or '', self.last_name or '').strip()

    def __str__(self):
        return self.full_name


@six.python_2_unicode_compatible
class MemberDate(Base):
    """
    Join/exit dates for members
    """
    __tablename__ = 'memDates'

    card_number = sa.Column('card_no', sa.Integer(), primary_key=True, autoincrement=False, nullable=False)

    start_date = sa.Column(sa.DateTime(), nullable=True)

    end_date = sa.Column(sa.DateTime(), nullable=True)

    def __str__(self):
        return "{} thru {}".format(
            self.start_date.date() if self.start_date else "??",
            self.end_date.date() if self.end_date else "??")


@six.python_2_unicode_compatible
class MemberContact(Base):
    """
    Contact preferences for members
    """
    __tablename__ = 'memContact'

    card_number = sa.Column('card_no', sa.Integer(), primary_key=True, autoincrement=False, nullable=False)

    preference = sa.Column('pref', sa.Integer(), nullable=True)

    member = orm.relationship(
        MemberInfo,
        primaryjoin=MemberInfo.card_number == card_number,
        foreign_keys=[MemberInfo.card_number],
        uselist=False,
        doc="""
        Reference to the member to whom the contact record applies.
        """,
        backref=orm.backref(
            'contact',
            uselist=False,
            doc="""
            Reference to contact preference record for the member.
            """))

    def __str__(self):
        return str(self.preference)


@six.python_2_unicode_compatible
class HouseCoupon(Base):
    """
    Represents a "house" (store) coupon.
    """
    __tablename__ = 'houseCoupons'
    __table_args__ = (
        sa.ForeignKeyConstraint(['department'], ['departments.dept_no']),
    )

    coupon_id = sa.Column('coupID', sa.Integer(), primary_key=True, nullable=False)

    description = sa.Column(sa.String(length=30), nullable=True)

    start_date = sa.Column('startDate', sa.DateTime(), nullable=True)

    end_date = sa.Column('endDate', sa.DateTime(), nullable=True)

    limit = sa.Column(sa.SmallInteger(), nullable=True)

    member_only = sa.Column('memberOnly', sa.SmallInteger(), nullable=True)

    discount_type = sa.Column('discountType', sa.String(length=2), nullable=True)

    discount_value = sa.Column('discountValue', sa.Numeric(precision=10, scale=2), nullable=True)

    min_type = sa.Column('minType', sa.String(length=2), nullable=True)

    min_value = sa.Column('minValue', sa.Numeric(precision=10, scale=2), nullable=True)

    department_id = sa.Column('department', sa.Integer(), nullable=True)
    department = orm.relationship(Department)

    auto = sa.Column(sa.Boolean(), nullable=True, default=False)

    # TODO: this isn't yet supported in all production DBs
    # virtual_only = sa.Column('virtualOnly', sa.Boolean(), nullable=True, default=False)

    def __str__(self):
        return self.description or ''
