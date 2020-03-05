'''_2038.py

ConceptGear
'''


from mastapy.system_model.part_model.gears import _2048, _2047
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.concept import _901
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConceptGear')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGear',)


class ConceptGear(_2047.Gear):
    '''ConceptGear

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGear.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def orientation(self) -> '_2048.GearOrientations':
        '''GearOrientations: 'Orientation' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.Orientation)
        return constructor.new(_2048.GearOrientations)(value) if value else None

    @orientation.setter
    def orientation(self, value: '_2048.GearOrientations'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Orientation = value

    @property
    def active_gear_design(self) -> '_901.ConceptGearDesign':
        '''ConceptGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_901.ConceptGearDesign)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign else None

    @property
    def concept_gear_design(self) -> '_901.ConceptGearDesign':
        '''ConceptGearDesign: 'ConceptGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_901.ConceptGearDesign)(self.wrapped.ConceptGearDesign) if self.wrapped.ConceptGearDesign else None
