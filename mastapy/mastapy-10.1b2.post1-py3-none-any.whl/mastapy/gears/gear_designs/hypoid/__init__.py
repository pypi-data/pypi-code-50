'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._741 import HypoidGearDesign
    from ._742 import HypoidGearMeshDesign
    from ._743 import HypoidGearSetDesign
    from ._744 import HypoidMeshedGearDesign
