'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1017 import AssemblyMethods
    from ._1018 import CalculationMethods
    from ._1019 import InterferenceFitDesign
    from ._1020 import InterferenceFitHalfDesign
    from ._1021 import StressRegions
    from ._1022 import Table4JointInterfaceTypes
