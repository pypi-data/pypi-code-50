'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._5224 import AbstractAssemblyStaticLoadCaseGroup
    from ._5225 import ComponentStaticLoadCaseGroup
    from ._5226 import ConnectionStaticLoadCaseGroup
    from ._5227 import DesignEntityStaticLoadCaseGroup
    from ._5228 import GearSetStaticLoadCaseGroup
    from ._5229 import PartStaticLoadCaseGroup
