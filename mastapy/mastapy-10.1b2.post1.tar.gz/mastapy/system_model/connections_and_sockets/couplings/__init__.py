'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1873 import ClutchConnection
    from ._1874 import ClutchSocket
    from ._1875 import ConceptCouplingConnection
    from ._1876 import ConceptCouplingSocket
    from ._1877 import CouplingConnection
    from ._1878 import CouplingSocket
    from ._1879 import PartToPartShearCouplingConnection
    from ._1880 import PartToPartShearCouplingSocket
    from ._1881 import SpringDamperConnection
    from ._1882 import SpringDamperSocket
    from ._1883 import TorqueConverterConnection
    from ._1884 import TorqueConverterPumpSocket
    from ._1885 import TorqueConverterTurbineSocket
