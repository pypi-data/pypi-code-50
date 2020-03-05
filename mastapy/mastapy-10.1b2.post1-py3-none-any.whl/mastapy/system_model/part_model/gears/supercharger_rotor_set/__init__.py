'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2072 import BoostPressureInputOptions
    from ._2073 import InputPowerInputOptions
    from ._2074 import PressureRatioInputOptions
    from ._2075 import RotorSetDataInputFileOptions
    from ._2076 import RotorSetMeasuredPoint
    from ._2077 import RotorSpeedInputOptions
    from ._2078 import SuperchargerMap
    from ._2079 import SuperchargerMaps
    from ._2080 import SuperchargerRotorSet
    from ._2081 import SuperchargerRotorSetDatabase
    from ._2082 import YVariableForImportedData
