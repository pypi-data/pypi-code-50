'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._712 import WormDesign
    from ._713 import WormGearDesign
    from ._714 import WormGearMeshDesign
    from ._715 import WormGearSetDesign
    from ._716 import WormWheelDesign
