""" Heritor low level API
"""
from zope.annotation.interfaces import IAnnotations
from zope.interface import implementer
from eea.faceted.inheritance.config import ANNO_ANCESTOR
from eea.faceted.inheritance.criteria.interfaces import IHeritorAccessor

@implementer(IHeritorAccessor)
class HeritorAccessor(object):
    """ Criteria handler
    """

    def __init__(self, context):
        self.context = context

    def ancestor(self=None):
        """ Ancestor property
        """
        def fget(self, default=None):
            """ Getter
            """
            anno = IAnnotations(self.context)
            return anno.get(ANNO_ANCESTOR, '')

        def fset(self, value):
            """ Setter
            """
            anno = IAnnotations(self.context)
            anno[ANNO_ANCESTOR] = value

        return property(fget, fset)
    ancestor = ancestor()
