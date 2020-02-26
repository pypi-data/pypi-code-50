from datetime import datetime
from datetime import date
from typing import Optional

from sqlalchemy.orm.attributes import InstrumentedAttribute

from flask_atomic.logger import getlogger
from flask_atomic.orm.database import db
from flask_atomic.orm.mixins.core import CoreMixin

logger = getlogger(__name__)


class DeclarativeBase(db.Model, CoreMixin):
    """
    Base model to be extended for use with Flask projects.

    Core concept of the model is common functions to help wrap up database
    interaction into a single interface. Testing can be rolled up easier this
    way also. Inheriting from this class automatically sets id field and db
    soft deletion field managed by active using the DYNA pattern (D, Y, N, A).

    Basic usage::

        from flask_atomic.sqlalchemy.declarative import DeclarativeBase

        class MyNewModel(DeclarativeBase):
            field_a = db.Column(db.String(256), nullable=True)

    """

    __abstract__ = True
    # active = db.Column(db.String(5), default='Y')

    def __str__(self):
        return self.whatami()

    @classmethod
    def identify_primary_key(cls):
        return list(cls.__table__.primary_key).pop().name

    @classmethod
    def checkfilters(cls, filters):
        resp = {}
        for k, v in filters.items():
            resp[cls.normalise(k)] = v
        return resp

    @classmethod
    def getquery(cls):
        return db.session.query

    @classmethod
    def makequery(cls, fields=None):
        try:
            # return db.session.query(cls, fields)
            if not fields:
                return cls.query
            return db.session.query(cls, *fields)
        except Exception as e:
            logger.error(str(e))
            db.session.rollback()
        return db.session.query(cls, *fields)

    @classmethod
    def relations(cls, flag):
        if flag == True:
            return set(cls.__mapper__.relationships.keys())
        elif isinstance(flag, list):
            return set(flag)
        return set()

    @classmethod
    def relationattrs(cls):
        return set(cls.__mapper__.relationships.keys())

    @classmethod
    def objectcolumns(cls, include_relationships=False):
        bound_columns = set(cls.__mapper__.columns)
        if include_relationships:
            rels = cls.__mapper__.relationships
            return bound_columns.union(set([i.class_attribute for i in cls.__mapper__.relationships]))
        return bound_columns

    @classmethod
    def keys(cls):
        return set(cls.__table__.columns.keys())

    @classmethod
    def schema(cls, rel=True, exclude=None):
        if exclude is None:
            exclude = []
        schema = []
        for item in [key for key in cls.keys() if key not in exclude]:
            schema.append(dict(name=item.replace('_', ' '), key=item))
        return schema

    @classmethod
    def getkey(cls, field):
        if isinstance(field, InstrumentedAttribute):
            return getattr(cls, field.key)
        return getattr(cls, field)

    def relationships(self, root=''):
        return list(filter(lambda r: r != root, self.__mapper__.relationships.keys()))

    def columns(self, exc: Optional[list] = None) -> list:
        """
        Gets a list of columns to work with, minus the excluded sublist (exc).

        :param exc:
        :return:
        """

        if exc is None:
            exc = list()
        return [key for key in list(self.__table__.columns.keys()) if key not in exc]

    def whatami(self) -> str:
        """
        Self-describe the model.

        :return: Descriptive name based on the tablename used at declaration.
        """

        # I am not a number :)
        return self.__tablename__

    def process_relationships(self, root: str, exclude: set = None, rels=None):
        resp = dict()
        if not rels or isinstance(rels, bool):
            rels = self.relationships(root)
        for item in rels:
            relationship_instance = getattr(self, item)
            if isinstance(relationship_instance, list):
                # if relationship_instance.uselist:
                resp[item] = []
                for index, entry in enumerate(relationship_instance):
                    fields = set(entry.keys()).difference(exclude)
                    resp[item].append(entry.extract_data(set(entry.keys()).difference(exclude)))
                    # for grandchild in entry.relationships(root):
                    #     if grandchild != item:
                    #         if isinstance(getattr(entry, grandchild), list):
                    #             resp[item][index][grandchild] = [i.extract_data(fields) for i in
                    #                                              getattr(entry, grandchild)]
                    #         else:
                    #             resp[item][index][grandchild] = getattr(entry, grandchild).extract_data(fields)
            elif relationship_instance:
                fields = set(relationship_instance.keys()).difference(exclude)
                resp[item] = relationship_instance.extract_data(fields)
        return resp

    def extract_data(self, fields, exclude: Optional[set] = None) -> dict:
        resp = dict()
        if exclude is None:
            exclude = set()
        for column in fields.difference(exclude):
            if isinstance(getattr(self, column), datetime) or isinstance(getattr(self, column), date):
                resp[column] = str(getattr(self, column))
            else:
                resp[column] = getattr(self, column)
        return resp

    def serialize(self, fields=None, exc: Optional[set] = None, rels=False, root=None, exclude=None, functions=None):
        """
        This utility function dynamically converts Alchemy model classes into a
        dict using introspective lookups. This saves on manually mapping each
        model and all the fields. However, exclusions should be noted. Such as
        passwords and protected properties.

        :param fields: More of a whitelist of fields to include (preferred way)
        :param rels: Whether or not to introspect to relationships
        :param exc: Fields to exclude from query result set
        :param root: Root model for processing relationships. This acts as a
        recursive sentinel to prevent infinite recursion due to selecting oneself
        as a related model, and then infinitely trying to traverse the roots
        own relationships, from itself over and over.
        :param exclude: Exclusion in set form. Currently in favour of exc param.

        Only remedy to this is also to use one way relationships. Avoiding any
        back referencing of models.

        :return: json data structure of model
        :rtype: dict
        """

        if exclude is None:
            exclude = set()
        else:
            exclude = set(exclude)
        if not fields:
            fields = set(self.fields())

        if root is None:
            root = self.whatami()

        if exc is None:
            exc = {'password'}

        set(exclude).union(exc)
        # Define our model properties here. Columns and Schema relationships
        resp = self.extract_data(fields, exc)

        for key, value in functions.items():
            resp[f'_{key}'] = value(getattr(self, key))

        restricted_fields = fields.discard(getattr(self, 'RESTRICTED_FIELDS', set()))
        if restricted_fields:
            fields.discard(restricted_fields)
            exclude = exclude.union(restricted_fields or set())

        rels = rels or set(self.relationships()).intersection(fields)
        if not rels or len(set(self.relationships())) < 1:
            return resp
        resp.update(self.process_relationships(root, rels=rels, exclude=exclude))
        return resp

    def __eq__(self, comparison):
        if type(self) != type(comparison):
            raise ValueError('Objects are not the same. Cannot compare')
        base = self.columns()
        base_dictionary = self.__dict__
        comp_dictionary = self.__dict__
        flag = True
        for column_name in base:
            if base_dictionary[column_name] != comp_dictionary[column_name]:
                flag = False
                break
        return flag
