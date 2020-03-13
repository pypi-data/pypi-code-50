from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aerie.schemas import Schema


class AerieException(Exception):
    ...


class DoesNotExist(AerieException):
    ...


class MultipleResults(AerieException):
    ...


class ImproperlyConfigured(AerieException):
    ...


class AssociationNotLoaded(AttributeError, AerieException):
    def _raise(self):
        raise self

    def __get__(self, instance, owner):
        self._raise()

    def __getattr__(self, item):
        self._raise()

    def __str__(self):
        return ''


class FieldError(AttributeError, AerieException):
    pass


class UniqueViolation(AerieException):
    def __init__(
            self, msg: str, hint: str, code: str, constraint: str,
            query: str,
    ):
        super().__init__(msg)
        self.hint = hint
        self.code = code
        self.query = query
        self.constraint = constraint


class DeletedEntity(AerieException):
    def __init__(self, msg: str, entity: Schema):
        super().__init__(msg)
        self.entity = entity
