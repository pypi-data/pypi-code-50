# coding: utf-8
"""
Order model
"""
import datetime


def _parse_date(date_string):
    return None if date_string is None else datetime.datetime.strptime(date_string, "%Y-%m-%d")


class Order(object):
    """
    CREATE TABLE "Order" (
        uid INTEGER NOT NULL,
        order_ref VARCHAR(50) NOT NULL,
        project_cat VARCHAR(50) NOT NULL,
        creation_date DATE NOT NULL,
        close_date DATE,
        PRIMARY KEY (uid)
    )
    """

    def __init__(
        self, order_ref, project_cat, creation_date, close_date,
    ):
        self._uid = None
        self.order_ref = order_ref
        self.project_cat = project_cat
        self.creation_date = creation_date
        self.close_date = close_date

    @property
    def uid(self):
        return self._uid

    @classmethod
    def from_row(cls, uid, order_ref, project_cat, creation_date, close_date):
        uid = int(uid)
        creation_date = _parse_date(creation_date)
        close_date = _parse_date(close_date)
        order = cls(order_ref, project_cat, creation_date, close_date)
        order._uid = uid
        return order

    def __str__(self):
        return u'Order #{uid:05d}: "{order_ref}"'.format(uid=self._uid, order_ref=self.order_ref)
