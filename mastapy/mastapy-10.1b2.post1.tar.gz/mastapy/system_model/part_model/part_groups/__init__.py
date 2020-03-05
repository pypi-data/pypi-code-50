'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2004 import ConcentricOrParallelPartGroup
    from ._2005 import ConcentricPartGroup
    from ._2006 import ConcentricPartGroupParallelToThis
    from ._2007 import DesignMeasurements
    from ._2008 import ParallelPartGroup
    from ._2009 import PartGroup
