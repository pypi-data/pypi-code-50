
import hdt
from . import local_hdt
from . import urishortener


class Predicate:

    @staticmethod
    def fromString(id: str):
        int_value = local_hdt.document().convert_term(id, hdt.IdentifierPosition.Predicate)
        if int_value <= 0:
            raise ValueError("{} does not exist as Predicate.".format(id))
        return Predicate(int_value)

    def __init__(self, id: int):
        self.id: int = id

    def __str__(self):
        return urishortener.shorten(local_hdt.document().convert_id(self.id, hdt.IdentifierPosition.Predicate))

    def __eq__(self, other):
        return type(other) == Predicate and self.id == other.id

    def __hash__(self):
        return self.id

class Vertex:

    @staticmethod
    def fromString(id: str) -> 'Vertex':
        s_id = local_hdt.document().convert_term(id, hdt.IdentifierPosition.Subject)
        o_id = local_hdt.document().convert_term(id, hdt.IdentifierPosition.Object)
        if s_id == 0 and o_id == 0:
            raise ValueError("{} does not exist in this HDT file.".format(id))
        return Vertex(s_id=s_id, o_id=o_id)
        
    @staticmethod
    def fromSubjectId(id: int) -> 'Vertex':
        if id == 0:
            raise ValueError("0 is not a valid Subject ID.")
        uri = local_hdt.document().convert_id(id, hdt.IdentifierPosition.Subject)
        o_id = local_hdt.document().convert_term(uri, hdt.IdentifierPosition.Object)
        return Vertex(s_id=id, o_id=o_id)

    @staticmethod
    def fromObjectId(id: int) -> 'Vertex':
        if id == 0:
            raise ValueError("0 is not a valid Object ID.")
        uri = local_hdt.document().convert_id(id, hdt.IdentifierPosition.Object)
        s_id = local_hdt.document().convert_term(uri, hdt.IdentifierPosition.Subject)
        return Vertex(s_id=s_id, o_id=id)

    def __init__(self, s_id: int = 0, o_id: int = 0):
        if s_id == 0 and o_id == 0:
            raise ValueError("Vertex does not exist in HDT file.")
        self.s_id = s_id
        self.o_id = o_id

    def is_subject(self):
        return self.s_id > 0

    def is_object(self):
        return self.o_id > 0

    def __str__(self):
        id: int
        pos: hdt.IdentifierPosition
        if self.is_subject():
            id = self.s_id
            pos = hdt.IdentifierPosition.Subject
        else:
            id = self.o_id
            pos = hdt.IdentifierPosition.Object
        return urishortener.shorten(local_hdt.document().convert_id(id, pos))

    def __eq__(self, other):
        return self.s_id == other.s_id and self.o_id == other.o_id

    def __hash__(self):
        return self.s_id * 31 + self.o_id
