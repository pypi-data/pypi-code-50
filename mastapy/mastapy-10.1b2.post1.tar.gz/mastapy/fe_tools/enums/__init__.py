'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._959 import ElementPropertyClass
    from ._960 import MaterialPropertyClass
