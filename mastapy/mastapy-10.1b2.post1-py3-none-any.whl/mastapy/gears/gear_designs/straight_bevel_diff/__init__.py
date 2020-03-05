'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._717 import StraightBevelDiffGearDesign
    from ._718 import StraightBevelDiffGearMeshDesign
    from ._719 import StraightBevelDiffGearSetDesign
    from ._720 import StraightBevelDiffMeshedGearDesign
