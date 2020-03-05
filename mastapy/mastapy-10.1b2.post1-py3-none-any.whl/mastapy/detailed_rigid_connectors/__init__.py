'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._961 import DetailedRigidConnectorDesign
    from ._962 import DetailedRigidConnectorHalfDesign
